import ply.lex as lex

tokens = (
    'ID',
    'EQUALS',
    'NUMBER',
    'STRING',
    'BOOLEAN',
)

# Tokens
def t_BOOLEAN(t):
    r'\b(True|False)\b'
    t.value = True if t.value == "True" else False
    return t

def t_ID(t):
    r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    return t

def t_EQUALS(t):
    r'='
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"|\'[^\']*\''
    t.value = t.value[1:-1]  # Remove quotes
    return t

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character encountered: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer with an input string
data = input("Enter Python code: ")
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
