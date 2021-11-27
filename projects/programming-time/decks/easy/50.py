table = [  # This is a simple
  [],      # hash table, from key
  [],      # to value.
  [],      # We store values based
  [],      # on first char of the
]          # key.

# naive, but reduces search time
# by 1/26 for random keys
def hash(s): # returns 0,1,2 or 3
  return ord(s[0]) % len(table)

def set(k,v):
  chain = table[hash(k)]
  if get(k) == None:
    chain.append([k,v]) # pair of
                        # key value
def get(k):
  chain = table[hash(k)]
  for e in chain: # only seach the
    if e[0] == k: # chain we need
      return e[1] # doesn't matter
  return None     # if we have
                  # million records
set('hello', 5)   # inserted in
set('world', 5)   # another chain
set('hoi',6)
print(get('hoi'))
