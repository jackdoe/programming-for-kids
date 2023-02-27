# pip install flask pyautogui
import pyautogui
import flask

app = flask.Flask(__name__)

@app.route('/type/<name>')
def typeit(name):
  pyautogui.typewrite(name)
  return 'done'

app.run(host='0.0.0.0',port=8899)

# connect to the computer's ip address
# on port 8899 going and open /type/abc
# to type abc on the computer, for example:
# if the ip is 192.168.0.10 open
# http://192.168.0.10:8899/type/abc
