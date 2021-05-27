
import ply.lex as lex


reserved = {'if': 'IF', 'else':'ELSE','int':'INT', 'while':'WHILE', 'print':'PRINT','scan':'SCAN'}

tokens = ['AP','FP','AC','FC', 'PRA' , 'PRF',
'ADD','MUL', 'DIV', 'SUB', 'MOD',
'OR','AND',
'GoE','LoE','Lower','Greater',
'EQUAL','DIFF','NOT','IGUAL',
'Nint','VAR',
] + list(reserved.values())

t_AP = r'\('

t_FP = r'\)'

t_AC = r'\{'

t_FC = r'\}'

t_PRA = r'\['

t_PRF = r'\]'

t_ADD = r'\+'

t_MUL = r'\*'

t_DIV = r'\/'

t_SUB = r'\-'

t_MOD = r'\%'

t_OR = r'\|\|'

t_AND = r'\&\&'

t_GoE = r'\>\='

t_LoE = r'\<\='

t_Lower = r'\<'

t_Greater = r'\>'

t_DIFF = r'\!\='

t_NOT = r'\!'

t_IGUAL = r'\=\='

t_EQUAL = r'\='

t_Nint = r'\d+'


def t_VAR(t):
	r'[a-zA-Z]+'
	t.type = reserved.get(t.value,'VAR')

	return t

t_ignore=' \t\n\r'


def t_error(t):
	t.lexer.skip(1)
	return t


lexer = lex.lex()

#import sys
#for linha in sys.stdin:
#    lexer.input(linha)
#    for tok in lexer:
#        print(tok) 
