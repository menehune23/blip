from .device import Device, Button, Buzzer
from .displays import OLED_I2C


class dev(Device):
    _display: OLED_I2C

    def __init__(self):
        self._display = OLED_I2C(scl=7, sda=6)
        self._buzzer = Buzzer(pin=5)
        self._buttons = {
            "a": Button(pin=3),
        }
