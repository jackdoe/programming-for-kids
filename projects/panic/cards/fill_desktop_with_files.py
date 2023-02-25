import os
import random
import string

# create 10000 files on the user's
# desktop

def random_string(n):
  a = random.choices(
    string.ascii_lowercase,
    k=n
  )
  return ''.join(a)
  
def random_file_name():
  name = random_string(8)
  ext = random_string(3)
  return f"{name}.{ext}"

home = os.path.expanduser('~')
desktop = os.path.join(home, 'Desktop')

for i in range(10000):
  name = random_file_name()
  p = os.path.join(desktop, name)
  with open(p, "w") as f:
    f.write("panic")
