from .device import Device
from .displays import OLED_I2C


class dev(Device):
    display: OLED_I2C

    def __init__(self):
        self.display = OLED_I2C(scl=7, sda=6)
