import ply.lex as lex

'''
Eduardo Sanchez
'''
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'MODULE',
    'DIVIDE',
    'AND',
    'OR',
    'NEGATE',
    'EQUAL',
    'INCREMENT',
    'DECREMENT',
    'EQUALTO',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL'
)

t_PLUS = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_MODULE = r'\%'
t_DIVIDE = r'/'
t_AND = r'&&'
t_OR = r'\|\|'
t_NEGATE = r'!'
t_EQUAL = r'\='
t_INCREMENT = r'\+\+'
t_DECREMENT = r'\-\-'
t_EQUALTO = r'\=\='
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()

data = '''
3 + 4 * 10 % && || ! ++ -- = == > < >= <=
'''

lexer.input(data)

while True:
    tok = lexer.token()
    
    if not tok:
        break
    
    print(tok)

'''
Eduardo Sanchez
'''