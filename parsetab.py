
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftEQEQNOTEQLTLTEQGTGTEQleftPLUSMINUSleftTIMESDIVIDEMODABSTRACT ACTUAL ADDEQ AND ANNOTATION ARROW AS ASSIGN BOOLEAN BREAK BY CATCH CHAR CLASS COLON COMMA COMPANION CONST CONSTRUCTOR CONTINUE CROSSINLINE DATA DECREMENT DELIMITED_COMMENT DIVEQ DIVIDE DO DOT DOUBLE DOUBLECOLON DYNAMIC EACH ELSE ENUM EQEQ EXPECT EXTERNAL FINAL FINALLY FLOAT FOR FUN GT GTEQ ID IF IMPORT IN INCREMENT INFIX INIT INLINE INNER INTERFACE INTERNAL IS LATEINIT LBRACE LBRACK LINE_COMMENT LIST LISTOF LPAREN LT LTEQ MAP MAPOF MINUS MOD MODEQ MODULE MULTEQ NOINLINE NOT NOTEQ NOT_IN NOT_IS NULL NUMBER OBJECT OF OPEN OPERATOR OR OUT OVERRIDE PACKAGE PLUS PRINT PRINTLN PRIVATE PROTECTED PUBLIC RANGE RBRACE RBRACK READLINE REIFIED REPEAT RETURN RPAREN SEALED SEMICOLON SETOF SHEBANG STRING SUBEQ SUPER SUSPEND TAILREC THEN THIS THROW TIMES TO TRY TYPEDATA TYPEOF TYPE_ALIAS UNIT VAL VAR VARARG WHEN WHERE WHILE WSstatement_list : statement\n                      | statement_list statementstatement : assignment\n                 | expression\n                 | print\n                 | input\n                 | repeat\n                 | condition\n                 | loop\n                 | range\n                 | data_structureassignment : VAR ID ASSIGN expression\n                  | VAL ID ASSIGN expressionassignment : ID ASSIGN expressionexpression : expression NOTEQ expression\n                  | expression LT expression\n                  | expression LTEQ expression\n                  | expression GT expression\n                  | expression GTEQ expression\n                  | expression AND expression\n                  | expression OR expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression MOD expressionexpression : LPAREN expression RPARENexpression : NUMBER\n                  | FLOAT\n                  | DOUBLEexpression : BOOLEANexpression : STRINGexpression : IDrange : NUMBER RANGE NUMBERprint : PRINTLN LPAREN argument_list RPAREN \n             | PRINT LPAREN argument_list RPARENargument_list : expression\n                     | expression COMMA expression\n                     | argument_list COMMA expression\n                     | emptyinput : READLINE LPAREN RPARENrepeat : REPEAT LPAREN NUMBER RPAREN LBRACE statement_list RBRACEcondition : IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE\n                 | IF LPAREN expression RPAREN LBRACE statement_list RBRACEloop : WHILE LPAREN expression RPAREN LBRACE statement_list RBRACEloop : FOR LPAREN ID IN data_structure RPAREN LBRACE statement_list RBRACE\n            | FOR LPAREN ID IN range RPAREN LBRACE statement_list RBRACEcondition : WHEN LPAREN expression RPAREN LBRACE when_cases RBRACEwhen_cases : when_case\n                  | when_cases when_casewhen_case : expression_list ARROW statement_list\n                 | ELSE ARROW statement_listexpression_list : expression\n                       | expression_list COMMA expressiondata_structure : LISTOF LPAREN argument_list RPAREN\n                      | MAPOF LPAREN map_argument_list RPAREN\n                      | SETOF LPAREN argument_list RPARENmap_argument_list : map_element\n                         | map_argument_list COMMA map_elementmap_element : expression TO expressiontype : IDempty :'
    
_lr_action_items = {'VAR':([0,1,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,106,107,110,113,114,116,122,123,129,132,133,134,136,138,139,140,141,143,145,146,147,148,149,150,151,152,],[12,12,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,-55,-56,-57,12,12,12,12,12,12,-42,-44,-48,12,12,-45,12,12,12,12,12,12,12,-46,-47,12,-43,]),'VAL':([0,1,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,106,107,110,113,114,116,122,123,129,132,133,134,136,138,139,140,141,143,145,146,147,148,149,150,151,152,],[14,14,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,-55,-56,-57,14,14,14,14,14,14,-42,-44,-48,14,14,-45,14,14,14,14,14,14,14,-46,-47,14,-43,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,32,33,34,35,36,37,38,39,40,41,42,43,44,46,49,50,52,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,95,96,97,98,99,100,106,107,108,109,110,113,114,115,116,122,123,125,126,129,132,133,134,135,136,137,138,139,140,141,143,145,146,147,148,149,150,151,152,],[13,13,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,45,-33,47,50,-28,-29,-30,-31,-32,-2,50,50,50,50,50,50,50,50,50,50,50,50,50,-28,-33,50,50,50,50,50,89,50,50,50,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,50,-14,50,-27,-34,-41,-12,-13,-35,50,50,-36,-55,-56,50,50,-57,13,13,50,13,13,13,50,-49,13,-42,-44,-48,-50,13,50,13,-45,13,13,13,13,13,13,13,-46,-47,13,-43,]),'LPAREN':([0,1,2,3,4,5,6,7,8,9,10,11,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,49,50,52,53,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,95,96,97,98,99,100,106,107,108,109,110,113,114,115,116,122,123,125,126,129,132,133,134,135,136,137,138,139,140,141,143,145,146,147,148,149,150,151,152,],[15,15,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,15,-28,-29,-30,-31,-32,52,53,54,55,56,57,58,59,60,61,62,-2,15,15,15,15,15,15,15,15,15,15,15,15,15,-28,-33,15,15,15,15,15,15,15,15,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,15,-14,15,-27,-34,-41,-12,-13,-35,15,15,-36,-55,-56,15,15,-57,15,15,15,15,15,15,15,-49,15,-42,-44,-48,-50,15,15,15,-45,15,15,15,15,15,15,15,-46,-47,15,-43,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,11,13,15,16,17,18,19,20,32,33,34,35,36,37,38,39,40,41,42,43,44,46,49,50,51,52,53,55,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,95,96,97,98,99,100,105,106,107,108,109,110,113,114,115,116,122,123,125,126,129,132,133,134,135,136,137,138,139,140,141,143,145,146,147,148,149,150,151,152,],[16,16,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,49,-28,-29,-30,-31,-32,-2,49,49,49,49,49,49,49,49,49,49,49,49,49,-28,-33,79,49,49,85,49,49,49,49,49,49,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,49,-14,49,-27,-34,-41,-12,-13,-35,49,49,-36,119,-55,-56,49,49,-57,16,16,49,16,16,16,49,-49,16,-42,-44,-48,-50,16,49,16,-45,16,16,16,16,16,16,16,-46,-47,16,-43,]),'FLOAT':([0,1,2,3,4,5,6,7,8,9,10,11,13,15,16,17,18,19,20,32,33,34,35,36,37,38,39,40,41,42,43,44,46,49,50,52,53,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,95,96,97,98,99,100,106,107,108,109,110,113,114,115,116,122,123,125,126,129,132,133,134,135,136,137,138,139,140,141,143,145,146,147,148,149,150,151,152,],[17,17,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,17,-28,-29,-30,-31,-32,-2,17,17,17,17,17,17,17,17,17,17,17,17,17,-28,-33,17,17,17,17,17,17,17,17,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,17,-14,17,-27,-34,-41,-12,-13,-35,17,17,-36,-55,-56,17,17,-57,17,17,17,17,17,17,17,-49,17,-42,-44,-48,-50,17,17,17,-45,17,17,17,17,17,17,17,-46,-47,17,-43,]),'DOUBLE':([0,1,2,3,4,5,6,7,8,9,10,11,13,15,16,17,18,19,20,32,33,34,35,36,37,38,39,40,41,42,43,44,46,49,50,52,53,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,95,96,97,98,99,100,106,107,108,109,110,113,114,115,116,122,123,125,126,129,132,133,134,135,136,137,138,139,140,141,143,145,146,147,148,149,150,151,152,],[18,18,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,18,-28,-29,-30,-31,-32,-2,18,18,18,18,18,18,18,18,18,18,18,18,18,-28,-33,18,18,18,18,18,18,18,18,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,18,-14,18,-27,-34,-41,-12,-13,-35,18,18,-36,-55,-56,18,18,-57,18,18,18,18,18,18,18,-49,18,-42,-44,-48,-50,18,18,18,-45,18,18,18,18,18,18,18,-46,-47,18,-43,]),'BOOLEAN':([0,1,2,3,4,5,6,7,8,9,10,11,13,15,16,17,18,19,20,32,33,34,35,36,37,38,39,40,41,42,43,44,46,49,50,52,53,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,95,96,97,98,99,100,106,107,108,109,110,113,114,115,116,122,123,125,126,129,132,133,134,135,136,137,138,139,140,141,143,145,146,147,148,149,150,151,152,],[19,19,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,19,-28,-29,-30,-31,-32,-2,19,19,19,19,19,19,19,19,19,19,19,19,19,-28,-33,19,19,19,19,19,19,19,19,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,19,-14,19,-27,-34,-41,-12,-13,-35,19,19,-36,-55,-56,19,19,-57,19,19,19,19,19,19,19,-49,19,-42,-44,-48,-50,19,19,19,-45,19,19,19,19,19,19,19,-46,-47,19,-43,]),'STRING':([0,1,2,3,4,5,6,7,8,9,10,11,13,15,16,17,18,19,20,32,33,34,35,36,37,38,39,40,41,42,43,44,46,49,50,52,53,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,84,95,96,97,98,99,100,106,107,108,109,110,113,114,115,116,122,123,125,126,129,132,133,134,135,136,137,138,139,140,141,143,145,146,147,148,149,150,151,152,],[20,20,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,20,-28,-29,-30,-31,-32,-2,20,20,20,20,20,20,20,20,20,20,20,20,20,-28,-33,20,20,20,20,20,20,20,20,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,20,-14,20,-27,-34,-41,-12,-13,-35,20,20,-36,-55,-56,20,20,-57,20,20,20,20,20,20,20,-49,20,-42,-44,-48,-50,20,20,20,-45,20,20,20,20,20,20,20,-46,-47,20,-43,]),'PRINTLN':([0,1,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,106,107,110,113,114,116,122,123,129,132,133,134,136,138,139,140,141,143,145,146,147,148,149,150,151,152,],[21,21,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,-55,-56,-57,21,21,21,21,21,21,-42,-44,-48,21,21,-45,21,21,21,21,21,21,21,-46,-47,21,-43,]),'PRINT':([0,1,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,106,107,110,113,114,116,122,123,129,132,133,134,136,138,139,140,141,143,145,146,147,148,149,150,151,152,],[22,22,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,-55,-56,-57,22,22,22,22,22,22,-42,-44,-48,22,22,-45,22,22,22,22,22,22,22,-46,-47,22,-43,]),'READLINE':([0,1,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,106,107,110,113,114,116,122,123,129,132,133,134,136,138,139,140,141,143,145,146,147,148,149,150,151,152,],[23,23,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,-55,-56,-57,23,23,23,23,23,23,-42,-44,-48,23,23,-45,23,23,23,23,23,23,23,-46,-47,23,-43,]),'REPEAT':([0,1,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,106,107,110,113,114,116,122,123,129,132,133,134,136,138,139,140,141,143,145,146,147,148,149,150,151,152,],[24,24,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,-55,-56,-57,24,24,24,24,24,24,-42,-44,-48,24,24,-45,24,24,24,24,24,24,24,-46,-47,24,-43,]),'IF':([0,1,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,106,107,110,113,114,116,122,123,129,132,133,134,136,138,139,140,141,143,145,146,147,148,149,150,151,152,],[25,25,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,-55,-56,-57,25,25,25,25,25,25,-42,-44,-48,25,25,-45,25,25,25,25,25,25,25,-46,-47,25,-43,]),'WHEN':([0,1,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,106,107,110,113,114,116,122,123,129,132,133,134,136,138,139,140,141,143,145,146,147,148,149,150,151,152,],[26,26,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,-55,-56,-57,26,26,26,26,26,26,-42,-44,-48,26,26,-45,26,26,26,26,26,26,26,-46,-47,26,-43,]),'WHILE':([0,1,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,106,107,110,113,114,116,122,123,129,132,133,134,136,138,139,140,141,143,145,146,147,148,149,150,151,152,],[27,27,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,-55,-56,-57,27,27,27,27,27,27,-42,-44,-48,27,27,-45,27,27,27,27,27,27,27,-46,-47,27,-43,]),'FOR':([0,1,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,106,107,110,113,114,116,122,123,129,132,133,134,136,138,139,140,141,143,145,146,147,148,149,150,151,152,],[28,28,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,-55,-56,-57,28,28,28,28,28,28,-42,-44,-48,28,28,-45,28,28,28,28,28,28,28,-46,-47,28,-43,]),'LISTOF':([0,1,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,105,106,107,110,113,114,116,122,123,129,132,133,134,136,138,139,140,141,143,145,146,147,148,149,150,151,152,],[29,29,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,29,-55,-56,-57,29,29,29,29,29,29,-42,-44,-48,29,29,-45,29,29,29,29,29,29,29,-46,-47,29,-43,]),'MAPOF':([0,1,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,105,106,107,110,113,114,116,122,123,129,132,133,134,136,138,139,140,141,143,145,146,147,148,149,150,151,152,],[30,30,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,30,-55,-56,-57,30,30,30,30,30,30,-42,-44,-48,30,30,-45,30,30,30,30,30,30,30,-46,-47,30,-43,]),'SETOF':([0,1,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,105,106,107,110,113,114,116,122,123,129,132,133,134,136,138,139,140,141,143,145,146,147,148,149,150,151,152,],[31,31,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,31,-55,-56,-57,31,31,31,31,31,31,-42,-44,-48,31,31,-45,31,31,31,31,31,31,31,-46,-47,31,-43,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,106,107,110,132,133,134,139,149,150,152,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,-55,-56,-57,-42,-44,-48,-45,-46,-47,-43,]),'RBRACE':([2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,106,107,110,122,123,125,126,129,132,133,134,135,139,143,145,146,147,149,150,151,152,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,-55,-56,-57,132,133,134,-49,139,-42,-44,-48,-50,-45,-51,-52,149,150,-46,-47,152,-43,]),'ELSE':([2,3,4,5,6,7,8,9,10,11,13,16,17,18,19,20,32,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,79,84,95,96,97,100,106,107,110,115,125,126,132,133,134,135,139,143,145,149,150,152,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-33,-28,-29,-30,-31,-32,-2,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-14,-27,-34,-41,-12,-13,-35,-36,-55,-56,-57,128,128,-49,-42,142,-48,-50,-45,-51,-52,-46,-47,-43,]),'NOTEQ':([4,13,16,17,18,19,20,48,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,81,86,87,88,93,95,96,111,112,121,124,144,],[33,-33,-28,-29,-30,-31,-32,33,-28,-33,-15,-16,-17,-18,-19,33,33,-22,-23,-24,-25,-26,33,-27,33,33,33,33,33,33,33,33,33,33,33,33,]),'LT':([4,13,16,17,18,19,20,48,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,81,86,87,88,93,95,96,111,112,121,124,144,],[34,-33,-28,-29,-30,-31,-32,34,-28,-33,-15,-16,-17,-18,-19,34,34,-22,-23,-24,-25,-26,34,-27,34,34,34,34,34,34,34,34,34,34,34,34,]),'LTEQ':([4,13,16,17,18,19,20,48,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,81,86,87,88,93,95,96,111,112,121,124,144,],[35,-33,-28,-29,-30,-31,-32,35,-28,-33,-15,-16,-17,-18,-19,35,35,-22,-23,-24,-25,-26,35,-27,35,35,35,35,35,35,35,35,35,35,35,35,]),'GT':([4,13,16,17,18,19,20,48,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,81,86,87,88,93,95,96,111,112,121,124,144,],[36,-33,-28,-29,-30,-31,-32,36,-28,-33,-15,-16,-17,-18,-19,36,36,-22,-23,-24,-25,-26,36,-27,36,36,36,36,36,36,36,36,36,36,36,36,]),'GTEQ':([4,13,16,17,18,19,20,48,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,81,86,87,88,93,95,96,111,112,121,124,144,],[37,-33,-28,-29,-30,-31,-32,37,-28,-33,-15,-16,-17,-18,-19,37,37,-22,-23,-24,-25,-26,37,-27,37,37,37,37,37,37,37,37,37,37,37,37,]),'AND':([4,13,16,17,18,19,20,48,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,81,86,87,88,93,95,96,111,112,121,124,144,],[38,-33,-28,-29,-30,-31,-32,38,-28,-33,-15,-16,-17,-18,-19,-20,38,-22,-23,-24,-25,-26,38,-27,38,38,38,38,38,38,38,38,38,38,38,38,]),'OR':([4,13,16,17,18,19,20,48,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,81,86,87,88,93,95,96,111,112,121,124,144,],[39,-33,-28,-29,-30,-31,-32,39,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,39,-27,39,39,39,39,39,39,39,39,39,39,39,39,]),'PLUS':([4,13,16,17,18,19,20,48,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,81,86,87,88,93,95,96,111,112,121,124,144,],[40,-33,-28,-29,-30,-31,-32,40,-28,-33,40,40,40,40,40,40,40,-22,-23,-24,-25,-26,40,-27,40,40,40,40,40,40,40,40,40,40,40,40,]),'MINUS':([4,13,16,17,18,19,20,48,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,81,86,87,88,93,95,96,111,112,121,124,144,],[41,-33,-28,-29,-30,-31,-32,41,-28,-33,41,41,41,41,41,41,41,-22,-23,-24,-25,-26,41,-27,41,41,41,41,41,41,41,41,41,41,41,41,]),'TIMES':([4,13,16,17,18,19,20,48,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,81,86,87,88,93,95,96,111,112,121,124,144,],[42,-33,-28,-29,-30,-31,-32,42,-28,-33,42,42,42,42,42,42,42,42,42,-24,-25,-26,42,-27,42,42,42,42,42,42,42,42,42,42,42,42,]),'DIVIDE':([4,13,16,17,18,19,20,48,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,81,86,87,88,93,95,96,111,112,121,124,144,],[43,-33,-28,-29,-30,-31,-32,43,-28,-33,43,43,43,43,43,43,43,43,43,-24,-25,-26,43,-27,43,43,43,43,43,43,43,43,43,43,43,43,]),'MOD':([4,13,16,17,18,19,20,48,49,50,63,64,65,66,67,68,69,70,71,72,73,74,76,78,81,86,87,88,93,95,96,111,112,121,124,144,],[44,-33,-28,-29,-30,-31,-32,44,-28,-33,44,44,44,44,44,44,44,44,44,-24,-25,-26,44,-27,44,44,44,44,44,44,44,44,44,44,44,44,]),'ASSIGN':([13,45,47,],[46,75,77,]),'RANGE':([16,119,],[51,51,]),'RPAREN':([17,18,19,20,48,49,50,52,53,54,60,62,63,64,65,66,67,68,69,70,71,72,73,74,78,79,80,81,82,83,85,86,87,88,90,91,92,94,106,107,110,111,112,117,118,120,121,],[-29,-30,-31,-32,78,-28,-33,-62,-62,84,-62,-62,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-34,97,-37,-40,100,101,102,103,104,106,107,-58,110,-55,-56,-57,-39,-38,130,131,-59,-60,]),'COMMA':([17,18,19,20,49,50,52,53,60,62,63,64,65,66,67,68,69,70,71,72,73,74,78,80,81,82,83,90,91,92,94,111,112,120,121,124,127,144,],[-29,-30,-31,-32,-28,-33,-62,-62,-62,-62,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,98,99,-40,98,98,108,-58,98,-39,-38,-59,-60,-53,137,-54,]),'TO':([17,18,19,20,49,50,63,64,65,66,67,68,69,70,71,72,73,74,78,93,],[-29,-30,-31,-32,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,109,]),'ARROW':([17,18,19,20,49,50,63,64,65,66,67,68,69,70,71,72,73,74,78,124,127,128,144,],[-29,-30,-31,-32,-28,-33,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-53,136,138,-54,]),'IN':([89,],[105,]),'LBRACE':([101,102,103,104,130,131,142,],[113,114,115,116,140,141,148,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement_list':([0,113,114,116,136,138,140,141,148,],[1,122,123,129,143,145,146,147,151,]),'statement':([0,1,113,114,116,122,123,129,136,138,140,141,143,145,146,147,148,151,],[2,32,2,2,2,32,32,32,2,2,2,2,32,32,32,32,2,32,]),'assignment':([0,1,113,114,116,122,123,129,136,138,140,141,143,145,146,147,148,151,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'expression':([0,1,15,33,34,35,36,37,38,39,40,41,42,43,44,46,52,53,56,57,58,60,61,62,75,77,98,99,108,109,113,114,115,116,122,123,125,129,136,137,138,140,141,143,145,146,147,148,151,],[4,4,48,63,64,65,66,67,68,69,70,71,72,73,74,76,81,81,86,87,88,81,93,81,95,96,111,112,93,121,4,4,124,4,4,4,124,4,4,144,4,4,4,4,4,4,4,4,4,]),'print':([0,1,113,114,116,122,123,129,136,138,140,141,143,145,146,147,148,151,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'input':([0,1,113,114,116,122,123,129,136,138,140,141,143,145,146,147,148,151,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'repeat':([0,1,113,114,116,122,123,129,136,138,140,141,143,145,146,147,148,151,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'condition':([0,1,113,114,116,122,123,129,136,138,140,141,143,145,146,147,148,151,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'loop':([0,1,113,114,116,122,123,129,136,138,140,141,143,145,146,147,148,151,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'range':([0,1,105,113,114,116,122,123,129,136,138,140,141,143,145,146,147,148,151,],[10,10,118,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'data_structure':([0,1,105,113,114,116,122,123,129,136,138,140,141,143,145,146,147,148,151,],[11,11,117,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'argument_list':([52,53,60,62,],[80,83,90,94,]),'empty':([52,53,60,62,],[82,82,82,82,]),'map_argument_list':([61,],[91,]),'map_element':([61,108,],[92,120,]),'when_cases':([115,],[125,]),'when_case':([115,125,],[126,135,]),'expression_list':([115,125,],[127,127,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement_list","S'",1,None,None,None),
  ('statement_list -> statement','statement_list',1,'p_statement_list','sintactico.py',18),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','sintactico.py',19),
  ('statement -> assignment','statement',1,'p_statement','sintactico.py',36),
  ('statement -> expression','statement',1,'p_statement','sintactico.py',37),
  ('statement -> print','statement',1,'p_statement','sintactico.py',38),
  ('statement -> input','statement',1,'p_statement','sintactico.py',39),
  ('statement -> repeat','statement',1,'p_statement','sintactico.py',40),
  ('statement -> condition','statement',1,'p_statement','sintactico.py',41),
  ('statement -> loop','statement',1,'p_statement','sintactico.py',42),
  ('statement -> range','statement',1,'p_statement','sintactico.py',43),
  ('statement -> data_structure','statement',1,'p_statement','sintactico.py',44),
  ('assignment -> VAR ID ASSIGN expression','assignment',4,'p_assignment','sintactico.py',52),
  ('assignment -> VAL ID ASSIGN expression','assignment',4,'p_assignment','sintactico.py',53),
  ('assignment -> ID ASSIGN expression','assignment',3,'p_reasignement','sintactico.py',59),
  ('expression -> expression NOTEQ expression','expression',3,'p_expression_binop_boolean','sintactico.py',65),
  ('expression -> expression LT expression','expression',3,'p_expression_binop_boolean','sintactico.py',66),
  ('expression -> expression LTEQ expression','expression',3,'p_expression_binop_boolean','sintactico.py',67),
  ('expression -> expression GT expression','expression',3,'p_expression_binop_boolean','sintactico.py',68),
  ('expression -> expression GTEQ expression','expression',3,'p_expression_binop_boolean','sintactico.py',69),
  ('expression -> expression AND expression','expression',3,'p_expression_binop_boolean','sintactico.py',70),
  ('expression -> expression OR expression','expression',3,'p_expression_binop_boolean','sintactico.py',71),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop_arimetic','sintactico.py',87),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop_arimetic','sintactico.py',88),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop_arimetic','sintactico.py',89),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop_arimetic','sintactico.py',90),
  ('expression -> expression MOD expression','expression',3,'p_expression_binop_arimetic','sintactico.py',91),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','sintactico.py',117),
  ('expression -> NUMBER','expression',1,'p_expression_number','sintactico.py',127),
  ('expression -> FLOAT','expression',1,'p_expression_number','sintactico.py',128),
  ('expression -> DOUBLE','expression',1,'p_expression_number','sintactico.py',129),
  ('expression -> BOOLEAN','expression',1,'p_expression_boolean','sintactico.py',139),
  ('expression -> STRING','expression',1,'p_expression_string','sintactico.py',149),
  ('expression -> ID','expression',1,'p_expression_id','sintactico.py',159),
  ('range -> NUMBER RANGE NUMBER','range',3,'p_range','sintactico.py',169),
  ('print -> PRINTLN LPAREN argument_list RPAREN','print',4,'p_print','sintactico.py',174),
  ('print -> PRINT LPAREN argument_list RPAREN','print',4,'p_print','sintactico.py',175),
  ('argument_list -> expression','argument_list',1,'p_argument_list','sintactico.py',184),
  ('argument_list -> expression COMMA expression','argument_list',3,'p_argument_list','sintactico.py',185),
  ('argument_list -> argument_list COMMA expression','argument_list',3,'p_argument_list','sintactico.py',186),
  ('argument_list -> empty','argument_list',1,'p_argument_list','sintactico.py',187),
  ('input -> READLINE LPAREN RPAREN','input',3,'p_input','sintactico.py',202),
  ('repeat -> REPEAT LPAREN NUMBER RPAREN LBRACE statement_list RBRACE','repeat',7,'p_repeat','sintactico.py',208),
  ('condition -> IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE','condition',11,'p_condition','sintactico.py',219),
  ('condition -> IF LPAREN expression RPAREN LBRACE statement_list RBRACE','condition',7,'p_condition','sintactico.py',220),
  ('loop -> WHILE LPAREN expression RPAREN LBRACE statement_list RBRACE','loop',7,'p_loop_while','sintactico.py',238),
  ('loop -> FOR LPAREN ID IN data_structure RPAREN LBRACE statement_list RBRACE','loop',9,'p_loop_for','sintactico.py',250),
  ('loop -> FOR LPAREN ID IN range RPAREN LBRACE statement_list RBRACE','loop',9,'p_loop_for','sintactico.py',251),
  ('condition -> WHEN LPAREN expression RPAREN LBRACE when_cases RBRACE','condition',7,'p_condition_when','sintactico.py',263),
  ('when_cases -> when_case','when_cases',1,'p_when_cases','sintactico.py',274),
  ('when_cases -> when_cases when_case','when_cases',2,'p_when_cases','sintactico.py',275),
  ('when_case -> expression_list ARROW statement_list','when_case',3,'p_when_case','sintactico.py',286),
  ('when_case -> ELSE ARROW statement_list','when_case',3,'p_when_case','sintactico.py',287),
  ('expression_list -> expression','expression_list',1,'p_expression_list','sintactico.py',299),
  ('expression_list -> expression_list COMMA expression','expression_list',3,'p_expression_list','sintactico.py',300),
  ('data_structure -> LISTOF LPAREN argument_list RPAREN','data_structure',4,'p_data_structure','sintactico.py',304),
  ('data_structure -> MAPOF LPAREN map_argument_list RPAREN','data_structure',4,'p_data_structure','sintactico.py',305),
  ('data_structure -> SETOF LPAREN argument_list RPAREN','data_structure',4,'p_data_structure','sintactico.py',306),
  ('map_argument_list -> map_element','map_argument_list',1,'p_map_argument_list','sintactico.py',309),
  ('map_argument_list -> map_argument_list COMMA map_element','map_argument_list',3,'p_map_argument_list','sintactico.py',310),
  ('map_element -> expression TO expression','map_element',3,'p_map_element','sintactico.py',313),
  ('type -> ID','type',1,'p_type','sintactico.py',315),
  ('empty -> <empty>','empty',0,'p_empty','sintactico.py',318),
]
