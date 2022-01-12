# Reverse Polish Notation (RPN).
# See `(3 + 2) * 4` in different
# notations:
#   Prefix    │  Infix  │ Postfix
#    (PN)     │         │  (RPN)
# ────────────┼─────────┼──────────
# * (+ 2 4) 4 │ (3+2)*4 │ 3 2 + 4 *
# ────────────┴─────────┴──────────
calc = [⚂, ⚂, '+', ⚂, '*']
# lambda is a way to make anonynmous
# (nameless) function
ops = {
  '+': lambda a,b: a + b,
  '*': lambda a,b: a * b,
  '/': lambda a,b: a / b,
}
# we can use a list like a stack of
# cards, append adds a card on top
# and pop removes the top card
stack = []
for tk in calc:
  print(stack)
  if tk in ops:
    x,y = stack.pop(),stack.pop()
    # lookup and call the operation
    result = ops[tk](x,y)
    stack.append(result)
  else:
    stack.append(tk)

print(stack.pop())
