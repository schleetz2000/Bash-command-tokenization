from ply import yacc
from Lexica import tokens
from Lexica import lexer

def p_command_list(p):
    '''command_list : command_list command SEMICOLON
                    | command SEMICOLON'''
    if len(p) == 4:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_command(p):
    '''command : CD ID
               | LS
               | PWD
               | TOUCH ID
               | RM ID
               | CAT ID
               | ECHO STRING
               | GREP STRING
               | IF LPAREN expression RPAREN LBRACE command_list RBRACE ELSE LBRACE command_list RBRACE
               | WHILE LPAREN expression RPAREN LBRACE command_list RBRACE'''
    if len(p) == 3:
        p[0] = {'type': p[1], 'value': p[2]}
    elif len(p) == 2:
        p[0] = {'type': p[1]}
    elif len(p) == 5:
        p[0] = {'type': p[1], 'value': p[2]}
    elif len(p) == 7:
        p[0] = {'type': p[1], 'value': p[2]}
    elif len(p) == 11:
        p[0] = {'type': 'if', 'condition': p[3], 'true_branch': p[6], 'false_branch': p[9]}
    elif len(p) == 8:
        p[0] = {'type': 'while', 'condition': p[3], 'body': p[6]}

def p_expression(p):
    '''expression : ID EQUALS ID
                  | ID GREATER ID
                  | ID LESS ID
                  | ID GREATER_EQUAL ID
                  | ID LESS_EQUAL ID
                  | ID NOT_EQUALS ID
                  | ID AND ID
                  | ID OR ID
                  | TRUE
                  | FALSE'''
    if len(p) == 4:
        p[0] = {'left': p[1], 'operator': p[2], 'right': p[3]}
    else:
        p[0] = p[1]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

def parse(data):
    return parser.parse(data, lexer=lexer)
