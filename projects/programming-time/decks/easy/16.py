# roll the dice until it is smaller
# than `max`
def roll(max):
  while True:
    dice = ⚂
    if dice < max:
      return dice

# make a line half with # and half %
# e.g line(5) will return ###%%
def line(n):
  s = ''
  for i in range(n):
    if i >= n/2:
      s += '%'
    else:
      s += '#'

  return s

def box(w,h):
  s = ''
  for i in range(h):
    s += line(w) + '\n'

  return s

width = roll(10)
height = roll(10)
print(box(width,height))
