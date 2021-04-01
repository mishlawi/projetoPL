import re
import webbrowser
import html
import os



def alpha(lista): 
	info = {}
	typo = []
	keyB = re.compile(r'^B-[A-Z]+')
	n = 1
	for lines in lista:
		if keyB.search(lines):
			category = lines.split('-')[1].split()[0]
			if category in info:
				typo = info[category]
			typo.append(n)
			info.update({category:typo})
			typo = []
		n+=1
	return info


#key -> categoria v: [nr da ocorrencia]
def organizer(lista):
	fich = []
	grupos = []
	for elem in lista:
		if elem != '':
			grupos.append(elem)
		else:
			fich.append(grupos)
			grupos = []
	return fich


def omega(file):
	dic= {} # key -> categoria v: ['brad pitt','john stalone']
	keyB = re.compile(r'^B-[A-Z]+')
	keyI = re.compile(r'^I-[A-Z]+')
	splits = organizer(file)
	typo = []
	for split in splits:
		for elem in split:
			
			if keyB.search(elem):
				category = elem.split('-')[1].split()[0]
				catInfo = elem.split('-')[1].split()[1]
				if category in dic:
					typo = dic[category]
				typo.append(catInfo)
				dic.update({category:typo})
				typo = []
			
			elif keyI.search(elem):
				category = elem.split('-')[1].split()[0]
				catInfo = elem.split('-')[1].split()[1]
				typo = dic[category]
				aux = typo[-1] + " " + catInfo
				del typo[-1]
				typo.append(aux)
				dic.update({category:typo})
				typo = []
			else:
				pass
	return dic



def beta (dic, info):
	semRepetidos = {}
	naoRepetidos = []
	for elem in dic:
		elemDic = {}
		for listado, nrs in zip(dic[elem], info[elem]):
			if listado in elemDic:
				elemDic[listado].append(nrs)
			else:
				elemDic.update({listado:[nrs]})
		semRepetidos.update({elem:elemDic})
	#aparte
	for elem in semRepetidos:
		a=0
		for category in semRepetidos[elem]:
			a+=1
		naoRepetidos.append(a)
	return semRepetidos, naoRepetidos


def main():
	directory = 'HTML/categorias'
	
	if len(os.listdir('HTML/categorias'))>0:
		print("Possui ficheiros (possivelmente) temporários em memória. Gostaria de os remover antes de prosseguir?(Y/N)")
		n=input()
		
		if n=='Y':
			for f in os.listdir(directory):
				os.remove(os.path.join(directory, f))
			print("Ficheiros eliminados")
		else:
			print("Não será removido qualquer ficheiro.")

	html.makeDirs()

	print("Por favor, insira o nome do ficheiro a tratar:")
	file = input()
	lista = open(file).read().split("\n")

	dic = omega(lista)
	info = alpha(lista)
	semRepetidos, naoRepetidos = beta(dic,info)

	html.htmlStyle()
	html.htmlHome(dic,naoRepetidos)
	html.htmlRepetidos(dic,info)
	html.htmlSemRepetidos(dic,semRepetidos)

	webbrowser.open('file://' + os.path.realpath('HTML/website.html'), new=2)  # open in new tab


main()