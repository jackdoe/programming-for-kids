from socket import *
from threading import Thread
def server():
  s = socket(AF_INET,SOCK_DGRAM)
  s.bind(("127.0.0.1", 31337))
  while True:
    d,addr = s.recvfrom(1024)
    x = int.from_bytes(d, 'little')
    x *= 2
    d = x.to_bytes(1,'little')
    s.sendto(d, addr)
    break
def client():
  s = socket(AF_INET,SOCK_DGRAM)
  dst = ("127.0.0.1", 31337)
  while True:
    dice = ⚂
    data = dice.to_bytes(1,'little')
    n = s.sendto(data, dst)
    d, addr = s.recvfrom(1024)
    x = int.from_bytes(d, 'little')
    print('sent: ' + str(dice))
    print('recv: ' + str(x))
    if x == dice * 2:
      break
t1 = Thread(target=server)
t2 = Thread(target=client)
t1.start()
t2.start()
t1.join()
t2.join()
