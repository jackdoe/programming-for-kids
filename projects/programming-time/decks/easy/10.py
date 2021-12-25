# reverse polish notation calculator
calc = [⚂, ⚂, '+', ⚂, '*', 3, '-']

# * take 2 numbers from the front
# * take 1 operation
# * compute the result and put back
# * print the result if only
#   one element is left
while True:
  a = calc.pop(0)
  b = calc.pop(0)
  op = calc.pop(0)
  if op == '+':
    calc.insert(0, a + b)
  if op == '-':
    calc.insert(0, a - b)
  if op == '*':
    calc.insert(0, a * b)
    
  if len(calc) == 1:
    print(calc[0])
    break
    
