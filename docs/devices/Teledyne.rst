.. _cameras_teledyne:

.. note::
    General camera communication concepts are described on the corresponding :ref:`page <cameras_basics>`

Teledyne Spinnaker cameras interface
=====================================

Teledyne manufactures a wide variety of cameras, which implement GenICam-based interface through its Spinnaker API. It has been tested with FLIR Blackfly S BFS-U3-04S2M.

The code is located in :mod:`pylablib.devices.Teledyne`, and the main camera class is :class:`pylablib.devices.Teledyne.TeledyneSpinnakerCamera<.Spinnaker.TeledyneSpinnakerCamera>`.

Software requirements
----------------------

These cameras require ``SpinnakerC_vXY.dll`` (where ``X`` and ``Y`` is the library version, e.g., ``SpinnakerC_v140.dll``), which is installed with the freely available upon registration `Teledyne Spinnaker SDK <https://www.teledynevisionsolutions.com/support/support-center/software-firmware-downloads/iis/spinnaker-sdk-download/spinnaker-sdk--download-files/>`__ (you need the standard version, not Python); the code was tested with the version `4.0.0.116`. The DLLs are contained both in the "Camera Evaluation" (default) and the "Application Development" version, so either is fine. After installation, the path to the DLL (for Spinnaker SDK 4.0.0.116 located by default in ``Teledyne/Spinnaker/bin64/vs2015`` folder in ``Program Files``) is automatically added to system ``PATH`` variable, which is one of the places where pylablib looks for it by default. If the DLLs are located elsewhere, the path (either to the DLL file, or to the containing folder) can be specified using the library parameter ``devices/dlls/teledyne_spinnaker``::

    import pylablib as pll
    pll.par["devices/dlls/teledyne_spinnaker"] = "path/to/dlls"
    from pylablib.devices import Teledyne
    cam = Teledyne.TeledyneSpinnakerCamera()



Connection
----------------------

The cameras are identified either by their index among the present cameras (starting from 0), or by their serial number. To get the list of all cameras, you can use Teledyne SpinView, or :func:`Teledyne.list_cameras<.Spinnaker.list_cameras>`::

    >> from pylablib.devices import Teledyne
    >> Teledyne.list_cameras()
    [TCameraInfo(name='FLIR Blackfly S BFS-U3-04S2M', model='Blackfly S BFS-U3-04S2M', serial='24100000', devclass='USB3Vision', devversion='1707.0.0.0', vendor='FLIR', user_name='')]
    >> cam = Teledyne.TeledyneSpinnakerCamera()  # by default, connect to the first available camera
    >> cam.close()
    >> cam = Teledyne.TeledyneSpinnakerCamera(serial="24100000")
    >> cam.close()


Operation
------------------------

The operation of these cameras is relatively standard. They support all the standard methods for dealing with ROI, starting and stopping acquisition, and operating the frame reading loop. The SDK also provides a universal interface for getting and setting various :ref:`camera attributes <cameras_basics_attributes>` using their name. You can use :meth:`.TeledyneSpinnakerCamera.get_attribute_value` and :meth:`.TeledyneSpinnakerCamera.set_attribute_value` for that, as well as ``.cav`` attribute which gives a dictionary-like access::

    >> cam = Teledyne.TeledyneSpinnakerCamera()
    >> cam.get_attribute_value("StatusInformation/AcqInProgress")  # check if the camera is acquiring
    0
    >> cam.set_attribute_value("Width", 512)  # set the ROI width to 512px
    >> cam.cav["Width"]  # get the width; could also use cam.get_attribute_value("Width")
    512

To see all available attributes, you can call :meth:`.TeledyneSpinnakerCamera.get_all_attributes` to get a dictionary with attribute objects, and :meth:`.TeledyneSpinnakerCamera.get_all_attribute_values` to get the dictionary of attribute values. The attribute objects provide additional information: attribute kind (integer, enum, string, etc.), range (either numerical range, or selection of values for enum attributes), description string, etc.::

    >> cam = Teledyne.TeledyneSpinnakerCamera()
    >> attr = cam.get_attribute("Width")
    >> attr.description
    'Width of the image provided by the device (in pixels).'
    >> attr.writable
    True
    >> (attr.min, attr.max)
    (8, 1024)

Since these properties vary a lot between different cameras, it is challenging to write a universal class covering a large range of cameras. Hence, currently the universal class only has the basic camera parameter control such as ROI (without binning), acquisition status, and exposure (if present). For many specific cameras you might need to explore the attributes tree (either using the Python class and, e.g., a console, or via SpinView in the Features tab) and operate them directly in your code.


Known issues
--------------------

- Currently only the basic unpacked monochrome pixel formats are supported: ``Mono8``, ``Mono10``, ``Mono12``, ``Mono16``, and ``Mono32``. The reason is that even nominally well-defined types (e.g., ``Mono12Packed``) have different formats for different cameras. Currently any unsupported format will raise an error on readout by default. It it still possible to read these out as raw frame data in the form of 1D or 2D numpy ``'u1'`` array by enabling raw frame readout using :meth:`.TeledyneSpinnakerCamera.enable_raw_readout` method::

    >> cam = Teledyne.TeledyneSpinnakerCamera()
    >> cam.get_detector_size()  # 1024px x 1024px frame
    (1024, 1024)
    >> cam.set_attribute_value("PixelFormat", "Mono12Packed")  # unsupported format
    >> cam.snap().shape
    ...
    TeledyneSpinnakerError: pixel format Mono12Packed is not supported
    >> cam.enable_raw_readout("frame")  # frame data is returned as a flat array
    >> cam.snap().shape  # 1024 * 1024 * 1.5 = 1572864 bytes
    (1, 1572864)