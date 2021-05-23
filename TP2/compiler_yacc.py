import ply.yacc as yacc
import sys
from compiler_lex import tokens





##########################################################COMANDOS

#Comands -> Comand Comands
#        | Comand
def p_program(p):
	"Program : Comands"
	p[0] = p[1]


def p_comands(p):
	"Comands : Comand Comands"
	print(p[1])
	print(p[2])
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
	print("found att")

def p_comand_cond (p):
	"Comand : Conditional"
	p[0] = p[1]
	

def p_comand_Exp (p):
	"Comand : Expression"
	p[0] = p[1]
	

def p_comand_cycle (p):
    "Comand : Cycle"
    p[0] = p[1]

def p_comand_IO(p):
	"Comand : IO"
	p[0] = p[1]
    
############################################################CONDICIONAL


#Conditional -> if '(' Conditions ')' '{' Comands '}' else '{'Comands '}'
#             | if '(' Conditions ')' '{' Comands '}'

def p_conditional (p):
	global sp
	global stack

	"Conditional : IF AP Conditions FP AC Comands FC ELSE AC Comands FC "
	#p[0] = p[3] + '\n' 


def p_conditional_simple(p):
	"Conditional : IF AP Conditions FP AC Comands FC"
	print("condicional so")
	


#Conditions -> Neg AP Condition FP LogicSymb Conditions
#            | Neg AP Condition FP   # !(a>b)|| a

def p_conditions(p):
	"Conditions : Neg Condition LogicSymb Conditions"
	print("condicao")

def p_conditions_simple(p):
	"Conditions : Neg Condition"


#Condition -> Expression OpRel Expression
#		    | Expression

def p_condition_complex(p):
	"Condition : Expression OpRel Expression"
	print("ihhh")

def p_condition_simple(p):
	"Condition : Expression"


###################################################SIMBOLOS CONDICIONAIS

#Neg -> NOT          #  !
#     |  $ 

def p_negacaoLogica(p):
	"Neg : NOT"


def p_negacao_empty(p):
	"Neg : "


#LogicSymb -> OR     # ||
#           | AND    # &&

def p_logicSymbol_OR(p):
	"LogicSymb : OR"


def p_logicSymbol_And(p):
	"LogicSymb : AND"



#OpRel -> GoE        >=
#	   | LoE         <= 
#	   | Lower       <
#	   | Greater     >
#	   | IGUAL       ==
#	   | DIFF        != 


def p_opRel_GoE(p):
	'''
	OpRel : GoE
          | LoE
		  | Lower
          | Greater
	      | IGUAL
          | DIFF
    '''

############################################################CICLOS

def p_cycle(p):
	
	"Cycle : WHILE AP Conditions FP AC Comands FC"
	

############################################################ATRIBUICAO
#ATT -> INT VAR '=' EXP
#     | VAR '='' EXP
#     | INT VAR


stack = {}
sp = -1
i = 0



def p_atribuition_first(p):

	"Atribuition : INT VAR EQUAL Expression"
	global stack
	global sp
	sp+=1
	stack[p[2]] = (sp,p[1])
	print(stack)
	
	p[0] =  p[4] +'\n'

def p_atribuition_second(p):
	"Atribuition :  VAR EQUAL Expression "
	
	p[0] = p[3] + '\n' + 'storeg ' + str(stack[p[1]][0]) +'\n'



def p_atribuition_simple(p):
	"Atribuition : INT VAR"
	global stack
	global sp
	sp+=1
	stack[p[2]] = (sp,p[1])
	print(stack)
	
	p[0] = 'PUSHI 0\n'

############################################################EXPRESSAO



#Expression -> Values
#            | Expression '+' Values
#            | Expression '-' Values




def p_expression_simple(p):
	"Expression : Values "
	p[0] = p[1]


def p_expression_plus(p):
	"Expression : Expression ADD Values"
	p[0] = p[1] + p[3] + 'ADD\n'

	

def p_expression_less(p):
	"Expression : Expression SUB Values"
	p[0] = p[1] + p[3] + 'SUB\n'


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


def p_IO_INPUT(p):
	"IO : INPUT"
	p[0] = p[1]

def p_IO_OUTPUT(p):
	"IO : OUTPUT"
	p[0] = p[1]

def p_INPUT(p):
	"INPUT : SCAN VAR"


def p_OUTPUT_var(p):
	"OUTPUT : PRINT VAR"
	if (sp)==stack[p[2]][0]:
		p[0] = "WRITEI \n"
	else:
		p[0] = "PUSHG " + str(stack[p[2]][0]) + '\n' + "WRITEI \n"

def p_OUTPUT_Exp(p):
	"OUTPUT : PRINT Expression"
	p[0] = p[2] + "WRITEI \n"




def p_tipo(p):
	"TIPO : INT"


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
