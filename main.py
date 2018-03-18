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

print '<html><head></head><body>'

print '<font size=50> FUCK YOU WORDPRESS </font>\n'

print gettext(joinpath(pagesroot,rnddir,'title.txt'))
print gettext(joinpath(pagesroot,rnddir,'text.txt'))
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

for i in imagestestlist:
    print '<img src="' + websitepath + pagesroot + '/' + rnddir + '/' +  i + '">\n'





print('</body></html>')

