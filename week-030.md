## [DAY-206] client server

In order for computers to talk to each other we use the Internet Protocol, there are other ways to do it, but at the moment using the internet protocol is the most common one. The two computers talking to each other will need unique IP addresses. An IP address is just a 4 byte (32 bit) number, the minimum one is 0 and the maximum one is 4294967295. This is quite hard to remember, so we split the 32 bit number into 4x8 bit numbers, so for example the IP address of google.com is 2899945710, but this is super hard to read, if we split it into 4x8 bit numbers it looks like this: 172.217.168.238.

In another lesson we will discuss how the packet goes from computer to computer to get from your PC to google.com, it probably goes through 20 computers on its way.

Going back to the 32 bit number, lets start with something simple, 1 bit is as simple as an on/off switch, like the one controlling your lights.

One switch can either be on or off, so the possible configurations is 2 (0 or 1)

```
     .----------.
     |   ~ON~   |
     |   ____   |
     |  |.--.|  |
     |  ||  ||  |
     |  ||__||  |
     |  ||\ \|  |
     |  |\ \_\  |
     |  |_\[_]  |
     |          |
     |  ~OFF~   |
     '----------'
     (art by jgs)
```


Once we add a switch, the possible configurations double, however the previous ones were, we can have them either with the new switch on or off. So with 2 switches we have `00 01 10 11`


```
     .----------.      .----------.
     |   ~ON~   |      |   ~ON~   |
     |   ____   |      |   ____   |
     |  |.--.|  |      |  |.--.|  |
     |  ||  ||  |      |  ||  ||  |
     |  ||__||  |      |  ||__||  |
     |  ||\ \|  |      |  ||\ \|  |
     |  |\ \_\  |      |  |\ \_\  |
     |  |_\[_]  |      |  |_\[_]  |
     |          |      |          |
     |  ~OFF~   |      |  ~OFF~   |
     '----------'      '----------'
```


Adding third switch, the possible configurations doubles again `000 001 010 011 100 101 110 111`:

```
     .----------.      .----------.       .----------. 
     |   ~ON~   |      |   ~ON~   |       |   ~ON~   | 
     |   ____   |      |   ____   |       |   ____   | 
     |  |.--.|  |      |  |.--.|  |       |  |.--.|  | 
     |  ||  ||  |      |  ||  ||  |       |  ||  ||  | 
     |  ||__||  |      |  ||__||  |       |  ||__||  | 
     |  ||\ \|  |      |  ||\ \|  |       |  ||\ \|  | 
     |  |\ \_\  |      |  |\ \_\  |       |  |\ \_\  | 
     |  |_\[_]  |      |  |_\[_]  |       |  |_\[_]  | 
     |          |      |          |       |          | 
     |  ~OFF~   |      |  ~OFF~   |       |  ~OFF~   | 
     '----------'      '----------'       '----------' 
```

Going back to the IP address, one byte is just 8 switches, 4 bytes is 32 switches.

Now imagine 32 switches.. the possible amount of configurations is 2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2 or 4294967295.

So over the internet for any two computers to communicate they need their own 32 bit number, this btw is version 4 of the Internet Protocol, now we are in the process of adopting the new version 6 which has 128 bits for the IP address. Imagine 128 switches, the possible configurations are: 340282366920938463463374607431768211456, which is very very big number.


There are other few things needed in order to send messages between computers, and this is to be able to communicate with a specific program on the computer, for that we need a PORT, you can tell the operating system that when it recives a packet on specific port to send it to your program. We will use this in order to make a super simple chat program. The port is only 2 bytes (16 bits), so from 0 to 65535.

We will make a simple helper module, just copy paste the code for now, we will investigate it later.

Make a file 'multiplayer.py' and type the following code in it:

```
from socket import *
from threading import Thread

def server(ip, port,fn):
    t = Thread(target=listen, args=(ip,int(port),fn))
    t.start()
    t.join()

def listen(ip, port, fn):
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.bind((ip, port))
    while True:
        data, addr = sock.recvfrom(1024)
        r = fn(data.decode("utf-8"), addr)
        sock.sendto(r.encode("utf-8"), addr)


def send(ip, port, message):
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.sendto(message.encode("utf-8"), (ip, int(port)))
    data, addr = sock.recvfrom(1024)
    return data.decode("utf-8")
```


Now make a server:

```
import multiplayer
import sys

messages = []
def incoming(text, sender):
    ip, port = sender
    if '>' in text:
        name, message = text.split("> ")
        if len(message) > 0:
            messages.append(text)
    return "\n".join(messages)

ip = sys.argv[1]
port = sys.argv[2]
print('listening on', 'ip:', ip, 'port:', port)

multiplayer.server(ip, port, incoming)
```

To see your ipaddress go to CMD and type `ipconfig`, on macos go to the terminal and type `ifconfig`, a computer can have multiple ip addresses, so use your parent to help you out. You will see `127.0.0.1`, you can use this ip address when you want to communicate with another program on the same computer, it is called the local host address.

Start the server with `python3 server.py 192.168.x.x 6500` we will use port 6500

Make a client:

```
import multiplayer
import sys

name = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]

while True:
    my_message = input("message> ")
    all_messages = multiplayer.send(ip, port, name + "> " + my_message)
    print(all_messages)
```

Start the client on two computers with `python3 client.py server_ip 6500`, then when you type something and send a message, the server will reply to you with all messages it recived so far.

There is a lot of code you dont understand here, and this is totally ok, we will get back to it in the future. The important part to remember is that IP version 4 addresses are 32 bits, and the port is 16 bits, and IP address allows you to talk to a computer and a port allows you to talk to a program.

