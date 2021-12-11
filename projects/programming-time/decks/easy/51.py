# choose a random element from a
# list
def choice(data):
  # in the real world
  # imagine a 4294967296 sided dice
  # but in this game, 20 sided will
  # have to do
  dice = ⚂
  return data[dice % len(data)]


name = choice(["Alice", "Bob"])
age = choice([9, 10, 11, 12])

print("Hello!")
print("Name: " + name)
print("Age: " + str(age))
