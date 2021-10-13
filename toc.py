from os import listdir, makedirs
from os.path import isfile, join

toc = open("toc.md", "w")
day = 0
dir =  listdir('.')
dir.sort()

toc.write("## week - 0\n")

for fn in dir:
    if isfile(fn) and fn.endswith('.md') and fn.startswith('week-0'):
        print("extracting",fn)

        f = open(fn, encoding="utf8", mode="r")
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line[:-1]
            if line.startswith('## [DAY-'):
                day += 1
                if day % 7 == 0:
                    toc.write("## week - " + str(int((day+1) / 7)) + "\n")
                    toc.write('\n\n')
                clear = line.lower().replace('## ','').replace('[','').replace(']','')
                toc.write('\n['+clear+'](#'+clear.replace(' ','-').replace(',','-').replace('/','').replace(';','-')+')\n')

toc.close()