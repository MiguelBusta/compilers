
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIV EQUAL EXP FUNCTION LPAREN MINUS NUMBER PLUS RPAREN TIMES VARIABLE\n    assignment : VARIABLE EQUAL expression\n    \n    assignment : expression\n    \n    expression : term\n    \n    expression : expression PLUS term\n    \n    expression : expression MINUS term\n    \n    term : exponent\n    \n    term : term TIMES exponent\n    \n    term : term DIV exponent\n    \n    exponent : factor\n    \n    exponent : factor EXP factor\n    \n    factor : NUMBER\n    \n    factor : VARIABLE\n    \n    factor : LPAREN expression RPAREN\n    '
    
_lr_action_items = {'VARIABLE':([0,8,9,10,11,12,13,14,],[2,16,16,16,16,16,16,16,]),'NUMBER':([0,8,9,10,11,12,13,14,],[7,7,7,7,7,7,7,7,]),'LPAREN':([0,8,9,10,11,12,13,14,],[8,8,8,8,8,8,8,8,]),'$end':([1,2,3,4,5,6,7,16,17,18,19,20,21,22,23,],[0,-12,-2,-3,-6,-9,-11,-12,-1,-4,-5,-7,-8,-10,-13,]),'EQUAL':([2,],[9,]),'EXP':([2,6,7,16,23,],[-12,14,-11,-12,-13,]),'TIMES':([2,4,5,6,7,16,18,19,20,21,22,23,],[-12,12,-6,-9,-11,-12,12,12,-7,-8,-10,-13,]),'DIV':([2,4,5,6,7,16,18,19,20,21,22,23,],[-12,13,-6,-9,-11,-12,13,13,-7,-8,-10,-13,]),'PLUS':([2,3,4,5,6,7,15,16,17,18,19,20,21,22,23,],[-12,10,-3,-6,-9,-11,10,-12,10,-4,-5,-7,-8,-10,-13,]),'MINUS':([2,3,4,5,6,7,15,16,17,18,19,20,21,22,23,],[-12,11,-3,-6,-9,-11,11,-12,11,-4,-5,-7,-8,-10,-13,]),'RPAREN':([4,5,6,7,15,16,18,19,20,21,22,23,],[-3,-6,-9,-11,23,-12,-4,-5,-7,-8,-10,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignment':([0,],[1,]),'expression':([0,8,9,],[3,15,17,]),'term':([0,8,9,10,11,],[4,4,4,18,19,]),'exponent':([0,8,9,10,11,12,13,],[5,5,5,5,5,20,21,]),'factor':([0,8,9,10,11,12,13,14,],[6,6,6,6,6,6,6,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assignment","S'",1,None,None,None),
  ('assignment -> VARIABLE EQUAL expression','assignment',3,'p_assignment_assign','translator-mik.py',81),
  ('assignment -> expression','assignment',1,'p_assignment_expression','translator-mik.py',89),
  ('expression -> term','expression',1,'p_expression_term','translator-mik.py',95),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','translator-mik.py',101),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','translator-mik.py',107),
  ('term -> exponent','term',1,'p_term_exponent','translator-mik.py',113),
  ('term -> term TIMES exponent','term',3,'p_term_times','translator-mik.py',119),
  ('term -> term DIV exponent','term',3,'p_term_divides','translator-mik.py',125),
  ('exponent -> factor','exponent',1,'p_exponent_factor','translator-mik.py',131),
  ('exponent -> factor EXP factor','exponent',3,'p_exponent_exp','translator-mik.py',137),
  ('factor -> NUMBER','factor',1,'p_factor_num','translator-mik.py',143),
  ('factor -> VARIABLE','factor',1,'p_factor_variable','translator-mik.py',149),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','translator-mik.py',155),
]