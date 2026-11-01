# Pico Bypass Layout

A robust, layout-independent typing library for Raspberry Pi Pico and CircuitPython USB HID targeting Windows systems.

## The Problem
Standard USB HID keyboard implementations (such as `adafruit_hid.keyboard_layout_us`) map ASCII characters to physical scancodes. When the active layout on the target machine is non-US (e.g. Russian, German, French), typing commands produces incorrect characters, failing execution.

## The Solution
`pico-bypass-layout` bypasses the active Windows keyboard layout using **Alt + Numpad** sequences:
- Detects the host's `NumLock` status using hardware keyboard LED feedback (`kbd.led_on`).
- Translates characters into 4-digit Windows Alt sequences via Numpad keys.
- Guaranteed character delivery regardless of active system language.

## Installation
1. Copy `pico_bypass_layout.py` into the `/lib` folder (or root directory) of your `CIRCUITPY` drive.
2. Ensure the standard `adafruit_hid` bundle is present in `/lib`.
IF YOU HAVE PROBLEMS WITH LETTERS, CHANGE THE DELAY TIME

## Basic Usage

```python
import usb_hid
from adafruit_hid.keyboard import Keyboard
from pico_bypass_layout import BypassLayout

kbd = Keyboard(usb_hid.devices)
layout = BypassLayout(kbd)

# Reliable typing on any active Windows layout
layout.write("cmd\n")
