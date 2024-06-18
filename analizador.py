import ply.lex as lex
import datetime

#Comienza aporte Robespierre Triviño Roman
def generar_nombre_log(nombre):
    ahora = datetime.datetime.now()
    nombre_archivo = ahora.strftime(f"lexico-{nombre}-%d%m%Y-%Hh%M.txt")
    return nombre_archivo

def leer_algoritmo(nombre_archivo):
    try:
        with open("algoritmos/"+nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return ""

#Termina aporte Robespierre Triviño Roman


'''
Eduardo Sanchez
'''
tokens = (
    'NUMBER', 'FLOAT', 'BOOLEAN', 'NULL', 'CHAR', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'MODULE','DIVIDE', 'MOD',
    'INCREMENT', 'DECREMENT', 'AND', 'OR', 'NOT',
    'ASSIGN', 'ADDEQ', 'SUBEQ', 'MULTEQ', 'DIVEQ', 'MODEQ',
    'EQEQ', 'NOTEQ', 'LTEQ', 'GTEQ', 'LT', 'GT',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACK', 'RBRACK',
    'COMMA', 'DOT', 'COLON', 'SEMICOLON', 'ARROW', 'DOUBLECOLON',
    'ID', 'COMMENT', 'COMMENT_MULTI'
)

t_PLUS = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_MODULE = r'\%'
t_DIVIDE = r'/'
t_MOD = r'%' #Robespierre Triviño
t_INCREMENT = r'\+\+'
t_DECREMENT = r'\-\-'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_ASSIGN = r'\='#Robespierre Triviño
# Robespierre Triviño
t_ADDEQ = r'\+='
t_SUBEQ = r'-='
t_MULTEQ = r'\*='
t_DIVEQ = r'/='
t_MODEQ = r'%='
# Eduardo Sanchez
t_EQEQ = r'\=\='
t_GT = r'>'
t_LT = r'<'
t_GTEQ = r'>='
t_LTEQ = r'<='
# Comienza aporte Robespierre Triviño
t_COMMA = r','
t_DOT = r'\.'
t_COLON = r':'
t_SEMICOLON = r';'
t_ARROW = r'->'
t_DOUBLECOLON = r'::'
# Termina aporte Robespierre Triviño


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Aqui comienza aporte de Robespierre
def t_FLOAT(t):
    r'\d+\.\d+([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t

def t_BOOLEAN(t):
    r'true|false'
    t.value = (t.value == 'true')
    return t

def t_NULL(t):
    r'null'
    t.value = None
    return t

def t_CHAR(t):
    r'\'([^\\\n]|(\\[nrt0\'"\\]))\''
    t.value = t.value[1:-1]
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\[nrt0\'"\\]))*\"'
    t.value = t.value[1:-1]
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_COMMENT(t):
    r'//.*'
    pass

def t_COMMENT_MULTI(t):
    r'/\*(.|\n)*?\*/'
    pass
# Aqui termina aporte de Robespierre
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
# Aporte Robespierre Triviño
data = leer_algoritmo("prueba_robtrivi.txt")
file = open("logs/"+generar_nombre_log("robtrivi"), "w")

lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    file.write(f"{tok}\n")
    print(tok)

file.close()
'''
Eduardo Sanchez
'''