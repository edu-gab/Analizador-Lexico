import ply.yacc as yacc
from lexico import *


def is_variable_initialized(var):
    return var in variables

def get_variable_type(var):
    return variables[var] if var in variables else None

# Definición de variables
variables = {}
semantic_log = []
syntactic_log = []
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
    syntactic_log.append(f'Processing rule: {p.slice}')

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

# Aporte de Ronny
def p_function(p):
    '''function : FUN ID LPAREN argument_list RPAREN LBRACE statement_list RBRACE'''

    syntactic_log.append(f'Processing rule: {p.slice}')
    if not isinstance(p[4], list):
        semantic_log.append(f"Error semántico: La lista de argumentos {p[4]} no es válida")
        return
    if not isinstance(p[7], list):
        semantic_log.append(f"Error semántico: La lista de declaraciones {p[7]} no es válida")
        return
    p[0] = ('function', p[2], p[4], p[7])


# Aporte de Ronny, Eduardo y Robespierre
def p_statement(p):
    '''statement : assignment
                 | expression
                 | print
                 | input
                 | repeat
                 | condition
                 | loop
                 | function'''
    syntactic_log.append(f'Processing rule: {p.slice}')
    #Aporte de Eduardo Sanchez
    p[0] = p[1]


# Aporte de Eduardo
def p_assignment(p):
    '''assignment : VAR ID ASSIGN expression
                  | VAL ID ASSIGN expression'''
    syntactic_log.append(f'Processing rule: {p.slice}')
    #Aporte de Eduardo Sanchez
    variables[p[2]] = p[4]

def p_reasignement(p):
    '''assignment : ID ASSIGN expression'''
    # Aporte Robespierre
    syntactic_log.append(f'Processing rule: {p.slice}')

    if p[1] not in variables:
        semantic_log.append(f"Error semántico: La variable {p[1]} no ha sido inicializada")
        return
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

    # Aporte Robespierre
    syntactic_log.append(f'Processing rule: {p.slice}')
    if isinstance(p[1], str) and p[1] not in variables:
        semantic_log.append(f"Error semántico: La variable {p[1]} no ha sido inicializada")
        return
    if isinstance(p[3], str) and p[3] not in variables:
        semantic_log.append(f"Error semántico: La variable {p[3]} no ha sido inicializada")
        return
    
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

    
def p_expression_binop_arimetic(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression'''

    #Aporte de Eduardo Sanchez
    syntactic_log.append(f'Processing rule: {p.slice}')
    if not isinstance(p[1], str) or p[1] in variables:
        pass
    else:
        semantic_log.append(f"Error semantico: La variable {p[1]} no ha sido inicializada")
        return
    if not isinstance(p[3], str) or p[3] in variables:
        pass
    else:
        semantic_log.append(f"Error semantico: La variable {p[3]} no ha sido inicializada")
        return

# Aporte de Eduardo
def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''

    #Aporte de Eduardo Sanchez
    syntactic_log.append(f'Processing rule: {p.slice}')

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
    syntactic_log.append(f'Processing rule: {p.slice}')

    if not isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]]
    else:
        p[0] = p[1]

# Aporte de Ronny
def p_expression_boolean(p):
    '''expression : BOOLEAN'''

    #Aporte de Eduardo Sanchez
    syntactic_log.append(f'Processing rule: {p.slice}')

    if not isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]]
    else:
        p[0] = p[1]

# Aporte de Robespierre
def p_expression_string(p):
    '''expression : STRING'''

    #Aporte de Eduardo Sanchez
    syntactic_log.append(f'Processing rule: {p.slice}')

    if not isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]]
    else:
        p[0] = p[1]

# Aporte de Eduardo
def p_expression_id(p):
    '''expression : ID'''
    syntactic_log.append(f'Processing rule: {p.slice}')

    #Aporte de Eduardo Sanchez
    if not isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]]
    else:
        variables[p[1]] = None
        p[0] = p[1]

# Aporte dr Robespierre
def p_range(p):
    '''range : NUMBER RANGE NUMBER'''
    syntactic_log.append(f'Processing rule: {p.slice}')
    # Aporte de Robespierre
    p[0] = (p[1], p[3])

def p_expression_range(p):
    '''expression : range'''
    p[0] = p[1]

    #Aporte de Eduardo Sanchez
    syntactic_log.append(f'Processing rule: {p.slice}')

    if isinstance(p[1], str) and p[1] in variables:
        pass
    elif isinstance(p[1], int):
        pass
    else:
        semantic_log.append(f"Error semantico: La variable {p[1]} no ha sido inicializada")
        return
    
    if isinstance(p[3], str) and p[3] in variables:
        pass
    elif isinstance(p[3], int):
        pass
    else:
        semantic_log.append(f"Error semantico: La variable {p[3]} no ha sido inicializada")
        return
    
    p[0] = range(p[1], p[3])

# Aporte de Robespierre funcion 1
# Aqui va argument_list, lo cambie para probar, habria que hacer el cambio en argument list
def p_print(p):
    '''print : PRINTLN LPAREN argument_list RPAREN
             | PRINT LPAREN argument_list RPAREN'''

    ##Aporte de Eduardo Sanchez
    syntactic_log.append(f'Processing rule: {p.slice}')

    for exp in p[3]:
        if isinstance(exp, str) and exp not in variables:
            semantic_log.append(f"Error semántico: La variable {exp} no ha sido inicializada")
    p[0] = ('print', p[3])

# Aporte de Eduardo
def p_argument_list(p):
    '''argument_list : expression
                     | expression COMMA expression
                     | argument_list COMMA expression
                     | empty'''
    syntactic_log.append(f'Processing rule: {p.slice}')

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
    syntactic_log.append(f'Processing rule: {p.slice}')
    print("Ingrese texto: ")
    p[0] = input()

# Aporte de Robespierre funcion 3
def p_repeat(p):
    '''repeat : REPEAT LPAREN NUMBER RPAREN LBRACE statement_list RBRACE'''
    syntactic_log.append(f'Processing rule: {p.slice}')

    #Aporte de Eduardo
    if not isinstance(p[6], list):
        semantic_log.append(f"Error semántico: La lista de declaraciones {p[6]} no es válida")
    else:
        #Aporte Robespierre
        p[0] = ('repeat', p[3], p[6])


# Aporte de Ronny
def p_condition(p):
    '''condition : IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE
                 | IF LPAREN expression RPAREN LBRACE statement_list RBRACE'''
    syntactic_log.append(f'Processing rule: {p.slice}')

    if not isinstance(p[3], bool):
        semantic_log.append(f"Error semántico: La expresión {p[3]} no es booleana")
        return

    if not isinstance(p[6], list):
        semantic_log.append(f"Error semántico: La lista de declaraciones {p[6]} no es válida")
        return

    if len(p) >= 12 and not isinstance(p[10], list):
        semantic_log.append(f"Error semántico: La lista de declaraciones {p[10]} no es válida")


# Aporte Eduardo
def p_loop_while(p):
    '''loop : WHILE LPAREN expression RPAREN LBRACE statement_list RBRACE'''
    syntactic_log.append(f'Processing rule: {p.slice}')

    # Verificación semántica
    if not isinstance(p[3], bool):
        semantic_log.append(f"Error semántico: La expresión {p[3]} no es booleana")
        return

    if not isinstance(p[6], list):
        semantic_log.append(f"Error semántico: La lista de declaraciones {p[6]} no es válida")
        return

# Aporte de Ronny
# Aporte de Ronny
def p_loop_for(p):
    '''loop : FOR LPAREN ID IN expression RPAREN LBRACE statement_list RBRACE
            | FOR LPAREN ID IN range RPAREN LBRACE statement_list RBRACE'''
    syntactic_log.append(f'Processing rule: {p.slice}')

    # Verificación semántica
    if isinstance(p[5], str):
        if p[5] not in variables:
            semantic_log.append(f"Error semántico: La variable {p[5]} no ha sido inicializada")
            return
        data_structure = variables[p[5]]
    else:
        if not isinstance(p[5], (list, dict, set, tuple, range)):
            semantic_log.append(f"Error semántico: La estructura de datos {p[5]} no es válida")
            return
        else:
            data_structure = p[5]

    if not isinstance(p[8], list):
        semantic_log.append(f"Error semántico: La lista de declaraciones {p[8]} no es válida")
        return

    p[0] = ('for', p[3], data_structure, p[8])


#Aporte Robespierre
def p_condition_when(p):
    '''condition : WHEN LPAREN expression RPAREN LBRACE when_cases RBRACE'''
    syntactic_log.append(f'Processing rule: {p.slice}')

    # Verificación semántica
    if not isinstance(p[3], bool):
        semantic_log.append(f"Error semántico: La expresión {p[3]} no es booleana")
        return

    if not isinstance(p[6], list):
        semantic_log.append(f"Error semántico: Los casos 'when' {p[6]} no son válidos")
        return
    

def p_when_cases(p):
    '''when_cases : when_case
                  | when_cases when_case'''
    syntactic_log.append(f'Processing rule: {p.slice}')

    # Asumiendo que when_cases es una lista de casos
    if not isinstance(p[1], list):
        semantic_log.append(f"Error semántico: Los casos 'when' {p[1]} no son válidos")
        return
    
    if len(p) == 3 and not isinstance(p[2], list):
        semantic_log.append(f"Error semántico: Los casos 'when' {p[2]} no son válidos")
        return
    

def p_when_case(p):
    '''when_case : expression_list ARROW statement_list
                 | ELSE ARROW statement_list'''
    syntactic_log.append(f'Processing rule: {p.slice}')

    # Verificación semántica
    if not isinstance(p[1], list):
        semantic_log.append(f"Error semántico: La lista de expresiones {p[1]} no es válida")
        return
    
    if not isinstance(p[3], list):
        semantic_log.append(f"Error semántico: La declaración {p[3]} no es válida")
        return
    
    p[0] = (p[1], p[3])

def p_expression_list(p):
    '''expression_list : expression
                       | expression_list COMMA expression'''
    syntactic_log.append(f'Processing rule: {p.slice}')

    # Verificación semántica
    if len(p) == 1:
        p[0] = [p[1]]
    elif len(p) == 3:
        if isinstance(p[1], list):
            p[0] = p[1] + [p[3]]
        else:
            p[0] = [p[1], p[3]]
    else:
        p[0] = []

# Aporte de Ronny, Eduardo, Robespierre (Ese orden)
def p_data_structure(p):
    '''data_structure : LISTOF LPAREN argument_list RPAREN
                      | MAPOF LPAREN map_argument_list RPAREN
                      | SETOF LPAREN argument_list RPAREN'''
    syntactic_log.append(f'Processing rule: {p.slice}')

    if p[1] == 'listOf' or p[1] == 'setOf':
        p[0] = p[3]
    elif p[1] == 'mapOf':
        p[0] = dict(p[3])

def p_expression_data_structure(p):
    '''expression : data_structure'''
    p[0] = p[1]

# Aporte de Robespierre
def p_map_argument_list(p):
    '''map_argument_list : map_element
                         | map_argument_list COMMA map_element'''
    syntactic_log.append(f'Processing rule: {p.slice}')

    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_map_element(p):
    '''map_element : expression TO expression'''
    syntactic_log.append(f'Processing rule: {p.slice}')

    p[0] = (p[1], p[3])

def p_type(p):
    '''type : ID'''

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        syntactic_log.append(f"Error de sintaxis en token: {p.value} (tipo: {p.type})")
    else:
        syntactic_log.append("Error de sintaxis en EOF")

def p_function(p):
    '''function : FUN ID LPAREN argument_list RPAREN LBRACE statement_list RBRACE'''
    
    # Verificación semántica
    syntactic_log.append(f'Processing rule: {p.slice}')

    if not isinstance(p[4], list):
        semantic_log.append(f"Error semántico: La lista de argumentos {p[4]} no es válida")
        return

    if not isinstance(p[7], list):
        semantic_log.append(f"Error semántico: La lista de declaraciones {p[7]} no es válida")
        return

    p[0] = ('function', p[2], p[4], p[7])


parser = yacc.yacc()
def analisis_semantico_sintactico(data):
    global semantic_log,syntactic_log
    semantic_log = []
    syntactic_log = []
    parser.parse(data)
    print(semantic_log,syntactic_log)
    return semantic_log,syntactic_log

# Ejemplo de uso

sin_analyzer = yacc.yacc()

# while True:
#   try:
#     s = input('kotlin > ')
#   except EOFError:
#     break
#   if not s: continue
#   result = sin_analyzer.parse(s)
#   if result != None:
#     print(result)
#
#
# parser = yacc.yacc()
#
# # Ejemplo de uso