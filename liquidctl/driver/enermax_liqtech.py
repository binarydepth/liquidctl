from liquidctl.driver.usb import UsbHidDriver

class EnermaxLiqtechXTR(UsbHidDriver):

    _MATCHES = [
        (
            0x2E3C,
            0x0A12,
            "ENERMAX LIQTECH XTR",
            {},
        )
    ]

    def initialize(self, **kwargs):
        return []

    def get_status(self, **kwargs):
        return []

    def set_screen(self, channel, mode, value, **kwargs):
        pkt = bytearray(65)

        pkt[1] = 0x20

        modes = {
            "cpu-c": 0x01,
            "cpu-f": 0x02,
            "gpu-c": 0x04,
            "gpu-f": 0x08,
            "rpm":   0x10,
        }

        pkt[2] = modes[mode]

        if mode == "cpu-c":
            pkt[7] = int(value)

        elif mode == "cpu-f":
            pkt[8] = int(value)

        elif mode == "gpu-c":
            pkt[10] = int(value)

        elif mode == "gpu-f":
            pkt[11] = int(value)

        elif mode == "rpm":
            pkt[12] = (int(value) >> 8) & 0xff
            pkt[13] = int(value) & 0xff

        self.device.write(pkt)
