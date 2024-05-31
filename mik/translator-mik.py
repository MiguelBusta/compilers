import ply.lex as lex
import ply.yacc as yacc
import matplotlib.pyplot as plt
import networkx as nx

from math import pi
from math import pow
from networkx.drawing.nx_pydot import graphviz_layout

parseGraph = None
NODE_COUNTER = 0

def add_node(attr):
    global parseGraph
    global NODE_COUNTER

    attr["counter"] = NODE_COUNTER
    parseGraph.add_node(NODE_COUNTER, **attr)
    NODE_COUNTER += 1

symbol_table = dict()

symbol_table["PI"] = pi
symbol_table["E"] = 2.718281828459045

def myPrint(value):
    print(value)

symbol_table["myPrint"] = myPrint

tokens = (
    'NUMBER',
    'FUNCTION',
    'VARIABLE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'EQUAL',
    'EXP',
    'LPAREN',
    'RPAREN'
    )

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_EQUAL = r'='
t_EXP = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+\.?\d*'
    t.value = float(t.value)
    return t


def t_FUNCTION(t):
    r'[a-zA-Z_][a-zA-Z0-9_]\(   (\d+\.?\d  |    [a-zA-Z_][a-zA-Z0-9_]*   )     \)'
    print("" , t.value)
    s = t.value[0:-1].split("(")
    t.value = s
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_error(t):
    print("Error on  ", t.value)
    t.lexer.skip(1)

print("Translator v1.0")

lexer = lex.lex()

def p_assignment_assign(p):
    """
    assignment : VARIABLE EQUAL expression
    """
    symbol_table[p[1]] = p[3]
    p[0] = p[3]


def p_assignment_expression(p):
    """
    assignment : expression
    """
    p[0] = p[1]

def p_expression_term(p):
    """
    expression : term
    """
    p[0] = p[1]

def p_expression_plus(p):
    """
    expression : expression PLUS term
    """
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    """
    expression : expression MINUS term
    """
    p[0] = p[1] - p[3]

def p_term_exponent(p):
    """
    term : exponent
    """
    p[0] = p[1]

def p_term_times(p):
    """
    term : term TIMES exponent
    """
    p[0] = p[1] * p[3]

def p_term_divides(p):
    """
    term : term DIV exponent
    """
    p[0] = p[1] / p[3]

def p_exponent_factor(p):
    """
    exponent : factor
    """
    p[0] = p[1]

def p_exponent_exp(p):
    """
    exponent : factor EXP factor
    """
    p[0] = pow(p[1], p[3])

def p_factor_num(p):
    """
    factor : NUMBER
    """
    p[0] = p[1]

def p_factor_variable(p):
    """
    factor : VARIABLE
    """
    p[0] = symbol_table[p[1]]

def p_factor_expr(p):
    """
    factor : LPAREN expression RPAREN
    """
    p[0] = p[2]

def p_error(p):
    print("Syntax error in input: ", p)

parser = yacc.yacc()

while True:
    data = input(">")

    if(data == 'exit'):
        break

    if(data == 'st'):
        print(symbol_table)
        continue

    parseGraph = nx.Graph()
    NODE_COUNTER = 0
    root = add_node({"type": "INITIAL", "label":"INIT"})

    result = parser.parse(data)

    labels = nx.get_node_attributes(parseGraph, "label")
    pos = graphviz_layout(parseGraph, prog="dot")
    nx.draw(parseGraph, pos, labels=labels, with_labels=True)
    plt.show()
    print("Result ", result)
print("\nended")