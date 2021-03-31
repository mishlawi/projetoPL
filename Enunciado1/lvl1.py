import re
name = "inscritos.json"

def moucheSplitter():
	
	fo = open(name).read()
	lists = [re.sub(r'}','',elem).lstrip() for elem in fo.split(r'{')][2:]
	return lists

def querie1():
	lists = moucheSplitter()
	key = r'"nome":"([a-záéíóúâêîôûãẽĩõũç]+\.?( [a-záéíóúâêîôûãẽĩõũç]+\.?)*)"'
	res = [re.search(key,elem, re.IGNORECASE).group(1).upper() for elem in lists if (lambda elem: re.search(r'"equipa":"individual"',elem,re.IGNORECASE))(elem) and (lambda elem:re.search(r'valongo',elem,re.IGNORECASE))(elem)]
	return res
	

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
	return res
	
	#print(res)

def querie3():
	keyTurbulentos = r'turbulentos'
	lists = moucheSplitter()
	res = [(re.sub(r'\t| {2,}','',(re.sub('\n','',elem)))) for elem in lists if (lambda elem : re.search(keyTurbulentos,elem,re.IGNORECASE))(elem)]
	res = [re.sub(r'",','"\n',elem) for elem in res]
	return res

def querie4():
	lists = moucheSplitter()
	dic = {}
	categorias = [re.search(r'"escalao":"(([0-9]|[a-zA-Z])+( ([0-9]|[a-zA-Z])+)?|)"',elem).group(1) for elem in lists]
	for elem in categorias:
		if elem in dic:
			a = dic[elem]+1
			dic.update({elem:a})
		else:
			dic.update({elem:1})
	return dic
	#print(dic)
	

def querie5():
	#not finished
	dic = {}
	lists = moucheSplitter()
	rascunho = [re.search(r'"equipa":"(.+)"',elem).group(1) for elem in lists]
	teams = []
	for elem in rascunho:
		if elem not in teams:
			teams.append(elem)

def main():
	q1 = querie1()

	print("***********************************")
	print("CONCORRENTES INDIVIDUAIS DE VALONGO - QUERIE 1")
	print("***********************************")
	for elem in q1:
		print(elem)

	print("\n\n")

	q2 = querie2()
	print("*********************************************")
	print("PAULOS E RICARDOS QUE USAM O GMAIL - QUERIE 2")
	print("*********************************************")
	for elem in q2:
		print(elem)
		print("------------------------------------------")
	print("\n\n")

	q3 = querie3()
	print("******************************************")
	print("INFO DOS ELEMENTOS DA EQUIPA 'TURBULENTOS' - QUERIE 3")
	print("******************************************")
	for elem in q3:
		print(elem)
		print("------------------------------------------")
	print("\n\n")
	q4 = querie4()

	print("***************QUERIE 4**************")
	print("Escalão           | Atletas inscritos")
	print("*************************************")
	for elem in sorted(q4):
		if not elem:
			print("não especificado", " "*(7-len("não especificado")),"|",q4[elem]," "*(16-len(str(q4[elem]))))	
		else:
			print(elem, " "*(16-len(elem)),"|",q4[elem]," "*(16-len(str(q4[elem]))))


main()