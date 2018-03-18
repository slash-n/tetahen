import os
import random

imagesdir = "wp/upl/images"
websitepath = "https://tetahen.freeshells.org/"

def getrandomdir(dirs):
    rndpos = random.randint(0,len(dirs) -1)
    return dirs[rndpos]

imagessubdirs = os.listdir(imagesdir)

rnddir = getrandomdir(imagessubdirs)

imagestestlist = os.listdir(imagesdir + '/' + rnddir)

print '<html><head></head><body>\n'

print '<font size=50> FUCK YOU WORDPRESS </font>\n'

imagestestlist = sorted(imagestestlist)

for i in imagestestlist:
    print '<img src="' + websitepath + imagesdir + '/' + rnddir + '/' +  i + '">\n'

print('</body></html>')
