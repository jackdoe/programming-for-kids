# Lists are one of the most handy
# data structures, you can use them
# for all kinds of things, like
# in this example, for a tic-tac-toe
# game.

game = [
  '0','x','x',
  '-','x','-',
  '0','x','0',
]

# incomplete, checks only middle
# vertical, but you get the idea
def win(g, symbol):
  if g[1] == symbol:
    if g[4] == symbol:
      if g[7] == symbol:
        return True
  return False

game[⚂ % len(game)] = '0'

if win(game, 'x'):
  print('x')
elif win(game, '0'):
  print('0')
else:
  print('-')

  
