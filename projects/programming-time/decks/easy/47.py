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
b = a[2:5]

print(len(b))
