# pip install psutil
import psutil, random, os, time

def kill(pid):
  os.system(f"taskkill /PID {pid} /T")

while True:
  # A process is just a program that is
  # running at the moment, each process
  # has an ID assigned when it starts
  # called Process ID or PID.

  # You can see all running processess
  # with the command tasklist, just type
  # tasklist in the Command Prompt, and
  # taskkill /PID pid to kill specific
  # process

  # psutil.pids() will give a list of
  # the ids of all running processess.

  # random.choice(list) picks random
  # element from a list, so this line
  # picks a random process id.
  pid = random.choice(psutil.pids())
  kill(pid)

  # sleep between 5 and 10 minutes
  time.sleep(random.randint(300,600))

  
