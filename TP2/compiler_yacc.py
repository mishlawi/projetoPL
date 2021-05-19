import ply.yacc as yacc
from compiler_lex import tokens
from compiler_lex import literals








#LogicSymb -> OR     # ||
#           | AND    # &&


def p_logicSymbol_OR(p):
	"LogicSymb : OR "


def p_logicSymbol_And(p):
	"LogicSymb: AND"


#Condition -> Expression OpRel Expression
#		    | Expression


def p_condition_complex(p):
	"Condition : Expression OpRel Expression"

def p_condition_simple(p):
	"Condition : Expression"


#OpRel -> GoE        >=
#	   | LoE         <= 
#	   | Lower       <
#	   | Greater     >
#	   | Equal       ==
#	   | Diff        != 


def p_opRel_GoE(p):
	"OpRel : GoE"

def p_opRel_LoE(p):
	"OpRel : LoE"

def p_opRel_Lower(p):
	"OpRel : Lower"

def p_opRel_Greater(p):
	"OpRel : Greater"

def p_opRel_Equal(p):
	"OpRel : Equal"

def p_opRel_Diff(p):
	"OpRel : Diff"



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
#        | '(' Expression')'

def p_nature_int(p):
	"Nature : Nint"
	print("pushi", p[1])

def p_nature_complex(p):
	"Nature : '(' Expression ')' "
	print("entrou num parentisis")


def p_error(p):
    print("erro")
    print(p.type)


fo = open("teste.txt").read()

parser = yacc.yacc() 

parser.parse(fo)