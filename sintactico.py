import ply.yacc as yacc
from lexico import *


## Analizador Sintáctico

# Comienza aporte de Ronny

# Estructura de control (WHILE)
def p_while(p):
    'exec : WHILE LPAREN ID comparation NUMBER RPAREN LBRACE option RBRACE'


# Estructura de datos (CLASS)
def p_classD(p):
    'exec : CLASS ID LBRACE atribC RBRACE'


def p_atrib(p):
    'atrib : vas ID COLON TYPEDATA ASSIGN data'


def p_comparation(p):
    '''comparation : EQEQ
    | GT
    | LT
    | GTEQ
    | LTEQ
    '''


def p_print(p):
    'print : PRINTLN LPAREN data RPAREN'


def p_printDW(p):
    '''printDW : print
    | print printDW
    '''


# Declaracion de funcion
def p_Sfunction(p):
    'exec : FUN ID LPAREN funcionparametro RPAREN COLON data LBRACE RETURN ID RBRACE'


def p_dataT(p):
    '''data : NUMBER 
    | CHAR 
    | FLOAT 
    | STRING '''


def p_atribC(p):
    ''' atribC : atrib
    | atrib atribC
    '''


def p_option(p):
    '''option : assignment
    | assignmentL
    | printDW
    '''


def p_Cif(p):
    'exec : IF LPAREN ID comparation NUMBER RPAREN LBRACE option RBRACE'


def p_elif(p):
    'exec : IF LPAREN ID comparation NUMBER RPAREN LBRACE option RBRACE ELSE LBRACE option RBRACE'


def p_assignment(p):
    'assignment : vas ID ASSIGN data'


def p_assignmentL(p):
    'assignmentL : assignmentL assignment'


def p_assignmentLU(p):
    'assignmentL : assignment'


def p_vas(p):
    '''vas : VAL
    | VAR'''

# Termina aporte de Ronny


# Comienza aporte Robespierre Triviño
# for (i in 2){}
def p_for1(p):
  'exec : FOR LPAREN ID IN NUMBER RPAREN LBRACE RBRACE'


# val nombres: List<String> = listOf("Juan", "María", "Pedro",....)
# val nombres: List<int> = listOf(1,2,3,4,....)
def p_lista1(p):
  'exec : VAL ID COLON LIST LT liststring RPAREN'

def p_liststring(p):
    ''' liststring : STRING GT ASSIGN listof LPAREN listadostringproduccion
  | NUMBER GT ASSIGN listof LPAREN listadointproduccion
  '''


def p_listadostring(p):
    'listadostring : STRING'


def p_listadostringproduccion(p):
    ''' listadostringproduccion : listadostring
  | listadostring COMMA listadostringproduccion
  '''


def p_listadoint(p):
    'listadoint : NUMBER'


def p_listadointproduccion(p):
    ''' listadointproduccion : listadoint
  | listadoint COMMA listadointproduccion
  '''


# fun nombreFuncion(parametro1: Tipo, parametro2: Tipo): Unit {}
def p_funcion(p):
  'exec : FUN ID LPAREN funcionproduccion RPAREN COLON UNIT LBRACE RBRACE'

def p_funcionparametro(p):
    ''' funcionparametro : ID COLON funciondato
  '''


def p_funciondato(p):
    ''' funciondato : STRING
  | NUMBER
  '''


def p_funcionproduccion(p):
    ''' funcionproduccion : funcionparametro
  | ID COLON funciondato COMMA funcionproduccion
  '''


def p_error(p):
    if p:
        print("Error de sintaxis en token:", p.type)
    # sintactico.errok()
    else:
        print("Syntax error at EOF")


# Estructura de control - ForEach
# For Each: list.forEach {(it)}
def p_forEach(p):
    'exec : ID DOT FOR EACH LBRACE PRINTLN LPAREN ID RPAREN RBRACE'


# Estructura de datos - Diccionario o Mapa
# Map<String, Int> = mapOf( Pair("Num1", 1), Pair("Num2", 2), Pair("Num3", 3))
def p_map(p):
    '''exec : MAPOF LPAREN pares RPAREN'''


def p_pares(p):
    '''pares : pair
            | pair COMMA pares
             '''
def p_pair(p):
    '''pair : data TO data'''

#Función con parámetro preterminado
#fun nombreFuncion(parametro1: Tipo, parametro2: Tipo = valorPredeterminado) { codigo }
def p_exec(p):
    '''exec : function'''


def p_function(p):
    '''function : FUN ID LPAREN params RPAREN COLON LBRACE RBRACE'''

def p_params(p):
    '''params : param
              | param COMMA params'''


def p_param(p):
    '''param : ID COLON TYPEDATA
             | ID COLON TYPEDATA ASSIGN data'''


# Función
def p_funUE(p):
  'exec : FUN ID LPAREN funcionproduccion RPAREN COLON TYPEDATA ASSIGN assignment'

sin_analyzer = yacc.yacc()


while True:
    try:
        s = input('sql > ')
    except EOFError:
        break
    if not s: continue
    result = sin_analyzer.parse(s)
    if result != None:
        print(result)
