import os
import codecs
joinpath = os.path.join

pages = os.listdir('pages')

def gettext(path):
	f = codecs.open(path,'rb','utf-8')
	text = f.read()
	f.close()
	return text

for p in pages:
	categories = gettext(joinpath('pages',p,'categ.txt')).split()
	
	for c in categories:
		categfile = joinpath('categories',c,p)
		if not os.path.exists(categfile):
			os.makedirs(categfile)
			print categfile
		else:
			print categfile,'classification already exists'


