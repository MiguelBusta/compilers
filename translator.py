import ply.lex as lex
from math import pi, pow
import ply.yacc as yacc
import networkx as nx
import matplotlib.pyplot as plt
import cv2
import numpy as np
from networkx.drawing.nx_pydot import graphviz_layout
from library import *

# Global variables
parseGraph = None
NODE_COUNTER = 0

def add_node(attr):
    global parseGraph
    global NODE_COUNTER
    attr["counter"] = NODE_COUNTER
    parseGraph.add_node(NODE_COUNTER, **attr)
    NODE_COUNTER += 1
    return parseGraph.nodes[NODE_COUNTER-1]

symbol_table = dict()
symbol_table["PI"] = pi
symbol_table["E"] = 2.718281828459045

# Custom functions
def myPrint(v1, v2, v3, v4):
    print("--->", v1, v2, v3, v4)

def do_nothing():
    print("We are Nothing....")

def sumAB(a, b):
    return a + b

def load_image(filepath):
    image = cv2.imread(filepath)
    if image is None:
        raise ValueError(f"Image at {filepath} could not be loaded.")
    return image

def show_image(image):
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

symbol_table["myPrint"] = myPrint
symbol_table["nothing"] = do_nothing
symbol_table["sumAB"] = sumAB
symbol_table["load"] = load_image
symbol_table["show"] = show_image
symbol_table["tuple"] = gen_vector
symbol_table["None"] = None
# Add numpy functions
symbol_table["np.mean"] = np.mean
symbol_table["np.std"] = np.std
symbol_table["np.var"] = np.var
symbol_table["np.min"] = np.min
symbol_table["np.max"] = np.max
symbol_table["np.sum"] = np.sum
symbol_table["np.prod"] = np.prod
symbol_table["np.cumsum"] = lambda x: np.cumsum(x).tolist()
symbol_table["linspace"] = lambda start, stop, num: np.linspace(start, stop, num).astype(int).tolist()

tokens = (
    'NUMBER',
    'VARIABLE',
    'DOT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'EQUAL',
    'EXP',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'CONNECT',
    'STRING',
    'LBRACKET',
    'RBRACKET',
    'COLON',
    'NONE'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_EQUAL = r'='
t_EXP = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_CONNECT = r'->'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COLON = r':'
t_DOT = r'\.'

def t_STRING(t):
    r'\"(.)*\"'
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r'\d+\.?\d*'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NONE(t):
    r'None'
    t.value = None
    return t

def t_error(t):
    print("Error on", t.value)
    t.lexer.skip(1)

lexer = lex.lex()

def p_assignment_assign(p):
    """
    assignment : VARIABLE EQUAL expression
               | VARIABLE LBRACKET expression RBRACKET EQUAL expression
               | list_access EQUAL expression
    """
    node = add_node({'type': 'ASSIGN', 'label': '=', 'value': ''})
    if len(p) == 4:
        node_var = add_node({'type': 'VARIABLE_ASSIGN', 'label': f'VAR_{p[1]}', 'value': p[1]})
        parseGraph.add_edge(node["counter"], node_var["counter"])
        parseGraph.add_edge(node["counter"], p[3]["counter"])
    elif len(p) == 7:
        node_list = add_node({'type': 'LIST_ASSIGN', 'label': 'LIST_ASSIGN', 'value': p[1]})
        parseGraph.add_edge(node["counter"], node_list["counter"])
        parseGraph.add_edge(node["counter"], p[6]["counter"])
    else:
        parseGraph.add_edge(node["counter"], p[1]["counter"])
        parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_assignment_flow(p):
    """
    assignment : VARIABLE EQUAL flow
    """
    node = add_node({'type': 'ASSIGN', 'label': '=', 'value': ''})
    node_var = add_node({'type': 'VARIABLE_ASSIGN', 'label': f'VAR_{p[1]}', 'value': p[1]})
    parseGraph.add_edge(node["counter"], node_var["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_flow(p):
    """
    flow : VARIABLE CONNECT flow_functions
    """
    connections = parseGraph.neighbors(p[3][0]["counter"])
    for c in connections:
        c = parseGraph.nodes[c]
        if c["type"] == "PENDING_NODE":
            c["type"] = "VARIABLE"
            c["label"] = f"VAR_{p[1]}"
            c["value"] = p[1]
            break
    p[0] = p[3][-1]

def p_flow_functions(p):
    """
    flow_functions : flow_function_call CONNECT flow_functions
    """
    connections = parseGraph.neighbors(p[3][0]["counter"])
    for c in connections:
        c = parseGraph.nodes[c]
        if c["type"] == "PENDING_NODE":
            parseGraph.add_edge(c["counter"], p[1]["counter"])
            break
    p[0] = [p[1]] + p[3]

def p_flow_functions_alone(p):
    """
    flow_functions : flow_function_call
    """
    p[0] = [p[1]]

def p_flow_function_call(p):
    """
    flow_function_call : VARIABLE LPAREN params RPAREN
    """
    node = add_node({"type": "FLOW_FUNCTION_CALL", "label": f"ff_{p[1]}", 'value': p[1]})
    pending_node = add_node({"type": "PENDING_NODE", "label": "pending", 'value': ''})
    parseGraph.add_edge(node["counter"], pending_node["counter"])
    for n in p[3]:
        parseGraph.add_edge(node["counter"], n["counter"])
    p[0] = node

def p_assignment_expression(p):
    """
    assignment : expression
    """
    p[0] = p[1]

def p_expression_term(p):
    """
    expression : term
               | string
               | list_access
               | function_call
               | none
    """
    p[0] = p[1]

def p_string_def(p):
    """
    string : STRING
    """
    p[0] = add_node({'type': 'STRING', 'label': p[1], 'value': p[1]})

def p_expression_plus(p):
    """
    expression : expression PLUS term
    """
    node = add_node({'type': 'PLUS', 'label': '+', 'value': ''})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_expression_minus(p):
    """
    expression : expression MINUS term
    """
    node = add_node({'type': 'MINUS', 'label': '-', 'value': ''})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_none_def(p):
    """
    none : NONE
    """
    p[0] = add_node({'type': 'NONE', 'label': 'None', 'value': None})

def p_term_exponent(p):
    """
    term : exponent
    """
    p[0] = p[1]

def p_term_times(p):
    """
    term : term TIMES exponent
    """
    node = add_node({'type': 'TIMES', 'label': '*', 'value': ''})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_term_divides(p):
    """
    term : term DIV exponent
    """
    node = add_node({'type': 'DIV', 'label': '/', 'value': ''})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_exponent_factor(p):
    """
    exponent : factor
    """
    p[0] = p[1]

def p_exponent_exp(p):
    """
    exponent : factor EXP factor
    """
    node = add_node({'type': 'POWER', 'label': 'POW', 'value': ''})
    parseGraph.add_edge(node["counter"], p[1]["counter"])
    parseGraph.add_edge(node["counter"], p[3]["counter"])
    p[0] = node

def p_factor_num(p):
    """
    factor : NUMBER
    """
    n = add_node({'type': 'NUMBER', 'label': f'NUM_{p[1]}', 'value': p[1]})
    p[0] = n

def p_factor_variable(p):
    """
    factor : VARIABLE
           | VARIABLE DOT VARIABLE
    """
    if len(p) == 2:
        p[0] = add_node({'type': 'VARIABLE', 'label': f'VAR_{p[1]}', 'value': p[1]})
    else:
        p[0] = add_node({'type': 'ATTRIBUTE', 'label': f'ATTR_{p[1]}.{p[3]}', 'value': f'{p[1]}.{p[3]}'})

def p_factor_expr(p):
    """
    factor : LPAREN expression RPAREN
    """
    node = add_node({'type': 'GROUP', 'label': '( )', 'value': ''})
    parseGraph.add_edge(node["counter"], p[2]["counter"])
    p[0] = node

def p_factor_function_call(p):
    """
    factor : function_call
    """
    p[0] = p[1]

def p_function_call_no_params(p):
    """
    function_call : VARIABLE LPAREN RPAREN
                  | VARIABLE DOT VARIABLE LPAREN RPAREN
    """
    if len(p) == 4:
        p[0] = add_node({'type': 'FUNCTION_CALL', 'label': f'FUN_{p[1]}', 'value': p[1]})
    else:
        p[0] = add_node({'type': 'METHOD_CALL', 'label': f'METHOD_{p[1]}.{p[3]}', 'value': f'{p[1]}.{p[3]}'})

def p_function_call_params(p):
    """
    function_call : VARIABLE LPAREN params RPAREN
                  | VARIABLE DOT VARIABLE LPAREN params RPAREN
    """
    if len(p) == 5:
        node = add_node({'type': 'FUNCTION_CALL', 'label': f'FUN_{p[1]}', 'value': p[1]})
    else:
        node = add_node({'type': 'METHOD_CALL', 'label': f'METHOD_{p[1]}.{p[3]}', 'value': f'{p[1]}.{p[3]}'})
    for n in p[len(p) - 2]:
        parseGraph.add_edge(node["counter"], n["counter"])
    p[0] = node

def p_params(p):
    """
    params : params COMMA expression
            | expression
    """
    if len(p) > 2:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_list_def(p):
    """
    factor : LBRACKET elements RBRACKET
    """
    node = add_node({'type': 'LIST', 'label': 'LIST', 'value': ''})
    for elem in p[2]:
        parseGraph.add_edge(node["counter"], elem["counter"])
    p[0] = node

def p_elements(p):
    """
    elements : elements COMMA expression
             | expression
    """
    if len(p) > 2:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_list_access(p):
    """
    list_access : VARIABLE LBRACKET expression RBRACKET
                | VARIABLE LBRACKET expression COLON expression RBRACKET
                | VARIABLE LBRACKET COLON expression RBRACKET
                | VARIABLE LBRACKET expression COLON RBRACKET
                | VARIABLE LBRACKET COLON RBRACKET
                | list_access LBRACKET expression RBRACKET
    """
    if len(p) == 5:
        node = add_node({'type': 'LIST_ACCESS', 'label': 'LIST_ACCESS', 'value': p[1]})
        parseGraph.add_edge(node["counter"], p[3]["counter"])
    elif len(p) == 7:
        node = add_node({'type': 'SLICE_ACCESS', 'label': 'SLICE_ACCESS', 'value': p[1]})
        parseGraph.add_edge(node["counter"], p[3]["counter"])
        parseGraph.add_edge(node["counter"], p[5]["counter"])
    elif p[3] == ':':
        node = add_node({'type': 'SLICE_ACCESS', 'label': 'SLICE_ACCESS', 'value': p[1]})
        parseGraph.add_edge(node["counter"], add_node({'type': 'NUMBER', 'label': '0', 'value': 0})["counter"])
        parseGraph.add_edge(node["counter"], add_node({'type': 'NUMBER', 'label': 'end', 'value': -1})["counter"])
    else:
        node = add_node({'type': 'SLICE_ACCESS', 'label': 'SLICE_ACCESS', 'value': p[1]})
        parseGraph.add_edge(node["counter"], p[3]["counter"])
        parseGraph.add_edge(node["counter"], add_node({'type': 'NUMBER', 'label': 'end', 'value': -1})["counter"])
    p[0] = node

def p_error(p):
    print("Syntax error in input: ", p)

def print_graph_info(graph):
    print("\nNodes of the graph:")
    for node, attr in graph.nodes(data=True):
        print(f"Node {node}: {attr}")

def execute_parse_tree(tree):
    root = tree.nodes[0]
    root_id = 0
    res = visit_node(tree, root_id, -1)
    return res

def visit_node(tree, node_id, from_id):
    children = list(tree.neighbors(node_id))
    res = []
    for c in children:
        if c != from_id:
            child_result = visit_node(tree, c, node_id)
            if child_result is not None:
                res.append(child_result)
    current_node = tree.nodes[node_id]

    if current_node["type"] == "INITIAL":
        if res:
            return res[0]
        return None

    if current_node["type"] == "ASSIGN":
        if len(res) >= 2:
            symbol_table[res[0]] = res[1]
            return res[1]
        print("ERROR! Assignment requires at least two values")
        return None

    if current_node["type"] == "NUMBER":
        return current_node["value"]

    if current_node["type"] == "STRING":
        return current_node["value"]

    if current_node["type"] == "PENDING_NODE":
        if res:
            return res[0]
        return None

    if current_node["type"] == "VARIABLE_ASSIGN":
        return current_node["value"]

    if current_node["type"] == "VARIABLE":
        if current_node["value"] in symbol_table:
            return symbol_table[current_node["value"]]
        print("ERROR! Variable not found, returning 0")
        return 0

    if current_node["type"] == "ATTRIBUTE":
        if current_node["value"] in symbol_table:
            return symbol_table[current_node["value"]]
        print("ERROR! Attribute not found, returning 0")
        return 0

    if current_node["type"] == "FUNCTION_CALL" or current_node["type"] == "METHOD_CALL":
        if current_node["value"] in symbol_table:
            return symbol_table[current_node["value"]](*res) if res else symbol_table[current_node["value"]]()
        fn = search_cv2(current_node["value"])
        if fn is not None:
            return fn(*res)
        print("ERROR! Function not found, returning 0")
        return 0

    if current_node["type"] == "PLUS":
        if len(res) >= 2:
            return res[0] + res[1]
        print("ERROR! Plus operation requires at least two values")
        return None

    if current_node["type"] == "MINUS":
        if len(res) >= 2:
            return res[0] - res[1]
        print("ERROR! Minus operation requires at least two values")
        return None

    if current_node["type"] == "TIMES":
        if len(res) >= 2:
            return res[0] * res[1]
        print("ERROR! Times operation requires at least two values")
        return None

    if current_node["type"] == "DIV":
        if len(res) >= 2:
            return res[0] / res[1]
        print("ERROR! Division operation requires at least two values")
        return None

    if current_node["type"] == "POWER":
        if len(res) >= 2:
            return pow(res[0], res[1])
        print("ERROR! Power operation requires at least two values")
        return None

    if current_node["type"] == "GROUP":
        if res:
            return res[0]
        return None

    if current_node["type"] == "LIST":
        list_elements = [visit_node(tree, c, node_id) for c in children]
        return [elem for elem in list_elements if elem is not None]

    if current_node["type"] == "LIST_ACCESS":
        var_name = current_node["value"]
        if len(res) == 1:
            index = res[0]
            if var_name in symbol_table and isinstance(symbol_table[var_name], list):
                return symbol_table[var_name][index]
        if len(res) == 2:
            sublist_var = visit_node(tree, children[0], node_id)
            index = res[1]
            if isinstance(sublist_var, list):
                return sublist_var[index]
        print("ERROR! List or index not found, returning 0")
        return 0

    if current_node["type"] == "SLICE_ACCESS":
        var_name = current_node["value"]
        if len(res) == 2:
            start = res[0]
            end = res[1]
            if end == -1:
                end = None
            if var_name in symbol_table and isinstance(symbol_table[var_name], list):
                return symbol_table[var_name][start:end]
        print("ERROR! Slice or indices not found, returning 0")
        return 0

    return None

parser = yacc.yacc()

def execute_from_file(input_file, output_file):
    global parseGraph, NODE_COUNTER
    
    with open(input_file, 'r') as f:
        lines = f.readlines()

    results = []

    for data in lines:
        data = data.strip()
        if not data:
            continue

        parseGraph = nx.Graph()
        NODE_COUNTER = 0
        root = add_node({"type": "INITIAL", "label": "INIT"})
        try:
            result = parser.parse(data)
            if result is not None:
                parseGraph.add_edge(root["counter"], result["counter"])
                result_value = execute_parse_tree(parseGraph)
                results.append(f"The result of this operation '{data}' is '{result_value}'")
            else:
                results.append(f"Syntax error in operation '{data}'")
        except Exception as e:
            results.append(f"Error in operation '{data}': {e}")

    with open(output_file, 'w') as f:
        for result in results:
            f.write(result + '\n')

# Interactive loop and file-based execution
while True:
    data = input(">")
    if data == 'exit':
        break
    if data == 'st':
        print(symbol_table)
        continue
    if data == 'execute':
        execute_from_file('execute.txt', 'results.txt')
        print("Execution completed and results saved to 'results.txt'")
        continue

    parseGraph = nx.Graph()
    NODE_COUNTER = 0
    root = add_node({"type": "INITIAL", "label": "INIT"})
    result = parser.parse(data)

    parseGraph.add_edge(root["counter"], result["counter"])

    labels = nx.get_node_attributes(parseGraph, "label")
    pos = graphviz_layout(parseGraph, prog="dot")
    nx.draw(parseGraph, pos, labels=labels, with_labels=True)
    plt.show()

    result_value = execute_parse_tree(parseGraph)
    print("Result", result_value)

print("ended")
