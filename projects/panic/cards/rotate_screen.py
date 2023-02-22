# pip install rotate-screen
import rotatescreen as r
import time
import random

screen = r.get_primary_display()
o = screen.current_orientation()

while True:
  # most of the time rotate it to the
  # current orientation but from time to
  # time, flip it around to the left
  # or right
  d = random.choice([o,o,o,90,270])
  screen.rotate_to(d)

  # sleep 5 to 10 minutes
  time.sleep(random.randint(300,600))

