from pylablib.core.utils import funcargparse
from .SpinnakerC_defs import spinNodeType, spinVisibility, spinAccessMode, spinRepresentation  # pylint: disable=unused-import
from .SpinnakerC_lib import wlib as lib, TeledyneSpinnakerError, TeledyneSpinnakerLibError  # pylint: disable=unused-import

from ...core.utils import py3, dictionary
from ...core.devio import interface
from ..interface import camera
from ..utils import load_lib
from ...core.utils.ctypes_tools import funcaddressof, as_ctypes_array
from ...core.utils.cext_tools import try_import_cext
with try_import_cext():
    from .utils import get_callback  # pylint: disable=no-name-in-module

import numpy as np
import collections
import ctypes


class TeledyneSpinnakerTimeoutError(TeledyneSpinnakerError):
    "Teledyne Spinnaker frame timeout error"




class LibraryController(load_lib.LibraryController):
    def __init__(self, lib):  # pylint: disable=redefined-outer-name
        super().__init__(lib)
        self.h=None
    def _do_init(self):
        self.h=lib.spinSystemGetInstance()
    def _do_uninit(self):
        if self.h is not None:
            lib.spinSystemReleaseInstance(self.h)
            self.h=None
libctl=LibraryController(lib)
def restart_lib():
    libctl.shutdown()

def get_SDK_version():
    """Get version of Teledyne Spinnaker SDK"""
    with libctl.temp_open():
        return ".".join([str(v) for v in lib.spinSystemGetLibraryVersion(libctl.h)])



_camera_info_alias={"DeviceDisplayName":"name", "DeviceModelName":"model", "DeviceSerialNumber":"serial", "DeviceType":"devclass", "DeviceVersion":"devversion",
    "DeviceVendorName":"vendor","DeviceUserID":"user_name"}
TCameraInfo=collections.namedtuple("TCameraInfo",["name","model","serial","devclass","devversion","vendor","user_name"])
def _get_device_info(cam):
    """Get Spinnaker camera info for a camera with the given index"""
    nmap=None
    cam_info={v:None for v in _camera_info_alias.values()}
    try:
        nmap=lib.spinCameraGetTLDeviceNodeMap(cam)
        for n,a in _camera_info_alias.items():
            try:
                node=lib.spinNodeMapGetNode(nmap,n)
                cam_info[a]=py3.as_str(lib.spinNodeToString(node))
                lib.spinNodeMapReleaseNode(nmap,node)
            except TeledyneSpinnakerError:
                pass
    except TeledyneSpinnakerError:
        pass
    return TCameraInfo(**cam_info)
def _parse_camera_list(camlst):
    ndev=lib.spinCameraListGetSize(camlst)
    infos=[]
    for i in range(ndev):
        cam=None
        try:
            cam=lib.spinCameraListGet(camlst,i)
            infos.append(_get_device_info(cam))
        finally:
            if cam is not None:
                lib.spinCameraRelease(cam)
    return infos
def list_cameras(desc=True):
    """
    List all cameras available through Teledyne Spinnaker interface
    
    If ``desc==True``, return complete camera descriptions; otherwise, simply return the names.
    """
    with libctl.temp_open():
        camlst=lib.spinCameraListCreateEmpty()
        lib.spinSystemGetCameras(libctl.h,camlst)
        infos=_parse_camera_list(camlst)
        lib.spinCameraListClear(camlst)
        lib.spinCameraListDestroy(camlst)
        return infos if desc else [inf.name for inf in infos]
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
    """Get number of connected Teledyne Spinnaker cameras"""
    with libctl.temp_open():
        camlst=lib.spinCameraListCreateEmpty()
        lib.spinSystemGetCameras(libctl.h,camlst)
        ndev=lib.spinCameraListGetSize(camlst)
        lib.spinCameraListClear(camlst)
        lib.spinCameraListDestroy(camlst)
        return ndev

    

class TeledyneSpinnakerAttribute:
    """
    Object representing an Teledyne Spinnaker GenAPI attribute.

    Allows to query and set values and get additional information.
    Usually created automatically by an :class:`SpinnakerCamera` instance.

    Args:
        node: Spinnaker GenApi node handler
        full_name: if supplied, attribute's full name, including the tree structure

    Attributes:
        name: attribute name
        kind: attribute kind; can be ``"int"``, ``"float"``, ``"bool"``, ``"enum"``, ``"str"``, 
            ``"command"``, ``"category"``, or ``"unknown"``
        display_name: attribute display name (short description name)
        tooltip: longer attribute description
        description: full attribute description (usually, same as `tooltip`)
        visibility: attribute visibility; can be ``"simple"``, ``"intermediate"``, ``"advanced"``, ``"invisible"``, or ``"unknown"``
        access: attribute access level; can be ``"read_only"``, ``"write_only"``, ``"read_write"``,
            ``"na"`` (not applicable, e.g., command), or ``"not_implemented"``
        readable (bool): whether attribute is readable
        writable (bool): whether attribute is writable
        implemented (bool): whether the attribute is implemented in the given camera (normally always ``True``)
        available (bool): whether the attribute can be changed or called
        min (float or int): minimal attribute value (if applicable)
        max (float or int): maximal attribute value (if applicable)
        inc (float or int): minimal attribute increment value (if applicable)
        units: attribute units (if applicable)
        repr: shows what a numerical unit represents; can be ``"lin"``, ``"log"``, ``"bool"``, ``"pure"``, ``"hex"``, or ``"unknown"``
        ivalues: list of possible integer values for enum attributes
        values: list of possible text values for enum attributes
        labels: dict ``{label: index}`` which shows all possible values of an enumerated attribute and their corresponding numerical values
        ilabels: dict ``{index: label}`` which shows labels corresponding to numerical values of an enumerated attribute
    """
    _attr_types={   spinNodeType.IntegerNode:"int",
                    spinNodeType.FloatNode:"float",
                    spinNodeType.BooleanNode:"bool",
                    spinNodeType.EnumerationNode:"enum",
                    spinNodeType.StringNode:"str",
                    spinNodeType.CommandNode:"command",
                    spinNodeType.CategoryNode:"category",
                    spinNodeType.UnknownNode:"unknown"}
    _vis_types={    spinVisibility.Beginner:"simple",
                    spinVisibility.Expert:"intermediate",
                    spinVisibility.Guru:"advanced",
                    spinVisibility.Invisible:"invisible",
                    spinVisibility._UndefinedVisibility:"unknown"}
    _acc_types={    spinAccessMode.RO:"read_only",
                    spinAccessMode.WO:"write_only",
                    spinAccessMode.RW:"read_write",
                    spinAccessMode.NA:"na",
                    spinAccessMode.NI:"not_implemented",
                    spinAccessMode._UndefinedAccesMode:"unknown"}
    _repr_type={    spinRepresentation.Linear:"lin",
                    spinRepresentation.Logarithmic:"log",
                    spinRepresentation.Boolean:"bool",
                    spinRepresentation.PureNumber:"pure",
                    spinRepresentation.HexNumber:"hex",
                    spinRepresentation.IPV4Address:"ipv4",
                    spinRepresentation.MACAddress:"mac",
                    spinRepresentation._UndefinedRepresentation:"unknown"}
    def __init__(self, node, full_name=None):
        self.node=node
        self.name=py3.as_str(lib.spinNodeGetName(node))
        self.full_name=full_name or self.name
        self.kind=self._attr_types.get(lib.spinNodeGetType(node),"unknown")
        self.display_name=py3.as_str(lib.spinNodeGetDisplayName(node))
        self.tooltip=py3.as_str(lib.spinNodeGetToolTip(node))
        self.description=py3.as_str(lib.spinNodeGetDescription(node))
        self.visibility=self._vis_types[lib.spinNodeGetVisibility(node)]
        self.access=self._acc_types[lib.spinNodeGetAccessMode(node)]
        self.implemented=bool(lib.spinNodeIsImplemented(node))
        self.available=bool(lib.spinNodeIsAvailable(node))
        self.readable=bool(lib.spinNodeIsReadable(node))
        self.writable=bool(lib.spinNodeIsWritable(node))
        self.units=None
        self.min=None
        self.max=None
        self.inc=None
        self.repr=None
        self._value_nodes=None
        self.values=[]
        self.ivalues=[]
        self.labels={}
        self.ilabels={}
        self._fill_info()
    
    def _fill_info(self):
        if self.kind=="int":
            self.repr=self._repr_type[lib.spinIntegerGetRepresentation(self.node)]
        elif self.kind=="float":
            self.repr=self._repr_type[lib.spinFloatGetRepresentation(self.node)]
            self.units=py3.as_str(lib.spinFloatGetUnit(self.node))
        elif self.kind=="enum":
            nenum=lib.spinEnumerationGetNumEntries(self.node)
            self._value_nodes=[lib.spinEnumerationGetEntryByIndex(self.node,i) for i in range(nenum)]
        self.update_limits()
    def _update_attributes(self):
        self.access=self._acc_types[lib.spinNodeGetAccessMode(self.node)]
        self.available=bool(lib.spinNodeIsAvailable(self.node))
        self.readable=bool(lib.spinNodeIsReadable(self.node))
        self.writable=bool(lib.spinNodeIsWritable(self.node))
    def update_limits(self):
        """Update minimal and maximal attribute limits and return tuple ``(min, max, inc)``"""
        self._update_attributes()
        if self.kind=="int":
            try:
                self.min=lib.spinIntegerGetMin(self.node)
            except TeledyneSpinnakerLibError:
                self.min=None
            try:
                self.max=lib.spinIntegerGetMax(self.node)
            except TeledyneSpinnakerLibError:
                self.max=None
            try:
                self.inc=lib.spinIntegerGetInc(self.node)
            except TeledyneSpinnakerLibError:
                self.inc=None
            return (self.min,self.max,self.inc)
        elif self.kind=="float":
            try:
                self.min=lib.spinFloatGetMin(self.node)
            except TeledyneSpinnakerLibError:
                self.min=None
            try:
                self.max=lib.spinFloatGetMax(self.node)
            except TeledyneSpinnakerLibError:
                self.max=None
            return (self.min,self.max,self.inc)
        elif self.kind=="enum":
            self.values=[py3.as_str(lib.spinEnumerationEntryGetSymbolic(n)) for n in self._value_nodes]
            self.ivalues=[lib.spinEnumerationEntryGetIntValue(n) for n in self._value_nodes]
            self.labels=dict(zip(self.values,self.ivalues))
            self.ilabels=dict(zip(self.ivalues,self.values))
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

    def get_value(self, enum_as_str=True):
        """
        Get attribute value.
        
        If ``enum_as_str==True``, return enum-style values as strings; otherwise, return corresponding integer values.
        """
        if self.kind=="command":
            return bool(lib.spinCommandIsDone(self.node))
        self._update_attributes()
        if not self.readable:
            raise TeledyneSpinnakerError("attribute {} is not readable".format(self.name))
        if self.kind=="int":
            return lib.spinIntegerGetValue(self.node)
        if self.kind=="float":
            return lib.spinFloatGetValue(self.node)
        if self.kind=="bool":
            return lib.spinBooleanGetValue(self.node)
        if self.kind=="str":
            return py3.as_str(lib.spinNodeToString(self.node))
        if self.kind=="enum":
            value=py3.as_str(lib.spinNodeToString(self.node))
            if not enum_as_str:
                value=self.labels[value]
            return value
        if self.kind=="unknown":
            return None
        raise TeledyneSpinnakerError("attribute {} of kind {} can not be read".format(self.name,self.kind))
    def set_value(self, value, truncate=True):
        """
        Set attribute value.
        
        If ``truncate==True``, automatically truncate value to lie within allowed range.
        """
        self._update_attributes()
        if not self.writable:
            raise TeledyneSpinnakerError("attribute {} is not writable".format(self.name))
        if truncate:
            value=self.truncate_value(value)
        if self.kind=="int":
            lib.spinIntegerSetValue(self.node,int(value))
        elif self.kind=="float":
            lib.spinFloatSetValue(self.node,float(value))
        elif self.kind=="bool":
            lib.spinBooleanSetValue(self.node,bool(value))
        elif self.kind=="str":
            lib.spinNodeFromString(self.node,str(value))
        elif self.kind=="enum":
            value=self.ilabels.get(value,value)
            lib.spinNodeFromString(self.node,str(value))
        elif self.kind!="unknown":
            raise TeledyneSpinnakerError("attribute {} of kind {} can not be set".format(self.name,self.kind))
    def call_command(self):
        """Execute the given command"""
        if self.kind=="command":
            if not self.implemented:
                raise TeledyneSpinnakerError("command is not implemented: {}".format(self.name))
            lib.spinCommandExecute(self.node)
        else:
            raise TeledyneSpinnakerError("attribute {} is not a command".format(self.name))

    def __repr__(self):
        return "{}(name='{}', kind='{}')".format(self.__class__.__name__,self.name,self.kind)







TDeviceInfo=collections.namedtuple("TDeviceInfo",TCameraInfo._fields)
TMissedFramesStatus=collections.namedtuple("TMissedFramesStatus",["stream_dropped","queue_overflows","unprocessed"])
TFrameInfo=collections.namedtuple("TFrameInfo",["frame_index","framestamp","timestamp"])
class TeledyneSpinnakerCamera(camera.IROICamera, camera.IAttributeCamera, camera.IExposureCamera):
    """
    Generic Teledyne Spinnaker camera interface.

    Args:
        idx: camera index among the cameras listed using :func:`list_cameras`
        name: camera name; if specified, then `idx` is ignored and the camera is determined based on the provided name
        serial: camera serial number; if specified, then `idx` and `name` is ignored and the camera is determined based on the provided serial number
    """
    Error=TeledyneSpinnakerError
    TimeoutError=TeledyneSpinnakerTimeoutError
    _TFrameInfo=TFrameInfo
    def __init__(self, idx=0, name=None, serial=None):
        super().__init__()
        lib.initlib()
        self.idx=idx
        self.name=name
        self.serial=serial
        self.hdev=None
        self._camlst=None
        self._cb_mgr=self.CallbackManager()
        self._buffer_mgr=None
        self._start_queue_overflows=0
        self.open()
        self._raw_readout_format=False
        self._add_info_variable("device_info",self.get_device_info)
        self._add_settings_variable("exposure",self.get_exposure,self.set_exposure,ignore_error=TeledyneSpinnakerError)
        self._update_device_variable_order("exposure")
        self._add_settings_variable("frame_period",self.get_frame_period,self.set_frame_period,ignore_error=TeledyneSpinnakerError)
        self._add_status_variable("missed_frames",self.get_missed_frames_status)
        self._update_queue_overflows()


    def _get_connection_parameters(self):
        return (self.idx,self.name,self.serial)
    def open(self):
        """Open connection to the camera"""
        if self.hdev is not None:
            return
        with libctl.temp_open():
            camlst=lib.spinCameraListCreateEmpty()
            lib.spinSystemGetCameras(libctl.h,camlst)
            self._camlst=camlst
            try:
                cams=_parse_camera_list(camlst)
                if self.name is not None or self.serial is not None:
                    use_serial=self.serial is not None
                    spar={"serial":self.serial} if use_serial else {"name":self.name}
                    idx=_find_camera(cams,**spar)
                    if idx is None:
                        kind,par=list(spar.items())[0]
                        camsstr=", ".join(["'{}'".format(c.serial if use_serial else c.cam) for c in cams])
                        raise TeledyneSpinnakerError("could not find camera with {} {}; available cameras are {}".format(kind,par,camsstr))
                else:
                    idx=self.idx
                if idx>=len(cams):
                    raise TeledyneSpinnakerError("camera index {} is not available ({} cameras exist)".format(idx,len(cams)))
                with self._close_on_error():
                    self.hdev=lib.spinCameraListGet(camlst,idx)
                    lib.spinCameraInit(self.hdev)
                    self._opid=libctl.open().opid
                    self._update_attributes()
                    self.post_open()
            except TeledyneSpinnakerError:
                self._close_camlst()
                raise
    def _close_camlst(self):
        try:
            lib.spinCameraListClear(self._camlst)
            lib.spinCameraListDestroy(self._camlst)
        finally:
            self._camlst=None
    def close(self):
        """Close connection to the camera"""
        if self.hdev is not None:
            try:
                self.clear_acquisition()
                self._cb_mgr.destroy()
            finally:
                try:
                    lib.spinCameraDeInit(self.hdev)
                    lib.spinCameraRelease(self.hdev)
                    self._close_camlst()
                finally:
                    self.hdev=None
                    libctl.close(self._opid)
                    self._opid=None
    def is_opened(self):
        return (self.hdev is not None) and bool(lib.spinCameraIsInitialized(self.hdev))

    def post_open(self):
        """Additional setup after camera opening"""

    _builtin_attrs=["OffsetX","OffsetY","Width","Height","PixelFormat","PayloadSize"]
    def _get_attribute_path(self, a):
        return a.full_name
    def _get_map_nodes(self, nmap, rn="Root", full_name=False, pfx=""):
        root=lib.spinNodeMapGetNode(nmap,rn)
        nodes=lib.collect_nodes(root,add_branch=True)
        nodes={(n[5:] if n.startswith(rn+"/") else n):v for n,v in nodes.items()}
        return [TeledyneSpinnakerAttribute(node,full_name=n if full_name else pfx+py3.as_str(lib.spinNodeGetName(node))) for n,node in nodes.items()]
    def _list_attributes(self):
        camnmap=lib.spinCameraGetNodeMap(self.hdev)
        attrs=self._get_map_nodes(camnmap)
        attrs+=self._get_map_nodes(lib.spinCameraGetTLStreamNodeMap(self.hdev),pfx="TLStream/")
        for n in self._builtin_attrs:
            node=lib.spinNodeMapGetNode(camnmap,n)
            if node:
                attrs.append(TeledyneSpinnakerAttribute(node,full_name=n))
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
                except TeledyneSpinnakerError:  # sometimes nominally implemented features still raise errors
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
        return TCameraInfo(*_get_device_info(self.hdev))

    def _get_data_dimensions_rc(self):
        return self.cav["Height"],self.cav["Width"]
    def get_detector_size(self):
        return self.ca["Width"].max,self.ca["Height"].max
    def get_roi(self):
        ox=self.get_attribute_value("OffsetX",default=0)
        oy=self.get_attribute_value("OffsetY",default=0)
        w=self.cav["Width"]
        h=self.cav["Height"]
        return ox,ox+w,oy,oy+h
    @camera.acqcleared
    def set_roi(self, hstart=0, hend=None, vstart=0, vend=None):
        for a in ["Width","Height","OffsetX","OffsetY"]:
            if a in self.ca:
                self.ca[a].update_limits()
                if self.ca[a].writable:
                    continue
                return self.get_roi()
        det_size=self.get_detector_size()
        if hend is None:
            hend=det_size[0]
        if vend is None:
            vend=det_size[1]
        self.cav["Width"]=self.ca["Width"].min
        self.cav["Height"]=self.ca["Height"].min
        self.cav["OffsetX"]=hstart
        self.cav["OffsetY"]=vstart
        self.cav["Width"]=max(self.cav["Width"],hend-hstart)
        self.cav["Height"]=max(self.cav["Height"],vend-vstart)
        return self.get_roi()
    def get_roi_limits(self, hbin=1, vbin=1):
        params=["Width","Height","OffsetX","OffsetY"]
        minp=tuple([(self.ca[p].min if p in self.ca else 0) for p in params])
        maxp=tuple([(self.ca[p].max if p in self.ca else 0) for p in params])
        incp=tuple([(self.ca[p].inc if p in self.ca else 0) for p in params])
        hlim=camera.TAxisROILimit(minp[0] or maxp[0],maxp[0],incp[2] or maxp[0],incp[0] or maxp[0],1)
        vlim=camera.TAxisROILimit(minp[1] or maxp[1],maxp[1],incp[3] or maxp[1],incp[1] or maxp[1],1)
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
        raise TeledyneSpinnakerError("camera does not support exposure")
    def set_exposure(self, exposure):
        for p in self._exposure_time_properties:
            if p in self.attributes:
                self.cav[p]=exposure*1E6
                return self.get_exposure()
        if "ExposureTimeBaseAbs" in self.attributes and "ExposureTimeRaw" in self.attributes:
            self.cav["ExposureTimeRaw"]=(exposure/self.cav["ExposureTimeBaseAbs"])*1E6
        else:
            raise TeledyneSpinnakerError("camera does not support exposure")
        return self.get_exposure()
    def get_frame_period(self):
        fps=self.get_attribute_value("AcquisitionResultingFrameRate",error_on_missing=False)
        if fps is not None:
            period=1./fps
            try:
                exposure=self.get_exposure()
                return max(exposure,period)
            except TeledyneSpinnakerError:
                return period
        try:
            return self.get_exposure()
        except TeledyneSpinnakerError:
            raise TeledyneSpinnakerError("camera does not support frame period")
    def set_frame_period(self, frame_period):
        """Set frame period (time between two consecutive frames in the internal trigger mode)"""
        if "AcquisitionFrameRate" in self.attributes:
            self.cav["AcquisitionFrameRate"]=1./frame_period if frame_period>0 else self.attributes["AcquisitionFrameRate"].max
            if "AcquisitionFrameRateEnable" in self.attributes:
                self.cav["AcquisitionFrameRateEnable"]=frame_period>0
        else:
            raise TeledyneSpinnakerError("camera does not support frame period")
        return self.get_frame_period()
    def get_frame_timings(self):
        return self._TAcqTimings(self.get_exposure(),self.get_frame_period())

    class CallbackManager:
        def __init__(self):
            self._cfuncs=(ctypes.c_size_t*7)()
            self._cfuncs[0]=funcaddressof(lib.lib.spinImageIsIncomplete)
            self._cfuncs[1]=funcaddressof(lib.lib.spinImageGetSize)
            self._cfuncs[2]=funcaddressof(lib.lib.spinImageGetWidth)
            self._cfuncs[3]=funcaddressof(lib.lib.spinImageGetHeight)
            self._cfuncs[4]=funcaddressof(lib.lib.spinImageGetData)
            self._cfuncs[5]=funcaddressof(lib.lib.spinImageGetFrameID)
            self._cfuncs[6]=funcaddressof(lib.lib.spinImageGetTimeStamp)
            self._cctl=(ctypes.c_size_t*3)(0)
            self._cstat=(ctypes.c_size_t*3)(0)
            self._cbuff=(ctypes.c_size_t*4)(0)
            self.commdata=as_ctypes_array([ctypes.addressof(c) for c in [self._cfuncs,self._cctl,self._cbuff,self._cstat]],ctypes.c_size_t)
            self.callback=get_callback()
            self.hcb=None
            self._reg_hdev=None
        def get_callback_ptr(self):
            return self.callback.address
        def create(self, force=False):
            if force:
                self.destroy()
            if self.hcb is None:
                self.hcb=lib.spinImageEventHandlerCreate(self.callback,ctypes.addressof(self.commdata))
        def destroy(self):
            if self.hcb is not None:
                self.unregister()
                try:
                    lib.spinImageEventHandlerDestroy(self.hcb)
                finally:
                    self.hcb=None
        def register(self, hdev, buff):
            self.reset()
            self._cbuff[0]=buff.nbuff
            self._cbuff[1]=buff.size
            self._cbuff[2]=buff.buff_ptr
            self._cbuff[3]=buff.fi_buff_ptr
            self.start()
            if self._reg_hdev is None:
                self.create()
                lib.spinCameraRegisterImageEventHandler(hdev,self.hcb)
                self._reg_hdev=hdev
        def unregister(self):
            if self._reg_hdev is not None:
                try:
                    lib.spinCameraUnregisterImageEventHandler(self._reg_hdev,self.hcb)
                finally:
                    self._reg_hdev=None
                    self._cbuff[:]=[0]*len(self._cbuff)
        def reset(self):
            self._cstat[:]=[0]*len(self._cstat)
            self._cctl[2]=0
        def start(self, acquire_frameinfo=True):
            self.reset()
            self._cctl[1]=1 if acquire_frameinfo else 0
            self._cctl[0]=1
        def stop(self):
            self._cctl[0]=0
        def get_stat(self):
            return tuple(int(v) for v in self._cstat)
        
    class BufferManager:
        """Buffer manager, which deals with buffer memory allocation, registering and deregistering, and retrieving the result and the leftovers"""
        def __init__(self, size, nbuff):
            self.size=size
            self.fi_size=2*8
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
        size=self.cav["PayloadSize"]
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
        self.set_attribute_value("AcquisitionMode","Continuous",error_on_missing=False)
        nframes=self._allocate_buffers(nbuff=nframes)
        self._cb_mgr.register(self.hdev,self._buffer_mgr)
        super().setup_acquisition(mode=mode,nframes=nframes)
    def clear_acquisition(self):
        self.stop_acquisition()
        if self._buffer_mgr is not None:
            self._cb_mgr.unregister()
            self._deallocate_buffers()
        super().clear_acquisition()
    def start_acquisition(self, *args, **kwargs):
        self.stop_acquisition()
        self._update_queue_overflows()
        super().start_acquisition(*args,**kwargs)
        self._frame_counter.reset(self._acq_params["nframes"])
        self._cb_mgr.start()
        lib.spinCameraBeginAcquisition(self.hdev)
    def stop_acquisition(self):
        if self.acquisition_in_progress():
            lib.spinCameraEndAcquisition(self.hdev)
            self._cb_mgr.stop()
            self._frame_counter.update_acquired_frames(self._get_acquired_frames())
        super().stop_acquisition()
    def acquisition_in_progress(self):
        return bool(lib.spinCameraIsStreaming(self.hdev))
    def _get_acquired_frames(self):
        return self._cb_mgr.get_stat()[0]
    def _update_queue_overflows(self):
        self._start_queue_overflows=self.get_attribute_value("TransferQueueOverflowCount",error_on_missing=False,default=0)
    def get_missed_frames_status(self):
        """
        Get missed frames status.

        Return tuple ``(stream_dropped, queue_overflows, unprocessed)`` with the number of frames dropped in the stream, the number of frames
        lost due to the PC queue overflow (not processed fast enough) and the number of frames which could not be processed (incomplete or wrong size).
        """
        stream_dropped=self.get_attribute_value("TLStream/StreamDroppedFrameCount",error_on_missing=False,default=0)
        queue_overflows=self.get_attribute_value("TransferQueueOverflowCount",error_on_missing=False,default=0)-self._start_queue_overflows
        fstat=self._cb_mgr.get_stat()
        unprocessed=fstat[1]+fstat[2]
        return TMissedFramesStatus(stream_dropped,queue_overflows,unprocessed)

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
        supported_formats=["Mono8","Mono10","Mono12","Mono16","Mono32"]
        if pixel_format not in supported_formats:
            sf_string=", ".join(supported_formats)
            raise TeledyneSpinnakerError("pixel format {} is not supported, only [{}] are supported; raw data readout can be enabled via enable_raw_readout method".format(pixel_format,sf_string))
        if pixel_format=="Mono8":
            return data.reshape((n,)+shape)
        elif pixel_format in ["Mono10","Mono12","Mono16"]:
            return data.view("<u2").reshape((n,)+shape)
        else:
            return data.view("<u4").reshape((n,)+shape)
    def _parse_frame_info(self, idx, buff, n=1):
        camfi=np.ctypeslib.as_array(ctypes.cast(buff,ctypes.POINTER(ctypes.c_uint64)),shape=(n,2))
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