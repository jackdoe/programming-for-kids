# do basic math operations on `a`
# and `b`, supports +,-,*,/
def calc(op, a, b):
  if op == '+':
    return a + b
  if op == '-':
    return a - b
  if op == '*':
    return a * b
  if op == '/':
    return a / b


x = ⚂
y = ⚂
r = calc('+',x,y) * calc('-',x,y)

print(r)
