from liquidctl.driver.enermax_liqtech import EnermaxLiqtechXTR


def test_match_table_contains_liqtech_xtr():
    assert (
        0x2E3C,
        0x0A12,
        "ENERMAX LIQTECH XTR",
        {},
    ) in EnermaxLiqtechXTR._MATCHES


def test_driver_is_usb_hid_driver():
    from liquidctl.driver.usb import UsbHidDriver

    assert issubclass(EnermaxLiqtechXTR, UsbHidDriver)


def test_driver_has_required_methods():
    assert hasattr(EnermaxLiqtechXTR, "initialize")
    assert hasattr(EnermaxLiqtechXTR, "get_status")
    assert hasattr(EnermaxLiqtechXTR, "set_screen")
