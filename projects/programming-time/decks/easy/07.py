# remove() element from a list takes
# a list and a value to remove it
# will walk over the list and skip
# all items equal to the value you
# want to remove, so
# remove([2,2,3,5],2) will return
# [3,5]. In python you can also do
# [2,4,6].remove(4) which will do
# remove "inplace" modifying the
# list itself.
def remove(data, removeme):
  filtered = []
  for element in data:
    if element != removeme:
      filtered.append(element)
  return filtered

players = [
  'jackie',
  'abby',
  'penny'
]

while len(players) != 1:
  # roll the dice every time
  # and select a player to kick out
  loser = players[⚂ % len(players)]
  players = remove(players, loser)

winner = players[0]
print(winner)
