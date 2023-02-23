import os
from itertools import cycle
CARD = 1

def card_meta(id, lang, symbol, symbol_style):
  color = '#6e7781' 
  bgcolor = 'white'
  theme='gptredzz'
  font='BlockZone'
  fontSize='25px'
  if lang == '':
    color = 'yellow'
    bgcolor = 'black'
    

  return f"CARD:{id}:{lang}:{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}:{symbol}:{symbol_style}"
  
  
def card_str(x):
  global CARD
  print(card_meta(CARD,"","",""))

  CARD+=1
  print(x)
  print()

card_str(f"""{'PANIC'.center(40)}
""")

card_str(f"""{'ETHICS'.center(40)}
""")

card_str(f"""{'INSTALL'.center(40)}

First you will need to install Python.
Start the Microsoft Store app and search
for 'python', then look for the latest
version (at the time of making this card
it is 3.11) click on it and then click
the Get button.

Thats it. Now you have python.

Some of the cards require python modules
that you also need to install. A module
is just a bunch of code that we will
import into our program to help us do
things.

To install python modules start the
Command Prompt app from the start menu,
and then type:
  pip install module_name

where the module_name will be what you
need, for example:n
  pip install pyautogui
will install the pyautogui module, which
helps us to control the keyboard and the
mouse.

The cards have a comment on top if you
need to install extra modules.
""")

card_str(f"""{'START AFTER LOGIN'.center(40)}

Any program you put in the directory:
C:\\Users\\$USER\\AppData\\Roaming\\
   Microsoft\\Windows\\Start Menu\\
   Programs\\Startup\\
Will start automatically after the $USER
logs in. You can open the folder by
pressing Win+R and then type: 
  shell:startup

If you want to start the program for all
users you need to put it in the global
Startup directory, to see where it is,
press Win+R (the windows key and the R
key) and then:
  shell:common startup

There is a helper start_after_login card
which copies the current python script
in the $USER's startup directory, and
returns True if the file already exists
there, so you can use it to exit.

Example usage:
  if not start_after_login():
    sys.exit(0)
This will install the script in the
$USER's startup directory and exit, but
if the file already exists it will run
the code after.
""")


card_str(f"""{'SERVICE'.center(40)}

You can install each program as a
windows service, the easiest way to do
that is by using the nssm program, you
can download it from http://nssm.cc.
just download it and put the win64
nssm.ex file it in c:

you can create a c:\\hello.bat file with
the contents:

   pythonw c:\\hello.py

and then install it as a service:
  c:\\nssm install hello c:\\hello.bat

to remove the hello service:
  c:\\nssm remove hello

You will need administrator privileges
in order to install/remove services, for
that when you start the Command Prompt
click on Run As Administrator.
""")


card_str(f"""{'EXPERIMENTING'.center(40)}

If you want to experiment, never use
your computer. There are some programs
that emulate computers and you can
install Windows inside the emulator.

VirtualBox is one, it is free and you
can get it from: https://virtualbox.org

Microsoft provices a preinstalled
Windows image you can download from
https://developer.microsoft.com, search
on google for 'developer windows virtual
machines'

Be carefull and only download things
from developer.microsoft.com.

The Windows Operating System in the
VirtualBox virtual computer does not
know its not running on actual computer.

VirtualBox is basically a software
computer.

You can try all kinds of things, try to
delete random files or fill the disk or
erase the whole disk, and then you can
just re-create it with the image.
""")


files = os.listdir(os.path.join(".","cards"))
files = [f for f in files if f.endswith('py')]
files.sort()

for fn in files:
  with open(os.path.join(".","cards",fn)) as f:
    print(card_meta(CARD,"python","", ""))
    CARD+=1
    title = f"filename: {fn}"
    if fn.endswith('py'):
      title = f"# {title}"
    else:
      title = f"// {title}"


    print(title)
    print(f.read())


# card_str(f"""{'LEFT MOUSE BUTTON SWAP'.center(40)}
# """)

# card_str(f"""{'SWAP KEYS'.center(40)}
# """)

# card_str(f"""{'CONSUME THE INTERNET SPEEED'.center(40)}
# """)

# card_str(f"""{'MAKE RANDOM SOUND'.center(40)}
# """)

# card_str(f"""{'OPEN ALL THE PROGRAMS'.center(40)}
# """)

# card_str(f"""{'CHANGE MOUSE DIRECTIONS'.center(40)}
# """)

# card_str(f"""{'HUGE FONT SIZE'.center(40)}
# """)

# card_str(f"""{'OPEN NOTEPAD WITH CREEPY NOTE'.center(40)}
# """)

# card_str(f"""{'RANDOM TIME'.center(40)}
# set the time to +3 or -3 minutes randomly
# """)

# card_str(f"""{'RANDOM PACKET DROP'.center(40)}
# """)

# card_str(f"""{'FIREWALL A PROGRAM'.center(40)}
# """)

# card_str(f"""{'RANDOM DELAY WHEN KEY IS PRESSED'.center(40)}
# """)

# card_str(f"""{'RANDOMLY DROP KEYS'.center(40)}
# """)

# card_str(f"""{'CLICK MANY TIMES ON BUTTON PRESS'.center(40)}
# """)

# card_str(f"""{'RANDOMLY INCREASE AND DECREASE VLUME'.center(40)}
# """)


# card_str(f"""{'FILL DESKTOP WITH FILES'.center(40)}
# """)

# card_str(f"""{'FAKE DESKTOP'.center(40)}
# """)

# card_str(f"""{'PLAY WEIRD SOUND ON MOUSE CLICK'.center(40)}
# """)

# card_str(f"""{'REMOTE CONTROL KEYBOARD'.center(40)}
# """)

# card_str(f"""{'THROTTLE THE INTERNET OF ONE PROGRAM'.center(40)}
# New-NetQosPolicy -Name "FTP" -AppPathNameMatchCondition "ftp.exe" -ThrottleRateActionBitsPerSecond 1MB
# """)

# card_str(f"""{'TALK RANDOMLY'.center(40)}
# """)

# card_str(f"""{'SPEECH TO TEXT AND OPEN NOTEPAD AND WRITE IT DOWN'.center(40)}
# """)

# card_str(f"""{'MATRIX DISPLAY'.center(40)}
# """)

# card_str(f"""{'PRINT CREEPY MESSAGES ON PRINTER'.center(40)}
# """)

# card_str(f"""{'TALK AND TYPE IN NOTEPAD'.center(40)}
# """)

# card_str(f"""{'BROKEN SCREEN EFFECT'.center(40)}
# """)

# card_str(f"""{'PRINT MORSE CODE'.center(40)}
# """)



# print(CARD)
