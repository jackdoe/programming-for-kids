# There are 3 doors
# behind one of them is a ghost,
# roll the dice until you find
# another door
while True:
  ghost = ⚂ % 3
  door = ⚂ % 3

  if door == ghost:
    print("RUUUNNN!!")
  else:
    print("phew! no ghost!")
    break
