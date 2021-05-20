import ply.yacc as yacc
import sys
from compiler_lex import tokens
from compiler_lex import literals




##########################################################COMANDOS

#Comands -> Comand Comands
#        | Comand

def p_comands(p):
	"Comands : Comand Comands"
	print("2+ comandos")

def p_comands_simple(p):
	"Comands : Comand"
	print("1 comando")

#Comand -> Atribution
#       | Conditional
#       | Cycle

def p_comand_atb (p):
	"Comand : Atribuition"
	print(f"found att")

def p_comand_cond (p):
	"Comand : Conditional"
	print("found Conditional")

def p_comand_Exp (p):
	"Comand : Expression"
	print("found expression")

def p_comand_cycle (p):
    "Comand : Cycle"
    print("cycle found")

############################################################CONDICIONAL


#Conditional -> if '(' Conditions ')' '{' Comands '}' else '{'Comands '}'
#             | if '(' Conditions ')' '{' Comands '}'

def p_conditional (p):
	"Conditional : IF '(' Conditions ')' AC Comands FC ELSE AC Comands FC "
	print("condicional completo")


def p_conditional_simple(p):
	"Conditional : IF '(' Conditions ')' AC  Comands FC"
	print("condicional so")
	


#Conditions -> Neg '(' Condition ')' LogicSymb Conditions
#            | Neg '(' Condition ')'   # !(a>b)|| a

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
	"LogicSymb : OR "


def p_logicSymbol_And(p):
	"LogicSymb : AND"



#OpRel -> GoE        >=
#	   | LoE         <= 
#	   | Lower       <
#	   | Greater     >
#	   | Equal       ==
#	   | Diff        != 


def p_opRel_GoE(p):
	
	'''
	OpRel : GoE
          | LoE
		  | Lower
          | Greater
	      | Equal
          | Diff
    '''

############################################################CICLOS

def p_cycle(p):
	
	"Cycle : WHILE '(' Conditions ')' AC Comands FC"
	

############################################################ATRIBUICAO

def p_atribuition(p):
	'''
	Atribuition : INT VAR IGUAL Expression
				| VAR IGUAL Expression 
	'''
	print("atribuicao check")

############################################################EXPRESSAO
#Expression -> Vals
#            | Expression '+' Vals
#            | Expression '-' Vals

def p_expression_simple(p):
	"Expression : Vals "

def p_expression_plus(p):
	"Expression : Expression '+' Vals "
	print("add")

def p_expression_less(p):
	"Expression : Expression '-' Vals "
	print("sub")

# Vals -> Nature
#      | Vals '*' Nature
#      | Vals '/' Nature

def p_vals_simple(p):
	"Vals : Nature"

def p_vals_1(p):
	"Vals : Vals '*' Nature"
	print("mul")

def p_vals_2(p):
	"Vals : Vals '/' Nature"
	print("div")

# Nature -> Nint
# 		 | VAR
#        | '(' Expression')'

def p_nature_int(p):
	"Nature : Nint"
	print("pushi", p[1])

def p_nature_var(p):
	"Nature : VAR"
	print("pushi", p[1])

def p_nature_complex(p):
	"Nature : '(' Expression ')' "
	print("entrou num parentisis")


def p_tipo(p):
	"TIPO : INT"


def p_error(p):
    print("erro")
    print(p.type)

parser = yacc.yacc() 
fo = open("teste.txt").read()


parser.parse(fo)