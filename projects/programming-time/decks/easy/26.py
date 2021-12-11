numbers = [1,2,3,4,5]
letters = ['a','b','c','d','e','f']
special = ['!','$','@']

# because we can not concatenate
# string and a integer, we need to
# make the integer into string
# str(1) makes the string '1'
n = str(numbers[⚂ % len(numbers)])
l = letters[⚂ % len(letters)]
s = special[⚂ % len(special)]

password = l + l + n + n + s + s

print(password)
