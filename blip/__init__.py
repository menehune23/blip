import time
from .devices import Device

device: Device


def start(device_type: str, setup: callable, loop: callable):
    module = __import__("devices."+device_type, None, None, [device_type], 1)
    device_cls = getattr(module, device_type)
    global device
    device = device_cls()

    setup()
    _loop(loop)


def _loop(loop: callable):
    last = time.ticks_ms()
    while True:
        now = time.ticks_ms()
        dt = time.ticks_diff(now, last) / 1000
        last = now
        loop(dt)
