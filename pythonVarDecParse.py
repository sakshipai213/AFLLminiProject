import ply.yacc as yacc
from pythonVarDecLex import tokens

flag = 0

# Grammar rules
def p_assignment(p):
    '''
    assignment : ID EQUALS expression
    '''
    p[0] = ('assignment', p[1], p[3])

def p_expression(p):
    '''
    expression : NUMBER
               | STRING
               | BOOLEAN
               | ID
    '''
    p[0] = p[1]

def p_error(p):
    print("Syntax error")
    global flag
    flag = 1

# Build the parser
parser = yacc.yacc()

while True:
    flag = 0
    try:
        s = input('Enter the Python statement: ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    if flag == 0 and result:
        print("Result:", result)
