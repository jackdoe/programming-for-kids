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

Now imagine 32 switches.. the possible amount of configurations is `2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2` or 4294967295.

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


## [DAY-207] 0; 1; infinity; how to break things down

When you think about any solution to any problem, it is very important to think in context of zero, one and infinity (or one million if infinity is impractical).

Lets look at this code for rot13:

```
def rot13(c):
    n = ord(c) - ord('a')
    return chr(97 + ((n + 13) % 26))
```

This `97 + ((n + 13) % 26)` seems a bit intimidating, but if we set `n = 0` then `(n + 13) % 26` becomes `13 % 26` which is just 13, so the whole thing becomes 97+13, which is 110. To get `n=0` we need to pass 'a' as a parameter, so this function takes `a` and returns `chr(110)` which is `n`. See 0 is incredibly powerful, now lets try with 1, 97+14 is 111, so if we pass `b` as parameter, the function will return `o`. And for infinity, the biggest `n` we can have here is 25 or `ord('z') - ord('a')`, `(25+13)%26` is 12, 97+12 is `m`, so `a` goes to `n` and `b` goes to `o` and `z` goes to `m`.

Always check the bounderies of the code: 0,1 and ∞ are your friends.

In math as well, you can see how things break down when you use 0 or ∞, everytime you see something divided by a variable, try to make this variable 0.

```
x = [1,2,3]
average = sum(x)/len(x)
```

What happens when you have an empty list? What happens when the list has exactly 1 element? What happens when you have infinite elements in the list?

In any problem, try to reduce it to nothing, one and everything, and each of those steps will help you to understand it better.


Look at some old code we wrote in day 81:

```
image = [
    1,3,3,3,3,3,1,
    2,4,5,4,5,4,2,
    2,4,4,5,4,4,2,
    2,4,5,4,5,4,2,
    1,3,3,3,3,3,1,
]

width = 7

for (index, pixel) in enumerate(image):
    if index > 0 and index % width == 0:
        print('')

    if pixel == 1:
        print('+', end='')
    elif pixel == 2:
        print('|', end='')
    elif pixel == 3:
        print('-', end='')
    elif pixel == 4:
        print(' ', end='')
    elif pixel == 5:
        print('*', end='')
    else:
        print("dont know what to do with: " + str(pixel))
```

Think of width as 0 and make the image with only 1 pixel and look at the code again:

```
image = [1]

for (index, pixel) in enumerate(image):
    if pixel == 1:
        print('+', end='')
```

the code becomes incredibly trivial: `if you see the pixel value 1, print '+'`.

Go back through your previous programs, and re-read them when you set various things to 0 (or empty lists) or 1 (or lists with 1 element).