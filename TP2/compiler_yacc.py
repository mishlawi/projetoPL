import ply.yacc as yacc
import sys
from compiler_lex import tokens


class Valor:
	def __init__(self,tipo,offset,size):
		self.tipo = tipo
		self.offset = offset
		self.size = size
		


stack = {}



sp = 0
gp = 0
pc = 0
#Described in 1.2.7 in VMdocpt

##########################################################COMANDOS

#Comands -> Comand Comands
#        | Comand

def p_program(p):
	"Program : Comands"
	p[0] = 'START\n' + p[1] + 'STOP\n'

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
	global gp
	print("kajshfkajsfh")
	p[0] = p[3] + '\n' + f"JZ ELSE_{gp}\n" + p[6] + p[8]
	gp += 1


def p_extension (p):
	"Extension :  ELSE AC Comands FC"
	global sp
	global stack
	global gp
	p[0] = f'JUMP ENDIF_{gp}\n' + f'ELSE_{gp}\n' + p[3] + f'ENDIF_{gp}\n' + 'STOP\n'
	#gp += 1

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
	p[0] = 'SUPEQ\n' 

def p_opRel_LoE(p):
	"OpRel : LoE"
	p[0] = 'INFEQ\n'

def p_opRel_Lower(p):
	"OpRel : Lower"
	p[0] = 'INF\n'

def p_opRel_Greater(p):
	"OpRel : Greater"
	p[0] = 'SUP\n'

def p_opRel_Equal(p):
	"OpRel : IGUAL"
	p[0] = 'EQUAL\n'

def p_opRel_Diff(p):
	"OpRel : DIFF"	
	p[0] = 'DIFF NOT\n'
         

############################################################CICLOS

def p_cycle(p):
	
	"Cycle : WHILE AP Condition FP AC Comands FC"
	

############################################################ATRIBUICAO

         

# a[2] = 4
def p_rest_array(p):
	"Atribuition : INT VAR PRA Nint PRF"
	global stack
	global sp
	p[0] = 'PUSHN ' + p[4] + '\n'
	stack[f'{p[2]}'] = (sp,'array'+p[1], p[4])
	sp+=int(p[4])


def p_atribuition_array_numbered(p):
	"Atribuition : VAR PRA Nint PRF EQUAL Nint"
	global stack
	print("ty")
	p[0] = 'PUSHGP\nPUSHI ' + str(stack[f'{p[1]}'][0])+ '\n' + 'PADD\nPUSHI ' + p[3] + '\nPUSHI ' + p[6] +'\nSTOREN\n'
	




#falta definir para variaveis 

#ATT -> INT VAR Rest
#	  | INT VAR [Nint] 
#     | VAR '=' Expression


#Rest -> '=' Expression
#      | 
#	   | $  




def p_atribuition (p):
	"Atribuition : INT VAR Rest"
	print("atribuition of " + p[2])
	global stack
	global sp
	stack[p[2]] = (sp,p[1],None)
	p[0] = p[3] + '\n'
	sp+=1

#int a = 4
def p_rest(p):
	"Rest : EQUAL Expression "
	p[0] = p[2] + '\n'

#int b
"""
def p_rest_array(p):
	"Atribuition : INT VAR PRA Nint PRF"
	global stack
	global sp
	p[0] = 'PUSHN ' + p[4] + '\n'
	sp+=int(p[4])
	stack[f'{p[2]}'] = (sp,'array'+p[1], p[4])
"""

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
	"INPUT : SCAN AP Expression FP"
	p[0] = p[3]




##################################################OUTPUT

# OUTPUT  -> PRINT VAR
#          | PRINT Exp
#		   | 


#print a * 7 + 2

def p_OUTPUT_var(p):
	"OUTPUT : PRINT AP Expression FP"
	global sp
	global stack
	print(p[2])
	p[0] = p[2] + "WRITEI \n"
		
#print ( a[ 14 ] )
def p_OUTPUT_array(p):
	"OUTPUT : PRINT AP VAR PRA Nint PRF FP"
	print("yo")
	print(stack)
	p[0] = 'PUSHGP\nPUSHI ' + str(stack[p[3]][0]) + '\nPADD\nPUSHI ' + p[5] + '\nLOADN\nWRITEI\n'


#######################################DefinicaoYACC

def p_error(p):
    print("erro")
    print(p)



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
 