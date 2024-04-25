Bluetooth
=========
Using Bluetooth Low Energy (BLE) to communicate with the NanoNav.

Quick Example
-------------

.. code-block:: python

    from nanonav import BLE

    # Create a Bluetooth object
    ble = BLE(name="NanoNav")  

    ble.send(43)
    response = ble.read()

Usage
-----
.. autoclass:: nanonav.BLE     
    :members: 
    :special-members: __init__,
    

Connecting from Mobile
----------------------

Various mobile apps are available for communicating with Bluetooth Low Energy. We recommend LightBlue which is available for both iOS and Android.
TODO: Add screenshots and instructions for connecting to the NanoNav using LightBlue.

