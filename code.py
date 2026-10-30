import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from pico_bypass_layout import BypassLayout

# check 

trigger = digitalio.DigitalInOut(board.GP9)
trigger.direction = digitalio.Direction.INPUT
trigger.pull = digitalio.Pull.UP


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT


while trigger.value:
    led.value = False
    time.sleep(0.1)


led.value = True
time.sleep(2)

# Main code 
time.sleep(0.3)

kbd = Keyboard(usb_hid.devices)
layout = BypassLayout(kbd, stroke_delay=0.01, char_delay=0.025)

layout.ensure_numlock()
time.sleep(0.4)

kbd.send(Keycode.GUI, Keycode.D)

kbd.send(Keycode.GUI, Keycode.R)
time.sleep(1)

layout.write("powershell\n")
time.sleep(2)

layout.write("Write-Host 'Have fun!' -ForegroundColor Cyan\n")

led.value = False 