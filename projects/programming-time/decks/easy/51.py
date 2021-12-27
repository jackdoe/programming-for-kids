# A LinkedList is a data structure,
# where each element has a value and
# a pointer to the next element. The
# lists you usually use are called
# arrays where you can get to each
# element by its index, in a linked
# list you can not directly go to
# specific index, unless you follow
# the chain.
class LinkedList:
  def __init__(self, next, value):
    self.next = next
    self.value = value
# HINT: use pen and paper to follow
root = LinkedList(
  LinkedList(
    LinkedList(
      None,
      ⚂ # first dice roll
    ),
    ⚂ # second dice roll
  ),
  ⚂ # third dice roll
)
# start from the root and follow the
# chain of .next elements until we
# reach None.
element = root
while element != None:
  print(element.value)
  element = element.next
