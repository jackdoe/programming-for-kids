# Welcome to the haunted house!
# ⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂
# 
#     ___
#   _/ @@\   +--0--+ +--1--+ +--2--+
#  ( \  O/__ |     | |     | |     |
#   \    \__)|*    | |*    | |*    |
#   /     \  |     | |     | |     |
#  /      _\ |     | |     | |     |
# `"""""``   +-----+ +-----+ +-----+
# (ghost art
#  by jgs)
#
#
# There are 3 doors.
# Behind one of the doors there is a
# ghost.
#
# Roll the dice until your door is
# different from the ghost's door.
while True:
  ghost_door = ⚂ % 3
  your_door = ⚂ % 3

  if your_door == ghost_door:
    print("RUUUNNN!!")
  else:
    print("phew! no ghost!")
    break
