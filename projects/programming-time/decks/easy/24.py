# A dictionary is a super nice way
# to organize data so that you can
# access things by their name or
# key. Unlike lists where we need to
# know the position of a value we
# need in order to use it, or we
# have to iterate over the whole
# list to see if we can find the
# value we are looking for.
# Dictionaries allow us to instantly
# lookup and find a value by its
# key.  The ASCII table is an
# example of a dictionary, from
# character (key) to its ASCII code
# (value)

ascii_letters = {
  'a': 97, 'b': 98, 'c': 99,
  'd': 100,'e': 101, 'f': 102,
  'g': 103, 'h': 104, 'i': 105,
  'j': 106, 'k': 107, 'l': 108,
  'm': 109, 'n': 110, 'o': 111,
  'p': 112, 'q': 113, 'r': 114,
  's': 115, 't': 116, 'u': 117,
  'v': 118, 'w': 119, 'x': 120,
  'y': 121, 'z': 122
}
# to get the code of 'z' we can look
# it up with ascii_letters['z']
code = ascii_letters[chr(96+⚂)]
print(code)
