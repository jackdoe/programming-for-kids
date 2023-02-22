from win32com.shell import *
import os

def start_after_login():
  # find the current user's startup dir
  startup = shell.SHGetFolderPath(
    0,
    shellcon.CSIDL_STARTUP,
    0,
    0)
  # will create:
  # C:\Users\$USER\AppData\Roaming\
  #  Microsoft\Windows\Start Menu\
  #  Programs\Startup\s.cmd
  #
  # which will run pythonw name.py
  # after the user logs in
  bat = os.path.join(startup, "s.cmd")
  tmp = bat + ".tmp"
  with open(tmp, "w") as f:
    # using pythonw instead of python
    # will not show the cmd window but
    # will just run the python script
    f.write(f"pythonw {__file__}")

  # if the write was successful rename
  # the temporary file into the actual
  # bat file name
  os.replace(tmp, bat)
