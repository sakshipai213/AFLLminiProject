import ply.lex as lex

# Token definitions
tokens = (
    'ID',
    'EQUALS',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'NUMBER',
)

# Regular expressions for tokens
t_EQUALS = r'='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'

# Function for NUMBER (to convert value to integer)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters (e.g., spaces and tabs)
t_ignore = ' \t'

# Error handling for invalid characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

if __name__ == '__main__':
    # Test the lexer
    data = 'list = [1, 2, 3]'
    lexer.input(data)
    for token in lexer:
        print(token)
