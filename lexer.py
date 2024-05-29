# El modulo lex sirve para analizadores léxicos
import ply.lex as lex
from math import pi

symbol_table = dict()

symbol_table["PI"] = pi
symbol_table["E"] = 2.718281828459045

# Tokens a utilizar
tokens = (
    'NUMBER',
    'VARIABLE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'EQUAL',
    'FUNCTION'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_EQUAL = r'='


# Para usar los tokens necesitamos una función que empieze con t y el nombre del token
def t_NUMBER(t):
    #regular expression
    r'\d+\.?\d*'
    t.value = float(t.value)
    return t

def t_FUNCTION(t):
    f'[a-zA-Z_][a-zA-Z0-9_]*\((\d+\.?\d*|[a-zA-Z_][a-zA-Z0-9_]*)\)'
    print("****", t.value)
    s = t.value[0:-1].split("(")
    t.value = s
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Cuando no acepta ninguno de los tokens va con este
def t_error(t):
    print("Error on ", t.value)
    t.lexer.skip(1)

print("Lexer v1.0")

"""
Del archivo en el que este busca el set de token donde busque la función que acepte esos tokens
A esto se le conoce como callback
Leer las reglas de tokens que se han definido en el script.
Crear un objeto lexer que utiliza estas reglas para tokenizar cadenas de texto de entrada.
"""

lexer = lex.lex()
result = 0
current_op = 0

PLUS_OP = 1
MINUS_OP = 2
TIMES_OP = 3
DIV_OP = 4

while True:
    data = input(">")

    if data == "exit":
        break

    if data == "st":
        print(symbol_table)
        continue

    lexer.input(data)
    # restart values
    result = 0
    current_op = 0
    last_read_var = ""
    assignment = 0
    while True:
        tok = lexer.token()
        # print(tok)
        if not tok:
            print(f"Finish: {result}")
            if assignment != 0:
                symbol_table[last_read_var] = result
            break

        if tok.type == "NUMBER":
            if current_op == 0:
                result = tok.value
            if current_op == PLUS_OP:
                result += tok.value
            if current_op == MINUS_OP:
                result -= tok.value
            if current_op == TIMES_OP:
                result *= tok.value
            if current_op == DIV_OP:
                result /= tok.value

        if tok.type == "EQUAL":
            assignment = last_read_var
            result = 0

        if tok.type == "FUNCTION":
            try:
                symbol_table[tok.value[0]](float(tok.value[1]))
            except ValueError:
                if tok.value[1] in symbol_table:
                    val = symbol_table[tok.value[1]]
                else:
                    val = ":C"
                symbol_table[tok.value[0]](val)

            result = 0

        if tok.type == "VARIABLE":
            if assignment == 0 and current_op == 0:
                last_read_var = tok.value

            if tok.value in symbol_table:
                val = symbol_table[tok.value]
                result = val
            else:
                #print("Warning: symbol not found, replaced with 0")
                val = result

            if current_op == 0:
                result = val
            if current_op == PLUS_OP:
                result += val
            if current_op == MINUS_OP:
                result -= val
            if current_op == TIMES_OP:
                result *= val
            if current_op == DIV_OP:
                result /= val

        if tok.type == "PLUS":
            current_op = PLUS_OP

        if tok.type == "MINUS":
            current_op = MINUS_OP

        if tok.type == "TIMES":
            current_op = TIMES_OP

        if tok.type == "DIV":
            current_op = DIV_OP

print("\n ended")