import os


def makeDirs():
    dir0 = './HTML'
    dir1 = './HTML/categorias'
    dir2 = './HTML/styles'
    if (os.path.exists(dir0) == False):
        os.mkdir(dir0)
    if (os.path.exists(dir1) == False):
        os.mkdir(dir1)
    if (os.path.exists(dir2) == False):
        os.mkdir(dir2)


def htmlStyle():
    directory = 'HTML/styles/style1.css'
    directory2 = 'HTML/styles/style2.css'
    
    if(os.path.isfile(directory) and os.path.isfile(directory2)):
        return

    htmlstyle = open(directory,"w")
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

tr:nth-child(even) {
    background-color: #75E6DA;
}

tr:nth-child(odd) {
    background-color: #D4F1F4;
}

table, th, td{
    border: 1px solid black;
    border-collapse: collapse;
    padding-top: 5px;
    text-align: center;
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
    background-color: #189AB4;
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
}  ''')

    htmlstyle = open(directory2,"w")
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

table, th, td{
    border: 1px solid black;
    border-collapse: collapse;
    padding-top: 5px;
    text-align: center;
    background-color: #75E6DA; 
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
    background-color: #189AB4;
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
}  ''')


def htmlHome(dic,naoRepetidos):
   
    htmlfirst = open("HTML/website.html","w")

    htmlfirst.write("""<!DOCTYPE html>
<html>
    <head>
        <title>Enunciado 5</title>
        <meta charset="UTF-8"/>
        <link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">
        <link href="styles/style1.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        <h1> 
            <b>Processamento de Linguagens</b>
            <br>
            Enunciado 5
        </h1>
        <p><h3><b> Realizado por: </b></h3></p>
        
            Duarte Oliveira A85517
            <br> 
            Tiago Barata A81195
            <br>
            Sim&atildeo Oliveira A57041
        <hr>""")
    x = 0
    for elem in dic:
        htmlfirst.write(
            rf"""           
        <h2>{elem}</h2>
            <p>n&ordm total de elementos nesta categoria: {len(dic[elem])} </p>
            <p>n&ordm total de elementos n&atildeo repetidos desta categoria {naoRepetidos[x]} </p>""")
            
        htmlfirst.write(
        rf"""
            <a href="categorias/{elem}Info.html"> Info {elem}</a>
            <br>
            <a href="categorias/{elem}InfoSRepeticao.html"> Info {elem} sem repetidos </a>
            <hr>""")
        x+=1

    htmlfirst.write(r"""
    </body>
</html>""")


def htmlRepetidos(dic, repetidos):
    for elem in dic:
        htmln = open(rf'HTML/categorias/{elem}Info.html',"w")
        htmln.write(rf"""
<!DOCTYPE html>
<html>
    <head>
        <link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">
        <link href="../styles/style1.css" rel="stylesheet" type="text/css">
        <title>Informa&ccedil&atildeo {elem} </title>""")
        htmln.write(r"""
        <meta charset="UTF-8"/>
    </head>
    <body>
        <div class="topnav">
        <a class="active" href="../website.html"> Home </a>
        </div>""")

        htmln.write(rf"""
        <h1>Lista de elementos da categoria {elem}</h1>
        <table>
            <tr>
                <th>Elementos</th>
                <th>Linha da ocorr&ecircncia</th>
            </tr>""")

        for listado, nrs in zip(dic[elem],repetidos[elem]):
            htmln.write(rf"""
            <tr>
                <td>{listado}</td>
                <td>{nrs}</td>
            </tr>""")
        
        htmln.write(rf"""
        </table>
    </body>
</html>""")


def htmlSemRepetidos(dic, semRepetidos):
    for elem in dic:
        htmlsemsepetidos = open(rf"HTML/categorias/{elem}InfoSRepeticao.html","w")
        htmlsemsepetidos.write(rf"""
<!DOCTYPE html>
<html>
    <head>
        <link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">
        <link href="../styles/style2.css" rel="stylesheet" type="text/css">
        <title>Informa&ccedilç&atildeo sem repetidos de {elem} </title>""")
        
        htmlsemsepetidos.write(r"""
        <meta charset="UTF-8"/>
    </head>
    <body>
        <div class="topnav">
            <a class="active" href="../website.html"> Home </a>
        </div>""")

        htmlsemsepetidos.write(rf"""
        <h1>Lista de elementos da categoria {elem}</h1>
        <table>
            <tr>
               <th>Elementos</th>
               <th>Linha da ocorr&ecircncia</th>
            </tr>""")

        for categoria in semRepetidos[elem]:
            tam = len(semRepetidos[elem][categoria])+1
            htmlsemsepetidos.write(rf"""
            <td rowspan={tam}>{categoria}</td>""")

            for ocorrencia in semRepetidos[elem][categoria]:
                htmlsemsepetidos.write(rf"""
            <tr>
                <td>{ocorrencia}</td>
            </tr>""")

        htmlsemsepetidos.write(rf"""
        </table>
    </body>
</html>""")