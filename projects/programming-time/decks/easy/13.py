# There are 3 doors
# behind one of them is a ghost,
# roll the dice until you find
# another door
while True:
  ghost_door = ⚂ % 3
  your_door = ⚂ % 3

  if your_door == ghost_door:
    print("RUUUNNN!!")
  else:
    print("phew! no ghost!")
    break
