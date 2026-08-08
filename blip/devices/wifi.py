import network

WIFI_DISCONNECTED = 0
WIFI_CONNECTING = 1
WIFI_CONNECTED = 2


class Wifi:
    _wlan: network.WLAN
    _connecting: bool = False

    def __init__(self):
        self._wlan = network.WLAN(network.STA_IF)
        self._wlan.active(False)

    def scan(self) -> list[str]:
        active = self._wlan.active()
        self._wlan.active(True)
        nets = {ssid.decode("UTF-8") for ssid, *_ in self._wlan.scan() if ssid}
        self._wlan.active(active)
        return sorted(list(nets))

    def connect(self, ssid, password):
        self._connecting = True
        self._wlan.active(True)
        self._wlan.disconnect()
        self._wlan.connect(ssid, password)

    def ssid(self) -> str:
        if not self._wlan.isconnected():
            return ""

        return self._wlan.config("ssid")

    def status(self) -> int:
        if self._wlan.isconnected():
            self._connecting = False
            return WIFI_CONNECTED

        if self._connecting:
            return WIFI_CONNECTING

        return WIFI_DISCONNECTED

    def disconnect(self):
        self._connecting = False
        self._wlan.active(False)
