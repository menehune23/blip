from machine import Pin, PWM
from .displays import Display
from .sound import Buzzer


class Button:
    _pin: Pin
    _last_value: int
    _value: int = 1

    def __init__(self, *, pin: int):
        self._pin = Pin(pin, Pin.IN, Pin.PULL_UP)

    @property
    def is_pressed(self) -> bool:
        return self._value == 0

    @property
    def just_pressed(self) -> bool:
        return self._last_value == 1 and self._value == 0

    @property
    def just_released(self) -> bool:
        return self._last_value == 0 and self._value == 1

    def _update(self):
        self._last_value = self._value
        self._value = self._pin.value()


class Device:
    _display: Display
    _buzzer: Buzzer
    _buttons: dict[str, Button]

    def _update(self, dt: float):
        for button in self._buttons.values():
            button._update()

    def button(self, name: str) -> Button:
        return self._buttons.get(name.lower())
