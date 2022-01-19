# Bloom filters are a probabilistic
# data structure, if you dont find
# your key in it, it is guaranteed
# it was never added, but if you
# find it, it might be some other
# key
bloom = [0,0,0,0,0,0,0,0]

def hash(key):
  return key * 31

def put(key):
  # depending on the has function,
  # and the bloom filter size, many
  # keys might collide
  slot = hash(key) % len(bloom)
  bloom[slot] = 1

def seen(key):
  slot = hash(key) % len(bloom)
  return bloom[slot] == 1
  
put(⚂)
put(⚂)
put(⚂)
put(⚂)

if not seen(3):
  print("we have never seen it")
else:
  print("we might have seen it")
