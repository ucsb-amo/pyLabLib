.. _vnas_picotech:

Pico Technology PicoVNA
==============================

.. note::
    General device communication concepts are described on the corresponding :ref:`page <devices_basics>`.

Pico Technology produces a PicoVNA series of USB-controlled vector network analyzers. The library has been tested with PicoVNA 106.

The main device class is :class:`pylablib.devices.PicoTech.PicoVNA<.PicoTech.vna_scpi.PicoVNA>`.

Software requirements
-----------------------

The network analyzer comes with `PicoVNA control software <https://www.picotech.com/vector-network-analyzer/picovna/picovna5-software>`__, which is required for operation. The library code uses SCPI server which is run by the PicoVNA software, so no additional installations are required.


Connection
-----------------------

The connection requires the PicoVNA software to be running and already connected to a network analyzer. In this case, the SCPI control server can be set up in the settings menu (by default, it is enabled and running on port 5025). Then the IP address (``127.0.0.1``, by default) and the port (``5025`` by default) are required to identify the instance of the PicoVNA software and, therefore, the VNA::

    >> from pylablib.devices import PicoTech
    >> vna = PicoTech.PicoVNA()  # port 5025 on the local PC, which is the default setup
    >> vna.close()

Operation
------------------------

The method names are self-explanatory. Currently only basic operations are supported: frequency range, IF bandwidth, output level, S parameter acquisition. There is a couple of points to keep in mind:

    - Reading sweep results (:meth:`.PicoVNA.read_single_trace` or :meth:`.PicoVNA.read_S_parameters`) can only be performed after a single sweep has been acquired (:meth:`.PicoVNA.acquire_single`), and it only returns once the sweep is finished. Therefore, it has an extra argument to increase the read timeout, which should be at least several seconds longer than the sweep time.
    - Operating the VNA using the software while using the control code is discouraged. It would still operate, but some values might be inconsistent. For example, the frequency axis values is calculated based on the currently set up frequency range, so if the range is change after a sweep has been acquired, the readout results would have incorrect frequency values.

