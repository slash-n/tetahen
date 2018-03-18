import os
import random
import codecs
joinpath = os.path.join

_root = ""

pagesroot = joinpath(_root,'pages')

websitepath = "https://tetahen.freeshells.org/site/"

def getrandomdir(dirs):
    rndpos = random.randint(0,len(dirs) -1)
    return dirs[rndpos]
    
def gettext(path):
	f = codecs.open(path,'rb','utf-8')
	text = f.read()
	f.close
	return text

imagessubdirs = os.listdir(pagesroot)

rnddir = getrandomdir(imagessubdirs)

imagestestlist = os.listdir(pagesroot + '/' + rnddir)

title = gettext(joinpath(pagesroot,rnddir,'title.txt'))
text = gettext(joinpath(pagesroot,rnddir,'text.txt'))
categories = gettext(joinpath(pagesroot,rnddir,'categ.txt')).split()

relatedpages = []

for cat in categories:
	catpages = os.listdir(joinpath(_root,'categories',cat))
	
	for c in catpages:		
		if not rnddir in c:
			relatedpages.append(c)
	
	if len(relatedpages) > 3:
		break

imagestestlist = sorted(imagestestlist)

body = """"""

for i in imagestestlist:
    body += '<img src="' + websitepath + pagesroot + '/' + rnddir + '/' +  i + '">\n'


template = gettext('maintemplate.html')

templatestyle,templatebody = template.split("</style>")
templatestyle += "</style>"

bodyformatted = templatebody.format(sitename='TetaHen',categories='c1 c2 c3 c4 c5',title=title,text=text,body=body,advert='')

print templatestyle.encode("utf-8")
print templatebody.encode("utf-8")


"""{sitename}
{categories}
{title}
{text}
{body}
{advert}"""
