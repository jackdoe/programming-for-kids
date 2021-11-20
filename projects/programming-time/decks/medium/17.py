# you can index into
# a string, just as 
# lists
#
# s = "abc"
# s[0] is 'a'
# s[1] is 'b'
# s[2] is 'c'

a = 'hello world'

m = 0

for i in range(len(a)):
  if a[i] == 'o':
    m += 1

print(m)
