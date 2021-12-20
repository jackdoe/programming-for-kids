# depending on the action apply
# different operation to the value
def reduce(v, action):
  if (action["type"] == "INC"):
    return v + 1

  if (action["type"] == "DEC"):
    return v - 1

dice = ⚂

dice = reduce(dice, {"type":"INC"})
dice = reduce(dice, {"type":"DEC"})
dice = reduce(dice, {"type":"INC"})
dice = reduce(dice, {"type":"INC"})

print(dice)
