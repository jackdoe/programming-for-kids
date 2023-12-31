import uasyncio as asyncio
import time

morseTable = {
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '-.-.--': '!',
    '-....-': '-',
    '-..-.': '/',
    '.--.-.': '@',
    '-.--.': '(',
    '-.--.-': ')',
    '-...-': '=',
    '.-.-.': '+',
    '.----.': "'",
    '-.-.-.': ';',
    '-...-': '=',
    '..--.-': '_',
    '.-..-.': '"',
    '---...': ':',
    '.-...': '&',
    '........': 'ERROR',
}


class Morse:
    def __init__(self, pin, on_progress, on_done):
        self.pin = pin
        self.on_progress = on_progress
        self.on_done = on_done
        self.current = []
        self.last_press = 0
        self.waiting_for_dash_or_dot = False

    async def send_done(self):
        sym = morseTable.get(''.join(self.current), '')
        if len(self.current) == 0:
            sym = 'BACKSPACE'
        self.on_done(self.current, sym)
        self.current = []
        self.last_press = 0
        await asyncio.sleep_ms(10)

    async def wait_for_release_after_press(self):
        while True:
            if self.last_press != 0 and time.ticks_diff(time.ticks_ms(), self.last_press) > 800:
                await self.send_done()
            await asyncio.sleep_ms(10)

    async def dash_or_dot(self):
        while True:
            if self.pin.value() == 1:
                break
            await asyncio.sleep_ms(5)

        self.last_press = time.ticks_ms()
        start = time.ticks_ms()
        while True:
            self.last_press = time.ticks_ms()
            if self.pin.value() == 0:
                break
            await asyncio.sleep_ms(5)
        took = time.ticks_diff(time.ticks_ms(), start)
        if took > 800:
            await self.send_done()
            return
        else:
            if took > 300:
                self.current.append('-')
            else:
                self.current.append('.')

            sym = morseTable.get(''.join(self.current), '')
            self.on_progress(self.current, sym)

    async def run(self):
        asyncio.create_task(self.wait_for_release_after_press())
        while True:
            await self.dash_or_dot()
            await asyncio.sleep_ms(10)
