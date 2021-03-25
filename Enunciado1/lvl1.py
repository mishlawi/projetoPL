import re
name = "inscritos.json"

def moucheSplitter():
	
	fo = open(name).read()
	lists = [re.sub(r'}','',elem).lstrip() for elem in fo.split(r'{')][2:]
	return lists

def querie1():
	lists = moucheSplitter()
	key = re.compile(r'"nome":"([a-záéíóúâêîôûãẽĩõũç]+\.?( [a-záéíóúâêîôûãẽĩõũç]+\.?)*)"')
	res = [re.search(key,elem, re.IGNORECASE).group(1).upper() for elem in lists if (lambda elem: re.search(r'"equipa":"individual"',elem,re.IGNORECASE))(elem) and (lambda elem:re.search(r'valongo',elem,re.IGNORECASE))(elem)]
	print(res)

def querie2():
	keyName = r'"nome":"(([a-záéíóúâêîôûãẽĩõũç]+)\.?( [a-záéíóúâêîôûãẽĩõũç]+\.?)*)"'
	keyEmail =r'"email":"([a-zA-Z0-9\-]+((\_|\.)[a-zA-Z0-9\-]+)*(@([a-zA-Z\-]+(\_|\.))+[a-zA-Z\-]+))"'
	keyProva = r'"prova":"([a-zA-Z\-0-9\:]+( [a-zA-Z\-0-9\:]+)*)"'
	keySpecific = r'(Paulo|Ricardo)\.?( [a-záéíóúâêîôûãẽĩõũç]+\.?)*"'
	
	lists = moucheSplitter()
	
	res = [(lambda elem: "\n".join(
		[re.search(keyName,elem, re.IGNORECASE).group(1),
		re.search(keyEmail,elem,re.IGNORECASE).group(1),
		re.search(keyProva,elem, re.IGNORECASE).group(1) ]))
		(elem) for elem in lists 	
		if (lambda elem: re.search(keySpecific,elem,re.IGNORECASE))(elem)
		and (lambda elem: re.search(r'@gmail.com',elem))(elem)]
	#print(res)

def querie3():
	keyTurbulentos = r'turbulentos'
	lists = moucheSplitter()
	res = [(re.sub(r'\s','',(re.sub('\n','',elem)))) for elem in lists if (lambda elem : re.search(keyTurbulentos,elem,re.IGNORECASE))(elem)]
	print(res)



querie3()
	