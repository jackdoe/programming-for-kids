# pip install psutil
import psutil
import random
import os
import time

def kill(pid):
  os.system(f"taskkill /PID {pid} /T /F")

while True:
  # sleep between 5 and 10 minutes
  time.sleep(random.randint(300,600))

  # A process is just a program that is
  # running at the moment, each process
  # has an ID assigned when it starts
  # called Process ID or PID.

  # You can see all running processess
  # with the command tasklist, just type
  # tasklist in the Command Prompt, and
  # taskkill /PID pid to kill specific
  # process

  # list all the processes and check if
  # Roblox is running
  for p in psutil.process_iter():
    if "Roblox" in p.name():
      kill(p.pid)

  
