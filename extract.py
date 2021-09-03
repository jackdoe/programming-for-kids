#! env
from os import listdir, makedirs
from os.path import isfile, join

for fn in listdir('.'):
    if isfile(fn) and fn.endswith('.md') and fn.startswith('week-0'):
        print("extracting",fn)
        path = join(".","examples",fn.replace('.md',''))
        try:
            makedirs(path)
        except FileExistsError:
            pass

        f = open(fn,"r")
        lines = f.readlines()
        f.close()

        id = 0
        current = None
        for line in lines:
            if line == '```\n':
                if current == None:
                    id += 1
                    current_name = join(path, "{:03d}.txt".format(id))
                    current = open(current_name,"w")
                    print("openning",current_name)
                else:
                    current.close()
                    current = None
            elif current != None:
                current.write(line)
        if current != None:
            current.close()
            current = None