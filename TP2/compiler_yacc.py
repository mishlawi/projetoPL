import ply.yacc as yacc
import sys
import re
from compiler_lex import tokens


stack = {}
#(sp,tipo,valor)

sp = 0
gp = 0
pc = 0
##########################################################COMANDOS

#Comands -> Comand Comands
#        | Comand



def p_program(p):
	"Program : Inits Comands"
	print("aaa")
	p[0] =  p[1] + 'START\n'  + p[2] + 'STOP\n'

def p_program_noInstructions(p):
	"Program : Comands"
	p[0] = 'START\n' + p[1]+ 'STOP\n'

def p_init(p):
	"Inits : Inicialization Inits"
	p[0] = p[1] + p[2]

def p_init_simple(p):
	"Inits : Inicialization"
	p[0] = p[1]

def p_comands(p):
	"Comands : Comand Comands"
	print("aaa")
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
  



############################################################CICLOS

def p_cycle(p):
	"Cycle : WHILE AP Condition FP AC Comands FC"
	print("ciclo")
	global pc 
	pc += 1
	p[0] = f"Ciclo{pc}:\n" + p[3] + '\n' + f"JZ ENDC{pc}\n" + p[6] +f'JUMP Ciclo{pc}\nENDC{pc}:\n'
	
############################################################CONDICIONAL

def p_conditional_simple(p):
	"Conditional : IF AP Condition FP AC Comands FC Extension" 
	global sp
	global stack 
	global gp
	
	p[0] = p[3] + '\n' + f"JZ ELSE{gp}\n" + p[6] + p[8]
	

def p_extension (p):
	"Extension :  ELSE AC Comands FC"
	global sp
	global stack
	global gp
	gp += 1
	p[0] = f'JUMP ENDIF{gp}\n' + f'ELSE{gp}:\n' + p[3] + f'ENDIF{gp}:\n'
	

def p_extension_empty (p):
	"Extension : "
	p[0] = ''


def p_condition_or(p):
	"Condition : Condition OR Condition2"
	p[0] = p[1]  + p[3] + 'ADD\n'
	print("condition ||")

def p_condition_simple(p):
	"Condition : Condition2"
	p[0] = p[1]

# Condition2 -> Condition2 AND Condition3
# 		      | Condition3

def p_condition2_and (p):
	"Condition2 : Condition2 AND Condition3"
	print("condition &&")
	p[0] = p[1] +  p[3]  + 'MUL\n'


def p_condition2_simple(p):
	"Condition2 : Condition3"
	p[0] = p[1]

#cond3 -> NOT CONDITION 
#       | RelExpression
#       | '(' Condition ')'

def p_condition3 (p):
	"Condition3 : NOT Condition"
	print("neg condition")
	p[0] = p[2] + 'NOT'

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
         

	

############################################################ATRIBUICAO




def p_Inicialization_integer(p) : 
	"Inicialization : INT VAR Rest"
	print("Inicialization of " + p[2])
	global stack
	global sp
	stack[p[2]] = (sp,p[1],None)
	p[0] = p[3] + '\n'
	sp+=1

def p_Inicialization_array(p) :
	"Inicialization : INT VAR PRA Nint PRF"
	global stack
	global sp
	print(stack)
	print("array entrou na stack")
	p[0] = 'PUSHN ' + p[4] + '\n'
	stack[f'{p[2]}'] = (sp,'array'+p[1], p[4])
	sp+=int(p[4])

#int a[2] 
"""
def p_atribuition_array(p):
	"Atribuition : INT VAR PRA Nint PRF"
	global stack
	global sp
	p[0] = 'PUSHN ' + p[4] + '\n'
	stack[f'{p[2]}'] = (sp,'array'+p[1], p[4])
	sp+=int(p[4])
"""

#def p_array_var(p):
#	"Atribuition : VAR PRA VAR PRF EQUAL Expression"


# int a[4] = 3
def p_atribuition_array_numbered(p):
	"Atribuition : VAR PRA Nint PRF EQUAL Expression"
	global stack
	print(stack)
	p[0] = 'PUSHGP\nPUSHI ' + str(stack[f'{p[1]}'][0])+ '\n' + 'PADD\nPUSHI ' + p[3] + '\n' + p[6] +'\nSTOREN\n'
	
#int a = ...
"""
def p_atribuition (p):
	"Atribuition : INT VAR Rest"
	print("atribuition of " + p[2])
	global stack
	global sp
	stack[p[2]] = (sp,p[1],None)
	p[0] = p[3] + '\n'
	sp+=1
"""
# a = 3
def p_atribuition_second(p):
	"Atribuition : VAR EQUAL Expression"
	p[0] = p[3] + '\n' + 'STOREG ' + str(stack[p[1]][0]) +'\n'


#int a = 4
def p_rest(p):
	"Rest : EQUAL Expression "
	p[0] = p[2] + '\n'

#int a
def p_rest_empty(p):
	"Rest : "
	p[0] = 'PUSHI 0'



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
	p[0] = "PUSHI " + p[1] 


def p_Value_var(p):	
	"Value : VAR"
	p[0] = "\nPUSHG " + str(stack[p[1]][0]) +'\n'
	 


def p_Value_complex(p):
	"Value : AP Expression FP"
	p[0] = p[2]

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
# scan ( int a[x] ) 
def p_INPUT(p):
	"INPUT : SCAN AP VAR PRA Expression PRF FP"
	x = stack[p[3]][0]
	p[0] = 'PUSHGP\n' + 'PUSHI '+ str(x) + 'PADD\n' + p[5] + 'READ\nATOI\nSTOREN\n'

##################################################OUTPUT

# OUTPUT  -> PRINT VAR
#          | PRINT Exp
#		   | 

#print a * 7 + 2

def p_OUTPUT_exp(p):
	"OUTPUT : PRINT AP Expression FP"
	print("yo")
	global sp
	global stack
	p[0] = p[3] + "WRITEI\n"

#print(a[10])
#print(a[i])
def p_OUTPUT_array(p):
	"OUTPUT : PRINT AP VAR PRA Expression PRF FP"
	p[0] = 'PUSHGP\nPUSHI ' + str(stack[p[3]][0]) + '\nPADD\nPUSHG ' + p[5] +'\nLOADN\nWRITEI'


#print ( a[ 14 ] )
#def p_OUTPUT_array(p):
#	"OUTPUT : PRINT AP VAR PRA Nint PRF FP"
#	p[0] = 'PUSHGP\nPUSHI ' + str(stack[p[3]][0]) + '\nPADD\nPUSHI ' + p[5] + '\nLOADN\nWRITEI\n'


################################################DefinicaoYACC

def p_error(p):
    print("erro")
    print(p)



parser = yacc.yacc() 
fo = open("teste.txt").read()

with open('teste.txt', 'r') as myfile:
    for line in myfile:
        m = re.search(r'while', line)
        if m is not None:
            print("while found")
        

result = parser.parse(fo)

file = open('kanye.vm',"w")

file.write(result)
file.flush()




#TODO:

# scan
#->definir e ACABAR CICLOS
#->CHECKAR VARIAVEIS EM ARRAYS
 