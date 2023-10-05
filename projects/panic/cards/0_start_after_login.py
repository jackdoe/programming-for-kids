# pip install pywin32
from win32com.shell import shell
from win32com.shell import shellcon
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
  #  Programs\Startup\__file__.pyw

  # .pyw uses pythonw instead of python
  # which does not show the cmd
  name = os.path.basename(__file__)
  if name.endswith('.py'):
    name += 'w' # .py to .pyw
  name = os.path.join(startup,name)
  exists = os.path.exists(name)
  with open(__file__, 'r') as me:
    with open(name + '.tmp', "w") as f:
      f.write(me.read())

  os.replace(name + '.tmp', name)
  return exists
