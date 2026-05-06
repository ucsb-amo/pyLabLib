.. _sensors_americanmagnetics:

.. note::
    Basic sensors communication concepts are described on the corresponding :ref:`page <basic_sensors_basics>`

American Magnetics 1700
==============================

American Magnetics manufactures cryogenic liquid level monitors, which are used for monitoring liquid nitrogen or helium levels inside cryostats. Level meter model 1700 is supported in the package.

The main device class is :class:`pylablib.devices.AmericanMagnetics.AM1700<.AmericanMagnetics.base.AM1700>`.

Software requirements
-----------------------

Model 1700 provides a bare RS232 interface (which should work with any appropriate USB-to-RS232), as well as an Ethernet interface. Neither require any specific software.


Connection
-----------------------

The device is identified either using a COM port (when RS232 port with an appropriate USB adapter is used), or a network address and a port (the default port 7180 is used unless explicitly specified). For the COM port, all you need to know is their COM-port address (e.g., ``COM5``)::

    >> from pylablib.devices import AmericanMagnetics
    >> sensor = AmericanMagnetics.AM1700("COM5")
    >> sensor.close()

For the Ethernet connection, a network address (e.g., an IP address) is required::

    >> from pylablib.devices import AmericanMagnetics
    >> sensor = AmericanMagnetics.AM1700("192.168.0.1")
    >> sensor.close()



Operation
-----------------------


The operation of this temperature sensor is fairly straightforward, but there is a couple of points to keep in mind:

    - Refill valve control is not available in the provided remote interface, and is only available in the web interface.
    - Like most similar devices, querying the level using :meth:`.AM1700.get_level` immediately returns the most recently measured value.