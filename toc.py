from os import listdir
from os.path import isfile
import re

toc = open("toc.md", "w")
day = 0
dir =  listdir('.')
dir.sort()

def sanitize(s):
    return s.replace(',','').replace('/','').replace('; ','-').replace(' ','-')

for fn in dir:
    if isfile(fn) and fn.endswith('.md') and fn.startswith('week-0'):
        m = re.match("week-(\d+)\.md", fn)
        if m:
            week = m.group(1)
        else:
            print("skipping ", fn)
            continue

        print("extracting",fn)
        f = open(fn, encoding="utf8", mode="r")
        lines = f.readlines()
        f.close()

        toc.write("## week - " + week + "\n")
        toc.write('\n\n')

        for line in lines:
            line = line[:-1]
            if line.startswith('## [DAY-'):
                clear = line.lower().replace('## ','').replace('[','').replace(']','')
                toc.write('\n['+clear+'](#'+sanitize(clear)+')\n')


toc.close()
