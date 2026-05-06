.. _cameras_allvis:

.. note::
    General camera communication concepts are described on the corresponding :ref:`page <cameras_basics>`.

Allied Vision VimbaX cameras interface
=======================================

Allied Vision manufactures a variety of cameras, which implement GenICam-based interface through its pylon API. It has been tested with Allied Vision 1800 U-052m camera.

The code is located in :mod:`pylablib.devices.AlliedVision`, and the main camera class is :class:`pylablib.devices.AlliedVision.AlliedVisionVimbaXCamera<.VimbaX.AlliedVisionVimbaXCamera>`.

Software requirements
----------------------

These cameras require ``VmbC.dll``, which is installed with the freely available upon registration `Allied Vision Vimba X SDK <https://www.alliedvision.com/en/support/software-downloads/vimba-x-sdk/vimba-x>`__. After installation, the path to the software folder (for located by default in ``Allied Vision/Vimba X`` folder in ``Program Files``) is automatically added as ``VIMBA_X_HOME`` environment variable, which is one of the places where pylablib looks for it by default. If the DLLs are located elsewhere, the path (either to the DLL file, or to the containing folder) can be specified using the library parameter ``devices/dlls/alliedvision_vimbax``::

    import pylablib as pll
    pll.par["devices/dlls/alliedvision_vimbax"] = "path/to/dlls"
    from pylablib.devices import AlliedVision
    cam = AlliedVision.AlliedVisionVimbaXCamera()



Connection
----------------------

The cameras are identified either by their index among the present cameras (starting from 0), by their name, or their serial number. To get the list of all cameras, you can use Vimba X software, or :func:`AlliedVision.list_cameras<.VimbaX.list_cameras>`::

    >> from pylablib.devices import AlliedVision
    >> AlliedVision.list_cameras()
    [TCameraInfo(name='DEV_Cam1', model='Camera Simulator (G1-030_VSWIR)', model_full='Allied Vision Camera Simulator (G1-030_VSWIR)(DEV_Cam1)', serial='0D512', name_full='69:C:\\Program Files\\Allied Vision\\Vimba X\\cti\\VimbaCameraSimulatorTL.cti26:Camera Simulator Interface8:DEV_Cam1')]
    >> cam = AlliedVision.AlliedVisionVimbaXCamera()  # by default, connect to the first available camera
    >> cam.close()
    >> cam = AlliedVision.AlliedVisionVimbaXCamera(serial="0D512")
    >> cam.close()
    >> cam = AlliedVision.AlliedVisionVimbaXCamera(name="DEV_Cam1")
    >> cam.close()


Operation
------------------------

The operation of these cameras is relatively standard. They support all the standard methods for dealing with ROI, starting and stopping acquisition, and operating the frame reading loop. The SDK also provides a universal interface for getting and setting various :ref:`camera attributes <cameras_basics_attributes>` using their name. You can use :meth:`.AlliedVisionVimbaXCamera.get_attribute_value` and :meth:`.AlliedVisionVimbaXCamera.set_attribute_value` for that, as well as ``.cav`` attribute which gives a dictionary-like access::

    >> cam = AlliedVision.AlliedVisionVimbaXCamera()
    >> cam.get_attribute_value("Width")  # cet the ROI width
    656
    >> cam.set_attribute_value("Width", 512)  # set the ROI width to 512px
    >> cam.cav["Width"]  # get the width; could also use cam.get_attribute_value("Width")
    512

To see all available attributes, you can call :meth:`.AlliedVisionVimbaXCamera.get_all_attributes` to get a dictionary with attribute objects, and :meth:`.AlliedVisionVimbaXCamera.get_all_attribute_values` to get the dictionary of attribute values. The attribute objects provide additional information: attribute kind (integer, enum, string, etc.), range (either numerical range, or selection of values for enum attributes), description string, etc.::

    >> cam = AlliedVision.AlliedVisionVimbaXCamera()
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

- Currently only the basic unpacked monochrome pixel formats are fully supported: ``Mono8``, ``Mono10``, ``Mono12``, ``Mono16``, and ``Mono32``. The reason is that even nominally well-defined types (e.g., ``Mono10p``) have different formats for different cameras. Currently any unsupported format will raise an error on readout by default. It it still possible to read these out as raw frame data in the form of 1D or 2D numpy ``'u1'`` array by enabling raw frame readout using :meth:`.AlliedVisionVimbaXCamera.enable_raw_readout` method::

    >> cam = AlliedVision.AlliedVisionVimbaXCamera()
    >> cam.get_detector_size()  # 1024px x 1024px frame
    (656, 520)
    >> cam.set_attribute_value("PixelFormat", "Mono10p")  # unsupported format (10 bits per pixel, i.e., 5 bytes for every 4 pixels)
    >> cam.snap().shape
    ...
    AlliedVisionVimbaXError: pixel format Mono10p is not supported
    >> cam.enable_raw_readout("frame")  # frame data is returned as a flat array
    >> cam.snap().shape  # 656 * 520 * (10/8) = 426400 bytes
    (1, 426400)

``Mono12p`` format is supported with a particular packing method used in the emulation cameras and Allied Vision 1800 U-052m camera. However, it is not guaranteed to work with other cameras, and needs to be checked first (e.g., by comparing results with ``Mono12`` and ``Mono12p`` format).


Allied Vision Bonito cameras
============================

Allied Vision manufactures a variety of cameras with different interfaces: USB, GigE, and CameraLink. Currently, only CameraLink Bonito cameras using NI IMAQ frame grabber are supported. It has been tested with Bonito CL-400B/C and NI IMAQ frame grabber.

The code is located in :mod:`pylablib.devices.AlliedVision`, and the main camera class is :class:`pylablib.devices.AlliedVision.BonitoIMAQCamera<.Bonito.BonitoIMAQCamera>`.

Software requirements
-----------------------

Since the camera control is done purely through the frame grabber interface, the requirements are the same as for generic :ref:`IMAQ cameras <cameras_imaq>`. However, the correct camera file still needs to be specified to determine the correct serial communication parameters (especially the termination character)


Connection
-----------------------

The cameras are identified by their name, which usually looks like ``"img0"``. To get the list of all cameras, you can use NI MAX (Measurement and Automation Explorer), or :func:`.IMAQ.list_cameras`::

    >> from pylablib.devices import IMAQ, AlliedVision
    >> IMAQ.list_cameras()
    ['img0']
    >> cam = AlliedVision.BonitoIMAQCamera('img0')
    >> cam.close()


Operation
------------------------

The operation of these cameras is relatively standard. They support all the standard methods for dealing with ROI and exposure, starting and stopping acquisition, and operating the frame reading loop. However, there's a couple of differences from the standard libraries worth highlighting:

    - :class:`.Bonito.BonitoIMAQCamera` supports all of :class:`.IMAQ.IMAQCamera` features, such as trigger control and fast buffer acquisition. Some methods have been modified to make them more convenient: e.g., :meth:`.Bonito.BonitoIMAQCamera.set_roi` method sets the camera ROI and automatically adjusts the frame grabber ROI to match.
    - Internally the camera only supports vertical ROI (number of rows), so the horizontal ROI is set via the frame grabber. This means that regardless of the horizontal ROI settings the whole rows are always transmitted between the camera and the frame grabber, so it does not affect, e.g., the maximal frame rate.
    - The camera supports a status line, which replaces the first 8 pixels in the upper row encoded frame number. You can use :func:`.AlliedVision.Bonito.get_status_lines` function to identify and extract the data in the status lines from the supplied frames. Note that due to the full row transfer mentioned earlier, the status line is only available if the horizontal ROI span starts from zero; otherwise, it will be partially or completely cut off.
    - You can use the function :func:`.AlliedVision.Bonito.check_grabber_association` to check if the given IMAQ camera is a Bonito model by sending several standard Bonito commands and checking replies.