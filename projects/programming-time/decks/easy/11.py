# characters are stored in the
# computer as numbers, using the
# ASCII standard, using ord(char)
# you can get the ascii code of a
# character, and chr(code) gets you
# the char.
# 
# ord('a') -> 97   chr(97) -> 'a'
# ord('b') -> 98   chr(98) -> 'b'
# ord('c') -> 99   chr(99) -> 'c'
#
# rot13() is an early encryption
# method, each character is replaced
# with character 13 places away
#
# a b c d e f g h i j k l m
# ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕ ↕
# n o p q r s t u v w x y z
def rot13(c):
  n =  ord(c) - ord('a')
  return chr(97 + ((n + 13) % 26))


message = [⚂, ⚂, ⚂]
encrypted = ''
for c in message:
  # 96+1 is 97
  # chr(97) is 'a'
  encrypted += rot13(chr(96 + c))

print(encrypted)
