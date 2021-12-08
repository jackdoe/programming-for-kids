# you can have multiline strings
# in python with """ instead of "
#
# '\n' is the new line character.
# so you can split by it. The ASCII
# code for \n is 10.

message = """Hi,
Long time no see, This is a letter
from Python, a new programming
language I am learning. It also
supports multiline strings.

Best,
Jack
"""

if chr(96+⚂) in message:
  message += "Have a nice day!"
else:
  message += "Have a good day!"

lines = message.split('\n')
print(lines[len(lines)-1])
