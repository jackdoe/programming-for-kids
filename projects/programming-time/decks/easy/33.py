# pop() removes the last element
# from the list and returns it to
# the caller.
#
# a = [1,2,3]
# b = a.pop()
# 
# 'a' will become [1,2]
# and 'b' will be 3
#
a = [7,2,5,9] # [@],[@],[@],[@]

b = a.pop()
c = a.pop()

print(a[len(a)-1])
