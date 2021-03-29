import re
import webbrowser

keyB = re.compile(r'^B-[A-Z]+')
keyI = re.compile(r'^I-[A-Z]+')
htmlfirst = open("file.html","w")


def alpha(lista):
	info = {}
	typo = []
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

def organizer(lista):
	splits = []
	splitter = []
	for elem in lista:
		if elem != '':
			splitter.append(elem)
		else:
			splits.append(splitter)
			splitter = []
	return splits


def omega(file):
	dic= {}
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


# (nome, linha)
def beta(file):
	repetidos = omega(file)
	linhaRepetida = alpha(file)
	semRepetidos = {}
	typo = ('',[])
	for elem in repetidos:
		for listado, nrs in zip(repetidos[elem],linhaRepetida[elem]):
				if elem  in semRepetidos:
					typo = semRepetidos[elem]
				semRepetidos.update({elem:typo})


def html(file):
	n=1
	dic = omega(file)
	info = alpha(file)
	htmlfirst.write("""<!DOCTYPE html>

<html>
	
	<head>
        <title>Enunciado 5</title>
        <meta charset="UTF-8"/>
        <link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">
    	<link href="styles/style.css" rel="stylesheet" type="text/css">
    	</head>
    <body>
    <h1> Enunciado 5, Trabalho Prático de Processamento de Linguagens, ano letivo 2020-2021</h1>
    <p>Realizado por:</p>
    <p> Duarte Oliveira a85517</p>
    <p> Tiago Barata a81195</p>
    <p> Simão Oliveira</p>
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
		<link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">
    	<link href="../styles/style.css" rel="stylesheet" type="text/css">
        <title>Info {elem} </title>""")

		htmln.write(r"""<meta charset="UTF-8"/>

        
    </head>
    <body>
  	   <div class="topnav">
	  <a class="active" href="../file.html"> Home </a>
	  <div class="search-container">
	    <form action="/action_page.php">
	      <input type="text" placeholder="Search.." name="search">
	      <button type="submit"><i class="fa fa-search"></i></button>
	    </form>
	  </div>
	</div>
	</div>
</div>
    """)
		htmln.write(rf"""<h1>Lista de elementos da categoria {elem}</h1>
    	
    	<table>
    		<tr>
    			<th>Elementos</th>
    			<th>Linha da ocorrência</th>
    		</tr>
    				<tr>""")
		
		for listado, nrs in zip(dic[elem],info[elem]):
			htmln.write("""
					<td>""")
		
			htmln.write(rf"""{listado} """
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
	file = input()
	file = open(file).read().split("\n")
	html(file)
	url = 'file.html'

	webbrowser.open(url, new=2)  # open in new tab


#main()
file = open("train.txt").read().split("\n")
beta(file)