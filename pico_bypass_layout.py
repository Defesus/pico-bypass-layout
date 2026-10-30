import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

class BypassLayout:

    NUMPAD_KEYS = {
        '0': Keycode.KEYPAD_ZERO,
        '1': Keycode.KEYPAD_ONE,
        '2': Keycode.KEYPAD_TWO,
        '3': Keycode.KEYPAD_THREE,
        '4': Keycode.KEYPAD_FOUR,
        '5': Keycode.KEYPAD_FIVE,
        '6': Keycode.KEYPAD_SIX,
        '7': Keycode.KEYPAD_SEVEN,
        '8': Keycode.KEYPAD_EIGHT,
        '9': Keycode.KEYPAD_NINE,
    }

    def __init__(self, keyboard: Keyboard, stroke_delay: float = 0.01, char_delay: float = 0.02):
        self.keyboard = keyboard
        self.stroke_delay = stroke_delay
        self.char_delay = char_delay

    def ensure_numlock(self):
        time.sleep(0.1)
        if not self.keyboard.led_on(Keyboard.LED_NUM_LOCK):
            self.keyboard.send(Keycode.KEYPAD_NUMLOCK)
            time.sleep(0.2)  

    def write_char(self, char: str):
        if char == '\n':
            self.keyboard.send(Keycode.ENTER)
            time.sleep(self.char_delay)
            return


        if char == ' ':
            self.keyboard.send(Keycode.SPACEBAR)
            time.sleep(self.char_delay)
            return

        code_str = f"{ord(char):04d}"


        self.keyboard.press(Keycode.LEFT_ALT)
        time.sleep(self.stroke_delay)

        for digit in code_str:
            key = self.NUMPAD_KEYS[digit]
            self.keyboard.press(key)
            time.sleep(self.stroke_delay)
            self.keyboard.release(key)
            time.sleep(self.stroke_delay)

        self.keyboard.release(Keycode.LEFT_ALT)
        time.sleep(self.char_delay)

    def write(self, text: str):
        self.ensure_numlock()
        for char in text:
            self.write_char(char)