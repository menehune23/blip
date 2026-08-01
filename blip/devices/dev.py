from machine import Pin
from .device import Device, Button
from .displays import OLED_I2C


class dev(Device):
    _display: OLED_I2C

    def __init__(self):
        # temp: turn light off
        Pin(20, Pin.OUT).value(0)

        self._display = OLED_I2C(scl=7, sda=6)
        self._buttons = {
            "a": Button(pin=3),   # built-in
            "b": Button(pin=21),  # UART port
        }
