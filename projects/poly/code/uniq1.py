# deduplicate a list of integers
#   [1,1,3,2,1]
# returns:
#   [1,3,2]
def uniq(x):
   r = []
   for v in x:
      seen = False
      for v1 in r:
         if v == v1:
            seen = True

      if not seen:
         r.append(v)

   return r

print(uniq([1,1,2,3,3,4,1,2,7,1]))
