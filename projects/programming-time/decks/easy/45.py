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
  if x > 10:
    print('up')

def observerB(x):
  if x < 10:
    print('down')

def send(v):
  for o in observers:
    o(v)

# Adding the functions observerA and
# B to the list, you see, its the
# function itself, not its return
# value
observers.append(observerA)
observers.append(observerB)

send(⚂)

