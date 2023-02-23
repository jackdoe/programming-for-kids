# pip install pyperclip
import pyperclip
import random
import time

# put scary strings inside the clipboard

scary = [
  'How dare you!',
  'I am alice inside this computer!',
  'Who are you?'
]

while True:
  pick = random.choice(scary)
  pyperclip.copy(pick)

  # sleep between 10 and 30 seconds
  time.sleep(random.randint(10,30))
  
