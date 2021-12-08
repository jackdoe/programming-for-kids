# Classes are blueprints of code
# that describe what an object can
# do. To make a new dog use
# Dog('Ruffles',5), this calls the
# __init__ function with magic
# parameter self(the newlly created
# dog), name and age. ruffles.bark()
# will call the bark() method on the
# object ruffles. Or you can make a
# bark() function that takes a name:
#   def bark(name):
#      print(name + 'oof!')
#   bark('Ruffles')
# The first one is called object
# oriented programming(OOP), and the
# second is called procedural
# programming
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    if self.age > 5:
      print(self.name + ' Woof!')
    else:
      print(self.name + ' oof!')

ruffles = Dog('Ruffles', ⚂)
ruffles.bark()
