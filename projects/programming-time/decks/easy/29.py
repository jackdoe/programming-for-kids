animal = 'hippopotamus'

b = ⚂

if b >= len(animal):
  b = 0

# you can access each character of a
# string by its index starting from
# 0, if the string is x = 'abc' then
# x[0] is 'a', x[1] is 'b' and x[2]
# is 'c', and len(x) is 3, if you
# try to access x[3], you will get
# IndexError: string index out of
# range.
print(animal[b])
