import re

fo = open("test.txt").read()
htmlfirst = open("file.html","w")

keyB = re.compile(r'^B-[A-Z]+')
keyI = re.compile(r'^I-[A-Z]+')


def organizer():
	global fo
	a = fo.split('\n')
	splits = []
	splitter = []

	for elem in a:
		if elem != '':
			splitter.append(elem)
		else:
			splits.append(splitter)
			splitter = []
	return splits

def omega():
	dic= {}
	splits = organizer()
	typo = []
	for split in splits:
		for elem in split:
			
			if keyB.search(elem):
				category = elem.split('-')[1].split()[0]
				catInfo = elem.split('-')[1].split()[1]
				if category in dic:
					typo = dic[category]
				typo.append([catInfo])
				dic.update({category:typo})
				typo = []
			else:	
				if keyI.search(elem):
					category = elem.split('-')[1].split()[0]
					catInfo = elem.split('-')[1].split()[1]
					typo = dic[category]
					aux = typo[-1]
					del typo[-1]
					aux.append(catInfo)
					typo.append(aux)
					dic.update({category:typo})
					typo = []
	print(dic)
	return dic





#esta parte está em obras
def html():
	n=1
	dic = omega()
	htmlfirst.write("""<!DOCTYPE html>

<html>)
	
	<head>

        <title>Enunciado 5</title>
        <meta charset="UTF-8"/></head>
    <body>
   
    """
    )

	for elem in dic:

		htmlfirst.write(rf"""
			
			<h{n}>{elem}</h{n}>
			<p>nº de elementos nesta categoria: {len(dic[elem])} </p>

			""")
		n+=1
		htmln = open(rf'categorias/{elem}.html',"w")
		htmln.write(rf"""<!DOCTYPE html>

<html>
	
	<head>

        <title>Info {elem} </title>

        <meta charset="UTF-8"/></head>
    <body>

    <h1>Lista de elementos da categoria {elem}</h1>
   	<a href="../file.html"> retornar à página principal </a>


    """)
		for listado in dic[elem]:
			htmln.write("<p>")
			for indices in listado:
				htmln.write(rf"""{indices} """
			)
			htmln.write("</p>")
		htmlfirst.write(rf"""		<a href="categorias/{elem}.html"> mais informação {elem}</a>
			<hr>
			""")



html()