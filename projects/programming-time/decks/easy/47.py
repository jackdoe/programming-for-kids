# You can get a substring or sublist
# with [from:to:step], for example
#
# s1 = [1,2,3]
# s2 = s1[0:2] will make s2 be [1,2]
#
# same with string
# s1 = 'hello'
# s2 = s1[0:2] will make s2 be 'he'
#
# s1 = 'banana'
# s2 = a[0:4:2]
# will make s2 equal 'bn' because it
# will start from 0th index, to 3rd
# index, and skip 2 characters at a
# time.

a = 'hello world'

# There is operator precedence in
# all programming languages, which
# means certain operations have
# higher priority than others, % has
# higher priority than +, so ⚂ %
# len(a) will be evaluated first,
# and then 2 + whatever the result
# from it was.
b = a[2:2 + ⚂ % len(a)]

print(len(b))
