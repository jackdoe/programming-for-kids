import os, random, time
def route(act,ip,mask,gw):
  s = [
    "route", act, ip,
    "MASK", mask, gw
  ]
  os.system(" ".join(s))

segments = [
  ['0.0.0.0', '128.0.0.0'],
  ['128.0.0.0', '128.0.0.0'],
]
# needs administrator privileges,
# install it as service (check out the
# service card)
while True:
  # pick either all the IPs having 1 in
  # their first, so all networks above
  # 128.0.0.0, e.g. google.com:
  # 142.250.179.142, or the other half
  # of the internet below 128.0.0.0
  # e.g. amazon.com: 54.239.28.85
  ip,mask = random.choice(segments)
  # break the internet
  route('add',ip,mask,'0.0.0.0')
  time.sleep(random.randint(5,15))
  # restore the internet
  route('delete',ip,mask,'0.0.0.0')

  time.sleep(random.randint(10,60))
