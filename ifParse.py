import ply.yacc as yacc
from ifLex import tokens  # Import tokens defined in the lexer

# Global flag for syntax errors
flag = 0

# Grammar rules
def p_if_statement(p):
    '''
    if_statement : IF conditions COLON statement
                 | IF conditions COLON NEWLINE INDENT statements DEDENT
    '''
    if len(p) == 5:
        p[0] = ('if', p[2], p[4])  # Single-line if statement
    else:
        p[0] = ('if', p[2], p[6])  # Multi-line if statement

def p_statements(p):
    '''
    statements : statements statement
               | statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''
    statement : assignment
              | if_statement
              | empty
    '''
    p[0] = p[1]

def p_assignment(p):
    '''
    assignment : ID EQUALS expression
    '''
    p[0] = ('assign', p[1], p[3])

def p_expression(p):
    '''
    expression : ID
               | NUMBER
               | STRING
               | expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_conditions(p):
    '''
    conditions : expression EQUALS expression
               | expression NOT_EQUALS expression
               | expression GREATER expression
               | expression LESSER expression
               | conditions AND conditions
               | conditions OR conditions
               | NOT conditions
    '''
    if len(p) == 3:
        p[0] = ('not', p[2])
    elif len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_error(p):
    print("Syntax error")
    global flag
    flag = 1

# Initialize the parser
parser = yacc.yacc()

if __name__ == "__main__":
    while True:
        flag = 0
        try:
            s = input('Enter the Python conditional statement: ')
        except EOFError:
            break
        if not s.strip():
            continue
        result = parser.parse(s)
        if flag == 0:
            print("Valid syntax")
            print("Result:", result)

