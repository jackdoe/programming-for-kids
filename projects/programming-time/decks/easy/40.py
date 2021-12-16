def equal(memory, addrA,addrB):
  type1 = memory[addrA]
  type2 = memory[addrB]
  if type1 != type2:
    return False

  if type1 == 1: # if integer
    v1 = memory[addrA + 1]
    v2 = memory[addrB + 1]
    return v1 == v2
  
  if type1 == 2:  # if string
    len1 = memory[addrA + 1]
    len2 = memory[addrB + 1]
    if len1 != len2:
      return False
    for i in range(len1):
      char1 = memory[addrA + 2 + i]
      char2 = memory[addrB + 2 + i]
      if char1 != char2:
        return False
    return True
# mem is a list with 1000 zeroes
mem = [0] * 1000 
x = 552
mem[x] = 1 # type 1 for integer
mem[x+1] = ⚂ % 4
y = 782
mem[y] = 1 # type 1 for integer
mem[y+1] =  ⚂ % 4
print(equal(mem,x,y))
