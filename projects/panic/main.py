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

  if lang == 'law':
    color = 'red'
    bgcolor = 'white'
    lang=''
  return f"CARD:{id}:{lang}:{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}:{symbol}:{symbol_style}"
  
  
def card_str(x,lang=''):
  global CARD
  print(card_meta(CARD,lang,"",""))

  CARD+=1
  print(x)
  print()

card_str(f"""

{'WARNING! WARING! WARNING!'.center(40)}

USE THE CODE FROM THESE CARDS AT YOUR
OWN RISK. THESE PRANKS ARE PURELY FOR
EDUCATIONAL PURPOSES AND ARE NOT
INTENDED TO CAUSE HARM. THE AUTHOR OF
THIS DECK IS NOT RESPONSIBLE FOR ANY
DAMAGE, LOSS OF DATA, OR OTHER
CONSEQUENCES THAT MAY ARISE FROM THE USE
OF THESE PRANKS.

BY USING THESE PRANKS, YOU ACKNOWLEDGE
THAT YOU ARE FULLY AWARE OF THE
CONSEQUENCES OF YOUR ACTIONS AND THAT
YOU UNDERSTAND THE CODE ON THESE
CARDS. IF YOU ARE UNDER 18 YEARS OLD,
YOU MUST OBTAIN THE CONSENT OF YOUR
PARENT OR LEGAL GUARDIAN BEFORE USING
THESE PRANKS.

BY USING THESE PRANKS, YOU AGREE TO
RELEASE AND HOLD HARMLESS THE AUTHOR OF
THIS DECK FROM ANY CLAIMS, DEMANDS, OR
DAMAGES, WHETHER KNOWN OR UNKNOWN,
ARISING OUT OF OR IN ANY WAY CONNECTED
WITH YOUR USE OF THESE PRANKS.
""",'law')

card_str(f"""{'PANIC'.center(40)}

PANIC is a deck of small computer prank
programs designed to give you a taste of
your own power over your computer. Each
card in the deck represents a prank, and
includes the code necessary to execute
it. The pranks range from simple screen
rotations to more elaborate tricks like
drawing random pixels on the screen or
playing sounds for each keystroke.

While the pranks provided in the deck
are great examples of what can be done,
the real fun comes from combining
multiple cards into one and creating
your own unique pranks. This allows you
to unleash your creativity and explore
the extent of your programming
knowledge.

However, it's important to remember that
all the cards require some level of
Python programming knowledge. If you're
just starting out, be sure to ask your
parent or legal guardian how to get
started with Python. They can help guide
you in the right direction and ensure
that you're using your newfound powers
safely and responsibly.
""")

card_str(f"""{'ETHICS'.center(40)}

To be ethical when playing with the
PANIC deck, consider these tips:

- Respect others and their property by
  avoiding pranks that could damage or
  harm their computer or device.

- Obtain consent before executing any
  prank programs.

- Steer clear of offensive or harassing
  pranks that could discriminate or
  bully others.

- Avoid compromising security with
  pranks that could install malware or
  steal personal information.

- Use your power wisely, without taking
  advantage of someone's trust or using
  your skills to harm others.

By following these tips, you can enjoy
the fun of computer pranks while
remaining a responsible and ethical
member of the technology community.
""")

card_str(f"""{'INSTALL'.center(40)}

To get started with Python, you'll need
to install it on your computer. To do
this, open the Microsoft Store app and
search for "Python". Once you've found
it, click on the latest version
(currently 3.11) and click "Get" to
install it.

Once you've installed Python, you may
also need to install additional modules
for some of the cards. Modules are
collections of code that we can import
into our programs to help us perform
certain tasks.

To install python modules start the
Command Prompt app from the start menu,
and then type:
  pip install module_name

where the module_name will be what you
need, for example:
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


card_str(f"""{'WINDOWS SERVICES'.center(40)}

Automatically start a program can also
be done if you make it a 'Windows
Service'.

The easiest way to do that is by using
the nssm program, you can download it
from http://nssm.cc.  just download it
and put the win64 nssm.ex file it in c:

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

# card_str(f"""{'RANDOM PACKET DROP'.center(40)}
# """)

# card_str(f"""{'SAY WHAT YOU TYPE'.center(40)}
# """)

# card_str(f"""{'FIREWALL A PROGRAM'.center(40)}
# """)

# card_str(f"""{'RANDOM DELAY WHEN KEY IS PRESSED'.center(40)}
# """)

# card_str(f"""{'RANDOMLY DROP KEYS'.center(40)}
# """)

# card_str(f"""{'CLICK MANY TIMES ON BUTTON PRESS'.center(40)}
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
