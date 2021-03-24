import re
import webbrowser

keyB = re.compile(r'^B-[A-Z]+')
keyI = re.compile(r'^I-[A-Z]+')
htmlfirst = open("file.html","w")


def alpha(name):
	fo = open(name)
	info = {}
	typo = []
	n = 1
	splits = fo.readlines()

	for lines in splits:
		if keyB.search(lines):
			category = lines.split('-')[1].split()[0]
			if category in info:
				typo = info[category]
			typo.append(n)
			info.update({category:typo})
			typo = []
		n+=1
	return info

def organizer(name):
	file = open(name).read()
	a = file.split('\n')
	splits = []
	splitter = []

	for elem in a:
		if elem != '':
			splitter.append(elem)
		else:
			splits.append(splitter)
			splitter = []
	return splits


def omega(name):
	dic= {}
	splits = organizer(name)
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
	
	return dic


def html(name):
	n=1
	dic = omega(name)
	info = alpha(name)
	htmlfirst.write("""<!DOCTYPE html>

<html>
	
	<head>

        <title>Enunciado 5</title>
        <meta charset="UTF-8"/></head>
    <body>
    <h1> Enunciado 5, Trabalho Prático de Processamento de Linguagens, ano letivo 2020-2021</h1>
    <p>Realizado por:</p>
    <p> Duarte Oliveira a85517</p>
    <p> Tiago Barata </p>
    <p> Simão Santa-Cruz</p>
   	<hr>
    """
    )

	for elem in dic:

		htmlfirst.write(rf"""
			
			<h2>{elem}</h2>
			<p>nº de elementos nesta categoria: {len(dic[elem])}</p>

			"""
			)

		htmln = open(rf'categorias/{elem}.html',"w")
		htmln.write(rf"""<!DOCTYPE html>

<html>
	
	<head>

        <title>Info {elem} </title>

        <meta charset="UTF-8"/></head>
    <body>
    <h1>Lista de elementos da categoria {elem}</h1>
    	<a href="../file.html"> retornar à página principal </a>
    	<table>
    		<tr>
    			<th>elementos</th>
    			<th>linha da ocorrência</th>
    		</tr>
    				<tr>""")
		
		for listado, nrs in zip(dic[elem],info[elem]):
			htmln.write("""
					<td>""")
			
			for indices in listado:
				htmln.write(rf"""{indices} """
			)
			htmln.write("""</td>
					<td>""")
			htmln.write(rf"""{nrs}</td>
				</tr>
				""")
		htmln.write(rf"""
		</table>
	</body>
</html>""")
			
		htmlfirst.write(rf"""<a href="categorias/{elem}.html"> mais informação categoria {elem}</a>
			<hr>
			""")
	htmlfirst.write(r"""</body>
		</html>""")

def main():
	print("Por favor, insira o nome do ficheiro a tratar:")
	name = input()
	html(name)
	url = 'file.html'

	webbrowser.open(url, new=2)  # open in new tab


main()