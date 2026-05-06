from pylablib.core.utils import funcargparse
from .VmbC_defs import VmbFeatureDataType, VmbFeatureVisibilityType, VmbAccessModeType
from .VmbC_lib import wlib as lib, AlliedVisionVimbaXError, AlliedVisionVimbaXLibError  # pylint: disable=unused-import

from ...core.utils import py3, dictionary
from ...core.devio import interface
from ..interface import camera
from ..utils import load_lib, pixel_format as pf
from ...core.utils.ctypes_tools import funcaddressof, as_ctypes_array
from ...core.utils.cext_tools import try_import_cext
with try_import_cext():
    from .utils import get_callback  # pylint: disable=no-name-in-module

import numpy as np
import collections
import ctypes

import functools
import time
import warnings


class AlliedVisionVimbaXTimeoutError(AlliedVisionVimbaXError):
    """Allied Vision Vimba X frame timeout error"""




class LibraryController(load_lib.LibraryController):
    def _do_init(self):
        lib.VmbStartup(None)
    def _do_uninit(self):
        lib.VmbShutdown()
libctl=LibraryController(lib)
def restart_lib():
    libctl.shutdown()

def get_SDK_version():
    """Get version of Allied Vision VimbaX SDK"""
    with libctl.temp_open():
        return ".".join([str(v) for v in lib.VmbVersionQuery()])



_camera_info_alias={"cameraIdString":"name", "modelName":"model", "cameraName":"model_full", "serialString":"serial", "cameraIdExtended":"name_full"}
TCameraInfo=collections.namedtuple("TCameraInfo",["name","model","model_full","serial","name_full"])
def _parse_cam_info(cam_info):
    """Get Allied Vision VimbaX camera info for a camera with the given index"""
    values={alias:py3.as_str(getattr(cam_info,name)) for name,alias in _camera_info_alias.items()}
    return TCameraInfo(**values)
def list_cameras(desc=True):
    """
    List all cameras available through Allied Vision VimbaX interface
    
    If ``desc==True``, return complete camera descriptions; otherwise, simply return the names.
    """
    with libctl.temp_open():
        camlst=lib.VmbCamerasList()
        cams=[_parse_cam_info(ci) for ci in camlst]
        return cams if desc else [c.name for c in cams]
def _find_camera(cameras, **kwargs):
    for i,c in enumerate(cameras):
        match=True
        for k,v in kwargs.items():
            if getattr(c,k)!=v:
                match=False
                break
        if match:
            return i
    return None

def get_cameras_number():
    """Get number of connected Allied Vision VimbaX cameras"""
    with libctl.temp_open():
        return len(lib.VmbCamerasList())

    

def _retry_on_fail(name, nrep=3, delay=0.1):
    def wrapper(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            for i in range(nrep):
                try:
                    return f(*args,**kwargs)
                except AlliedVisionVimbaXError as err:
                    if i==nrep-1:
                        raise
                    warnings.warn("functon {} with arguments *{}, **{} raised an error {}".format(name,args,kwargs,err))
                    time.sleep(delay)
        return wrapped
    return wrapper

class AlliedVisionVimbaXAttribute:
    """
    Object representing an Allied Vision VimbaX GenAPI attribute.

    Allows to query and set values and get additional information.
    Usually created automatically by an :class:`AlliedVisionVimbaXCamera` instance.

    Args:
        cam: camera handle
        name: attribute name
        full_name: if supplied, attribute's full name, including the tree structure

    Attributes:
        name: attribute name
        kind: attribute kind; can be ``"int"``, ``"float"``, ``"bool"``, ``"enum"``, ``"str"``, 
            ``"command"``, ``"raw"``, ``"none"``, or ``"unknown"``
        display_name: attribute display name (short description name)
        tooltip: longer attribute description
        description: full attribute description (usually, same as `tooltip`)
        visibility: attribute visibility; can be ``"simple"``, ``"intermediate"``, ``"advanced"``, ``"invisible"``, or ``"unknown"``
        category: attribute category (parent path within the parameter tree)
        namespace: attribute namespace (e.g., ``"Standard"`` or ``"Custom"``)
        representation: numerical attribute representation (e.g., ``"PureNumber"`` or ``"Logarithmic"``)
        readable (bool): whether attribute is readable
        writable (bool): whether attribute is writable
        min (float or int): minimal attribute value (if applicable)
        max (float or int): maximal attribute value (if applicable)
        inc (float or int): minimal attribute increment value (if applicable)
        units: attribute units (if applicable)
        ivalues: list of possible integer values for enum attributes
        values: list of possible text values for enum attributes
        labels: dict ``{label: index}`` which shows all possible values of an enumerated attribute and their corresponding numerical values
        ilabels: dict ``{index: label}`` which shows labels corresponding to numerical values of an enumerated attribute
    """
    _attr_types={   VmbFeatureDataType.VmbFeatureDataInt:"int",
                    VmbFeatureDataType.VmbFeatureDataFloat:"float",
                    VmbFeatureDataType.VmbFeatureDataBool:"bool",
                    VmbFeatureDataType.VmbFeatureDataEnum:"enum",
                    VmbFeatureDataType.VmbFeatureDataString:"str",
                    VmbFeatureDataType.VmbFeatureDataCommand:"command",
                    VmbFeatureDataType.VmbFeatureDataRaw:"raw",
                    VmbFeatureDataType.VmbFeatureDataNone:"none",
                    VmbFeatureDataType.VmbFeatureDataUnknown:"unknown"}
    _vis_types={    VmbFeatureVisibilityType.VmbFeatureVisibilityBeginner:"simple",
                    VmbFeatureVisibilityType.VmbFeatureVisibilityExpert:"intermediate",
                    VmbFeatureVisibilityType.VmbFeatureVisibilityGuru:"advanced",
                    VmbFeatureVisibilityType.VmbFeatureVisibilityInvisible:"invisible",
                    VmbFeatureVisibilityType.VmbFeatureVisibilityUnknown:"unknown"}
    def __init__(self, cam, name, full_name=None):
        self.cam=cam
        self.name=py3.as_str(name)
        info=lib.VmbFeatureInfoQuery(cam,name)
        self.kind=self._attr_types.get(info.featureDataType,"unknown")
        self.display_name=py3.as_str(info.displayName)
        self.tooltip=py3.as_str(info.tooltip)
        self.description=py3.as_str(info.description)
        self.category=py3.as_str(info.category)
        self.full_name=full_name or self.category.lstrip("/")+"/"+self.name
        self.namespace=py3.as_str(info.sfncNamespace)
        self.representation=py3.as_str(info.representation)
        self.visibility=self._vis_types[info.visibility]
        access=lib.VmbFeatureAccessQuery(cam,name)
        self.readable=bool(access[0])
        self.writable=bool(access[1])
        self.units=py3.as_str(info.unit)
        self.min=None
        self.max=None
        self.inc=None
        self.repr=None
        self._value_nodes=None
        self.values=[]
        self.ivalues=[]
        self.labels={}
        self.ilabels={}
        self.enum_expanded={}
        self._fill_info()
    
    def _fill_info(self):
        self.update_limits()
    def _update_attributes(self):
        access=lib.VmbFeatureAccessQuery(self.cam,self.name)
        self.readable=bool(access[0])
        self.writable=bool(access[1])
    def update_limits(self):
        """Update minimal and maximal attribute limits and return tuple ``(min, max, inc)``"""
        self._update_attributes()
        if self.kind=="int":
            try:
                self.min,self.max=lib.VmbFeatureIntRangeQuery(self.cam,self.name)
            except AlliedVisionVimbaXError:
                self.min,self.max=None,None
            try:
                self.inc=lib.VmbFeatureIntIncrementQuery(self.cam,self.name)
            except AlliedVisionVimbaXError:
                self.inc=None
            return (self.min,self.max,self.inc)
        elif self.kind=="float":
            try:
                self.min,self.max=lib.VmbFeatureFloatRangeQuery(self.cam,self.name)
            except AlliedVisionVimbaXError:
                self.min,self.max=None,None
            try:
                ena,inc=lib.VmbFeatureFloatIncrementQuery(self.cam,self.name)
                self.inc=inc if ena else None
            except AlliedVisionVimbaXError:
                self.inc=None
            return (self.min,self.max,self.inc)
        elif self.kind=="enum":
            self.values=[py3.as_str(v) for v in lib.VmbFeatureEnumRangeQuery(self.cam,self.name)]
            self.ivalues=[lib.VmbFeatureEnumAsInt(self.cam,self.name,n) for n in self.values]
            self.labels=dict(zip(self.values,self.ivalues))
            self.ilabels=dict(zip(self.ivalues,self.values))
            enum_entries=[lib.VmbFeatureEnumEntryGet(self.cam,self.name,v) for v in self.values]
            self.enum_expanded={v:(py3.as_str(ee.displayName),py3.as_str(ee.tooltip),py3.as_str(ee.description)) for v,ee in zip(self.values,enum_entries)}
    def truncate_value(self, value):
        """Truncate value to lie within attribute limits"""
        self.update_limits()
        if self.kind in ["int","float"]:
            if self.min is not None and value<self.min:
                value=self.min
            elif self.max is not None and value>self.max:
                value=self.max
            else:
                if self.min is not None and self.inc and self.inc>0:
                    value=((value-self.min)//self.inc)*self.inc+self.min
        return value

    @_retry_on_fail("get_value")
    def get_value(self, enum_as_str=True):
        """
        Get attribute value.
        
        If ``enum_as_str==True``, return enum-style values as strings; otherwise, return corresponding integer values.
        """
        if self.kind=="command":
            return bool(lib.VmbFeatureCommandIsDone(self.cam,self.name))
        self._update_attributes()
        if not self.readable:
            raise AlliedVisionVimbaXError("attribute {} is not readable".format(self.name))
        if self.kind=="int":
            return lib.VmbFeatureIntGet(self.cam,self.name)
        if self.kind=="float":
            return lib.VmbFeatureFloatGet(self.cam,self.name)
        if self.kind=="bool":
            return bool(lib.VmbFeatureBoolGet(self.cam,self.name))
        if self.kind=="str":
            return py3.as_str(lib.VmbFeatureStringGet(self.cam,self.name))
        if self.kind=="enum":
            value=py3.as_str(lib.VmbFeatureEnumGet(self.cam,self.name))
            if not enum_as_str:
                value=self.labels[value]
            return value
        if self.kind=="unknown":
            return None
        raise AlliedVisionVimbaXError("attribute {} of kind {} can not be read".format(self.name,self.kind))
    @_retry_on_fail("set_value")
    def set_value(self, value, truncate=True):
        """
        Set attribute value.
        
        If ``truncate==True``, automatically truncate value to lie within allowed range.
        """
        self._update_attributes()
        if not self.writable:
            raise AlliedVisionVimbaXError("attribute {} is not writable".format(self.name))
        if truncate:
            value=self.truncate_value(value)
        if self.kind=="int":
            lib.VmbFeatureIntSet(self.cam,self.name,int(value))
        elif self.kind=="float":
            lib.VmbFeatureFloatSet(self.cam,self.name,float(value))
        elif self.kind=="bool":
            lib.VmbFeatureBoolSet(self.cam,self.name,bool(value))
        elif self.kind=="str":
            lib.VmbFeatureStringSet(self.cam,self.name,str(value))
        elif self.kind=="enum":
            value=self.ilabels.get(value,value)
            lib.VmbFeatureEnumSet(self.cam,self.name,str(value))
        elif self.kind!="unknown":
            raise AlliedVisionVimbaXError("attribute {} of kind {} can not be set".format(self.name,self.kind))
    def call_command(self):
        """Execute the given command"""
        if self.kind=="command":
            lib.VmbFeatureCommandRun(self.cam,self.name)
        else:
            raise AlliedVisionVimbaXError("attribute {} is not a command".format(self.name))

    def __repr__(self):
        return "{}(name='{}', kind='{}')".format(self.__class__.__name__,self.name,self.kind)







TDeviceInfo=collections.namedtuple("TDeviceInfo",TCameraInfo._fields)
TFrameInfo=collections.namedtuple("TFrameInfo",["frame_index","framestamp","timestamp","offset_x","offset_y"])
class AlliedVisionVimbaXCamera(camera.IROICamera, camera.IAttributeCamera, camera.IExposureCamera):
    """
    Generic Allied Vision VimbaX camera interface.

    Args:
        idx: camera index among the cameras listed using :func:`list_cameras`
        name: camera name; if specified, then `idx` is ignored and the camera is determined based on the provided name
        serial: camera serial number; if specified, then `idx` and `name` is ignored and the camera is determined based on the provided serial number
    """
    Error=AlliedVisionVimbaXError
    TimeoutError=AlliedVisionVimbaXTimeoutError
    _TFrameInfo=TFrameInfo
    def __init__(self, idx=0, name=None, serial=None):
        super().__init__()
        lib.initlib()
        self.idx=idx
        self.name=name
        self.serial=serial
        self.handle=None
        self._cb_mgr=None
        self._buffer_mgr=None
        # self._start_queue_overflows=0
        self.open()
        self._raw_readout_format=False
        self._add_info_variable("device_info",self.get_device_info)
        self._add_settings_variable("exposure",self.get_exposure,self.set_exposure,ignore_error=AlliedVisionVimbaXError)
        self._update_device_variable_order("exposure")
        self._add_settings_variable("frame_period",self.get_frame_period,self.set_frame_period,ignore_error=AlliedVisionVimbaXError)
        # self._add_status_variable("missed_frames",self.get_missed_frames_status)
        # self._update_queue_overflows()


    def _get_connection_parameters(self):
        return (self.idx,self.name,self.serial)
    def open(self):
        """Open connection to the camera"""
        if self.handle is not None:
            return
        with libctl.temp_open():
            cams=list_cameras()
            if self.name is not None or self.serial is not None:
                use_serial=self.serial is not None
                spar={"serial":self.serial} if use_serial else {"name":self.name}
                idx=_find_camera(cams,**spar)
                if idx is None:
                    kind,par=list(spar.items())[0]
                    camsstr=", ".join(["'{}'".format(c.serial if use_serial else c.name) for c in cams])
                    raise AlliedVisionVimbaXError("could not find camera with {} {}; available cameras are {}".format(kind,par,camsstr))
            else:
                idx=self.idx
            if idx>=len(cams):
                raise AlliedVisionVimbaXError("camera index {} is not available ({} cameras exist)".format(idx,len(cams)))
            name=cams[idx].name
            with self._close_on_error():
                self.handle=lib.VmbCameraOpen(name,VmbAccessModeType.VmbAccessModeFull)
                self._opid=libctl.open().opid
                self._update_attributes()
                self._cb_mgr=self.CallbackManager(self.handle)
                self.post_open()
    def close(self):
        """Close connection to the camera"""
        if self.handle is not None:
            try:
                self.clear_acquisition()
            finally:
                try:
                    lib.VmbCameraClose(self.handle)
                finally:
                    self._cb_mgr=None
                    self.handle=None
                    libctl.close(self._opid)
                    self._opid=None
    def is_opened(self):
        return self.handle is not None

    def post_open(self):
        """Additional setup after camera opening"""

    _builtin_attrs=["OffsetX","OffsetY","Width","Height","SensorWidth","SensorHeight","PixelFormat","PayloadSize",
                    "AcquisitionStart","AcquisitionStop","AcquisitionStatus",
                    "AcquisitionFrameRate","AcquisitionFrameRateEnable"]
    def _get_attribute_path(self, a):
        return a.full_name
    _use_full_attribute_names=False
    def _list_attributes(self):
        anames=[py3.as_str(a.name) for a in lib.VmbFeaturesList(self.handle)]
        attrs=[AlliedVisionVimbaXAttribute(self.handle,n,full_name=None if self._use_full_attribute_names else n) for n in anames]
        if self._use_full_attribute_names:
            attrs+=[AlliedVisionVimbaXAttribute(self.handle,n,full_name=n) for n in self._builtin_attrs if n in anames]
        attrs=[a for a in attrs if a.kind in ["int","float","bool","enum","str","command"]]
        return attrs

    def get_attribute_value(self, name, error_on_missing=True, default=None, enum_as_str=True):  # pylint: disable=arguments-differ
        """
        Get value of an attribute with the given name.
        
        If the value doesn't exist or can not be read and ``error_on_missing==True``, raise error; otherwise, return `default`.
        If `default` is not ``None``, assume that ``error_on_missing==False``.
        If `name` points at a dictionary branch, return a dictionary with all values in this branch.
        If ``enum_as_str==True``, return enum-style values as strings; otherwise, return corresponding integer values.
        """
        return super().get_attribute_value(name,error_on_missing=error_on_missing,default=default,enum_as_str=enum_as_str)
    def set_attribute_value(self, name, value, truncate=True, error_on_missing=True):  # pylint: disable=arguments-differ, arguments-renamed
        """
        Set value of an attribute with the given name.
        
        If the value doesn't exist or can not be written and ``error_on_missing==True``, raise error; otherwise, do nothing.
        If `name` points at a dictionary branch, set all values in this branch (in this case `value` must be a dictionary).
        If ``truncate==True``, truncate value to lie within attribute range.
        """
        return super().set_attribute_value(name,value,truncate=truncate,error_on_missing=error_on_missing)
    def call_command(self, name):
        """Execute the given command"""
        self.ca[name].call_command()
    def get_all_attribute_values(self, root="", enum_as_str=True, ignore_errors=True):  # pylint: disable=arguments-differ
        """Get values of all attributes with the given `root`"""
        values=dictionary.Dictionary()
        for n,att in self.get_attribute(root).as_dict("flat").items():
            if att.readable:
                try:
                    values[n]=att.get_value(enum_as_str=enum_as_str)
                except AlliedVisionVimbaXError:  # sometimes nominally implemented features still raise errors
                    if not ignore_errors:
                        raise
        return values
    def set_all_attribute_values(self, settings, root="", truncate=True):  # pylint: disable=arguments-differ
        """
        Set values of all attributes with the given `root`.
        
        If ``truncate==True``, truncate value to lie within attribute range.
        """
        return super().set_all_attribute_values(settings,root=root,truncate=truncate)

    def get_device_info(self):
        """
        Get camera information.

        Return tuple ``(name, model, serial, devclass, devversion, vendor, friendly_name, user_name, props)``.
        """
        caminfo=lib.VmbCameraInfoQueryByHandle(self.handle)
        return TDeviceInfo(*_parse_cam_info(caminfo))

    def _get_data_dimensions_rc(self):
        return self.cav["Height"],self.cav["Width"]
    def get_detector_size(self):
        return self.cav["SensorWidth"],self.cav["SensorHeight"]
    def get_roi(self):
        ox=self.get_attribute_value("OffsetX",default=0)
        oy=self.get_attribute_value("OffsetY",default=0)
        w=self.cav["Width"]
        h=self.cav["Height"]
        return ox,ox+w,oy,oy+h
    def _set_minimal_value(self, attr):
        v=self.ca[attr].min
        vm=self.ca[attr].max
        i=self.ca[attr].inc or 1
        while True:
            try:
                self.cav[attr]=v
                return v
            except AlliedVisionVimbaXLibError:
                if v>=vm:
                    raise
                v+=i
    @camera.acqcleared
    def set_roi(self, hstart=0, hend=None, vstart=0, vend=None):
        for a in ["Width","Height","OffsetX","OffsetY"]:
            if a in self.ca:
                self.ca[a].update_limits()
                if not self.ca[a].writable:
                    return self.get_roi()
        det_size=self.get_detector_size()
        if hend is None:
            hend=det_size[0]
        if vend is None:
            vend=det_size[1]
        self._set_minimal_value("Width")
        self._set_minimal_value("Height")
        self.cav["OffsetX"]=hstart
        self.cav["OffsetY"]=vstart
        self.cav["Width"]=max(self.cav["Width"],hend-hstart)
        self.cav["Height"]=max(self.cav["Height"],vend-vstart)
        return self.get_roi()
    def get_roi_limits(self, hbin=1, vbin=1):
        params=["Width","Height","OffsetX","OffsetY"]
        valp=tuple([(self.ca[p].get_value() if p in self.ca else 0) for p in params])
        minp=tuple([(self.ca[p].min if p in self.ca else 0) for p in params])
        maxp=tuple([(self.ca[p].max if p in self.ca else 0) for p in params])
        incp=tuple([(self.ca[p].inc if p in self.ca else 0) for p in params])
        hlim=camera.TAxisROILimit(minp[0] or maxp[0],maxp[0]+valp[2],incp[2] or maxp[0],incp[0] or maxp[0],1)
        vlim=camera.TAxisROILimit(minp[1],maxp[1],incp[3] or maxp[1],incp[1] or maxp[1],1)
        return hlim,vlim

    _exposure_time_properties=["ExposureTimeAbs","ExposureTime"]
    def get_exposure(self):
        for p in self._exposure_time_properties:
            exp=self.get_attribute_value(p,error_on_missing=False)
            if exp is not None:
                return exp/1E6  # in us by default
        bexp=self.get_attribute_value("ExposureTimeBaseAbs",error_on_missing=False)
        rexp=self.get_attribute_value("ExposureTimeRaw",error_on_missing=False)
        if bexp is not None and rexp is not None:
            return bexp*rexp/1E6
        raise AlliedVisionVimbaXError("camera does not support exposure")
    def set_exposure(self, exposure):
        for p in self._exposure_time_properties:
            if p in self.attributes:
                self.cav[p]=exposure*1E6
                return self.get_exposure()
        if "ExposureTimeBaseAbs" in self.attributes and "ExposureTimeRaw" in self.attributes:
            self.cav["ExposureTimeRaw"]=(exposure/self.cav["ExposureTimeBaseAbs"])*1E6
        else:
            raise AlliedVisionVimbaXError("camera does not support exposure")
        return self.get_exposure()
    def get_frame_period(self):
        fps=self.get_attribute_value("AcquisitionFrameRate",error_on_missing=False)
        if fps is not None:
            period=1./fps
            try:
                exposure=self.get_exposure()
                return max(exposure,period)
            except AlliedVisionVimbaXError:
                return period
        try:
            return self.get_exposure()
        except AlliedVisionVimbaXError:
            raise AlliedVisionVimbaXError("camera does not support frame period")
    def set_frame_period(self, frame_period):
        """Set frame period (time between two consecutive frames in the internal trigger mode)"""
        enable_period=frame_period>0
        if "AcquisitionFrameRate" in self.attributes:
            if "AcquisitionFrameRateEnable" in self.attributes:
                self.cav["AcquisitionFrameRateEnable"]=enable_period
            if enable_period:
                self.cav["AcquisitionFrameRate"]=1./frame_period if frame_period>0 else self.attributes["AcquisitionFrameRate"].max
        else:
            raise AlliedVisionVimbaXError("camera does not support frame period")
        return self.get_frame_period()
    def get_frame_timings(self):
        return self._TAcqTimings(self.get_exposure(),self.get_frame_period())

    class CallbackManager:
        def __init__(self, handle):
            self.handle=handle
            self.callback=get_callback()
            self._cfuncs=(ctypes.c_size_t*2)()
            self._cfuncs[0]=funcaddressof(lib.lib.VmbCaptureFrameQueue)
            self._cfuncs[1]=self.get_callback_ptr()
            self._cctl=(ctypes.c_size_t*3)(0)
            self._cstat=(ctypes.c_size_t*3)(0)
            self._cbuff=(ctypes.c_size_t*5)(0)
            self.frames=None
            self.commdata=as_ctypes_array([ctypes.addressof(c) for c in [self._cfuncs,self._cctl,self._cbuff,self._cstat]],ctypes.c_size_t)
        def get_callback_ptr(self):
            return self.callback
        def announce(self, buff):
            self.revoke()
            context=ctypes.addressof(self.commdata)
            self.frames=[lib.VmbFrameAnnounce(self.handle,buff.get_buffer(i),buff.size,context) for i in range(buff.nbuff)]
            self._cbuff[0]=buff.nbuff
            self._cbuff[1]=buff.size
            self._cbuff[2]=buff.fi_size
            self._cbuff[3]=buff.buff_ptr
            self._cbuff[4]=buff.fi_buff_ptr
        def revoke(self):
            if self.frames is None:
                return
            self.stop()
            lib.VmbFrameRevokeAll(self.handle)
            self.frames=[]
        def reset(self):
            self._cstat[:]=[0]*len(self._cstat)
            self._cctl[2]=0
        def start(self, acquire_frameinfo=True):
            self.stop()
            self.reset()
            for f in self.frames:
                lib.VmbCaptureFrameQueue(self.handle,ctypes.pointer(f),self.get_callback_ptr())
            self._cctl[1]=1 if acquire_frameinfo else 0
            self._cctl[0]=1
        def stop(self):
            self._cctl[0]=0
            lib.VmbCaptureQueueFlush(self.handle)
        def is_running(self):
            return bool(self._cctl[0])
        def get_stat(self):
            return tuple(int(v) for v in self._cstat)
        
    class BufferManager:
        """Buffer manager, which deals with buffer memory allocation, registering and deregistering, and retrieving the result and the leftovers"""
        _frame_info_size=6
        def __init__(self, size, nbuff):
            self.size=size
            self.fi_size=self._frame_info_size*8
            self.nbuff=nbuff
            self._full_buffer=ctypes.create_string_buffer(self.size*nbuff)
            self.buff_ptr=ctypes.addressof(self._full_buffer)
            self._full_fi_buffer=ctypes.create_string_buffer(self.fi_size*nbuff)
            self.fi_buff_ptr=ctypes.addressof(self._full_fi_buffer)
        def get_buffer(self, fidx):
            """Get buffer corresponding to the given frame index"""
            return self.buff_ptr+(fidx%self.nbuff)*self.size
        def get_frameinfo_buffer(self, fidx):
            """Get frame info buffer corresponding to the given frame index"""
            return self.fi_buff_ptr+(fidx%self.nbuff)*self.fi_size
    

    def _allocate_buffers(self, nbuff):
        self._deallocate_buffers()
        size=lib.VmbPayloadSizeGet(self.handle)
        # nbuff=min(nbuff,2**30//size)
        self._buffer_mgr=self.BufferManager(size,nbuff)
        return nbuff
    def _deallocate_buffers(self):
        if self._buffer_mgr is not None:
            self._buffer_mgr=None

    @interface.use_parameters(mode="acq_mode")
    def setup_acquisition(self, mode="sequence", nframes=100):  # pylint: disable=arguments-differ
        """
        Setup acquisition mode.

        `mode` can be either ``"snap"`` (single frame or a fixed number of frames) or ``"sequence"`` (continuous acquisition).
        `nframes` sets up number of frame buffers.
        """
        self.clear_acquisition()
        # self.set_attribute_value("AcquisitionMode","Continuous",error_on_missing=False)
        nframes=self._allocate_buffers(nbuff=nframes)
        self._cb_mgr.announce(self._buffer_mgr)
        super().setup_acquisition(mode=mode,nframes=nframes)
    def clear_acquisition(self):
        self.stop_acquisition()
        if self._buffer_mgr is not None:
            self._cb_mgr.revoke()
            self._deallocate_buffers()
        super().clear_acquisition()
    def start_acquisition(self, *args, **kwargs):
        self.stop_acquisition()
        if self._buffer_mgr is not None and lib.VmbPayloadSizeGet(self.handle)!=self._buffer_mgr.size:
            self.clear_acquisition()
        super().start_acquisition(*args,**kwargs)
        self._frame_counter.reset(self._acq_params["nframes"])
        self._cb_mgr.start()
        lib.VmbCaptureStart(self.handle)
        self.call_command("AcquisitionStart")
    def stop_acquisition(self):
        if self.acquisition_in_progress():
            self.call_command("AcquisitionStop")
            lib.VmbCaptureEnd(self.handle)
            self._cb_mgr.stop()
            self._frame_counter.update_acquired_frames(self._get_acquired_frames())
        super().stop_acquisition()
    def acquisition_in_progress(self):
        # return self._cb_mgr.is_running() and self.get_attribute_value("AcquisitionStatus",False)
        return self._cb_mgr.is_running()
    def _get_acquired_frames(self):
        return self._cb_mgr.get_stat()[0]

    def enable_raw_readout(self, enable="rows"):
        """
        Enable raw frame transfer.

        Should be used if the camera uses unsupported pixel format.
        Can be ``"frame"`` (return the whole frame as a 1D ``"u1"`` numpy array),
        ``"rows"`` (return a 2D array, where each row corresponds to a single image row),
        or ``False`` (convert to image data, or raise an error if the format is not supported; default)
        """
        funcargparse.check_parameter_range(enable,"enable",{False,"rows","frame"})
        self._raw_readout_format=enable

    def _parse_buffer(self, buff, size, shape, pixel_format, n=1):
        data=np.ctypeslib.as_array(ctypes.cast(buff,ctypes.POINTER(ctypes.c_ubyte)),shape=(n,size))
        if self._raw_readout_format=="frame":
            return data[:,None,:]
        if self._raw_readout_format=="rows":
            return data.reshape((n,shape[0],-1))
        supported_formats=["Mono8","Mono10","Mono12","Mono12p","Mono16","Mono32"]
        if pixel_format not in supported_formats:
            sf_string=", ".join(supported_formats)
            raise AlliedVisionVimbaXError("pixel format {} is not supported, only [{}] are supported; raw data readout can be enabled via enable_raw_readout method".format(pixel_format,sf_string))
        if pixel_format=="Mono8":
            return data.reshape((n,)+shape)
        elif pixel_format in ["Mono10","Mono12","Mono16"]:
            return data.view("<u2").reshape((n,)+shape)
        elif pixel_format =="Mono12p":
            return pf.convert_uint12(data.reshape(n,shape[0],-1),mode="little_endian",width=shape[1])
        else:
            return data.view("<u4").reshape((n,)+shape)
    def _parse_frame_info(self, idx, buff, n=1):
        camfi=np.ctypeslib.as_array(ctypes.cast(buff,ctypes.POINTER(ctypes.c_uint64)),shape=(n,self.BufferManager._frame_info_size))[:,[0,1,4,5]]
        return np.column_stack((np.arange(idx,idx+n,dtype=camfi.dtype),camfi))
    _support_chunks=True
    def _read_frames(self, rng, return_info=False):
        size=self._buffer_mgr.size
        shape=self.cav["Height"],self.cav["Width"]
        pixel_format=self.cav["PixelFormat"]
        nbuff=self._buffer_mgr.nbuff
        i0,i1=rng
        if (i1-1)//nbuff==i0//nbuff:
            chunks=[(i0,i1-i0)]
        else:
            cut=(i1//nbuff)*nbuff
            chunks=[(i0,cut-i0),(cut,i1-cut)]
        frames=[self._parse_buffer(self._buffer_mgr.get_buffer(b),size,shape,pixel_format,n=n) for b,n in chunks]
        if not self._raw_readout_format:
            frames=[self._convert_indexing(f,"rct",axes=(-2,-1)) for f in frames]
        frame_info=None
        if return_info:
            frame_info=[self._parse_frame_info(b,self._buffer_mgr.get_frameinfo_buffer(b),n=n) for b,n in chunks]
        return frames,frame_info