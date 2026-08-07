import time
from .devices import Device
from .devices.wifi import WIFI_DISCONNECTED, WIFI_CONNECTING, WIFI_CONNECTED

device: Device


def start(device_type: str, setup: callable, loop: callable):
    # Instantiate device
    module = __import__("devices."+device_type, None, None, [device_type], 1)
    device_cls = getattr(module, device_type)
    global device
    device = device_cls()

    # Import component public class members into top-level
    for _obj in [
        device,
        device._wifi,
        device._display,
        device._buzzer,
    ]:
        for _name in dir(_obj):
            if not _name.startswith("_"):
                _attr = getattr(_obj, _name)
                globals()[_name] = _attr

    # Run
    setup()
    _loop(loop)


def _loop(loop: callable):
    last = time.ticks_ms()
    while True:
        now = time.ticks_ms()
        dt = time.ticks_diff(now, last) / 1000
        last = now

        device._update(dt)

        loop(dt)
