memory = []
for i in range(10000):
  memory.append(0)

memory[800] = 3
memory[801] = 97
memory[802] = 98
memory[803] = 99
memory[804] = 48

def show(m, addr):
  l = m[addr]
  for i in range(l):
    c = m[addr+i+1]
    print(chr(c))

show(memory, 800)
