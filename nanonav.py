
from ble_advertising import advertising_payload
import bluetooth
from machine import Pin, PWM, ADC, freq
import machine
from micropython import const
import rp2

import time

# Define BLE constants (these are not packaged in bluetooth for space efficiency)
_IO_CAPABILITY_DISPLAY_ONLY = const(0)
_FLAG_READ = const(0x0002)
_FLAG_WRITE = const(0x0008)
_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE = const(3)

class BLE:
    """
    A helpful wraper around the BLE service functions needed for the Wumpus World project
    """
    def __init__(self, ble=bluetooth.BLE(), name="NANO RP2040"):
        # Setup bluetooth low energy communication service
        _SERVICE_UUID = bluetooth.UUID(0x1523) # unique service id for the communication
        _NanoBot_CHAR_UUID = (bluetooth.UUID(0x1525), _FLAG_WRITE | _FLAG_READ) # characteristic
        _NanoBot_SERVICE = (_SERVICE_UUID, (_NanoBot_CHAR_UUID,),) # service to provide the characteristic

        self._ble = ble
        self._ble.active(True)
        self._ble.config(
            bond=True,
            mitm=True,
            le_secure=True,
            io=_IO_CAPABILITY_DISPLAY_ONLY
        )
        self._ble.irq(self._irq)
        ((self._handle,),) = self._ble.gatts_register_services((_NanoBot_SERVICE,))
        self._connections = set()
        self._payload = advertising_payload(name=name, services=[_SERVICE_UUID])
        self._advertise()
        self.value = b'a'

    def _advertise(self, interval_us=500000):
        self._ble.gap_advertise(interval_us, adv_data=self._payload)

    def _irq(self, event, data):
        # handle bluetooth event
        if event == _IRQ_CENTRAL_CONNECT:
            # handle succesfull connection
            conn_handle, addr_type, addr = data
            self._connections.add(conn_handle)

        elif event == _IRQ_CENTRAL_DISCONNECT:
            # handle disconnect
            conn_handle, _, _ = data
            self._connections.remove(conn_handle)
            self._advertise()

        elif event == _IRQ_GATTS_WRITE:
            conn_handle, value_handle = data
            if conn_handle in self._connections:
                # Value has been written to the characteristic
                self.value = self._ble.gatts_read(value_handle)


    def send(self, value):
        """
        Send value to the bluetooth characteristic.

        :param value: The value to send.
        :type value: bytes, int, str
        :raise ValueError: If the value is not bytes, int, or str.

        """
        if not isinstance(value, bytes):
            if isinstance(value, int):
                value = value.to_bytes(1, "big")
            elif isinstance(value, str):
                value = value.encode('utf-8')
            else:
                raise ValueError("send value should be type bytes, int, or string")
        self.value = value
        self._ble.gatts_write(self._handle, value)

    def read(self, as_type="bytes"):
        """
        Return the current value of the bluetooth characteristic, or None if an error occurred.

        :param as_type: The type to return the value as. Must be one of 'bytes', 'str', or 'int'.
        :type as_type: str
        :return: The value of the characteristic.
        :rtype: bytes, str, int, None
        :raise ValueError: If as_type is not 'bytes', 'str', or 'int'.
        """
        value = self.value  # try using the last value written to characteristic
        try:
            if as_type == "bytes":
                return value
            elif as_type == "str":
                return value.decode("utf-8")
            elif as_type == "int":
                print(f'read {value}')
                return int.from_bytes(value, "big")
        except Exception as e:
            return None

        raise ValueError("as_type must be one of 'bytes', 'str', or 'int'")