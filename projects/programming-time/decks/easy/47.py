# You can get a substring or sublist
# with [from:to:step], for example
#
# a = [1,2,3]
# b = a[0:2] will make 'b' be [1,2]
#
# same with string
# a = 'hello'
# b = a[0:2] wlll make 'b' be 'he'
#
# a = 'banana'
# b = a[0:4:2]
# will make 'b' equal 'bn' because
# it will start fro 0th index, to
# 3rd index, and skip 2 characters
# at a time.

a = 'hello world'
b = a[2:5]

print(len(b))
