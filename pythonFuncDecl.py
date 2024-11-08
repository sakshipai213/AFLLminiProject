import ply.lex as lex
import ply.yacc as yacc

# List of token names
tokens = (
    'DEF', 'IDENTIFIER', 'LPAREN', 'RPAREN', 'COLON', 'COMMA'
)

# Reserved keywords
reserved = {
    'def': 'DEF'
}

# Regular expressions for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_COMMA = r','

# A regular expression rule for identifiers (variable/function names)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Check if the identifier is actually a reserved keyword
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Define a rule for newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules
def p_function_declaration(p):
    '''function_declaration : DEF IDENTIFIER LPAREN parameters RPAREN COLON'''
    print("Valid function declaration!")
    p[0] = True  # Indicate successful parsing

def p_parameters(p):
    '''parameters : IDENTIFIER
                  | IDENTIFIER COMMA parameters
                  | empty'''
    pass

def p_empty(p):
    '''empty :'''
    pass

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}'")
    else:
        print("Syntax error at EOF")
    # Return an error indicator
    return None

# Build the parser
parser = yacc.yacc()

# Test the lexer and parser
def test_function_syntax(code):
    lexer.input(code)
    for token in lexer:
        print(token)
    result = parser.parse(code)
    if result:
        print("Function declaration syntax is correct.")
    else:
        print("Function declaration syntax is incorrect.")

# Example tests
test_code = [
    "def my_function():",
    "def another_function(param1, param2):",
    "def missing_paren(",
    "func():"
]

for code in test_code:
    print("\nTesting:", code)
    test_function_syntax(code)
