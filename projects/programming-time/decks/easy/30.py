def pick(data):
  return data[⚂ % len(data)]

# R = Rock, P = Paper, S = Scissors
game = ["R","P","S"]

wins_a = 0
wins_b = 0

while wins_a < 3 and wins_b < 3:
  a = pick(game)
  b = pick(game)

  if a == b:
    print('Tie!')    
  elif a == 'R' and b == 'S':
    wins_a += 1
  elif a == 'R' and b == 'P':
    wins_b += 1
  elif a == 'P' and b == 'S':
    wins_b += 1
  elif a == 'P' and b == 'R':
    wins_a += 1
  elif a == 'S' and b == 'P':
    wins_a += 1
  elif a == 'S' and b == 'R':
    wins_b += 1

print(wins_a)
print(wins_b)
