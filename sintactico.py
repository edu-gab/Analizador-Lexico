import ply.yacc as yacc
from lexico import *

## Analizador Sintáctico

# Comienza aporte de Ronny

# Estructura de control (WHILE)
def p_while(p):
    'ejec : WHILE LPAREN ID comparation INT RPAREN LBRACE option RBRACE'


# Estructura de datos (CLASS)
def p_classD(p):
    'ejec : CLASS ID LBRACE atribC RBRACE'


def p_atrib(p):
    'atrib : vas ID DOUBLEP TYPEDATA EQUALS data'


def p_comparation(p):
    '''comparation : EQUALS
    | GREATERTHAN
    | LESSTHAN
    '''


def p_print(p):
    'print : PRINTLN LPAREN data RPAREN'


def p_printDW(p):
    '''printDW : print
    | print printDW
    '''


# declaracion de funcion
def p_Sfunction(p):
    'ejec : FUN ID LPAREN funcionparametro RPAREN DOUBLEP data LBRACE RETURN ID RBRACE'


def p_dataT(p):
    'data : INT | CHAR | FLOAT | STR '


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
    'ejec : IF LPAREN ID comparation INT RPAREN LBRACE option RBRACE'


def p_elif(p):
    'ejec : IF LPAREN ID comparation INT RPAREN LBRACE option RBRACE ELSE LBRACE option RBRACE'


def p_assignment(p):
    'assignment : vas ID EQUALS data'


def p_assignmentL(p):
    'assignmentL : assignmentL assignment'


def p_assignmentLU(p):
    'assignmentL : assignment'


def p_vas(p):
    'vas : VAL|VAR'

# Termina aporte de Ronny



