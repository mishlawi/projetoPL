import re
import webbrowser
import html
import os



def omega(lista):
	keyB = re.compile(r'B-([^ ]+)\s(.+)')
	keyI = re.compile(r'I-([^ ]+)\s(.+)')
	
	dic= {}
	typo = []
	for line in lista:
		
		if res:= keyB.search(line):
			category = res.group(1)
			catInfo = res.group(2)
			if category in dic:
				typo = dic[category]
			typo.append(catInfo)
			dic.update({category:typo})
			typo = []
		
		elif res:=keyI.search(line):
			category = res.group(1)
			catInfo = res.group(2)
			typo = dic[category]
			aux = typo[-1] + " " + catInfo
			del typo[-1]
			typo.append(aux)
			dic.update({category:typo})
			typo = []
		else:
			pass
	
	return dic


def alpha(lista): 
	keyB = re.compile(r'B-([^ ]+)\s(.+)')
	info = {}
	typo = []
	n = 1
	for lines in lista:
		if res:=keyB.search(lines):
			category = res.group(1)
			if category in info:
				typo = info[category]
			typo.append(n)
			info.update({category:typo})
			typo = []
		n+=1
	return info


def beta (dic, info):
	semRepetidos = {}
	naoRepetidos = []
	for categoria in dic:
		elemDic = {}
		for elemento, ocorrencia in zip(dic[categoria], info[categoria]):
			if elemento in elemDic:
				elemDic[elemento].append(ocorrencia)
			else:
				elemDic.update({elemento:[ocorrencia]})
		semRepetidos.update({categoria:elemDic})

	for elem in semRepetidos:
		a=0
		for lista in semRepetidos[elem]:
			a+=1
		naoRepetidos.append(a)
	return semRepetidos, naoRepetidos


def main():
	html.makeDirs()

	directory = 'HTML/categorias'
	
	if len(os.listdir(directory))>0:
		print("Possui ficheiros (possivelmente) temporários em memória. Gostaria de os remover antes de prosseguir?(Y/N)")
		n=input().upper()

		if n=='Y':
			for f in os.listdir(directory):
				os.remove(os.path.join(directory, f))
			print("Ficheiros eliminados")
		else:
			print("Não será removido qualquer ficheiro.")

	print("Por favor, insira o nome do ficheiro a tratar:")
	file = input()

	if(os.path.isfile(file)):
		lista = re.split(r'\n',open(file).read())
	else:
		print("O ficheiro não existe")
		return

	dic = omega(lista)
	info = alpha(lista)
	semRepetidos, naoRepetidos = beta(dic,info)

	html.htmlStyle()
	html.htmlHome(dic,naoRepetidos)
	html.htmlRepetidos(dic,info)
	html.htmlSemRepetidos(dic,semRepetidos)

	webbrowser.open('file://' + os.path.realpath('HTML/website.html'), new=2)  # open in new tab


main()