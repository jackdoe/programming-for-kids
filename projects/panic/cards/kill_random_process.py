# install psutil with running:
#   pip install psutil
# in the command prompt
import psutil
import random
import os
import time

def kill(pid):
  os.system(f"taskkill /PID {pid} /T")

while True:
  # a process is just a program that is
  # running at the moment

  # psutil.pids() will give a list
  # of the ids of all running processess

  # random.choice(list) picks random
  # element from a list, so this picks a
  # random process id
  pid = random.choice(psutil.pids())
  kill(pid)

  # sleep between 5 and 10 minutes
  time.sleep(random.randint(300,600))

  
