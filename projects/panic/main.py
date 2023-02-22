import os
from itertools import cycle
CARD = 1

def card_meta(id, lang, symbol, symbol_style):
  color = '#6e7781' 
  bgcolor = 'white'
  theme='gptredzz'
  font='BlockZone'
  fontSize='25px'
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
""")

card_str(f"""{'EXPERIMENTING'.center(40)}

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


# card_str(f"""{'RANDOM PIXELS ON DISPLAY'.center(40)}
# """)

# card_str(f"""{'TURNS MONITOR UPSIDE DOWN'.center(40)}
# """)

# card_str(f"""{'LEFT MOUSE BUTTON SWAP'.center(40)}
# """)

# card_str(f"""{'SWAP KEYS'.center(40)}
# """)

# card_str(f"""{'CONSUME THE INTERNET SPEEED'.center(40)}
# """)


# card_str(f"""{'FILTER HALF THE INTERNET'.center(40)}
# """)

# card_str(f"""{'MAKE RANDOM SOUND'.center(40)}
# """)

# card_str(f"""{'OPEN ALL THE PROGRAMS'.center(40)}
# """)


# card_str(f"""{'STOP THE INTERNET EVERY 10 SEC FOR 1 SEC'.center(40)}
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

# card_str(f"""{'RANDOMLY PLAY RICKROLL'.center(40)}
# """)

# card_str(f"""{'FILL DESKTOP WITH FILES'.center(40)}
# """)

# card_str(f"""{'FAKE DESKTOP'.center(40)}
# """)

# card_str(f"""{'PLAY WEIRD SOUND ON MOUSE CLICK'.center(40)}
# """)

# card_str(f"""{'RANDOMLY CHANGE BRIGHTNESS'.center(40)}
# and play ominous sound
# """)

# card_str(f"""{'RANDOMLY ROTATE THE SCREEN'.center(40)}
# and play ominous sound
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

# card_str(f"""{'MAKE IT SNOW'.center(40)}
# """)

# card_str(f"""{'MATRIX DISPLAY'.center(40)}
# """)

# card_str(f"""{'RANDOMLY PUT THINGS IN CLIPBOARD'.center(40)}
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
