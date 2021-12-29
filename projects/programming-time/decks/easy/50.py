table = [  # This is a simple
  [],      # Chaining Hash Table
  [],      # with 4 chains(buckets).
  [],      # We store [key,value]
  [],      # pairs in specific chain
]          # based on the hash
           # function.
# Naive hash function. Many words
# start with the same character.
def hash(s): # returns 0,1,2 or 3
  return ord(s[0]) % len(table)

def put(k,v): # key, value
  if get(k) == None:
    chain = table[hash(k)]
    chain.append([k,v]) # pair of
                        # key value
def get(k):
  chain = table[hash(k)]
  for e in chain: # only search the
    if e[0] == k: # chain we need
      return e[1] # doesn't matter
  return None     # if we have
                  # million records
put('hello', ⚂)   # inserted in
put('world', ⚂)   # another chain
put('hoi', ⚂)
if get('hoi') > 5:
  print(get('hello'))
else:
  print(get('world'))
