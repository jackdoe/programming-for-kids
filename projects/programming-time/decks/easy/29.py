# depending on the action apply
# different operation to the value
def reduce(v, action):
  # check if the action is a
  # function
  if callable(action):
    return action(v)
    
  if (action["type"] == "INC"):
    return v + 1

  if (action["type"] == "DEC"):
    return v - 1

dice = ⚂

dice = reduce(dice, {"type":"INC"})
dice = reduce(dice, {"type":"DEC"})
dice = reduce(dice, {"type":"INC"})
dice = reduce(dice, {"type":"INC"})

# You can make anonymous or nameless
# function with the `lambda`
# keyword, in this case we a
# function that takes one parameter
# x and returns x/2.
dice = reduce(dice, lambda x: x/2)

print(dice)
