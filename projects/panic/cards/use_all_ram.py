# pip install psutil
import psutil
import time

def make_1gb_string():
  data = "Z" * 1024 * 1024 * 1024
  return data

l = []


total = psutil.virtual_memory().total

while total > 0:
  d = make_1gb_string()
  total -= len(d)
  l.append(d)

while True:
  n = 0
  # touch every byte of the used memory
  # so it is not swapped out
  for d in l:
    for c in d:
      n += ord(c)
  
  time.sleep(1)
