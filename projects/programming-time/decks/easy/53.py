class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    if self.age > 5:
      print(self.name + ' Woof!')
    else:
      print(self.name + ' oof!')

  def older(self, other_dog):
    # am I older than the other dog
    if self.age > other_dog.age:
      return True
    else:
      return False


ruffles = Dog('Ruffles', ⚂)
ruffles.bark()

max = Dog('Max', ⚂)
max.bark()

if max.older(ruffles):
  print("max is older")
else:
  print("ruffles is older")
