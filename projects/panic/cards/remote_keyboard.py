# pip install flask pyautogui
import pyautogui
import flask
app = flask.Flask(__name__)

@app.route('/write/<name>')
def write(name):
  pyautogui.typewrite(name)
  return 'done'

@app.route('/move/<x>/<y>')
def move(x,y):
  x = int(x)
  y = int(y)
  pyautogui.moveTo(x,y, duration=1)
  return 'done'

@app.route('/click/<x>/<y>')
def click(x,y):
  x = int(x)
  y = int(y)
  pyautogui.click(x,y)
  return 'done'

app.run(host='0.0.0.0',port=8899)
# connect to the computer's ip address
# on port 8899 and open /write/abc to
# type abc on the computer, for example:
# if the ip is 192.168.0.10 use
# http://192.168.0.10:8899/write/abc
