from machine import Pin, I2C
from math import *
import ssd1306

from morse import Morse
import uasyncio as asyncio


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd(*integers):
    if len(integers) == 1:
        return integers[0]

    r = integers[0]
    for i in integers[1:]:
        r = _gcd(r, i)
    return r


def _lcm(a, b):
    return a * b // gcd(a, b)


def lcm(*integers):
    if len(integers) == 1:
        return integers[0]

    r = integers[0]
    for i in integers[1:]:
        r = _lcm(r, i)
    return r


def p(x, y):
    d.pixel(x, y, 1)


def l(x, y, x1, y1):
    d.line(x, y, x1, y1, 1)


def render(status):
    global line
    display.fill(0)

    truncatedLine = line
    if len(truncatedLine) > 14:
        truncatedLine = '>' + truncatedLine[len(truncatedLine) - 14:]

    cursor_x = len(truncatedLine) * 8
    display.hline(cursor_x, 8, 8, 1)
    display.text(truncatedLine, 0, 0, 1)
    try:
        result = str(eval(line))
        display.text(result, 0, 26, 1)
    except Exception as e:
        pass

    display.text(status, 0, 56, 1)
    display.show()


def on_progress(current, sym):
    render(''.join(current) + ': ' + sym)


def on_done(current, sym):
    global line
    if sym == '':
        render('')
        return

    if sym == 'BACKSPACE' or sym == 'ERROR':
        line = line[:-1]
    else:
        if sym == 'x':
            sym = '*'  # x is used for multiplication
        line += sym
    render(''.join(current) + ': ' + sym)


i2c = I2C(sda=Pin(20), scl=Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

sos = 'calling 112..'
h = 'punkx.org/calc'
help = 'punkx.org/calc'
d = display
line = ''

render('')
morse = Morse(pin=Pin(5, mode=Pin.IN, pull=Pin.PULL_DOWN),
              on_progress=on_progress, on_done=on_done)

loop = asyncio.new_event_loop()
loop.create_task(morse.run())
loop.run_forever()
