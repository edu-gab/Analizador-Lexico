import ply.yacc as yacc
from lexico import *

variables = {}

# Definiciones de precedencia para manejar operadores
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQEQ', 'NOTEQ', 'LT', 'LTEQ', 'GT', 'GTEQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
)

# Definición de reglas de gramática
# Aporte de Ronny
def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''

    #Aporte de Eduardo Sanchez
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        if p[1] is None:
            p[0] = [p[2]]
        elif isinstance(p[1], list):
            p[0] = p[1] + [p[2]]
        else:
            p[0] = [p[1], p[2]]
    else:
        p[0] = []

# Aporte de Ronny, Eduardo y Robespierre
def p_statement(p):
    '''statement : assignment
                 | expression
                 | print
                 | input
                 | repeat
                 | condition
                 | loop
                 | range'''

    #Aporte de Eduardo Sanchez
    p[0] = p[1]


# Aporte de Eduardo
def p_assignment(p):
    '''assignment : VAR ID ASSIGN expression
                  | VAL ID ASSIGN expression'''

    #Aporte de Eduardo Sanchez
    variables[p[2]] = p[4]

def p_reasignement(p):
    '''assignment : ID ASSIGN expression'''
    # Aporte Robespierre
    if p[1] not in variables:
        print(f"Error semántico: La variable {p[1]} no ha sido inicializada")
    else:
        variables[p[1]] = p[3]
        p[0] = (p[1], p[3])

# Aporte de Robespierre
def p_expression_binop_boolean(p):
    '''expression : expression NOTEQ expression
                  | expression LT expression
                  | expression LTEQ expression
                  | expression GT expression
                  | expression GTEQ expression
                  | expression AND expression
                  | expression OR expression'''
    if p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '&&':
        p[0] = p[1] and p[3]
    elif p[2] == '||':
        p[0] = p[1] or p[3]

    # Aporte Robespierre
    if isinstance(p[1], str) and p[1] not in variables:
        print(f"Error semántico: La variable {p[1]} no ha sido inicializada")
    if isinstance(p[3], str) and p[3] not in variables:
        print(f"Error semántico: La variable {p[3]} no ha sido inicializada")
def p_expression_binop_arimetic(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '%':
        p[0] = p[1] % p[3]
    #Aporte de Eduardo Sanchez
    if not isinstance(p[1], str) or p[1] in variables:
        pass
    else:
        print(f"Error semantico: La variable {p[1]} no ha sido inicializada")
        return

    if not isinstance(p[3], str) or p[3] in variables:
        pass
    else:
        print(f"Error semantico: La variable {p[3]} no ha sido inicializada")
        return

# Aporte de Eduardo
def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''

    #Aporte de Eduardo Sanchez
    if not isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]]
    else:
        p[0] = p[1]

# Aporte de Robespierre
def p_expression_number(p):
    '''expression : NUMBER
                  | FLOAT
                  | DOUBLE'''

    #Aporte de Eduardo Sanchez
    if not isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]]
    else:
        p[0] = p[1]

# Aporte de Ronny
def p_expression_boolean(p):
    '''expression : BOOLEAN'''

    #Aporte de Eduardo Sanchez
    if not isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]]
    else:
        p[0] = p[1]

# Aporte de Robespierre
def p_expression_string(p):
    '''expression : STRING'''

    #Aporte de Eduardo Sanchez
    if not isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]]
    else:
        p[0] = p[1]

# Aporte de Eduardo
def p_expression_id(p):
    '''expression : ID'''

    #Aporte de Eduardo Sanchez
    if not isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]]
    else:
        p[0] = p[1]

# Aporte dr Robespierre
def p_range(p):
    '''range : NUMBER RANGE NUMBER'''

# Aporte de Robespierre funcion 1
# Aqui va argument_list, lo cambie para probar, habria que hacer el cambio en argument list
def p_print(p):
    '''print : PRINTLN LPAREN argument_list RPAREN
             | PRINT LPAREN argument_list RPAREN'''

    ##Aporte de Eduardo Sanchez
    for exp in p[3]:
        if isinstance(exp, str) and exp not in variables:
            print(f"Error semántico: La variable {exp} no ha sido inicializada")
    p[0] = ('print', p[3])

# Aporte de Eduardo
def p_argument_list(p):
    '''argument_list : expression
                     | expression COMMA expression
                     | argument_list COMMA expression
                     | empty'''

    ##Aporte de Eduardo Sanchez
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        if isinstance(p[1], list):
            p[0] = p[1] + [p[3]]  # Si p[1] es una lista, concatenamos el nuevo argumento
        else:
            p[0] = [p[1], p[3]]  # Si p[1] no es una lista, creamos una nueva lista
    else:
        p[0] = []

# Aporte de Eduardo funcion 2
def p_input(p):
    '''input : READLINE LPAREN RPAREN'''
    print("Ingrese texto: ")
    p[0] = input()

# Aporte de Robespierre funcion 3
def p_repeat(p):
    '''repeat : REPEAT LPAREN NUMBER RPAREN LBRACE statement_list RBRACE'''

    #Aporte de Eduardo
    if not isinstance(p[6], list):
        print(f"Error semántico: La lista de declaraciones {p[6]} no es válida")
    else:
        #Aporte Robespierre
        p[0] = ('repeat', p[3], p[6])


# Aporte de Ronny
def p_condition(p):
    '''condition : IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE
                 | IF LPAREN expression RPAREN LBRACE statement_list RBRACE'''

    print(p[3])
    # Verificación semántica
    if not isinstance(p[3], bool):
        print(f"Error semántico: La expresión {p[3]} no es booleana")
        return

    if not isinstance(p[6], list):
        print(f"Error semántico: La lista de declaraciones {p[6]} no es válida")
        return

    if len(p) >= 12 and not isinstance(p[10], list):
        print(f"Error semántico: La lista de declaraciones {p[10]} no es válida")


# Aporte Eduardo
def p_loop_while(p):
    '''loop : WHILE LPAREN expression RPAREN LBRACE statement_list RBRACE'''
    # Verificación semántica
    if not isinstance(p[3], bool):
        print(f"Error semántico: La expresión {p[3]} no es booleana")
        return

    if not isinstance(p[6], list):
        print(f"Error semántico: La lista de declaraciones {p[6]} no es válida")
        return

# Aporte Robespierre
def p_loop_for(p):
    '''loop : FOR LPAREN ID IN expression RPAREN LBRACE statement_list RBRACE
            | FOR LPAREN ID IN range RPAREN LBRACE statement_list RBRACE'''

    # Aporte de Robespierre
    if isinstance(p[4], str) and p[4] not in variables:
        print(f"Error semántico: La variable {p[4]} no ha sido inicializada")
        return
    elif isinstance(p[4], str):
        data_structure = variables[p[4]]
    else:
        data_structure = p[4]

    if not isinstance(data_structure, (list, dict, set, tuple)):
        print(f"Error semántico: La estructura de datos {data_structure} no es válida")
        return

    if not isinstance(p[7], list):
        print(f"Error semántico: La lista de declaraciones {p[7]} no es válida")
        return

    p[0] = ('for', p[3], data_structure, p[7])

#Aporte Robespierre
def p_condition_when(p):
    '''condition : WHEN LPAREN expression RPAREN LBRACE when_cases RBRACE'''

    # Verificación semántica
    if not isinstance(p[2], bool):
        print(f"Error semántico: La expresión {p[2]} no es booleana")
    elif not isinstance(p[5], list):
        print(f"Error semántico: Los casos 'when' {p[5]} no son válidos")
    else:
        p[0] = ('when', p[3], p[6])


def p_when_cases(p):
    '''when_cases : when_case
                  | when_cases when_case'''

    # Asumiendo que when_cases es una lista de casos
    if not isinstance(p[1], list):
        print(f"Error semántico: Los casos 'when' {p[1]} no son válidos")
    elif len(p) == 3 and not isinstance(p[2], list):
        print(f"Error semántico: Los casos 'when' {p[2]} no son válidos")
    else:
        pass

def p_when_case(p):
    '''when_case : expression_list ARROW statement_list
                 | ELSE ARROW statement_list'''

    # Verificación semántica
    if not isinstance(p[1], list):
        print(f"Error semántico: La lista de expresiones {p[1]} no es válida")
    elif not isinstance(p[3], list):
        print(f"Error semántico: La declaración {p[3]} no es válida")
    else:
        pass


def p_expression_list(p):
    '''expression_list : expression
                       | expression_list COMMA expression'''

# Aporte de Ronny, Eduardo, Robespierre (Ese orden)
def p_data_structure(p):
    '''data_structure : LISTOF LPAREN argument_list RPAREN
                      | MAPOF LPAREN map_argument_list RPAREN
                      | SETOF LPAREN argument_list RPAREN'''
    if p[1] == 'LISTOF' or p[1] == 'SETOF':
        p[0] = p[3]
    elif p[1] == 'MAPOF':
        p[0] = dict(p[3])
def p_expression_data_structure(p):
    '''expression : data_structure'''
    p[0] = p[1]

# Aporte de Robespierre
def p_map_argument_list(p):
    '''map_argument_list : map_element
                         | map_argument_list COMMA map_element'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_map_element(p):
    '''map_element : expression TO expression'''
    p[0] = (p[1], p[3])
def p_type(p):
    '''type : ID'''

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        print("Error de sintaxis en token:", p)
    else:
        print("Syntax error at EOF")
parser = yacc.yacc()

# Ejemplo de uso

sin_analyzer = yacc.yacc()

while True:
  try:
    s = input('kotlin > ')
  except EOFError:
    break
  if not s: continue
  result = sin_analyzer.parse(s)
  if result != None:
    print(result)
#
#
# parser = yacc.yacc()
#
# # Ejemplo de uso