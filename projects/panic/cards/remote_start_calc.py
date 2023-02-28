# pip install flask
import flask
import os

app = flask.Flask(__name__)

@app.route('/calc')
def calc():
  os.system("start calc")
  return 'done'

app.run(host='0.0.0.0',port=8899)
# connect to the computer's IP address
# on port 8899 and open /calc
# for example: if the IP is 192.168.0.10
# use: http://192.168.0.10:8899/calc
