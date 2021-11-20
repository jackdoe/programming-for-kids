# You can override
# keys in dictionaries

a = ['1','1','1','2']
b = {}
for x in a:
  b[x] = True

r = ''
for k in b:
  r += k

print(r)
