Quick Start
===========

Installation
------------
You will need to download `OpenMV IDE <https://openmv.io/pages/download>`_ to transfer your MicroPython code onto the arduino. See :ref:`Workflow` for more information about this process.

Your Arduino Nano RP2040 can run either C++ or MicroPython, but not both at the same time. So before moving on, it is important that the Arduino is configured for MicroPython mode.
`Link this guide <https://docs.arduino.cc/tutorials/nano-rp2040-connect/rp2040-openmv-setup/>` from Arduino will walk you through the process of "bootloading" the Nano RP2040 so that 
you can run MicroPython code on it. After you have done this once, you should not need to do it again.

To use the NanoNav supplementary code, either download :download:`nanonav.py </../../nanonav.py>` to your project directory

Or copy the code below into a file called nanonav.py

.. raw:: html

   <div style="max-height: 50vh; overflow-y: scroll;">

.. literalinclude:: /../../nanonav.py
    :language: python
    :linenos:

.. raw:: html

   </div>

..  _Workflow:

Workflow
--------
Here is how you can program your Arduino. You will need a file called `main.py` that contains your MicroPython code - you can create other files 
and import them as usual, but `main.py` is the one that will be run on the Arduino. For getting started quickly, we recommend downloading this installation check 
:download:`main.py </../../tests/installation_check/main.py>` to verify that everything is working correctly so far. Alternatively, copy the following into a file called `main.py`:

.. raw:: html

   <div style="max-height: 50vh; overflow-y: scroll;">

.. literalinclude:: /../../tests/installation_check/main.py
    :language: python
    :linenos:

.. raw:: html

   </div>

We recommend creating a folder that you will use for your MicroPython code - put both `nanonav.py` and `main.py` in that folder. Open the OpenMV IDE application. Use the File -> Open Files menu to select the `main.py` file that you downloaded.
Connect your Arduino to your computer using a USB cable. Click the "Connect" button in the bottom left of OpenMV IDE. The arrow below it should turn green when connected. Click that arrow to run
your code on the Arduino. If all worked well, you should see :red:`TODO`.

.. note::
   We recommend testing your

..  _MicroPython:

MicroPython
-----------

In general, MicroPython is very similar to regular Python, but there are some difference we would like to point you to before you begin. MicroPython has its own library of 
packages, which are different from the PyPi packages you may be used to (if you ever ```pip install``` anything). We provide helper functions for the ways we think you'll need to 
interact with the Arduino, Bluetooth, and peripherals, and just about anything you can do in Python 3.11 can also be done in MicroPython, but note that you will not have access to the full standard Python library. For instance, you can import `time` since this has been added to
MicroPython's library, but you cannot import `Queue` or other familiar packages. If ever in doubt about whether MicroPython supports a particular package, simply google "MicroPython [package name]", 
and you will likely find the information you need.
You can find the MicroPython documentation `here <https://docs.micropython.org/en/latest/>`_.