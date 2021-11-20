class Actor:
  x = 0
  y = 0

player = Actor()

def update():
  player.x += 1
  player.y += 1

def draw():
  print(player.x)
  print(player.y)

while True:
  update()
  draw()

  break
