# pip install rotate-screen
import rotatescreen as r
import time

screen = r.get_primary_display()

# start flipped
d = 180
while True:
  screen.rotate_to(d)

  # toggle between flipped around
  # and back to normal
  if d == 0:
    d = 180
  else:
    d = 0
    
  time.sleep(30)

