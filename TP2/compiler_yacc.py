import ply.yacc as yacc
import sys
import re
from compiler_lex import tokens


stack = {}
#(sp,tipo,valor,valor)
heap = {}

hp = 0
sp = 0
gp = 0
pc = 0

##########################################################COMANDOS
#Comands -> Comand Comands
#        | Comand


def p_Function(p):
	"Function : INT VAR AP ARGS FP AC Inits Comands FC"
	global stack
	global sp
	p[0] =  p[4] + p[7] + 'START\n'  + p[8] + 'STOP\n'

def p_Function_noInstructions(p):
	"Function : INT VAR AP ARGS FP AC Comands FC"
	print("yo2")
	p[0] = p[4] + 'START\n' + p[7] + 'STOP\n'

def p_Function_noCommands(p):
	"Function : INT VAR AP ARGS FP AC Inits FC"
	print("yo3")
	p[0] = p[4] + p[7] + 'START\n' + 'STOP\n'

def p_args(p):
	"ARGS : ARG VIRG ARGS"
	p[0] = p[1] + p[3]

def p_args_simple(p):
	"ARGS : ARG "
	p[0] = p[1]

def p_arg(p):
	"ARG : INT VAR"
	global sp
	global stack
	stack[p[2]] = (sp,p[1],None) 
	x = stack[p[2]][0]
	y = '\tPUSHI 0\n' + f'\tREAD\n\tATOI\n\tSTOREG {x}\n'
	p[0] = y
	sp+=1

def p_arg_empty(p):
	"ARG : "
	p[0] = ''

def p_init(p):
	"Inits : Inicialization Inits"
	p[0] = p[1] + p[2]

def p_init_simple(p):
	"Inits : Inicialization"
	p[0] = p[1]

def p_comands(p):
	"Comands : Comand Comands"
	p[0] = p[1] + p[2]

def p_comands_simple(p):
	"Comands : Comand"
	p[0] = p[1]

#Comand -> Atribution
#       | Conditional
#       | Cycle

def p_comand_atb (p):
	"Comand : Atribuition"
	p[0] = p[1]

def p_comand_cond (p):
	"Comand : Conditional"
	p[0] = p[1]
	

def p_comand_cycle (p):
    "Comand : Cycle"
    p[0] = p[1]

def p_comand_IO(p):
	"Comand : IO"
	p[0] = p[1]
  

#BARATA IS THE OG OF THE DEBUG


############################################INPUT OUTPUT

# IO -> INPUT
#     | OUTPUT

def p_IO_INPUT(p):
	"IO : INPUT"
	p[0] = p[1]

def p_IO_OUTPUT(p):
	"IO : OUTPUT"
	p[0] = p[1]

##################################################INPUT
# INPUT -> SCAN Exp
# scan ( a[x] ) 
def p_INPUT_array(p):
	"INPUT : SCAN AP VAR PRA Value PRF FP"
	print("yo")
	x = stack[p[3]][0]
	p[0] = '\tPUSHGP\n' + '\tPUSHI '+ str(x) + '\n\tPADD\n' + p[5] + '\tREAD\n\tATOI\n\tSTOREN\n'

def p_INPUT_var(p):
	"INPUT : SCAN AP VAR FP"
	x= stack[p[3]][0]
	p[0] = f'\tREAD\n\tATOI\n\tSTOREG {x}\n'


##################################################OUTPUT

# OUTPUT  -> PRINT VAR
#          | PRINT Exp
#		   | 

#print a * 7 + 2

# print(Expression)
def p_OUTPUT_exp(p):
	"OUTPUT : PRINT AP Expression FP"
	global sp
	global stack
	p[0] = p[3] + "\tWRITEI\n"

# print(a[4]) ou print (a[x])

def p_OUTPUT_array(p):
	"OUTPUT : PRINT AP VAR PRA Value PRF FP"
	p[0] = '\tPUSHGP\n\tPUSHI ' + str(stack[p[3]][0]) + '\n\tPADD\n ' + p[5] +'\tLOADN\n\tWRITEI\n'



############################################################CICLOS

def p_cycle_while(p):
	"Cycle : WHILE AP Condition FP AC Comands FC"
	global pc 
	pc += 1
	p[0] = f"Ciclo{pc}:\n" + p[3]  + f"\tJZ ENDC{pc}\n" + p[6] +f'JUMP Ciclo{pc}\nENDC{pc}:\n'

def p_cycle_rep_until(p):
	"Cycle : REPEAT AC Comands FC UNTIL AP Condition FP"
	global pc
	pc+=1
	p[0] = f"Ciclo{pc}:\n" + p[3] + p[7] + f"\tJZ Ciclo{pc}\n"


############################################################CONDICIONAL

def p_conditional_simple(p):
	"Conditional : IF AP Condition FP AC Comands FC Extension" 
	global sp
	global stack 
	p[0] = p[3]+ f"\tJZ ELSE{gp}\n"   + p[6] + f"\tJUMP ENDIF{gp}\n" + p[8] + f'ENDIF{gp}:\n' 
	

def p_extension (p):
	"Extension :  ELSE AC Comands FC"
	global sp
	global stack
	global gp
	gp += 1
	p[0] =  f'ELSE{gp}:\n' + p[3] 
	

def p_extension_empty (p):
	"Extension : "
	global gp
	gp += 1
	p[0] = f'ELSE{gp}:\n'


def p_condition_or(p):
	"Condition : Condition OR Condition2"
	p[0] = p[1]  + p[3] + '\tADD\n'

def p_condition_simple(p):
	"Condition : Condition2"
	p[0] = p[1]

# Condition2 -> Condition2 AND Condition3
# 		      | Condition3

def p_condition2_and (p):
	"Condition2 : Condition2 AND Condition3"
	p[0] = p[1] +  p[3]  + '\tMUL\n'


def p_condition2_simple(p):
	"Condition2 : Condition3"
	p[0] = p[1]

#cond3 -> NOT CONDITION 
#       | RelExpression
#       | '(' Condition ')'

def p_condition3 (p):
	"Condition3 : NOT Condition"
	p[0] = p[2] + '\tNOT\n'

def p_condition3_exp(p):
	"Condition3 : RelExpression"
	p[0] = p[1]

def p_condition3_priority(p):
	"Condition3 : AP Condition FP"
	p[0] = p[2]

#RelExpression -> Expression Continuation

# Continuation -> OpRel Expression
#				| $

def p_RelExpression_complex(p):
	"RelExpression : Expression Continuation"
	p[0] = p[1] + p[2] 

def p_continuation(p):
	"Continuation : OpRel Expression"
	p[0] = p[2] + p[1]

def p_continuation_empty(p):
	"Continuation : "
	p[0] = ''

###################################################SIMBOLOS CONDICIONAIS

#OpRel -> GoE        >=
#	   | LoE         <= 
#	   | Lower       <
#	   | Greater     >
#	   | IGUAL       ==
#	   | DIFF        != 


def p_opRel_GoE(p):
	"OpRel : GoE"	
	p[0] = '\tSUPEQ\n' 

def p_opRel_LoE(p):
	"OpRel : LoE"
	p[0] = '\tINFEQ\n'

def p_opRel_Lower(p):
	"OpRel : Lower"
	p[0] = '\tINF\n'

def p_opRel_Greater(p):
	"OpRel : Greater"
	p[0] = '\tSUP\n'

def p_opRel_Equal(p):
	"OpRel : IGUAL"
	p[0] = '\tEQUAL\n'

def p_opRel_Diff(p):
	"OpRel : DIFF"	
	p[0] = '\tEQUAL\n\tNOT\n'
         
	

############################################################ATRIBUICAO

def p_Inicialization_integer(p) : 
	"Inicialization : INT VAR Rest"
	global stack
	global sp
	stack[p[2]] = (sp,p[1],None)
	p[0] = p[3]
	sp+=1

#int a [4]

def p_Inicialization_array(p) :
	"Inicialization : INT VAR PRA Nint PRF"
	global stack
	global sp
	p[0] = '\tPUSHN ' + p[4] + '\n'
	stack[f'{p[2]}'] = (sp,'array'+p[1], p[4])
	sp+=int(p[4])

#int a[N]
def p_Inicialization_array_heap(p) :
	"Inicialization : INT VAR PRA VAR PRF"
	global stack
	global sp
	#heap[f'{p[2]}'] = (hp,'array') 
	varSp = stack[p[4]][3]

	p[0] = '\tPUSHG ' + str(varSp) + '\n' + '\tALLOCN\n' 
	stack[f'{p[2]}'] = (sp,'heapPointer',1)
	sp+=1


#int a = 4
def p_rest(p):
	"Rest : EQUAL Expression "
	p[0] = p[2]

#int a
def p_rest_empty(p):
	"Rest : "
	p[0] = '\tPUSHI 0\n'


# int a[4] = 3
def p_atribuition_array_numbered(p):
	"Atribuition : VAR PRA Value PRF EQUAL Expression"
	global stack
	print(stack)
	p[0] = '\tPUSHGP\n\tPUSHI ' + str(stack[f'{p[1]}'][0])+ '\n' + '\tPADD\n' + p[3] + '\n' + p[6] +'\n\tSTOREN\n'
	


def p_atribuition_second(p):
	"Atribuition : VAR EQUAL Expression"
	p[0] = p[3] + '\tSTOREG ' + str(stack[p[1]][0]) +'\n'





############################################################EXPRESSAO

#Expression -> Values
#            | Expression '+' Values
#            | Expression '-' Values


def p_expression_plus(p):
	"Expression : Expression ADD Values"
	p[0] = p[1] + p[3] + '\tADD\n'

	
def p_expression_minus(p):
	"Expression : Expression SUB Values"
	p[0] = p[1] + p[3] + '\tSUB\n'

def p_expression_simple(p):
	"Expression : Values "
	p[0] = p[1]

# Values -> Value
#      | Values '*' Value
#      | Values '/' Value
#      | Values '%' Value


def p_Values_simple(p):
	"Values : Value"
	p[0] = p[1] 


def p_Values_1(p):
	"Values : Values MUL Value"
	p[0] = p[1] + p[3] + '\tMUL\n'

def p_Values_2(p):
	"Values : Values DIV Value"
	p[0] = p[1] + p[3] + '\tDIV\n' 

def p_Values_3(p):
	"Values : Values MOD Value"
	p[0] = p[1] + p[3] + '\tMOD\n' 


# Value -> Nint
# 		 | VAR
#        | '(' Expression ')'

def p_Value_int(p):
	"Value : Nint"
	p[0] = "\tPUSHI " + p[1] + '\n'


def p_Value_var(p):	
	"Value : VAR"
	p[0] = "\tPUSHG " + str(stack[p[1]][0]) +'\n'
	 


def p_Value_complex(p):
	"Value : AP Expression FP"
	p[0] = p[2]


################################################DefinicaoYACC

def p_error(p):
    print("erro")
    print(p)



parser = yacc.yacc() 
fo = open("teste.txt").read()     

result = parser.parse(fo)

file = open('kanye.vm',"w")

file.write(result)
file.flush()


 