
import ply.lex as lex


#ABRE PARENTISIS FECHA PARENTISIS ?

tokens = ['OR','AND',
'GoE','LoE','Lower','Greater','Equal','Diff',
'Nint',
'NOT']

literals = ['{','}','(',')','*','/','+','-']

t_NOT = r'\!'

t_OR = r'\|\|'

t_AND = r'&&'

t_GoE = r'>='

t_LoE = r'<='

t_Lower = r'<'

t_Greater = r'>'

t_Equal = r'=='

t_Diff = r'!='

def t_Nint(t):
	r'\d+'
	t.value = int(t.value)
	return t

t_ignore=' \t\n'


def t_error(t):
	t.lexer.skip(1)
	return t



lexer = lex.lex()