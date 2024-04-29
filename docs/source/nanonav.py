
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
    A helpful wraper around the BLE service functions needed for the Wumpus World project
    """
    def __init__(self, ble=bluetooth.BLE(), name="NANO RP2040"):
        pass

    def send(self, value):
        """
        Send value to the bluetooth characteristic.

        :param value: The value to send.
        :type value: bytes, int, str
        :raise ValueError: If the value is not bytes, int, or str.

        """
        pass

    def read(self, as_type="bytes"):
        """
        Return the current value of the bluetooth characteristic, or None if an error occurred.

        :param as_type: The type to return the value as. Must be one of 'bytes', 'str', or 'int'.
        :type as_type: str
        :return: The value of the characteristic.
        :rtype: bytes, str, int, None
        :raise ValueError: If as_type is not 'bytes', 'str', or 'int'.
        """
        pass