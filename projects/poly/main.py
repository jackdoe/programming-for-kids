from os import listdir
CARD = 5
listed = listdir('./code')
listed.sort()
for fn in listed:
    if not '.' in fn:
        continue
    
    lang = ''
    if fn.endswith('.c'):
        lang = 'c'
    if fn.endswith('.js'):
        lang = "js"

    if fn.endswith('.go'):
        lang = "go"
        
    if fn.endswith('.py'):
        lang = 'python'
        
    print(f"CARD:{CARD}:{lang}")
    skip = True
    with open(f"./code/{fn}","r") as f:
        CARD+=1
        card = []
        for line in f.read().splitlines():
            line = line.rstrip()

            if 'package' in line:
                continue

            if 'main' in line:
                break

            if 'console' in line or line.startswith("\t\"") or line == ')' or line == 'import (':
                continue

            if 'function' in line or 'func' in line or 'def' in line or '(' in line and not 'import' in line:
                skip = False

            if line.startswith('import'):
                continue
            
            if 'print' in line:
                break

            if not line.startswith('#include') and (not skip or len(line) > 0):
                line = line.replace("\t","  ")
                card.append(line)

        n = int((32/2)) - int((len(card)) / 2)
        print('\n' * n, end='')
        for line in card:
                print(line)
