import os
from itertools import cycle
CARD = 1

def card_meta(id, lang, symbol, symbol_style, force_color = ''):
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
  if force_color:
    color = force_color
  return f"CARD:{id}:{lang}:{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}:{symbol}:{symbol}:{symbol_style}"
  
  
def card_str(x,lang=''):
  global CARD
  print(card_meta(CARD,lang,"",""))

  CARD+=1
  print(x)
  print()

card_str(f"""

{'WARNING! WARING! WARNING!'.center(40)}




THE SOFTWARE IS PROVIDED “AS IS”,
WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

""",'law')

card_str(f"""{'EPILEPSY WARNING!'.center(40)}

To ensure the safety of readers who have
photosensitive epilepsy, certain cards
in this game have the potential to
produce flashing lights, shaking, or
screen rotation that could trigger
seizures. If you or anyone in your
household has a history of epilepsy or
seizures, we strongly advise against
using these cards. If you experience any
discomfort while using these cards,
please stop immediately and seek medical
attention.

To indicate the presence of this
warning, the cards are identified with a
red border and the text "EPILEPSY
WARNING". These cards are particularly
dangerous, but others might be as well,
so it is crucial to understand what the
card is doing before using it.

By using this deck, you acknowledge that
you have read and understood this
warning, and you assume all risks
associated with using the cards.
""",'law')


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


files = os.listdir(os.path.join(".","cards"))
files = [f for f in files if f.endswith('py')]
files.sort()

for fn in files:
  with open(os.path.join(".","cards",fn)) as f:
    force_color = ''
    data = f.read()
    if "EPILEPSY" in data:
      force_color = 'red'
    print(card_meta(CARD,"python","", "",force_color))
    CARD+=1
    title = f"filename: {fn}"
    if fn.endswith('py'):
      title = f"# {title}"
    else:
      title = f"// {title}"


    print(title)
    print(data)
