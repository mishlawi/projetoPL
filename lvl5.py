import re

fo = open("test.txt").read()
ff = open("file.html","w")

keyB = re.compile(r'^B-[A-Z]+')
keyI = re.compile(r'^I-[A-Z]+')


#rascunho = [line.rstrip() for line in fo]

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
			if keyB.search(elem) or keyI.search(elem):
				category = elem.split('-')[1].split()[0]
				catInfo = elem.split('-')[1].split()[1]
				if category in dic:
					typo = dic[category]
				typo.append(catInfo)
				dic.update({category:typo})
				typo = []
	return dic
	print(dic)

def categoryMaker():
	dic = omega()
	print(dic)

categoryMaker()



#esta parte está em obras
def htmlfirst():
	n=1
	dic = omega()
	ff.write("""<!DOCTYPE html>

<html>)
	
	<head>

        <title>Enunciado 5</title>

        <meta charset="UTF-8"/>
    </head>
    <body>
    	<section>
    """
    )

	for elem in dic:

		ff.write(rf"""<h{n}>{elem}</h{n}>
			""")
		n+=1
		ff.write(rf'<a href="{elem}.html"> ')


