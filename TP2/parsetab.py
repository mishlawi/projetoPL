
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AC ADD AND AP DIFF DIV ELSE EQUAL FC FP GoE Greater IF IGUAL INT LoE Lower MOD MUL NOT Nint OR PRA PRF PRINT SCAN SUB VAR WHILEProgram : Inits ComandsProgram : ComandsInits : Inicialization InitsInits : InicializationComands : Comand ComandsComands : ComandComand : AtribuitionComand : ConditionalComand : CycleComand : IOCycle : WHILE AP Condition FP AC Comands FCConditional : IF AP Condition FP AC Comands FC ExtensionExtension :  ELSE AC Comands FCExtension : Condition : Condition OR Condition2Condition : Condition2Condition2 : Condition2 AND Condition3Condition2 : Condition3Condition3 : NOT ConditionCondition3 : RelExpressionCondition3 : AP Condition FPRelExpression : Expression ContinuationContinuation : OpRel ExpressionContinuation : OpRel : GoEOpRel : LoEOpRel : LowerOpRel : GreaterOpRel : IGUALOpRel : DIFFInicialization : INT VAR RestInicialization : INT VAR PRA Nint PRFRest : EQUAL Expression Rest : Atribuition : VAR PRA Nint PRF EQUAL ExpressionAtribuition : VAR EQUAL ExpressionExpression : Expression ADD ValuesExpression : Expression SUB ValuesExpression : Values Values : ValueValues : Values MUL ValueValues : Values DIV ValueValues : Values MOD ValueValue : NintValue : VARValue : AP Expression FPIO : INPUTIO : OUTPUTINPUT : SCAN AP VAR PRA Expression PRF FPOUTPUT : PRINT AP Expression FPOUTPUT : PRINT AP VAR PRA Expression PRF FP'
    
_lr_action_items = {'INT':([0,4,21,28,32,34,35,36,50,76,78,79,80,81,82,83,],[6,6,-34,-31,-45,-39,-40,-44,-33,-32,-37,-38,-41,-42,-43,-46,]),'VAR':([0,2,4,5,6,8,9,10,11,14,15,19,21,23,24,25,26,27,28,30,32,33,34,35,36,37,38,42,50,52,53,54,55,56,61,62,65,66,67,68,69,70,71,73,74,75,76,77,78,79,80,81,82,83,85,89,92,97,98,99,100,101,103,105,],[7,7,-4,7,21,-7,-8,-9,-10,-47,-48,-3,-34,32,32,32,46,48,-31,32,-45,-36,-39,-40,-44,32,32,32,-33,32,32,32,32,32,32,32,32,-25,-26,-27,-28,-29,-30,32,-50,32,-32,32,-37,-38,-41,-42,-43,-46,7,7,-35,-14,-11,-49,-51,-12,7,-13,]),'IF':([0,2,4,5,8,9,10,11,14,15,19,21,28,32,33,34,35,36,50,74,76,78,79,80,81,82,83,85,89,92,97,98,99,100,101,103,105,],[12,12,-4,12,-7,-8,-9,-10,-47,-48,-3,-34,-31,-45,-36,-39,-40,-44,-33,-50,-32,-37,-38,-41,-42,-43,-46,12,12,-35,-14,-11,-49,-51,-12,12,-13,]),'WHILE':([0,2,4,5,8,9,10,11,14,15,19,21,28,32,33,34,35,36,50,74,76,78,79,80,81,82,83,85,89,92,97,98,99,100,101,103,105,],[13,13,-4,13,-7,-8,-9,-10,-47,-48,-3,-34,-31,-45,-36,-39,-40,-44,-33,-50,-32,-37,-38,-41,-42,-43,-46,13,13,-35,-14,-11,-49,-51,-12,13,-13,]),'SCAN':([0,2,4,5,8,9,10,11,14,15,19,21,28,32,33,34,35,36,50,74,76,78,79,80,81,82,83,85,89,92,97,98,99,100,101,103,105,],[16,16,-4,16,-7,-8,-9,-10,-47,-48,-3,-34,-31,-45,-36,-39,-40,-44,-33,-50,-32,-37,-38,-41,-42,-43,-46,16,16,-35,-14,-11,-49,-51,-12,16,-13,]),'PRINT':([0,2,4,5,8,9,10,11,14,15,19,21,28,32,33,34,35,36,50,74,76,78,79,80,81,82,83,85,89,92,97,98,99,100,101,103,105,],[17,17,-4,17,-7,-8,-9,-10,-47,-48,-3,-34,-31,-45,-36,-39,-40,-44,-33,-50,-32,-37,-38,-41,-42,-43,-46,17,17,-35,-14,-11,-49,-51,-12,17,-13,]),'$end':([1,3,5,8,9,10,11,14,15,18,20,32,33,34,35,36,74,78,79,80,81,82,83,92,97,98,99,100,101,105,],[0,-2,-6,-7,-8,-9,-10,-47,-48,-1,-5,-45,-36,-39,-40,-44,-50,-37,-38,-41,-42,-43,-46,-35,-14,-11,-49,-51,-12,-13,]),'FC':([5,8,9,10,11,14,15,20,32,33,34,35,36,74,78,79,80,81,82,83,92,93,94,97,98,99,100,101,104,105,],[-6,-7,-8,-9,-10,-47,-48,-5,-45,-36,-39,-40,-44,-50,-37,-38,-41,-42,-43,-46,-35,97,98,-14,-11,-49,-51,-12,105,-13,]),'PRA':([7,21,46,48,],[22,29,73,75,]),'EQUAL':([7,21,51,],[23,30,77,]),'AP':([12,13,16,17,23,24,25,27,30,37,38,42,52,53,54,55,56,61,62,65,66,67,68,69,70,71,73,75,77,],[24,25,26,27,37,38,38,37,37,37,38,38,37,37,37,37,37,38,38,37,-25,-26,-27,-28,-29,-30,37,37,37,]),'Nint':([22,23,24,25,27,29,30,37,38,42,52,53,54,55,56,61,62,65,66,67,68,69,70,71,73,75,77,],[31,36,36,36,36,49,36,36,36,36,36,36,36,36,36,36,36,36,-25,-26,-27,-28,-29,-30,36,36,36,]),'NOT':([24,25,38,42,61,62,],[42,42,42,42,42,42,]),'PRF':([31,32,34,35,36,49,78,79,80,81,82,83,90,91,],[51,-45,-39,-40,-44,76,-37,-38,-41,-42,-43,-46,95,96,]),'MUL':([32,34,35,36,48,78,79,80,81,82,83,],[-45,54,-40,-44,-45,54,54,-41,-42,-43,-46,]),'DIV':([32,34,35,36,48,78,79,80,81,82,83,],[-45,55,-40,-44,-45,55,55,-41,-42,-43,-46,]),'MOD':([32,34,35,36,48,78,79,80,81,82,83,],[-45,56,-40,-44,-45,56,56,-41,-42,-43,-46,]),'ADD':([32,33,34,35,36,44,47,48,50,57,59,78,79,80,81,82,83,88,90,91,92,],[-45,52,-39,-40,-44,52,52,-45,52,52,52,-37,-38,-41,-42,-43,-46,52,52,52,52,]),'SUB':([32,33,34,35,36,44,47,48,50,57,59,78,79,80,81,82,83,88,90,91,92,],[-45,53,-39,-40,-44,53,53,-45,53,53,53,-37,-38,-41,-42,-43,-46,53,53,53,53,]),'GoE':([32,34,35,36,44,59,78,79,80,81,82,83,],[-45,-39,-40,-44,66,66,-37,-38,-41,-42,-43,-46,]),'LoE':([32,34,35,36,44,59,78,79,80,81,82,83,],[-45,-39,-40,-44,67,67,-37,-38,-41,-42,-43,-46,]),'Lower':([32,34,35,36,44,59,78,79,80,81,82,83,],[-45,-39,-40,-44,68,68,-37,-38,-41,-42,-43,-46,]),'Greater':([32,34,35,36,44,59,78,79,80,81,82,83,],[-45,-39,-40,-44,69,69,-37,-38,-41,-42,-43,-46,]),'IGUAL':([32,34,35,36,44,59,78,79,80,81,82,83,],[-45,-39,-40,-44,70,70,-37,-38,-41,-42,-43,-46,]),'DIFF':([32,34,35,36,44,59,78,79,80,81,82,83,],[-45,-39,-40,-44,71,71,-37,-38,-41,-42,-43,-46,]),'AND':([32,34,35,36,40,41,43,44,59,63,64,78,79,80,81,82,83,84,86,87,88,],[-45,-39,-40,-44,62,-18,-20,-24,-24,-19,-22,-37,-38,-41,-42,-43,-46,-21,62,-17,-23,]),'FP':([32,34,35,36,39,40,41,43,44,45,47,48,57,58,59,63,64,78,79,80,81,82,83,84,86,87,88,95,96,],[-45,-39,-40,-44,60,-16,-18,-20,-24,72,74,-45,83,84,83,-19,-22,-37,-38,-41,-42,-43,-46,-21,-15,-17,-23,99,100,]),'OR':([32,34,35,36,39,40,41,43,44,45,58,59,63,64,78,79,80,81,82,83,84,86,87,88,],[-45,-39,-40,-44,61,-16,-18,-20,-24,61,61,-24,61,-22,-37,-38,-41,-42,-43,-46,-21,-15,-17,-23,]),'AC':([60,72,102,],[85,89,103,]),'ELSE':([97,],[102,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'Inits':([0,4,],[2,19,]),'Comands':([0,2,5,85,89,103,],[3,18,20,93,94,104,]),'Inicialization':([0,4,],[4,4,]),'Comand':([0,2,5,85,89,103,],[5,5,5,5,5,5,]),'Atribuition':([0,2,5,85,89,103,],[8,8,8,8,8,8,]),'Conditional':([0,2,5,85,89,103,],[9,9,9,9,9,9,]),'Cycle':([0,2,5,85,89,103,],[10,10,10,10,10,10,]),'IO':([0,2,5,85,89,103,],[11,11,11,11,11,11,]),'INPUT':([0,2,5,85,89,103,],[14,14,14,14,14,14,]),'OUTPUT':([0,2,5,85,89,103,],[15,15,15,15,15,15,]),'Rest':([21,],[28,]),'Expression':([23,24,25,27,30,37,38,42,61,62,65,73,75,77,],[33,44,44,47,50,57,59,44,44,44,88,90,91,92,]),'Values':([23,24,25,27,30,37,38,42,52,53,61,62,65,73,75,77,],[34,34,34,34,34,34,34,34,78,79,34,34,34,34,34,34,]),'Value':([23,24,25,27,30,37,38,42,52,53,54,55,56,61,62,65,73,75,77,],[35,35,35,35,35,35,35,35,35,35,80,81,82,35,35,35,35,35,35,]),'Condition':([24,25,38,42,],[39,45,58,63,]),'Condition2':([24,25,38,42,61,],[40,40,40,40,86,]),'Condition3':([24,25,38,42,61,62,],[41,41,41,41,41,87,]),'RelExpression':([24,25,38,42,61,62,],[43,43,43,43,43,43,]),'Continuation':([44,59,],[64,64,]),'OpRel':([44,59,],[65,65,]),'Extension':([97,],[101,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> Inits Comands','Program',2,'p_program','compiler_yacc.py',21),
  ('Program -> Comands','Program',1,'p_program_noInstructions','compiler_yacc.py',26),
  ('Inits -> Inicialization Inits','Inits',2,'p_init','compiler_yacc.py',30),
  ('Inits -> Inicialization','Inits',1,'p_init_simple','compiler_yacc.py',34),
  ('Comands -> Comand Comands','Comands',2,'p_comands','compiler_yacc.py',38),
  ('Comands -> Comand','Comands',1,'p_comands_simple','compiler_yacc.py',43),
  ('Comand -> Atribuition','Comand',1,'p_comand_atb','compiler_yacc.py',51),
  ('Comand -> Conditional','Comand',1,'p_comand_cond','compiler_yacc.py',55),
  ('Comand -> Cycle','Comand',1,'p_comand_cycle','compiler_yacc.py',60),
  ('Comand -> IO','Comand',1,'p_comand_IO','compiler_yacc.py',64),
  ('Cycle -> WHILE AP Condition FP AC Comands FC','Cycle',7,'p_cycle','compiler_yacc.py',73),
  ('Conditional -> IF AP Condition FP AC Comands FC Extension','Conditional',8,'p_conditional_simple','compiler_yacc.py',82),
  ('Extension -> ELSE AC Comands FC','Extension',4,'p_extension','compiler_yacc.py',91),
  ('Extension -> <empty>','Extension',0,'p_extension_empty','compiler_yacc.py',100),
  ('Condition -> Condition OR Condition2','Condition',3,'p_condition_or','compiler_yacc.py',105),
  ('Condition -> Condition2','Condition',1,'p_condition_simple','compiler_yacc.py',110),
  ('Condition2 -> Condition2 AND Condition3','Condition2',3,'p_condition2_and','compiler_yacc.py',117),
  ('Condition2 -> Condition3','Condition2',1,'p_condition2_simple','compiler_yacc.py',123),
  ('Condition3 -> NOT Condition','Condition3',2,'p_condition3','compiler_yacc.py',131),
  ('Condition3 -> RelExpression','Condition3',1,'p_condition3_exp','compiler_yacc.py',136),
  ('Condition3 -> AP Condition FP','Condition3',3,'p_condition3_priority','compiler_yacc.py',140),
  ('RelExpression -> Expression Continuation','RelExpression',2,'p_RelExpression_complex','compiler_yacc.py',149),
  ('Continuation -> OpRel Expression','Continuation',2,'p_continuation','compiler_yacc.py',153),
  ('Continuation -> <empty>','Continuation',0,'p_continuation_empty','compiler_yacc.py',157),
  ('OpRel -> GoE','OpRel',1,'p_opRel_GoE','compiler_yacc.py',171),
  ('OpRel -> LoE','OpRel',1,'p_opRel_LoE','compiler_yacc.py',175),
  ('OpRel -> Lower','OpRel',1,'p_opRel_Lower','compiler_yacc.py',179),
  ('OpRel -> Greater','OpRel',1,'p_opRel_Greater','compiler_yacc.py',183),
  ('OpRel -> IGUAL','OpRel',1,'p_opRel_Equal','compiler_yacc.py',187),
  ('OpRel -> DIFF','OpRel',1,'p_opRel_Diff','compiler_yacc.py',191),
  ('Inicialization -> INT VAR Rest','Inicialization',3,'p_Inicialization_integer','compiler_yacc.py',200),
  ('Inicialization -> INT VAR PRA Nint PRF','Inicialization',5,'p_Inicialization_array','compiler_yacc.py',209),
  ('Rest -> EQUAL Expression','Rest',2,'p_rest','compiler_yacc.py',221),
  ('Rest -> <empty>','Rest',0,'p_rest_empty','compiler_yacc.py',226),
  ('Atribuition -> VAR PRA Nint PRF EQUAL Expression','Atribuition',6,'p_atribuition_array_numbered','compiler_yacc.py',247),
  ('Atribuition -> VAR EQUAL Expression','Atribuition',3,'p_atribuition_second','compiler_yacc.py',266),
  ('Expression -> Expression ADD Values','Expression',3,'p_expression_plus','compiler_yacc.py',281),
  ('Expression -> Expression SUB Values','Expression',3,'p_expression_minus','compiler_yacc.py',286),
  ('Expression -> Values','Expression',1,'p_expression_simple','compiler_yacc.py',290),
  ('Values -> Value','Values',1,'p_Values_simple','compiler_yacc.py',300),
  ('Values -> Values MUL Value','Values',3,'p_Values_1','compiler_yacc.py',305),
  ('Values -> Values DIV Value','Values',3,'p_Values_2','compiler_yacc.py',309),
  ('Values -> Values MOD Value','Values',3,'p_Values_3','compiler_yacc.py',313),
  ('Value -> Nint','Value',1,'p_Value_int','compiler_yacc.py',322),
  ('Value -> VAR','Value',1,'p_Value_var','compiler_yacc.py',327),
  ('Value -> AP Expression FP','Value',3,'p_Value_complex','compiler_yacc.py',333),
  ('IO -> INPUT','IO',1,'p_IO_INPUT','compiler_yacc.py',342),
  ('IO -> OUTPUT','IO',1,'p_IO_OUTPUT','compiler_yacc.py',346),
  ('INPUT -> SCAN AP VAR PRA Expression PRF FP','INPUT',7,'p_INPUT','compiler_yacc.py',353),
  ('OUTPUT -> PRINT AP Expression FP','OUTPUT',4,'p_OUTPUT_exp','compiler_yacc.py',366),
  ('OUTPUT -> PRINT AP VAR PRA Expression PRF FP','OUTPUT',7,'p_OUTPUT_array','compiler_yacc.py',375),
]
