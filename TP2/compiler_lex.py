
import ply.lex as lex




reserved = {'if': 'IF', 'else':'ELSE','int':'INT','==':'Equal','!=':'Diff', 'while':'WHILE'}

tokens = ['AC','FC','OR','AND',
'GoE','LoE','Lower','Greater',
'NOT','IGUAL','Nint','VAR'] + list(reserved.values())

literals = ['{','}','(',')','*','/','+','-']


t_AC = r'\{'

t_FC = r'\}'

t_OR = r'\|\|'

t_AND = r'\&\&'

t_GoE = r'\>\='

t_LoE = r'\<\='

t_Lower = r'\<'

t_Greater = r'\>'

t_NOT = r'\!'

t_IGUAL =r'\='


def t_Nint(t):
	r'\d+'
	t.value = int(t.value)
	return t



def t_VAR(t):
	r'[a-zA-Z]+'
	#t.type = reserved.get(t.value,'VAR')
	if t.value == 'if':
		t.type = 'IF'
	elif t.value == 'else':
		t.type = 'ELSE'
	elif t.value == 'while':
		t.type = 'WHILE'

	return t

t_ignore=' \t\n'


def t_error(t):
	t.lexer.skip(1)
	return t



lexer = lex.lex()