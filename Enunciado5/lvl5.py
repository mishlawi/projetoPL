import re
import webbrowser

def alpha(lista):
	info = {}
	typo = []
	keyB = re.compile(r'^B-[A-Z]+')
	keyI = re.compile(r'^I-[A-Z]+')
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
		print(elem, " " , a)
	return semRepetidos


#HTML FUNCTIONS

def htmlStyle():
	htmlstyle = open(rf'styles/style.css',"w")
	htmlstyle.write(r'''html {
  font-size: 14px;
  font-family: 'Open Sans', sans-serif;
}


h1 {
  font-size: 60px;
  text-align: center;
}

p, li {
  font-size: 16px;
  line-height: 2;
  letter-spacing: 1px;
}

table {
  padding-top: 5px;
  text-align: center;
}

tr:nth-child(even) {background-color: #75E6DA;}

td{
  font-size: 16px;
  border: 1px solid black;
  padding: 15px;
}

th{
  font-size: 20px; 
  text-align: left;
  height: 50%;
  background-color: #05445E; 
  color: white;
}

html {
  background-color: #05445E;
}

body {
  width: 1200px;
  margin: 0 auto;
  background-color: #75E6DA;
  padding: 0 20px 20px 20px;
  border: 5px solid black;
}

h1 {
  margin: 0;
  padding: 20px 0;
  color: #00539F;
  text-shadow: 3px 3px 1px black;
}

/* Add a black background color to the top navigation bar */
.topnav {
  overflow: hidden;
  background-color: #e9e9e9;
}

/* Style the links inside the navigation bar */
.topnav a {
  float: left;
  display: block;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

/* Change the color of links on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Style the "active" element to highlight the current page */
.topnav a.active {
  background-color: #2196F3;
  color: white;
}

/* Style the search box inside the navigation bar */
.topnav input[type=text] {
  float: right;
  padding: 6px;
  border: none;
  margin-top: 8px;
  margin-right: 16px;
  font-size: 17px;
}

/* When the screen is less than 600px wide, stack the links and the search field vertically instead of horizontally */
@media screen and (max-width: 600px) {
  .topnav a, .topnav input[type=text] {
    float: none;
    display: block;
    text-align: left;
    width: 100%;
    margin: 0;
    padding: 14px;
  }
  .topnav input[type=text] {
    border: 1px solid #ccc;
  }
} ''')



def htmlcopy(file):
	fo = open(file,"w")
	fo.write(r"""<meta charset="UTF-8"/>
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


def html(file):
	htmlfirst = open("file.html","w")
	n=1
	htmlStyle()
	dic = omega(file)
	info = alpha(file)
	repetidos = beta(dic,info)
	htmlfirst.write("""<!DOCTYPE html>
<html>
   <head>
      <title>Enunciado 5</title>
      <meta charset="UTF-8"/>
      <link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">
      <link href="styles/style.css" rel="stylesheet" type="text/css">
   </head>
   <body>
      <h1> Enunciado 5, Trabalho Prático de Processamento de Linguagens</h1>
      <p>Realizado por:</p>
      <p> Duarte Oliveira A85517</p>
      <p> Tiago Barata A81195</p>
      <p> Simão Oliveira A57041</p>
      <hr>
    """
    )

	for elem in dic:

		htmlfirst.write(
			rf"""			
			<h2>{elem}</h2>
			<p>nº de elementos nesta categoria: {len(dic[elem])}</p>
			"""
			)

		htmln = open(rf'categorias/{elem}.html',"w")
		htmlrepeated = open(rf"categorias/{elem}2.html","w")
		
		htmln.write(
rf"""<!DOCTYPE html>
<html>
   <head>
      <link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">
      <link href="../styles/style.css" rel="stylesheet" type="text/css">
      <title>Info {elem} </title>
""")
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
# ______________________________________________________________________________________
		#supostamente a cena de escrever no html com os repetidos esta aqui
		htmlrepeated.write(
rf"""<!DOCTYPE html>
<html>
   <head>
      <link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">
      <link href="../styles/style.css" rel="stylesheet" type="text/css">
      <title>Info {elem} </title>
""")
		htmlrepeated.write(r"""<meta charset="UTF-8"/>
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

		htmlrepeated.write(rf"""<h1>Lista de elementos da categoria {elem}</h1>
<table>
<tr>
   <th>Elementos</th>
   <th>Linha da ocorrência</th>
</tr>
<tr>""")

		for categoria in repetidos[elem]:
			tam = len(repetidos[elem][categoria])+1
			htmlrepeated.write(rf"""
						<td rowspan={tam}>
	   {categoria} 
	</td>""")
			for ocorrencia in repetidos[elem][categoria]:
				htmlrepeated.write(rf"""
	<tr>
	<td>{ocorrencia}</td>
	</tr>
					""")
		#acaba aqui, o que está abaixo desta seccao esta bem
		for listado, nrs in zip(dic[elem],info[elem]):
			htmln.write(rf"""
					<td>
   {listado} 
</td>
<td>{nrs}</td>
</tr>
				""")
		htmln.write(rf"""
		</table>
	</body>
</html>""")
			
		htmlfirst.write(rf"""<a href="categorias/{elem}.html"> mais informação categoria {elem}</a>
			<a href="categorias/{elem}2.html"> Info repetidos categoria {elem}</a>

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

main()