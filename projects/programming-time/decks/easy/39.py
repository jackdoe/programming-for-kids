# To split a string by a separator
# start from the left, and build
# a temporary string char by char
# until you see a character matching
# the separator, then append the
# temporary string to the result,
# and reset it to empty.

def split(str, sep):
  r = []
  tmp = ''
  for char in str:
    if char == sep:
      r.append(tmp)
      tmp = ''
    else:
      tmp += char

  r.append(tmp)
  return r
    
text = "hellothisispython"

# or just use the split method on
# the string object: text.split(" ")
splitted = split(text, chr(96+⚂))

print(splitted[0])
