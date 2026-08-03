from machine import Pin, PWM


class Buzzer:
    _DUTY_50_PCT = 512

    _pwm: PWM

    def __init__(self, *, pin: int):
        self._pwm = PWM(Pin(pin))
        self.stop()

    def beep(self, freq: int):
        self._pwm.freq(freq)
        self._pwm.duty(Buzzer._DUTY_50_PCT)

    def stop(self):
        self._pwm.duty(0)
