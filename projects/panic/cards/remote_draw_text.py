# pip install pywin32 flask
import win32gui as g
import flask

dc = g.GetDC(0)

app = flask.Flask(__name__)

@app.route('/text/<x>/<y>/<text>')
def text(x,y,text):
  x = int(x)
  y = int(y)
  g.DrawText(dc, 
             text, 
             len(text), 
             (x,y,x+500,y+500),
             0)
  return 'done'

app.run(host='0.0.0.0',port=8899)
# connect to the computer's IP address
# on port 8899 and open /say/hello to
# say hello from the computer, for
# example: if the IP is 192.168.0.10
# use:
# http://192.168.0.10:8899/say/hello
