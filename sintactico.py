import ply.yacc as yacc
from lexico import *

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
# Aporte de Ronny, Eduardo y Robespierre
def p_statement(p):
    '''statement : assignment
                 | expression
                 | print
                 | input
                 | condition
                 | loop
                 | data_structure'''
# Aporte de Eduardo
def p_assignment(p):
    '''assignment : VAR ID ASSIGN expression
                  | VAL ID ASSIGN expression'''
# Aporte de Robespierre
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression EQEQ expression
                  | expression NOTEQ expression
                  | expression LT expression
                  | expression LTEQ expression
                  | expression GT expression
                  | expression GTEQ expression
                  | expression AND expression
                  | expression OR expression'''
# Aporte de Eduardo
def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
# Aporte de Robespierre
def p_expression_number(p):
    '''expression : NUMBER
                  | FLOAT
                  | DOUBLE'''
# Aporte de Ronny
def p_expression_boolean(p):
    '''expression : BOOLEAN'''
# Aporte de Robespierre
def p_expression_string(p):
    '''expression : STRING'''
# Aporte de Eduardo
def p_expression_id(p):
    '''expression : ID'''
# Aporte de Robespierre funcion 1
def p_print(p):
    '''print : PRINTLN LPAREN argument_list RPAREN
             | PRINT LPAREN argument_list RPAREN'''
# Aporte de Eduardo
def p_argument_list(p):
    '''argument_list : expression
                     | expression COMMA expression
                     | argument_list COMMA expression
                     | empty'''
# Aporte de Eduardo funcion 2
def p_input(p):
    '''input : READLINE LPAREN RPAREN'''
# Aporte de Ronny
def p_condition(p):
    '''condition : IF expression LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE
                 | IF expression LBRACE statement_list RBRACE'''
# Aporte Eduardo
def p_loop_while(p):
    '''loop : WHILE LPAREN expression RPAREN LBRACE statement_list RBRACE'''
# Aporte Robespierre
def p_loop_for(p):
    '''loop : FOR LPAREN ID IN data_structure RPAREN LBRACE statement_list RBRACE'''
#Aporte Robespierre
def p_condition_when(p):
    '''condition : WHEN LPAREN expression RPAREN LBRACE when_cases RBRACE'''

def p_when_cases(p):
    '''when_cases : when_case
                  | when_cases when_case'''

def p_when_case(p):
    '''when_case : expression_list ARROW statement_list
                 | ELSE ARROW statement_list'''

def p_expression_list(p):
    '''expression_list : expression
                       | expression_list COMMA expression'''

# Aporte de Ronny, Eduardo, Robespierre (Ese orden)
def p_data_structure(p):
    '''data_structure : LISTOF LPAREN argument_list RPAREN
                      | MAPOF LPAREN map_argument_list RPAREN
                      | SETOF LPAREN argument_list RPAREN'''
# Aporte de Robespierre
def p_map_argument_list(p):
    '''map_argument_list : map_element
                         | map_argument_list COMMA map_element'''
# Aporte de Robespierre
def p_map_element(p):
    '''map_element : expression TO expression'''
def p_type(p):
    '''type : ID'''

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print(f"Syntax error at '{p}'")

parser = yacc.yacc()

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


parser = yacc.yacc()

# Ejemplo de uso