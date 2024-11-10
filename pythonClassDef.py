import ply.lex as lex
import ply.yacc as yacc

# =============================
# Lexer Part
# =============================

# List of token names
tokens = [
    'CLASS', 'COLON', 'LPAREN', 'RPAREN',
    'ID', 'COMMA', 'DEF', 'PASS'
]

# Reserved keywords
reserved = {
    'class': 'CLASS',
    'def': 'DEF',
    'pass': 'PASS'
}

# Regular expressions for simple tokens
t_COLON = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','

# Token for identifiers (variable names, function names, etc.)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Token for newlines (to handle line numbers)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# =============================
# Parser Part
# =============================

# Parsing rules

# Dictionary to hold class definitions (for verification)
class_definitions = {}

def p_program(p):
    '''program : class_def program
               | empty'''
    pass

def p_class_definition(p):
    '''class_def : CLASS ID class_inheritance COLON class_body'''
    class_name = p[2]
    class_definitions[class_name] = True

def p_class_inheritance(p):
    '''class_inheritance : LPAREN ID RPAREN
                         | LPAREN ID COMMA ID RPAREN
                         | empty'''
    pass

def p_class_body(p):
    '''class_body : method_def class_body
                  | PASS class_body
                  | empty'''
    pass

def p_method_def(p):
    '''method_def : DEF ID LPAREN method_args RPAREN COLON statement_list'''
    pass

def p_method_args(p):
    '''method_args : ID
                   | ID COMMA method_args
                   | empty'''
    pass

def p_statement_list(p):
    '''statement_list : PASS
                      | empty'''
    pass

def p_empty(p):
    '''empty :'''
    pass

# Error rule for syntax errors
syntax_error_found = False

def p_error(p):
    global syntax_error_found
    syntax_error_found = True
    if p:
        print(f"Syntax error at token {p.type} (value: {p.value})")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# =============================
# Testing
# =============================
if __name__ == "__main__":
    # Sample Python code to test
    data = '''
class Test:
    def hello(self):
        pass

class AnotherClass{
    pass}
'''

    # Tokenize and parse the input
    lexer.input(data)
    print("Tokenizing input:")
    for tok in lexer:
        print(tok)

    # Reset syntax error flag
    syntax_error_found = False

    # Parse the code
    parser.parse(data)

    # Output result
    if not syntax_error_found:
        print("\nThe syntax is correct.")
    else:
        print("\nThe syntax is incorrect.")
