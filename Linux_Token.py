from ply import lex
from ply import yacc

tokens = (
    'CD',
    'LS',
    'PWD',
    'TOUCH',
    'RM',
    'CAT',
    'ECHO',
    'GREP',
    'ID',
    'STRING',
    'GREATER',
    'LESS',
    'PIPE',
    'COMMENT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'NOT_EQUALS',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'TRUE',
    'FALSE',
    'IF',
    'ELSE',
    'FOR',
    'WHILE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'AND',
    'OR',
    'SEMICOLON',
    'DOLLAR',
)

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'=='
t_TRUE    = r'true'
t_FALSE   = r'false'
t_IF      = r'if'
t_ELSE    = r'else'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOLLAR  = r'\$'
t_CD      = r'cd'
t_ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_STRING  = r'"([^"]*)"'
t_GREATER = r'>'
t_LESS    = r'<'
t_PIPE    = r'\|'
t_SEMICOLON = r';'
t_COMMENT = r'\#.*'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
