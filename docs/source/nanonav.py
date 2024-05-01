
"""
Skeleton file for documentation docstrings
"""

from ble_advertising import advertising_payload
import bluetooth
from machine import Pin, PWM, ADC, freq
import machine
from micropython import const
import rp2

import time



class BLE:
    """
    A helpful wraper around the MicroPython BLE service functions.

    :param ble: The bluetooth object to use for BLE communication (leave as default unless you know why it should be different).
    :type ble: bluetooth.BLE
    :param name: The name of the device to advertise (default: "NANO RP2040").
    :type name: str
    """
    def __init__(self, ble=bluetooth.BLE(), name="NANO RP2040"):
        pass

    def send(self, value):
        """
        Send value to the bluetooth characteristic.

        :param value: The value to send.
        :type value: int, bytes, or str
        :raise ValueError: If the value is not int, bytes, or str.
        """
        pass

    def read(self):
        """
        Return the current value of the bluetooth characteristic, or None if an error occurred.

        :type as_type: str
        :return: The value of the characteristic.
        :rtype: int, None
        """
        pass

    def on_connected(self):
        """
        You may specify this method to be called once the BLE connection is established.
        """
        pass

    def on_disconnected(self):
        """
        You may specify this method to be called once the BLE connection is lost.
        """
        pass