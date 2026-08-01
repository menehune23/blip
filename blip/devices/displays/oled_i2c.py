from machine import Pin, I2C
import ssd1306
from .display import Display


class OLED_I2C(Display):
    width: int = 128
    height: int = 64

    _oled: ssd1306.SSD1306_I2C

    def __init__(self, *, scl: int, sda: int):
        i2c = I2C(0, scl=Pin(scl), sda=Pin(sda), freq=1000000)
        self._oled = ssd1306.SSD1306_I2C(self.width, self.height, i2c)

    def clear(self, color: int = 0):
        self._oled.fill(color)

    def text(self, string: str, x: int, y: int, color: int = 1):
        self._oled.text(string, x, y, color)

    def show(self):
        self._oled.show()
