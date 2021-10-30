import os
from mmap import mmap
from fcntl import ioctl
from io import BytesIO
import struct
import threading
import tty, termios, sys
import time
os.system("clear")
font = {
    'a': [
        [0,1,0],
        [1,0,1],
        [1,1,1],
        [1,0,1],
        [1,0,1],
    ],

    'b': [
        [1,0,0],
        [1,0,0],
        [1,1,1],
        [1,0,1],
        [1,1,1],
    ],

    'c': [
        [1,1,1],
        [1,0,0],
        [1,0,0],
        [1,0,0],
        [1,1,1],
    ],

    'd': [
        [0,0,1],
        [0,0,1],
        [1,1,1],
        [1,0,1],
        [1,1,1],
    ],

    'e': [
        [1,1,1],
        [1,0,0],
        [1,1,1],
        [1,0,0],
        [1,1,1],
    ],

    'f': [
        [1,1,1],
        [1,0,0],
        [1,1,0],
        [1,0,0],
        [1,0,0],
    ],

    'g': [
        [1,1,1],
        [1,0,0],
        [1,0,1],
        [1,0,1],
        [1,1,1],
    ],
    'h': [
        [1,0,1],
        [1,0,1],
        [1,1,1],
        [1,0,1],
        [1,0,1],
    ],

    'i': [
        [1,1,1],
        [0,1,0],
        [0,1,0],
        [0,1,0],
        [1,1,1],
    ],

    'j': [
        [1,1,1],
        [0,1,0],
        [0,1,0],
        [0,1,0],
        [1,1,0],
    ],

    'k': [
        [1,0,1],
        [1,1,0],
        [1,0,0],
        [1,1,0],
        [1,0,1],
    ],

    'l': [
        [1,0,0],
        [1,0,0],
        [1,0,0],
        [1,0,0],
        [1,1,1],
    ],

    # FIXME: we have a problem with m..
    'm': [
        [0,0,0],
        [1,1,1],
        [1,1,1],
        [1,1,1],
        [1,0,1],
    ],

    'n': [
        [0,0,0],
        [1,1,0],
        [1,0,1],
        [1,0,1],
        [1,0,1],
    ],


    'o': [
        [0,1,0],
        [1,0,1],
        [1,0,1],
        [1,0,1],
        [0,1,0],
    ],

    'p': [
        [1,1,1],
        [1,0,1],
        [1,1,1],
        [1,0,0],
        [1,0,0],
    ],


    's': [
        [0,1,1],
        [1,0,0],
        [0,1,1],
        [0,0,1],
        [1,1,0],
    ],

    '=': [
        [0,0,0],
        [1,1,1],
        [0,0,0],
        [1,1,1],
        [0,0,0],
    ],



    'w': [
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,1,1,1,1],
    ],

    't': [
        [0,1,0],
        [1,1,1],
        [0,1,0],
        [0,1,0],
        [0,0,1],
    ],

    'u': [
        [0,0,0],
        [1,0,1],
        [1,0,1],
        [1,0,1],
        [0,1,1],
    ],


    'T': [
        [1,1,1],
        [0,1,0],
        [0,1,0],
        [0,1,0],
        [0,1,0],
    ],



    '0': [
        [1,1,1],
        [1,0,1],
        [1,0,1],
        [1,0,1],
        [1,1,1],
    ],

    '1': [
        [0,1,1],
        [0,0,1],
        [0,0,1],
        [0,0,1],
        [0,0,1],
    ],

    '2': [
        [1,1,1],
        [0,0,1],
        [1,1,1],
        [1,0,0],
        [1,1,1],
    ],

    '%': [
        [1,0,1],
        [0,0,0],
        [0,1,0],
        [0,0,0],
        [1,0,1],
    ],

    '+': [
        [0,0,0],
        [0,1,0],
        [1,1,1],
        [0,1,0],
        [0,0,0],
    ],

    '*': [
        [0,0,0],
        [1,0,1],
        [0,1,0],
        [1,0,1],
        [0,0,0],
    ],

    ':': [
        [0,1,0],
        [0,1,0],
        [0,0,0],
        [0,1,0],
        [0,1,0],
    ],

    'r': [
        [0,0,0],
        [1,1,1],
        [1,0,0],
        [1,0,0],
        [1,0,0],
    ],


    'x': [
        [1,0,1],
        [1,0,1],
        [0,1,0],
        [1,0,1],
        [1,0,1],
    ],

    '\'': [
        [0,1,0],
        [0,1,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ],

    '"': [
        [1,1,0],
        [1,1,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ],

    '.': [
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,1,1],
        [0,1,1],
    ],

    ',': [
        [0,0,0],
        [0,0,0],
        [0,0,1],
        [0,0,1],
        [0,1,1],
    ],

    '(': [
        [0,1,0],
        [1,0,0],
        [1,0,0],
        [1,0,0],
        [0,1,0],
    ],

    ')': [
        [0,1,0],
        [0,0,1],
        [0,0,1],
        [0,0,1],
        [0,1,0],
    ],


    ' ': [
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ],


}


class Input(threading.Thread):
    def __init__(self, cb):
        threading.Thread.__init__(self)

        self.fd = sys.stdin.fileno()
        self.cb = cb
        self.esc = False
        self.seq = ''
    def run(self):
        while True:
            c = self.getchr()
            if ord(c) == 27:
                self.esc = True
            self.seq += c

            if self.esc:
                if len(self.seq) == 4:
                    self.cb(self.seq)

                    self.esc = False
                    self.seq = ''
            else:
                self.seq = ''
                if c == 'q':
                    break
                self.cb(c)

    def getchr(self):
        old_settings = termios.tcgetattr(self.fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(self.fd, termios.TCSADRAIN, old_settings)
            return ch

FBIOGET_VSCREENINFO=0x4600
FBIOPUT_VSCREENINFO=0x4601
FBIOGET_FSCREENINFO=0x4602

class FrameBuffer:
    def __init__(self):
        #
        # most of this is from https://github.com/chidea/FBpyGIF/blob/master/FBpyGIF/fb.py
        #

        f = open('/dev/fb0','r+b')
        vi = ioctl(f, FBIOGET_VSCREENINFO, bytes(160))
        vi = list(struct.unpack('I'*40, vi))
        #(1920, 1080, 1920, 1080, 0, 0, 24, 0,
        #   w     h     vw    vh  xo yo bpp col
        #            virtual size offset    1=gray
        # 16, 8, 0, 8, 8, 0, 0, 8, 0, 24, 0, 0, 0, 0, 4294967295, 4294967295, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        #   (bit offset, bits, bigend)         non acv   height(mm) width(mm) accl, pixclock, .....                angle, colorspace, reserved[4]
        #     R        G      B      A        std
        vi = ioctl(f, FBIOPUT_VSCREENINFO, struct.pack('I'*40, *vi)) # fb_var_screeninfo
        vi = struct.unpack('I'*40,vi)
        bpp = vi[6]
        bytepp = bpp//8


        ffm = 'c'*16+'L'+'I'*4+'H'*3+'ILIIHHH'
        fic = struct.calcsize(ffm)
        fi = struct.unpack(ffm, ioctl(f, FBIOGET_FSCREENINFO, bytes(fic)))
        #(b'B', b'C', b'M', b'2', b'7', b'0', b'8', b' ', b'F', b'B', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00',
        # 16 char =id
        # 1025519616, 6220800, 0, 0, 2, 1, 1, 0, 5760, 0, 0, 0, 0, 0, 0)
        # smem_len      type type_aux, visual, xpanstep, ypanstep, ywrapstep, line_length, mmio_start, mmio_len, accel, capabilities, reserved[2]
        msize = fi[17] # = w*h*bpp//8
        ll, start = fi[-7:-5]
        # bpp = vi[9]+vi[12]+vi[15]+vi[18]
        w, h = ll//bytepp, vi[1] # when screen is vertical, width becomes wrong. ll//3 is more accurate at such time.
        vw, vh = w,h
        msize_kb = vw*vh*bytepp//1024 # more accurate FB memory size in kb
        #xo, yo = vi[4], vi[5]

        self.mm = mmap(f.fileno(), msize, offset=start)

        self.w = w
        self.h = h
        self.bpp = bpp
        self.bytepp = bytepp
        self.RGB = False
        if vi[8] == 0:
            self.RGB = True

    def move(self, x,y):
        self.mm.seek((x + y*self.w) * self.bytepp)

    def dot(self, x, y, color):
        (r, g, b) = color
        self.move(x,y)
        self.mm.write(struct.pack('BBB',*((r,g,b) if self.RGB else (b,g,r))))

    def fill(self, r,g,b):
        seed = 0
        if self.bpp == 32:
            seed = struct.pack('BBBB', b, g, r, 255)
        elif bpp == 24:
            seed = struct.pack('BBB', b, g, r)
        elif bpp == 16:
            seed = struct.pack('H', r>>3<<11 | g>>2<<5 | b>>3)
            self.mm.seek(0)
        self.fillb(seed * self.w * self.h)

    def fillb(self, img):
        b = BytesIO(img)
        s = self.w*self.bytepp
        for y in range(self.h):
            self.move(0,y)
            self.mm.write(b.read(s))

    def text(self, offX, offY, t, color=(255,255,255), pixelsize=5):
        origX = offX
        for (n,c) in enumerate(t):
            if c == '\n' or c == '\r':
                glyph = font[' ']
                offY += len(glyph)*pixelsize + pixelsize
                offX = origX
            else:
                glyph = font[' ']
                if c in font:
                    glyph = font[c]

                self.char(offX, offY, glyph, color, pixelsize)
                offX += (len(glyph[0])*pixelsize + int(pixelsize/2))


    def char(self, offX, offY, glyph, color=(255,255,255), pixelsize=4):
        for (y, col) in enumerate(glyph):
            for (x, enabled) in enumerate(col):
                pixelcolor = (0,0,0)
                if enabled > 0:
                    pixelcolor = color
                for pixelX in range(pixelsize):
                    for pixelY in range(pixelsize):
                        ox = offX + (x*pixelsize) + pixelX
                        oy =  offY + (y *pixelsize) + pixelY
                        if ox < self.w and oy < self.h:
                            self.dot(ox,oy, pixelcolor)


os.system("setterm -cursor off")
fb = FrameBuffer()
fb.fill(0, 0,0)

text = ''
#from random import randint
#for i in range(10000):
#    fb.text(randint(0,fb.w), randint(0,fb.h), 'hello')
#"""

def refresh(c):
    global text
    fb.fill(0, 0,0)

    # HELP
    if c == '\x1b[[A': # F1
        pass

    # SAVE
    if c == '\x1b[[B': # F2
        f = open('current.txt', 'w')
        f.write(text)
        f.close()

    # LOAD
    if c == '\x1b[[C': # F3
        f = open('current.txt', 'r')
        text = f.read()
        f.close()

    # CLEAR
    if c == '\x1b[[D': # F4
        pass

    # RUN
    os.system("clear")
    if c == '\x1b[[E': # F5
        try:
            exec(compile(text, '<string>','exec'))
        except Exception as e:
            fb.text(0,fb.h-100,str(e), (255,0,0))

        return


    if len(c) == 1:
        if c == '\x7f':
            text = text[:len(text)-1]
        else:
            text += c

    fb.text(0,0,text, (100,200,255))

    
#    for x in range(ord(c)):
#        for y in range(ord(c)):
#            fb.dot(x,y,100+x,100+y,0)


console = Input(refresh)
console.start()
console.join()

#os.system("reset")
