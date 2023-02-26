# pip install pywin32
import win32com.client as wincl
import random
import time

# say random things from time to time

words = [
  "Hello, who are you?",
  "I am just thinking about stuff.",
  "What are you thinking about?",
  "Make sure you turn your computer \
  off the night before year 2000",
  "Stop playing videogames and study!",
]

speak = wincl.Dispatch("SAPI.SpVoice")

random.seed(time.time())

while True:
  time.sleep(random.randint(10,30))
  speak.Speak(random.choice(words))
