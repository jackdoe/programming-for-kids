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
# key. The ASCII table is an
# example of a dictionary, from
# character (key) to its ASCII code
# (value)
ascii = {
     97: 'a',  98: 'b',  99: 'c',
    100: 'd', 101: 'e', 102: 'f',
    103: 'g', 104: 'h', 105: 'i',
    106: 'j', 107: 'k', 108: 'l',
    109: 'm', 110: 'n', 111: 'o',
    112: 'p', 113: 'q', 114: 'r',
    115: 's', 116: 't', 117: 'u',
    118: 'v', 119: 'w', 120: 'x',
    121: 'y', 122: 'z'
}
# to get the character of code 122
# we can look it up with ascii[122]
c = ascii[96 + ⚂]
print(c)
