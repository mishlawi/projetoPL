
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AC ADD AND AP DIFF DIV ELSE EQUAL FC FP GoE Greater IF IGUAL INT LoE Lower MOD MUL NOT Nint OR PRA PRF PRINT SCAN SUB VAR WHILEProgram : ComandsComands : Comand ComandsComands : ComandComand : AtribuitionComand : ConditionalComand : IOConditional : IF AP Condition FP AC Comands FC ExtensionExtension :  ELSE AC Comands FCExtension : Condition : Condition OR Condition2Condition : Condition2Condition2 : Condition2 AND Condition3Condition2 : Condition3Condition3 : NOT ConditionCondition3 : RelExpressionCondition3 : AP Condition FPRelExpression : Expression ContinuationContinuation : OpRel ExpressionContinuation : OpRel : GoEOpRel : LoEOpRel : LowerOpRel : GreaterOpRel : IGUALOpRel : DIFFAtribuition : VAR PRA Nint PRFAtribuition : INT VAR PRA Nint PRF EQUAL NintAtribuition : INT VAR RestRest : EQUAL Expression Rest : Atribuition : VAR EQUAL ExpressionExpression : Expression ADD ValuesExpression : Expression SUB ValuesExpression : Values Values : ValueValues : Values MUL ValueValues : Values DIV ValueValues : Values MOD ValueValue : NintValue : VARValue : AP Expression FPIO : INPUTIO : OUTPUTINPUT : SCAN AP Expression FPOUTPUT : PRINT AP Expression FPOUTPUT : PRINT AP VAR PRA Nint PRF FP'
    
_lr_action_items = {'VAR':([0,3,4,5,6,8,10,11,16,17,18,19,20,22,23,24,25,26,27,29,30,31,35,41,42,43,44,45,46,49,53,54,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,75,83,84,85,86,88,90,],[7,7,-4,-5,-6,17,-42,-43,22,-30,22,22,40,-40,-31,-34,-35,-39,22,22,-28,22,22,-26,22,22,22,22,22,-29,22,22,22,-20,-21,-22,-23,-24,-25,-44,-45,-32,-33,-36,-37,-38,-41,7,-27,-9,-46,-7,7,-8,]),'INT':([0,3,4,5,6,10,11,17,22,23,24,25,26,30,41,49,64,65,67,68,69,70,71,72,75,83,84,85,86,88,90,],[8,8,-4,-5,-6,-42,-43,-30,-40,-31,-34,-35,-39,-28,-26,-29,-44,-45,-32,-33,-36,-37,-38,-41,8,-27,-9,-46,-7,8,-8,]),'IF':([0,3,4,5,6,10,11,17,22,23,24,25,26,30,41,49,64,65,67,68,69,70,71,72,75,83,84,85,86,88,90,],[9,9,-4,-5,-6,-42,-43,-30,-40,-31,-34,-35,-39,-28,-26,-29,-44,-45,-32,-33,-36,-37,-38,-41,9,-27,-9,-46,-7,9,-8,]),'SCAN':([0,3,4,5,6,10,11,17,22,23,24,25,26,30,41,49,64,65,67,68,69,70,71,72,75,83,84,85,86,88,90,],[12,12,-4,-5,-6,-42,-43,-30,-40,-31,-34,-35,-39,-28,-26,-29,-44,-45,-32,-33,-36,-37,-38,-41,12,-27,-9,-46,-7,12,-8,]),'PRINT':([0,3,4,5,6,10,11,17,22,23,24,25,26,30,41,49,64,65,67,68,69,70,71,72,75,83,84,85,86,88,90,],[13,13,-4,-5,-6,-42,-43,-30,-40,-31,-34,-35,-39,-28,-26,-29,-44,-45,-32,-33,-36,-37,-38,-41,13,-27,-9,-46,-7,13,-8,]),'$end':([1,2,3,4,5,6,10,11,14,17,22,23,24,25,26,30,41,49,64,65,67,68,69,70,71,72,83,84,85,86,90,],[0,-1,-3,-4,-5,-6,-42,-43,-2,-30,-40,-31,-34,-35,-39,-28,-26,-29,-44,-45,-32,-33,-36,-37,-38,-41,-27,-9,-46,-7,-8,]),'FC':([3,4,5,6,10,11,14,17,22,23,24,25,26,30,41,49,64,65,67,68,69,70,71,72,81,83,84,85,86,89,90,],[-3,-4,-5,-6,-42,-43,-2,-30,-40,-31,-34,-35,-39,-28,-26,-29,-44,-45,-32,-33,-36,-37,-38,-41,84,-27,-9,-46,-7,90,-8,]),'PRA':([7,17,40,],[15,28,66,]),'EQUAL':([7,17,73,],[16,29,80,]),'AP':([9,12,13,16,18,19,20,27,29,31,35,42,43,44,45,46,53,54,57,58,59,60,61,62,63,],[18,19,20,27,31,27,27,27,27,31,31,27,27,27,27,27,31,31,27,-20,-21,-22,-23,-24,-25,]),'Nint':([15,16,18,19,20,27,28,29,31,35,42,43,44,45,46,53,54,57,58,59,60,61,62,63,66,80,],[21,26,26,26,26,26,48,26,26,26,26,26,26,26,26,26,26,26,-20,-21,-22,-23,-24,-25,79,83,]),'NOT':([18,31,35,53,54,],[35,35,35,35,35,]),'PRF':([21,48,79,],[41,73,82,]),'MUL':([22,24,25,26,40,67,68,69,70,71,72,],[-40,44,-35,-39,-40,44,44,-36,-37,-38,-41,]),'DIV':([22,24,25,26,40,67,68,69,70,71,72,],[-40,45,-35,-39,-40,45,45,-36,-37,-38,-41,]),'MOD':([22,24,25,26,40,67,68,69,70,71,72,],[-40,46,-35,-39,-40,46,46,-36,-37,-38,-41,]),'ADD':([22,23,24,25,26,37,38,39,40,47,49,51,67,68,69,70,71,72,78,],[-40,42,-34,-35,-39,42,42,42,-40,42,42,42,-32,-33,-36,-37,-38,-41,42,]),'SUB':([22,23,24,25,26,37,38,39,40,47,49,51,67,68,69,70,71,72,78,],[-40,43,-34,-35,-39,43,43,43,-40,43,43,43,-32,-33,-36,-37,-38,-41,43,]),'GoE':([22,24,25,26,37,51,67,68,69,70,71,72,],[-40,-34,-35,-39,58,58,-32,-33,-36,-37,-38,-41,]),'LoE':([22,24,25,26,37,51,67,68,69,70,71,72,],[-40,-34,-35,-39,59,59,-32,-33,-36,-37,-38,-41,]),'Lower':([22,24,25,26,37,51,67,68,69,70,71,72,],[-40,-34,-35,-39,60,60,-32,-33,-36,-37,-38,-41,]),'Greater':([22,24,25,26,37,51,67,68,69,70,71,72,],[-40,-34,-35,-39,61,61,-32,-33,-36,-37,-38,-41,]),'IGUAL':([22,24,25,26,37,51,67,68,69,70,71,72,],[-40,-34,-35,-39,62,62,-32,-33,-36,-37,-38,-41,]),'DIFF':([22,24,25,26,37,51,67,68,69,70,71,72,],[-40,-34,-35,-39,63,63,-32,-33,-36,-37,-38,-41,]),'AND':([22,24,25,26,33,34,36,37,51,55,56,67,68,69,70,71,72,74,76,77,78,],[-40,-34,-35,-39,54,-13,-15,-19,-19,-14,-17,-32,-33,-36,-37,-38,-41,-16,54,-12,-18,]),'FP':([22,24,25,26,32,33,34,36,37,38,39,40,47,50,51,55,56,67,68,69,70,71,72,74,76,77,78,82,],[-40,-34,-35,-39,52,-11,-13,-15,-19,64,65,-40,72,74,72,-14,-17,-32,-33,-36,-37,-38,-41,-16,-10,-12,-18,85,]),'OR':([22,24,25,26,32,33,34,36,37,50,51,55,56,67,68,69,70,71,72,74,76,77,78,],[-40,-34,-35,-39,53,-11,-13,-15,-19,53,-19,53,-17,-32,-33,-36,-37,-38,-41,-16,-10,-12,-18,]),'AC':([52,87,],[75,88,]),'ELSE':([84,],[87,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'Comands':([0,3,75,88,],[2,14,81,89,]),'Comand':([0,3,75,88,],[3,3,3,3,]),'Atribuition':([0,3,75,88,],[4,4,4,4,]),'Conditional':([0,3,75,88,],[5,5,5,5,]),'IO':([0,3,75,88,],[6,6,6,6,]),'INPUT':([0,3,75,88,],[10,10,10,10,]),'OUTPUT':([0,3,75,88,],[11,11,11,11,]),'Expression':([16,18,19,20,27,29,31,35,53,54,57,],[23,37,38,39,47,49,51,37,37,37,78,]),'Values':([16,18,19,20,27,29,31,35,42,43,53,54,57,],[24,24,24,24,24,24,24,24,67,68,24,24,24,]),'Value':([16,18,19,20,27,29,31,35,42,43,44,45,46,53,54,57,],[25,25,25,25,25,25,25,25,25,25,69,70,71,25,25,25,]),'Rest':([17,],[30,]),'Condition':([18,31,35,],[32,50,55,]),'Condition2':([18,31,35,53,],[33,33,33,76,]),'Condition3':([18,31,35,53,54,],[34,34,34,34,77,]),'RelExpression':([18,31,35,53,54,],[36,36,36,36,36,]),'Continuation':([37,51,],[56,56,]),'OpRel':([37,51,],[57,57,]),'Extension':([84,],[86,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> Comands','Program',1,'p_program','compiler_yacc.py',20),
  ('Comands -> Comand Comands','Comands',2,'p_comands','compiler_yacc.py',25),
  ('Comands -> Comand','Comands',1,'p_comands_simple','compiler_yacc.py',29),
  ('Comand -> Atribuition','Comand',1,'p_comand_atb','compiler_yacc.py',37),
  ('Comand -> Conditional','Comand',1,'p_comand_cond','compiler_yacc.py',41),
  ('Comand -> IO','Comand',1,'p_comand_IO','compiler_yacc.py',50),
  ('Conditional -> IF AP Condition FP AC Comands FC Extension','Conditional',8,'p_conditional_simple','compiler_yacc.py',86),
  ('Extension -> ELSE AC Comands FC','Extension',4,'p_extension','compiler_yacc.py',96),
  ('Extension -> <empty>','Extension',0,'p_extension_empty','compiler_yacc.py',104),
  ('Condition -> Condition OR Condition2','Condition',3,'p_condition_or','compiler_yacc.py',109),
  ('Condition -> Condition2','Condition',1,'p_condition_simple','compiler_yacc.py',114),
  ('Condition2 -> Condition2 AND Condition3','Condition2',3,'p_condition2_and','compiler_yacc.py',121),
  ('Condition2 -> Condition3','Condition2',1,'p_condition2_simple','compiler_yacc.py',127),
  ('Condition3 -> NOT Condition','Condition3',2,'p_condition3','compiler_yacc.py',135),
  ('Condition3 -> RelExpression','Condition3',1,'p_condition3_exp','compiler_yacc.py',140),
  ('Condition3 -> AP Condition FP','Condition3',3,'p_condition3_priority','compiler_yacc.py',144),
  ('RelExpression -> Expression Continuation','RelExpression',2,'p_RelExpression_complex','compiler_yacc.py',153),
  ('Continuation -> OpRel Expression','Continuation',2,'p_continuation','compiler_yacc.py',157),
  ('Continuation -> <empty>','Continuation',0,'p_continuation_empty','compiler_yacc.py',161),
  ('OpRel -> GoE','OpRel',1,'p_opRel_GoE','compiler_yacc.py',175),
  ('OpRel -> LoE','OpRel',1,'p_opRel_LoE','compiler_yacc.py',179),
  ('OpRel -> Lower','OpRel',1,'p_opRel_Lower','compiler_yacc.py',183),
  ('OpRel -> Greater','OpRel',1,'p_opRel_Greater','compiler_yacc.py',187),
  ('OpRel -> IGUAL','OpRel',1,'p_opRel_Equal','compiler_yacc.py',191),
  ('OpRel -> DIFF','OpRel',1,'p_opRel_Diff','compiler_yacc.py',195),
  ('Atribuition -> VAR PRA Nint PRF','Atribuition',4,'p_rest_array','compiler_yacc.py',215),
  ('Atribuition -> INT VAR PRA Nint PRF EQUAL Nint','Atribuition',7,'p_atribuition_array_numbered','compiler_yacc.py',224),
  ('Atribuition -> INT VAR Rest','Atribuition',3,'p_atribuition','compiler_yacc.py',244),
  ('Rest -> EQUAL Expression','Rest',2,'p_rest','compiler_yacc.py',254),
  ('Rest -> <empty>','Rest',0,'p_rest_empty','compiler_yacc.py',259),
  ('Atribuition -> VAR EQUAL Expression','Atribuition',3,'p_atribuition_second','compiler_yacc.py',263),
  ('Expression -> Expression ADD Values','Expression',3,'p_expression_plus','compiler_yacc.py',277),
  ('Expression -> Expression SUB Values','Expression',3,'p_expression_minus','compiler_yacc.py',282),
  ('Expression -> Values','Expression',1,'p_expression_simple','compiler_yacc.py',286),
  ('Values -> Value','Values',1,'p_Values_simple','compiler_yacc.py',296),
  ('Values -> Values MUL Value','Values',3,'p_Values_1','compiler_yacc.py',301),
  ('Values -> Values DIV Value','Values',3,'p_Values_2','compiler_yacc.py',305),
  ('Values -> Values MOD Value','Values',3,'p_Values_3','compiler_yacc.py',309),
  ('Value -> Nint','Value',1,'p_Value_int','compiler_yacc.py',318),
  ('Value -> VAR','Value',1,'p_Value_var','compiler_yacc.py',323),
  ('Value -> AP Expression FP','Value',3,'p_Value_complex','compiler_yacc.py',329),
  ('IO -> INPUT','IO',1,'p_IO_INPUT','compiler_yacc.py',339),
  ('IO -> OUTPUT','IO',1,'p_IO_OUTPUT','compiler_yacc.py',343),
  ('INPUT -> SCAN AP Expression FP','INPUT',4,'p_INPUT','compiler_yacc.py',350),
  ('OUTPUT -> PRINT AP Expression FP','OUTPUT',4,'p_OUTPUT_exp','compiler_yacc.py',362),
  ('OUTPUT -> PRINT AP VAR PRA Nint PRF FP','OUTPUT',7,'p_OUTPUT_array','compiler_yacc.py',369),
]
