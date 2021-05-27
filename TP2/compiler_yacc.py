import ply.yacc as yacc
import sys
from compiler_lex import tokens

stack = {}
sp = -1
pointer = 0

##########################################################COMANDOS

#Comands -> Comand Comands
#        | Comand

def p_program(p):
	"Program : Comands"
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
	

#def p_comand_cycle (p):
#    "Comand : Cycle"
#    p[0] = p[1]

def p_comand_IO(p):
	"Comand : IO"
	p[0] = p[1]
  
"""
def comandos_open(p):
	"Comandos : Aberto "

def comandos_closed(p):
	"Comandos : Fechado"

def open_1 (p):
	"Aberto : IF PA Condition PF AC Comandos FC"

def open_2(p):
	"Aberto: IF PA Condition PF AC Fechado FC ELSE AC Aberto FC"


def closed_1(p):
	"Fechado : Atribuition"

def closed_2(p):
	"Fechado : IF PA Condition PF Fechado ELSE Fechado"
"""

############################################################CONDICIONAL


#Conditional -> if '(' Conditions ')' '{' Comands '}' Extension

#Extension -> else '{' Comands '}'
#			| $ 




def p_conditional_simple(p):
	"Conditional : IF AP Condition FP AC Comands FC Extension" 
	global sp
	global stack
	global pointer
	print("kajshfkajsfh")
	p[0] = p[3] + '\n' + f"JZ ELSE_{pointer}\n" + p[6] + p[8]
	pointer += 1


def p_extension (p):
	"Extension :  ELSE AC Comands FC"
	global sp
	global stack
	global pointer
	p[0] = f'JUMP ENDIF_{pointer}\n' + f'ELSE_{pointer}\n' + p[3] + f'ENDIF_{pointer}\n' + 'STOP\n'
	#pointer += 1

def p_extension_empty (p):
	"Extension : "
	p[0] = ''


def p_condition_or(p):
	"Condition : Condition OR Condition2"
	p[0] = p[1] +'ADD\n' + p[3] 
	print("condition ou")

def p_condition_simple(p):
	"Condition : Condition2"
	p[0] = p[1]

# Condition2 -> Condition2 AND Condition3
# 		      | Condition3

def p_condition2_and (p):
	"Condition2 : Condition2 AND Condition3"
	print("condition e")
	p[0] = p[1] + 'MUL\n' +  p[3] 


def p_condition2_simple(p):
	"Condition2 : Condition3"
	p[0] = p[1]

#cond3 -> NOT CONDITION 
#       | RelExpression
#       | '(' Condition ')'

def p_condition3 (p):
	"Condition3 : NOT Condition"
	print("neg condition")
	p[0] = p[2]

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
	p[0] = p[1] + '\n' + p[2] 

def p_continuation(p):
	"Continuation : OpRel Expression"
	p[0] = p[1] + p[2]

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
	p[0] = 'SUPEQ' 

def p_opRel_LoE(p):
	"OpRel : LoE"
	p[0] = 'INFEQ'

def p_opRel_Lower(p):
	"OpRel : Lower"
	p[0] = 'INF'

def p_opRel_Greater(p):
	"OpRel : Greater"
	p[0] = 'SUP'

def p_opRel_Equal(p):
	"OpRel : IGUAL"
	p[0] = 'EQUAL'

def p_opRel_Diff(p):
	"OpRel : DIFF"	
	p[0] = 'DIFF NOT'
         

############################################################CICLOS

#def p_cycle(p):
	
#	"Cycle : WHILE AP Condition FP AC Comands FC"
	

############################################################ATRIBUICAO

         



def p_atribuition_array_numbered(p):
	"Atribuition : VAR PRA Nint PRF EQUAL Expression"
	global stack
	global sp
	p[0] = 'PUSHGP\nPUSHI ' + stack[p[1]]+ '\n' + 'PADD\nPUSHI ' + p[3] + '\n' + p[6] +'\nSTOREN '
	for n in range(int(p[4])):
		sp+=1
		stack[f'{p[2]} [{n}]'] = (sp,'array'+p[1],int(p[4]))
	


def p_atribuition_array_numbered(p):
	"Atribuition : INT VAR PRA Nint PRF"
	p[0] = 'PUSHN ' + p[4] + '\n' 


#falta definir para variaveis 

#ATT -> INT VAR Rest
#	  | INT VAR [Nint] 
#     | VAR '=' Expression


#Rest -> '=' Expression
#      | 
#	   | $  

def p_atribuition (p):
	"Atribuition : INT VAR Rest"
	global stack
	global sp
	sp+=1
	stack[p[2]] = (sp,p[1],None)
	p[0] = p[3] + '\n'

def p_rest(p):
	"Rest : EQUAL Expression "
	p[0] = p[2] + '\n'

def p_rest_empty(p):
	"Rest : "
	p[0] = 'PUSHI 0\n'

def p_atribuition_second(p):
	"Atribuition : VAR EQUAL Expression"
	p[0] = p[3] + '\n' + 'storeg ' + str(stack[p[1]][0]) +'\n'




############################################################EXPRESSAO



#Expression -> Values
#            | Expression '+' Values
#            | Expression '-' Values


def p_expression_plus(p):
	"Expression : Expression ADD Values"
	p[0] = p[1] + p[3] + 'ADD\n'

	
def p_expression_minus(p):
	"Expression : Expression SUB Values"
	p[0] = p[1] + p[3] + 'SUB\n'

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
	p[0] = p[1] + p[3] + 'MUL' + '\n'

def p_Values_2(p):
	"Values : Values DIV Value"
	p[0] = p[1] + p[3] + 'DIV' + '\n'

def p_Values_3(p):
	"Values : Values MOD Value"
	p[0] = p[1] + p[3] + 'MOD' + '\n'


# Value -> Nint
# 		 | VAR
#        | '(' Expression ')'

def p_Value_int(p):
	"Value : Nint"
	p[0] = "PUSHI " + p[1] + '\n'


def p_Value_var(p):	
	"Value : VAR"
	p[0] = "PUSHG " + str(stack[p[1]][0]) +'\n'
	 


def p_Value_complex(p):
	"Value : AP Expression FP"
	p[0] = p[2]

############################################INPUT OUTPUT


#IO -> INPUT
#   | OUTPUT

def p_IO_INPUT(p):
	"IO : INPUT"
	p[0] = p[1]

def p_IO_OUTPUT(p):
	"IO : OUTPUT"
	p[0] = p[1]

##################################################INPUT
# INPUT -> SCAN Exp

def p_INPUT(p):
	"INPUT : SCAN Expression"
	p[0] = p[2]

# OUTPUT  -> PRINT VAR
#          | PRINT Exp
#		   | 



##################################################OUTPUT

def p_OUTPUT_var(p):
	"OUTPUT : PRINT Expression"
	global sp
	global stack
	if sp==stack[p[2]][0]:
		p[0] = "WRITEI \n"

	else:
		sp = stack[p[2]][0]
		p[0] = "PUSHG " + str(stack[p[2]][0]) + '\n' + "WRITEI \n"
		

def p_OUTPUT_array(p):
	"OUTPUT : PRINT VAR PRA Nint PRF"
	print(stack)
	P[0] = 'PUSHGP1\nPUSHI ' + str(stack[p[2]][0]) + '\nPADD\nPUSHG' + p[4] + '\nLOADN\nWRITEI'


#def p_OUTPUT_Exp(p):
#	"OUTPUT : PRINT Expression"
#	p[0] = p[2] + "WRITEI \n"


def p_error(p):
    print("erro")
    print(p)



#######################################DefinicaoYACC

parser = yacc.yacc() 
fo = open("teste.txt").read()


result = parser.parse(fo)

file = open('kanye.txt',"w")

file.write(result)
file.flush()


#for linha in fo:
#	print(linha)
#   result = parser.parse(linha)
#	print(result)



#TODO:
#->corrigir erros
#->definir e ACABAR CICLOS
#->CHECKAR VARIAVEIS EM ARRAYS
 