# Functions can also be values.
# We can add function to a list.
# For example, if we want to
# send a message, and let functions
# react to the message, its a common
# pattern, to just have a list of
# functions and call each one with
# the message.
observers = []

def observerA(x):
  if x == 5:
    print(x)

def observerB(x):
  if x == 3:
    print(x)

def send(v):
  for o in observers:
    o(v)

observers.append(observerA)
observers.append(observerB)

send(6)
send(5)
