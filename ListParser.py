import ply.yacc as yacc
from ListLex import tokens

# Grammar rules for list definition
def p_list_assignment(p):
    '''list_assignment : ID EQUALS LBRACKET elements RBRACKET'''
    p[0] = {'name': p[1], 'values': p[4]}

def p_elements(p):
    '''elements : element
                | element COMMA elements'''
    if len(p) == 2:  # Single element
        p[0] = [p[1]]
    else:  # Multiple elements
        p[0] = [p[1]] + p[3]

def p_elements_trailing_comma(p):
    '''elements : element COMMA'''
    print(f"Syntax error: Trailing comma detected at position {p.lexpos(2)}")
    p_error(p)

def p_element(p):
    '''element : NUMBER'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    p[0] = None

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' (position {p.lexpos})")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

if __name__ == '__main__':
    # Interactive mode for testing
    print("Enter your list declaration (e.g., 'list = [1, 2, 3]')")
    print("Type 'exit' to quit.")
    while True:
        try:
            s = input('Enter a line: ')
            if s.lower() == 'exit':
                break
        except EOFError:
            break
        if not s.strip():
            continue
        try:
            result = parser.parse(s)
            if result:
                print("Parsed list:", result)
        except Exception as e:
            print(f"Error: {e}")
