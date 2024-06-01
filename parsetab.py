
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA CONNECT DIV EQUAL EXP LBRACKET LPAREN MINUS NUMBER PLUS RBRACKET RPAREN STRING TIMES VARIABLE\n    assignment : VARIABLE EQUAL expression\n               | VARIABLE LBRACKET expression RBRACKET EQUAL expression\n               | list_access EQUAL expression\n    \n    assignment : VARIABLE EQUAL flow\n    \n    flow : VARIABLE CONNECT flow_functions\n    \n    flow_functions : flow_function_call CONNECT flow_functions\n    \n    flow_functions : flow_function_call\n    \n    flow_function_call : VARIABLE LPAREN params RPAREN\n    \n    assignment : expression\n    \n    expression : term\n               | string\n               | list_access\n    \n    string : STRING\n    \n    expression : expression PLUS term\n    \n    expression : expression MINUS term\n    \n    term : exponent\n    \n    term : term TIMES exponent\n    \n    term : term DIV exponent\n    \n    exponent : factor\n    \n    exponent : factor EXP factor\n    \n    factor : NUMBER\n    \n    factor : VARIABLE\n    \n    factor : LPAREN expression RPAREN\n    \n    factor : function_call\n    \n    function_call : VARIABLE LPAREN RPAREN\n    \n    function_call : VARIABLE LPAREN params RPAREN\n    \n    params : params COMMA expression\n            | expression\n    \n    factor : LBRACKET elements RBRACKET\n    \n    elements : elements COMMA expression\n             | expression\n    \n    list_access : VARIABLE LBRACKET expression RBRACKET\n                | VARIABLE LBRACKET expression COLON expression RBRACKET\n                | VARIABLE LBRACKET COLON expression RBRACKET\n                | VARIABLE LBRACKET expression COLON RBRACKET\n                | VARIABLE LBRACKET COLON RBRACKET\n                | list_access LBRACKET expression RBRACKET\n    '
    
_lr_action_items = {'VARIABLE':([0,4,12,14,15,16,17,18,23,24,25,26,27,33,41,42,49,51,55,62,68,69,],[2,22,22,29,22,22,38,38,22,22,38,38,38,22,22,22,59,22,22,22,22,59,]),'STRING':([0,4,12,14,15,16,23,24,33,41,42,51,55,62,68,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'NUMBER':([0,4,12,14,15,16,17,18,23,24,25,26,27,33,41,42,51,55,62,68,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'LPAREN':([0,2,4,12,14,15,16,17,18,22,23,24,25,26,27,29,33,38,41,42,51,55,59,62,68,],[12,16,12,12,12,12,12,12,12,16,12,12,12,12,12,16,12,16,12,12,12,12,68,12,12,]),'LBRACKET':([0,2,4,5,12,14,15,16,17,18,21,22,23,24,25,26,27,29,33,41,42,50,51,53,55,58,62,64,65,67,68,71,],[4,15,4,24,4,4,4,4,4,4,24,42,4,4,4,4,4,42,4,4,4,-32,4,-36,4,-37,4,-35,-34,-32,4,-33,]),'$end':([1,2,3,5,6,7,8,9,10,11,13,21,22,29,30,31,34,37,38,39,40,43,45,46,47,48,50,53,54,58,60,61,64,65,67,70,71,73,74,],[0,-22,-9,-12,-10,-11,-16,-13,-19,-21,-24,-12,-22,-22,-1,-4,-25,-14,-22,-15,-29,-3,-17,-18,-20,-23,-32,-36,-26,-37,-5,-7,-35,-34,-32,-2,-33,-6,-8,]),'EQUAL':([2,5,50,53,58,64,65,71,],[14,23,62,-36,-37,-35,-34,-33,]),'EXP':([2,10,11,13,22,29,34,38,40,48,54,],[-22,27,-21,-24,-22,-22,-25,-22,-29,-23,-26,]),'TIMES':([2,6,8,10,11,13,22,29,34,37,38,39,40,45,46,47,48,54,],[-22,25,-16,-19,-21,-24,-22,-22,-25,25,-22,25,-29,-17,-18,-20,-23,-26,]),'DIV':([2,6,8,10,11,13,22,29,34,37,38,39,40,45,46,47,48,54,],[-22,26,-16,-19,-21,-24,-22,-22,-25,26,-22,26,-29,-17,-18,-20,-23,-26,]),'PLUS':([2,3,5,6,7,8,9,10,11,13,20,21,22,28,29,30,32,34,36,37,38,39,40,43,44,45,46,47,48,50,52,53,54,56,57,58,63,64,65,66,67,70,71,],[-22,17,-12,-10,-11,-16,-13,-19,-21,-24,17,-12,-22,17,-22,17,17,-25,17,-14,-22,-15,-29,17,17,-17,-18,-20,-23,-32,17,-36,-26,17,17,-37,17,-35,-34,17,-32,17,-33,]),'MINUS':([2,3,5,6,7,8,9,10,11,13,20,21,22,28,29,30,32,34,36,37,38,39,40,43,44,45,46,47,48,50,52,53,54,56,57,58,63,64,65,66,67,70,71,],[-22,18,-12,-10,-11,-16,-13,-19,-21,-24,18,-12,-22,18,-22,18,18,-25,18,-14,-22,-15,-29,18,18,-17,-18,-20,-23,-32,18,-36,-26,18,18,-37,18,-35,-34,18,-32,18,-33,]),'RBRACKET':([6,7,8,9,10,11,13,19,20,21,22,32,33,34,37,38,39,40,44,45,46,47,48,51,52,53,54,56,57,58,63,64,65,67,71,],[-10,-11,-16,-13,-19,-21,-24,40,-31,-12,-22,50,53,-25,-14,-22,-15,-29,58,-17,-18,-20,-23,64,65,-36,-26,-30,67,-37,71,-35,-34,-32,-33,]),'COMMA':([6,7,8,9,10,11,13,19,20,21,22,34,35,36,37,38,39,40,45,46,47,48,53,54,56,58,64,65,66,67,71,72,],[-10,-11,-16,-13,-19,-21,-24,41,-31,-12,-22,-25,55,-28,-14,-22,-15,-29,-17,-18,-20,-23,-36,-26,-30,-37,-35,-34,-27,-32,-33,55,]),'RPAREN':([6,7,8,9,10,11,13,16,21,22,28,34,35,36,37,38,39,40,45,46,47,48,53,54,58,64,65,66,67,71,72,],[-10,-11,-16,-13,-19,-21,-24,34,-12,-22,48,-25,54,-28,-14,-22,-15,-29,-17,-18,-20,-23,-36,-26,-37,-35,-34,-27,-32,-33,74,]),'COLON':([6,7,8,9,10,11,13,15,21,22,32,34,37,38,39,40,42,45,46,47,48,53,54,57,58,64,65,67,71,],[-10,-11,-16,-13,-19,-21,-24,33,-12,-22,51,-25,-14,-22,-15,-29,33,-17,-18,-20,-23,-36,-26,51,-37,-35,-34,-32,-33,]),'CONNECT':([29,61,74,],[49,69,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignment':([0,],[1,]),'expression':([0,4,12,14,15,16,23,24,33,41,42,51,55,62,68,],[3,20,28,30,32,36,43,44,52,56,57,63,66,70,36,]),'list_access':([0,4,12,14,15,16,23,24,33,41,42,51,55,62,68,],[5,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'term':([0,4,12,14,15,16,17,18,23,24,33,41,42,51,55,62,68,],[6,6,6,6,6,6,37,39,6,6,6,6,6,6,6,6,6,]),'string':([0,4,12,14,15,16,23,24,33,41,42,51,55,62,68,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'exponent':([0,4,12,14,15,16,17,18,23,24,25,26,33,41,42,51,55,62,68,],[8,8,8,8,8,8,8,8,8,8,45,46,8,8,8,8,8,8,8,]),'factor':([0,4,12,14,15,16,17,18,23,24,25,26,27,33,41,42,51,55,62,68,],[10,10,10,10,10,10,10,10,10,10,10,10,47,10,10,10,10,10,10,10,]),'function_call':([0,4,12,14,15,16,17,18,23,24,25,26,27,33,41,42,51,55,62,68,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'elements':([4,],[19,]),'flow':([14,],[31,]),'params':([16,68,],[35,72,]),'flow_functions':([49,69,],[60,73,]),'flow_function_call':([49,69,],[61,61,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assignment","S'",1,None,None,None),
  ('assignment -> VARIABLE EQUAL expression','assignment',3,'p_assignment_assign','pars.py',97),
  ('assignment -> VARIABLE LBRACKET expression RBRACKET EQUAL expression','assignment',6,'p_assignment_assign','pars.py',98),
  ('assignment -> list_access EQUAL expression','assignment',3,'p_assignment_assign','pars.py',99),
  ('assignment -> VARIABLE EQUAL flow','assignment',3,'p_assignment_flow','pars.py',117),
  ('flow -> VARIABLE CONNECT flow_functions','flow',3,'p_flow','pars.py',127),
  ('flow_functions -> flow_function_call CONNECT flow_functions','flow_functions',3,'p_flow_functions','pars.py',141),
  ('flow_functions -> flow_function_call','flow_functions',1,'p_flow_functions_alone','pars.py',153),
  ('flow_function_call -> VARIABLE LPAREN params RPAREN','flow_function_call',4,'p_flow_function_call','pars.py',159),
  ('assignment -> expression','assignment',1,'p_assignment_expression','pars.py',170),
  ('expression -> term','expression',1,'p_expression_term','pars.py',176),
  ('expression -> string','expression',1,'p_expression_term','pars.py',177),
  ('expression -> list_access','expression',1,'p_expression_term','pars.py',178),
  ('string -> STRING','string',1,'p_string_def','pars.py',184),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','pars.py',190),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','pars.py',199),
  ('term -> exponent','term',1,'p_term_exponent','pars.py',208),
  ('term -> term TIMES exponent','term',3,'p_term_times','pars.py',214),
  ('term -> term DIV exponent','term',3,'p_term_divides','pars.py',223),
  ('exponent -> factor','exponent',1,'p_exponent_factor','pars.py',232),
  ('exponent -> factor EXP factor','exponent',3,'p_exponent_exp','pars.py',238),
  ('factor -> NUMBER','factor',1,'p_factor_num','pars.py',247),
  ('factor -> VARIABLE','factor',1,'p_factor_variable','pars.py',254),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','pars.py',260),
  ('factor -> function_call','factor',1,'p_factor_function_call','pars.py',268),
  ('function_call -> VARIABLE LPAREN RPAREN','function_call',3,'p_function_call_no_params','pars.py',274),
  ('function_call -> VARIABLE LPAREN params RPAREN','function_call',4,'p_function_call_params','pars.py',280),
  ('params -> params COMMA expression','params',3,'p_params','pars.py',289),
  ('params -> expression','params',1,'p_params','pars.py',290),
  ('factor -> LBRACKET elements RBRACKET','factor',3,'p_list_def','pars.py',299),
  ('elements -> elements COMMA expression','elements',3,'p_elements','pars.py',308),
  ('elements -> expression','elements',1,'p_elements','pars.py',309),
  ('list_access -> VARIABLE LBRACKET expression RBRACKET','list_access',4,'p_list_access','pars.py',318),
  ('list_access -> VARIABLE LBRACKET expression COLON expression RBRACKET','list_access',6,'p_list_access','pars.py',319),
  ('list_access -> VARIABLE LBRACKET COLON expression RBRACKET','list_access',5,'p_list_access','pars.py',320),
  ('list_access -> VARIABLE LBRACKET expression COLON RBRACKET','list_access',5,'p_list_access','pars.py',321),
  ('list_access -> VARIABLE LBRACKET COLON RBRACKET','list_access',4,'p_list_access','pars.py',322),
  ('list_access -> list_access LBRACKET expression RBRACKET','list_access',4,'p_list_access','pars.py',323),
]
