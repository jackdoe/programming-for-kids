# pip install pywin32 flask
import win32com.client as wincl
import flask

speak = wincl.Dispatch("SAPI.SpVoice")

app = flask.Flask(__name__)

@app.route('/say/<text>')
def say(text):
  speak.Speak(text)
  return 'done'

app.run(host='0.0.0.0',port=8899)
# connect to the computer's IP address
# on port 8899 going and open /say/hello
# to say hello from the computer, for
# example: if the IP is 192.168.0.10
# use:
# http://192.168.0.10:8899/say/hello
