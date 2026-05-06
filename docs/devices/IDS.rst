.. _cameras_ids:

.. note::
    General camera communication concepts are described on the corresponding :ref:`page <cameras_basics>`.

IDS peak cameras interface
==========================

IDS manufactures a variety of cameras, which implement GenICam-based interface through its peak API. It has been tested with IDS U3-31A0SE-M camera.

The code is located in :mod:`pylablib.devices.IDS`, and the main camera class is :class:`pylablib.devices.IDS.IDSPeakCamera<.peak.IDSPeakCamera>`.

Software requirements
----------------------

These cameras require ``ids_peak.dll``, which is installed with the freely available upon registration `IDS peak software <https://en.ids-imaging.com/download-peak.html>`__. After installation, the path to the IDS peak SDK (for located by default in ``IDS/ids_peak/generic_sdk`` folder in ``Program Files``) is automatically added as ``IDS_PEAK_SDK_PATH`` environment variable, which is one of the places where pylablib looks for it by default. If the DLLs are located elsewhere, the path (either to the DLL file, or to the containing folder) can be specified using the library parameter ``devices/dlls/ids_peak``::

    import pylablib as pll
    pll.par["devices/dlls/ids_peak"] = "path/to/dlls"
    from pylablib.devices import IDS
    cam = IDS.IDSPeakCamera()



Connection
----------------------

The cameras are identified either by their index among the present cameras (starting from 0), by their key, or their serial number. To get the list of all cameras, you can use IDS peak software, or :func:`IDS.list_cameras<.peak.list_cameras>`::

    >> from pylablib.devices import IDS
    >> IDS.list_cameras()
    [TIDSPeakDeviceDescriptorInfo(key='C:\\Program Files\\IDS\\ids_peak\\ids_u3vgentl\\64\\ids_u3vgentlk.cti|IDS GenICam Producer (U3VK)|IDS USB3 Vision Ifc|000000000000U3-31AxSE-M-0', display_name='IDS Imaging Development Systems GmbH U3-31AxSE-M (000000000000fU3-31AxSE-M-0)', user_name='', vendor='IDS Imaging Development Systems GmbH', model='U3-31AxSE-M', serial='0000000000', version='10007.12.1.1.1000073.1.352', tl_type='U3V')]
    >> cam = IDS.IDSPeakCamera()  # by default, connect to the first available camera
    >> cam.close()
    >> cam = IDS.IDSPeakCamera(serial="0000000000")
    >> cam.close()
    >> cam = IDS.IDSPeakCamera(key="C:\\Program Files\\IDS\\ids_peak\\ids_u3vgentl\\64\\ids_u3vgentlk.cti|IDS GenICam Producer (U3VK)|IDS USB3 Vision Ifc|000000000000U3-31AxSE-M-0")
    >> cam.close()


Operation
------------------------

The operation of these cameras is relatively standard. They support all the standard methods for dealing with ROI, starting and stopping acquisition, and operating the frame reading loop. The SDK also provides a universal interface for getting and setting various :ref:`camera attributes <cameras_basics_attributes>` using their name. You can use :meth:`.IDSPeakCamera.get_attribute_value` and :meth:`.IDSPeakCamera.set_attribute_value` for that, as well as ``.cav`` attribute which gives a dictionary-like access::

    >> cam = IDS.IDSPeakCamera()
    >> cam.get_attribute_value("Width")  # cet the ROI width
    656
    >> cam.set_attribute_value("Width", 512)  # set the ROI width to 512px
    >> cam.cav["Width"]  # get the width; could also use cam.get_attribute_value("Width")
    512

To see all available attributes, you can call :meth:`.IDSPeakCamera.get_all_attributes` to get a dictionary with attribute objects, and :meth:`.IDSPeakCamera.get_all_attribute_values` to get the dictionary of attribute values. The attribute objects provide additional information: attribute kind (integer, enum, string, etc.), range (either numerical range, or selection of values for enum attributes), description string, etc.::

    >> cam = IDS.IDSPeakCamera()
    >> attr = cam.get_attribute("Width")
    >> attr.description
    'Width of the image provided by the device (in pixels).'
    >> attr.writable
    True
    >> (attr.min, attr.max)
    (1, 656)

Since these properties vary a lot between different cameras, it is challenging to write a universal class covering a large range of cameras. Hence, currently the universal class only has the basic camera parameter control such as ROI (without binning) and exposure (if present). For many specific cameras you might need to explore the attributes tree (either using the Python class and, e.g., a console, or via Vimba X) and operate them directly in your code.


Known issues
--------------------

- Currently only the basic unpacked monochrome pixel formats are fully supported: ``Mono8``, ``Mono10``, ``Mono12``, ``Mono16``, and ``Mono32``. The reason is that even nominally well-defined types (e.g., ``Mono10p``) have different formats for different cameras. Currently any unsupported format will raise an error on readout by default. It it still possible to read these out as raw frame data in the form of 1D or 2D numpy ``'u1'`` array by enabling raw frame readout using :meth:`.IDSPeakCamera.enable_raw_readout` method::

    >> cam = IDS.IDSPeakCamera()
    >> cam.get_detector_size()  # 1024px x 1024px frame
    (816, 624)
    >> cam.set_attribute_value("PixelFormat", "Mono10p")  # unsupported format (10 bits per pixel, i.e., 5 bytes for every 4 pixels)
    >> cam.snap().shape
    ...
    IDSPeakError: pixel format Mono10p is not supported
    >> cam.enable_raw_readout("frame")  # frame data is returned as a flat array
    >> cam.snap().shape  # 816 * 624 * (10/8) = 426400 bytes
    (1, 636480)

``Mono12p`` format is supported with a particular packing method used in the IDS U3-31A0SE-M camera. However, it is not guaranteed to work with other cameras, and needs to be checked first (e.g., by comparing results with ``Mono12`` and ``Mono12p`` format).