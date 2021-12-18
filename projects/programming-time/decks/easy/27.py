# Morse code is an old method to
# encode characters into a sequence
# of short and long signals.
morse = {
  'a': '.-',     'b': '-...',
  'c': '-.-.',   'd': '-..',
  'e': '.',      'f': '..-.',
  'g': '--.',    'h':'....',
  'i': '..',     'j': '.---',
  'k': '-.-',    'l': '.-..',
  'm': '--',     'n': '-.',
  'o': '---',    'p': '.--.',
  'q': '--.-',   'r': '.-.',
  's': '...',    't': '-',
  'u': '..-',    'v': '...-',
  'w': '.--',    'x': '-..-',
  'y': '-.--',   'z': '--..',
  ' ': '/',
}
# encode string into a list of
# morse code signals, encode("sos")
# will return ['...','---','...']
def encode(str):
  r = []
  for c in str:
    r.append(morse[c])

  return r
password = "donald duck"
encoded = encode(password)
print(encoded[⚂ % len(encoded)])
