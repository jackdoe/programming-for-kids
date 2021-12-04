# Start left to right, character
# by character, and multiply
# it by 10 with len(s) - i
# 10**3 means 10 to the power
# of 3, or 10*10*10, or 100
#
# To convert the char '3' ASCII 51
# to number 3 you have to subtract
# the ascii of 0, which is 48,
# so 51 - 48 = 3
#
# 3*100 + 2*10 + 8*1 = 328

def to_integer(s):
  result = 0
  zero = ord('0')
  ten = len(s) - 1

  for char in s:
    digit = ord(char) - zero
    result += digit * (10 ** ten)
    ten -= 1
  return result

a = '328' # [@][@][@]

# or just use int(a)
print(to_integer(a))
