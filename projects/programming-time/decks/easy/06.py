# render the tic tac toe game,
# example output:
#  0 - - 
#  - 0 x 
#  x - -
def render(game):
  for i in range(len(game)):
    if i != 0 and i % 3 == 0:
      # pring empty line every
      # 3rd item
      print('')

    # by default end='\n' which
    # means if you dont specify
    # print() will add new line to
    # the end, end=' ' prints space
    print(game[i], end=' ')
  # 8 is not divisable by 3
  print('')

game = [
  '-','-','-',
  '-','-','-',
  '-','-','-',
]

game[0] = '0'
game[⚂ % 9] = 'x'
game[4] = '0'
game[⚂ % 9] = 'x'
render(game)
