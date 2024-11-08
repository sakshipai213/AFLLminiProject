import ply.lex as lex

# Define the tokens
tokens = (
    'IF', 'ELSE', 'COLON', 'NEWLINE', 'INDENT', 'DEDENT', 'ID',
    'NUMBER', 'STRING', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LESSER', 'GREATER', 'EQUALS', 'NOT_EQUALS', 'AND', 'OR', 'NOT'
)

# Keywords
def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

# Operators and delimiters
t_COLON = r':'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LESSER = r'<'
t_GREATER = r'>'
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_AND = r'and'
t_OR = r'or'
t_NOT = r'not'

# Literals
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\".*?\"|\'.*?\''
    return t

# Identifier
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Newline handling
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Placeholder for INDENT and DEDENT (requires custom logic)
t_INDENT = r'\t'
t_DEDENT = r'\t'

# Ignored characters
t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

if __name__ == "__main__":
    data = input("Enter code to tokenize: ")
    lexer.input(data)

    print("\nTokens:")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
