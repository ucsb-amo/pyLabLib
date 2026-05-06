from .peak_backend_defs import PEAK_NODE_TYPE_t, PEAK_NODE_VISIBILITY_t, PEAK_NODE_NAMESPACE_t, PEAK_NODE_CACHING_MODE_t, PEAK_NODE_ACCESS_STATUS_t, PEAK_NODE_REPRESENTATION_t, PEAK_NODE_INCREMENT_TYPE_t
from .peak_backend_defs import PEAK_NODE_CACHE_USE_POLICY_t
from .peak_backend_defs import PEAK_DEVICE_ACCESS_TYPE_t, PEAK_ACQUISITION_START_MODE_t, PEAK_ACQUISITION_STOP_MODE_t, PEAK_DATA_STREAM_FLUSH_MODE_t
from .peak_backend_lib import wlib as lib, IDSPeakError, IDSPeakLibError  # pylint: disable=unused-import

from ...core.utils import py3, dictionary, general as general_utils, funcargparse
from ...core.devio import interface as devio_interface
from ...core.utils.ctypes_tools import funcaddressof
from ..utils import load_lib, pixel_format as pf
from ..interface import camera
from .utils import looper  # pylint: disable=no-name-in-module

import numpy as np
import ctypes
import collections
import threading


class IDSPeakTimeoutError(IDSPeakError):
    "IDS peak frame timeout error"




class LibraryController(load_lib.LibraryController):
    def _do_init(self):
        self.lib.PEAK_Library_Initialize()
    def _do_uninit(self):
        self.lib.PEAK_Library_Close()
libctl=LibraryController(lib)
        



class GenericIDSPeakAttribute:
    """
    Object representing an IDS peak attribute (node).

    Args:
        handle: node handle

    Attributes:
        name: attribute name
        kind: attribute kind; can be ``"u32"``, ``"i64"``, ``"f64"``, ``"str"``, ``"enum"``,
            ``"bool"``, ``"command"``, or ``"blob"``
        display_name: attribute display name (short description name)
        tooltip: longer attribute description
        description: full attribute description (usually, same as `tooltip`)
        units: attribute units (if applicable)
        visibility: attribute visibility (``"simple"``, ``"intermediate"``, or ``"advanced"``)
        readable (bool): whether attribute is readable
        writable (bool): whether attribute is writable
        min (float or int): minimal attribute value (if applicable)
        max (float or int): maximal attribute value (if applicable)
        inc (float or int): minimal attribute increment value (if applicable)
        ivalues: list of possible integer values for enum attributes
        values: list of possible text values for enum attributes
        labels: dict ``{label: index}`` which shows all possible values of an enumerated attribute and their corresponding numerical values
        ilabels: dict ``{index: label}`` which shows labels corresponding to numerical values of an enumerated attribute
    """
    _attr_types={   PEAK_NODE_TYPE_t.PEAK_NODE_TYPE_INTEGER:"int",
                    PEAK_NODE_TYPE_t.PEAK_NODE_TYPE_BOOLEAN:"bool",
                    PEAK_NODE_TYPE_t.PEAK_NODE_TYPE_FLOAT:"float",
                    PEAK_NODE_TYPE_t.PEAK_NODE_TYPE_STRING:"str",
                    PEAK_NODE_TYPE_t.PEAK_NODE_TYPE_ENUMERATION:"enum",
                    PEAK_NODE_TYPE_t.PEAK_NODE_TYPE_ENUMERATION_ENTRY:"enum_entry",
                    PEAK_NODE_TYPE_t.PEAK_NODE_TYPE_REGISTER:"reg",
                    PEAK_NODE_TYPE_t.PEAK_NODE_TYPE_COMMAND:"command",
                    PEAK_NODE_TYPE_t.PEAK_NODE_TYPE_CATEGORY:"category"}
    _vis_types={    PEAK_NODE_VISIBILITY_t.PEAK_NODE_VISIBILITY_BEGINNER:"simple",
                    PEAK_NODE_VISIBILITY_t.PEAK_NODE_VISIBILITY_EXPERT:"intermediate",
                    PEAK_NODE_VISIBILITY_t.PEAK_NODE_VISIBILITY_GURU:"advanced",
                    PEAK_NODE_VISIBILITY_t.PEAK_NODE_VISIBILITY_INVISIBLE:"invisible"}
    _namespace_types={PEAK_NODE_NAMESPACE_t.PEAK_NODE_NAMESPACE_STANDARD:"standard",
                    PEAK_NODE_NAMESPACE_t.PEAK_NODE_NAMESPACE_CUSTOM:"custom"}
    _cache_mode_types={PEAK_NODE_CACHING_MODE_t.PEAK_NODE_CACHING_MODE_NO_CACHE:"none",
                    PEAK_NODE_CACHING_MODE_t.PEAK_NODE_CACHING_MODE_WRITE_AROUND:"write_around",
                    PEAK_NODE_CACHING_MODE_t.PEAK_NODE_CACHING_MODE_WRITE_THROUGH:"write_through"}
    _access_status_types={PEAK_NODE_ACCESS_STATUS_t.PEAK_NODE_ACCESS_STATUS_NOT_IMPLEMENTED:"not_implemented",
                    PEAK_NODE_ACCESS_STATUS_t.PEAK_NODE_ACCESS_STATUS_NOT_AVAILABLE:"not_available",
                    PEAK_NODE_ACCESS_STATUS_t.PEAK_NODE_ACCESS_STATUS_WRITE_ONLY:"write_only",
                    PEAK_NODE_ACCESS_STATUS_t.PEAK_NODE_ACCESS_STATUS_READ_ONLY:"read_only",
                    PEAK_NODE_ACCESS_STATUS_t.PEAK_NODE_ACCESS_STATUS_READ_WRITE:"read_write"}
    _repr_types={PEAK_NODE_REPRESENTATION_t.PEAK_NODE_REPRESENTATION_LINEAR:"linear",
                    PEAK_NODE_REPRESENTATION_t.PEAK_NODE_REPRESENTATION_LOGARITHMIC:"log",
                    PEAK_NODE_REPRESENTATION_t.PEAK_NODE_REPRESENTATION_BOOLEAN:"bool",
                    PEAK_NODE_REPRESENTATION_t.PEAK_NODE_REPRESENTATION_PURE_NUMBER:"pure",
                    PEAK_NODE_REPRESENTATION_t.PEAK_NODE_REPRESENTATION_HEX_NUMBER:"hex",
                    PEAK_NODE_REPRESENTATION_t.PEAK_NODE_REPRESENTATION_IP4_ADDRESS:"ip4",
                    PEAK_NODE_REPRESENTATION_t.PEAK_NODE_REPRESENTATION_MAC_ADDRESS:"mac"}
    _inc_types={PEAK_NODE_INCREMENT_TYPE_t.PEAK_NODE_INCREMENT_TYPE_NO_INCREMENT:"none",
                    PEAK_NODE_INCREMENT_TYPE_t.PEAK_NODE_INCREMENT_TYPE_FIXED_INCREMENT:"fixed",
                    PEAK_NODE_INCREMENT_TYPE_t.PEAK_NODE_INCREMENT_TYPE_LIST_INCREMENT:"list"}
    def __init__(self, handle):
        self.handle=handle
        self.name=py3.as_str(lib.PEAK_Node_GetName(self.handle))
        self.kind=self._attr_types.get(lib.PEAK_Node_GetType(self.handle),None)
        self.display_name=py3.as_str(lib.PEAK_Node_GetDisplayName(self.handle))
        self.tooltip=py3.as_str(lib.PEAK_Node_GetToolTip(self.handle))
        self.description=py3.as_str(lib.PEAK_Node_GetDescription(self.handle))
        self.visibility=self._vis_types.get(lib.PEAK_Node_GetVisibility(self.handle),None)
        self.access_status=self._access_status_types.get(lib.PEAK_Node_GetAccessStatus(self.handle),None)
        self.readable=self.access_status in ["read_only","read_write"]
        self.writable=self.access_status in ["write_only","read_write"]
        self.implemented=self.access_status!="not_implemented"
        self.available=self.access_status in ["write_only","read_only","read_write"]
        self.cacheable=bool(lib.PEAK_Node_GetIsCacheable(self.handle))
        self.cache_mode=self._cache_mode_types.get(lib.PEAK_Node_GetCachingMode(self.handle),None)
        self.access_status_cacheable=bool(lib.PEAK_Node_GetIsAccessStatusCacheable(self.handle))
        self.is_feature=bool(lib.PEAK_Node_GetIsFeature(self.handle))
        self.deprecated=bool(lib.PEAK_Node_GetIsDeprecated(self.handle))
        self.streamable=bool(lib.PEAK_Node_GetIsStreamable(self.handle))
        self.namespace=self._namespace_types.get(lib.PEAK_Node_GetNamespace(self.handle),None)
        self.polling_time=lib.PEAK_Node_GetPollingTime(self.handle)*1E-3
        self._vhandle=None
        if self.kind=="int":
            self._vhandle=lib.PEAK_Node_ToIntegerNode(self.handle)
        elif self.kind=="bool":
            self._vhandle=lib.PEAK_Node_ToBooleanNode(self.handle)
        elif self.kind=="float":
            self._vhandle=lib.PEAK_Node_ToFloatNode(self.handle)
        elif self.kind=="str":
            self._vhandle=lib.PEAK_Node_ToStringNode(self.handle)
        elif self.kind=="enum":
            self._vhandle=lib.PEAK_Node_ToEnumerationNode(self.handle)
        self._chandle=None
        if self.kind=="command":
            self._chandle=lib.PEAK_Node_ToCommandNode(self.handle)
        self.update_limits()
    def update_limits(self):
        """Update limits for value attributes"""
        self.min=None
        self.max=None
        self.inc=None
        self.inc_type=None
        self.inc_const=None
        self.unit=None
        self.vrepr=None
        self.values=[]
        self.ivalues=[]
        self.labels={}
        self.ilabels={}
        if self._vhandle is None or not self.available:
            return
        if self.kind=="int":
            self.min=lib.PEAK_IntegerNode_GetMinimum(self._vhandle)
            self.max=lib.PEAK_IntegerNode_GetMaximum(self._vhandle)
            self.inc_type=self._inc_types.get(lib.PEAK_IntegerNode_GetIncrementType(self._vhandle),None)
            self.inc=lib.PEAK_IntegerNode_GetIncrement(self._vhandle) if self.inc_type=="fixed" else None
            self.unit=lib.PEAK_IntegerNode_GetUnit(self._vhandle)
            self.vrepr=lib.PEAK_IntegerNode_GetRepresentation(self._vhandle)
            return self.min,self.max,self.inc
        elif self.kind=="float":
            self.min=lib.PEAK_FloatNode_GetMinimum(self._vhandle)
            self.max=lib.PEAK_FloatNode_GetMaximum(self._vhandle)
            self.inc_type=self._inc_types.get(lib.PEAK_FloatNode_GetIncrementType(self._vhandle),None)
            self.inc=lib.PEAK_FloatNode_GetIncrement(self._vhandle) if self.inc_type=="fixed" else None
            self.inc_const=bool(lib.PEAK_FloatNode_GetHasConstantIncrement(self._vhandle))
            self.unit=lib.PEAK_FloatNode_GetUnit(self._vhandle)
            self.vrepr=lib.PEAK_FloatNode_GetRepresentation(self._vhandle)
            return self.min,self.max,self.inc
        elif self.kind=="enum":
            enum=lib.PEAK_EnumerationNode_GetNumEntries(self._vhandle)
            eevs=[lib.PEAK_EnumerationNode_GetEntry(self._vhandle,i) for i in range(enum)]
            self.values=[py3.as_str(lib.PEAK_EnumerationEntryNode_GetSymbolicValue(ev)) for ev in eevs]
            self.ivalues=[lib.PEAK_EnumerationEntryNode_GetValue(ev) for ev in eevs]
            self.labels=dict(zip(self.values,self.ivalues))
            self.ilabels=dict(zip(self.ivalues,self.values))
            return self.ilabels
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
    def get_value(self, enum_as_str=True, use_cache=True, ignore_errors=False):
        """
        Get attribute value.
        
        If ``enum_as_str==True``, return enum-style values as strings; otherwise, return corresponding integer values.
        """
        if ignore_errors:
            try:
                return self.get_value(enum_as_str=enum_as_str,use_cache=use_cache)
            except IDSPeakError:
                return None
        if not self.readable:
            raise IDSPeakError("attribute {} ({}) is not readable".format(self.name,self.kind))
        if self.kind=="command":
            return bool(lib.PEAK_CommandNode_GetIsDone(self._chandle))
        if self._vhandle is None:
            raise IDSPeakError("attribute {} with kind {} does not have values".format(self.name,self.kind))
        cache_policy=PEAK_NODE_CACHE_USE_POLICY_t.PEAK_NODE_CACHE_USE_POLICY_USE_CACHE if use_cache else PEAK_NODE_CACHE_USE_POLICY_t.PEAK_NODE_CACHE_USE_POLICY_IGNORE_CACHE
        if self.kind=="int":
            return lib.PEAK_IntegerNode_GetValue(self._vhandle,cache_policy)
        if self.kind=="bool":
            return bool(lib.PEAK_BooleanNode_GetValue(self._vhandle,cache_policy))
        if self.kind=="float":
            return lib.PEAK_FloatNode_GetValue(self._vhandle,cache_policy)
        if self.kind=="str":
            return py3.as_str(lib.PEAK_StringNode_GetValue(self._vhandle,cache_policy))
        if self.kind=="enum":
            ev=lib.PEAK_EnumerationNode_GetCurrentEntry(self._vhandle,cache_policy)
            if enum_as_str:
                return py3.as_str(lib.PEAK_EnumerationEntryNode_GetSymbolicValue(ev))
            return lib.PEAK_EnumerationEntryNode_GetValue(ev)
    def set_value(self, value, truncate=True):
        """
        Set attribute value.
        
        If ``truncate==True``, automatically truncate value to lie within allowed range.
        """
        if not self.writable:
            raise IDSPeakError("attribute {} ({}) is not writable".format(self.name,self.kind))
        if self._vhandle is None:
            raise IDSPeakError("attribute {} with kind {} does not have values".format(self.name,self.kind))
        if truncate:
            value=self.truncate_value(value)
        if self.kind=="int":
            lib.PEAK_IntegerNode_SetValue(self._vhandle,int(value))
        elif self.kind=="bool":
            bool(lib.PEAK_IntegerNode_SetValue(self._vhandle,1 if value else 0))
        elif self.kind=="float":
            lib.PEAK_FloatNode_SetValue(self._vhandle,float(value))
        elif self.kind=="str":
            py3.as_str(lib.PEAK_StringNode_SetValue(self._vhandle,py3.as_builtin_bytes(value)))
        elif self.kind=="enum":
            value=self.labels.get(value,value)
            if value not in self.ivalues:
                raise IDSPeakError("unsupported value: {}".format(value))
            lib.PEAK_EnumerationNode_SetCurrentEntryByValue(self._vhandle,value)
    def _check_command_implemented(self):
        if self.kind=="command":
            if not self.implemented:
                raise IDSPeakError("command {} is not implemented".format(self.name))
        else:
            raise IDSPeakError("attribute {} is not a command".format(self.name))
    def call_command(self, wait=False, wait_timeout=None):
        """Execute the given command"""
        self._check_command_implemented()
        lib.PEAK_CommandNode_Execute(self._chandle)
        if wait:
            self.wait_command_done(wait_timeout)
    def wait_command_done(self, timeout=None):
        """Wait until the command is done or the given timeout is elapsed (by default, infinite timeout)"""
        self._check_command_implemented()
        if timeout is None:
            lib.PEAK_CommandNode_WaitUntilDoneInfinite(self._chandle)
        lib.PEAK_CommandNode_WaitUntilDone(self._chandle,int(timeout*1000))
    def is_command_done(self):
        """Check if the command is done"""
        self._check_command_implemented()
        return lib.PEAK_CommandNode_GetIsDone(self._chandle)
    def __repr__(self):
        return "{}(name='{}', kind='{}')".format(self.__class__.__name__,self.name,self.kind)




def get_library_version():
    """Get peak library version"""
    return "{}.{}.{}".format(lib.PEAK_Library_GetVersionMajor(),lib.PEAK_Library_GetVersionMinor(),lib.PEAK_Library_GetVersionSubminor())

def get_cti_paths(update=True):
    """Return all found CTI paths"""
    with libctl.temp_open():
        if update:
            lib.PEAK_EnvironmentInspector_UpdateCTIPaths()
        npaths=lib.PEAK_EnvironmentInspector_GetNumCTIPaths()
        return [py3.as_str(lib.PEAK_EnvironmentInspector_GetCTIPath(i)) for i in range(npaths)]







TIDSPeakSystemDescriptorInfo=collections.namedtuple("TIDSPeakSystemDescriptorInfo",["key","display_name","vendor","model","version","tl_type","tl_version","cti_name","cti_path"])
def _get_system_descriptor_info(handle):
    key=py3.as_str(lib.PEAK_SystemDescriptor_GetKey(handle))
    display_name=py3.as_str(lib.PEAK_SystemDescriptor_GetDisplayName(handle))
    vendor=py3.as_str(lib.PEAK_SystemDescriptor_GetVendorName(handle))
    model=py3.as_str(lib.PEAK_SystemDescriptor_GetModelName(handle))
    version=py3.as_str(lib.PEAK_SystemDescriptor_GetVersion(handle))
    tl_type=py3.as_str(lib.PEAK_SystemDescriptor_GetTLType(handle))
    tl_version="{}.{}".format(lib.PEAK_SystemDescriptor_GetGenTLVersionMajor(handle),lib.PEAK_SystemDescriptor_GetGenTLVersionMinor(handle))
    cti_name=py3.as_str(lib.PEAK_SystemDescriptor_GetCTIFileName(handle))
    cti_path=py3.as_str(lib.PEAK_SystemDescriptor_GetCTIFullPath(handle))
    return TIDSPeakSystemDescriptorInfo(key,display_name,vendor,model,version,tl_type,tl_version,cti_name,cti_path)
        
TIDSPeakSystemInfo=collections.namedtuple("TIDSPeakSystemInfo",["key","id","display_name","vendor","model","version","tl_type","tl_version","cti_name","cti_path"])
def _get_system_info(handle):
    key=py3.as_str(lib.PEAK_System_GetKey(handle))
    sid=py3.as_str(lib.PEAK_System_GetID(handle))
    display_name=py3.as_str(lib.PEAK_System_GetDisplayName(handle))
    vendor=py3.as_str(lib.PEAK_System_GetVendorName(handle))
    model=py3.as_str(lib.PEAK_System_GetModelName(handle))
    version=py3.as_str(lib.PEAK_System_GetVersion(handle))
    tl_type=py3.as_str(lib.PEAK_System_GetTLType(handle))
    tl_version="{}.{}".format(lib.PEAK_System_GetGenTLVersionMajor(handle),lib.PEAK_System_GetGenTLVersionMinor(handle))
    cti_name=py3.as_str(lib.PEAK_System_GetCTIFileName(handle))
    cti_path=py3.as_str(lib.PEAK_System_GetCTIFullPath(handle))
    return TIDSPeakSystemInfo(key,sid,display_name,vendor,model,version,tl_type,tl_version,cti_name,cti_path)
        
TIDSPeakInterfaceDescriptorInfo=collections.namedtuple("TIDSPeakInterfaceDescriptorInfo",["key","display_name","tl_type"])
def _get_interface_descriptor_info(handle):
    key=py3.as_str(lib.PEAK_InterfaceDescriptor_GetKey(handle))
    display_name=py3.as_str(lib.PEAK_InterfaceDescriptor_GetDisplayName(handle))
    tl_type=py3.as_str(lib.PEAK_InterfaceDescriptor_GetTLType(handle))
    return TIDSPeakInterfaceDescriptorInfo(key,display_name,tl_type)
        
TIDSPeakInterfaceInfo=collections.namedtuple("TIDSPeakInterfaceInfo",["key","id","display_name","tl_type"])
def _get_interface_info(handle):
    key=py3.as_str(lib.PEAK_Interface_GetKey(handle))
    iid=py3.as_str(lib.PEAK_Interface_GetID(handle))
    display_name=py3.as_str(lib.PEAK_Interface_GetDisplayName(handle))
    tl_type=py3.as_str(lib.PEAK_Interface_GetTLType(handle))
    return TIDSPeakInterfaceInfo(key,iid,display_name,tl_type)

TIDSPeakDeviceDescriptorInfo=collections.namedtuple("TIDSPeakDeviceDescriptorInfo",["key","display_name","user_name","vendor","model","serial","version","tl_type"])
def _get_device_descriptor_info(handle):
    key=py3.as_str(lib.PEAK_DeviceDescriptor_GetKey(handle))
    display_name=py3.as_str(lib.PEAK_DeviceDescriptor_GetDisplayName(handle))
    user_name=py3.as_str(lib.PEAK_DeviceDescriptor_GetUserDefinedName(handle))
    vendor=py3.as_str(lib.PEAK_DeviceDescriptor_GetVendorName(handle))
    model=py3.as_str(lib.PEAK_DeviceDescriptor_GetModelName(handle))
    serial=py3.as_str(lib.PEAK_DeviceDescriptor_GetSerialNumber(handle))
    version=py3.as_str(lib.PEAK_DeviceDescriptor_GetVersion(handle))
    tl_type=py3.as_str(lib.PEAK_DeviceDescriptor_GetTLType(handle))
    return TIDSPeakDeviceDescriptorInfo(key,display_name,user_name,vendor,model,serial,version,tl_type)

TIDSPeakDeviceInfo=collections.namedtuple("TIDSPeakDeviceInfo",["key","id","display_name","user_name","vendor","model","serial","version","tl_type"])
def _get_device_info(handle):
    key=py3.as_str(lib.PEAK_Device_GetKey(handle))
    did=py3.as_str(lib.PEAK_Device_GetID(handle))
    display_name=py3.as_str(lib.PEAK_Device_GetDisplayName(handle))
    user_name=py3.as_str(lib.PEAK_Device_GetUserDefinedName(handle))
    vendor=py3.as_str(lib.PEAK_Device_GetVendorName(handle))
    model=py3.as_str(lib.PEAK_Device_GetModelName(handle))
    serial=py3.as_str(lib.PEAK_Device_GetSerialNumber(handle))
    version=py3.as_str(lib.PEAK_Device_GetVersion(handle))
    tl_type=py3.as_str(lib.PEAK_Device_GetTLType(handle))
    return TIDSPeakDeviceInfo(key,did,display_name,user_name,vendor,model,serial,version,tl_type)

TIDSPeakStreamDescriptorInfo=collections.namedtuple("TIDSPeakStreamDescriptorInfo",["key"])
def _get_stream_descriptor_info(handle):
    key=py3.as_str(lib.PEAK_DataStreamDescriptor_GetKey(handle))
    return TIDSPeakStreamDescriptorInfo(key)

TIDSPeakStreamInfo=collections.namedtuple("TIDSPeakStreamInfo",["key","id","tl_type"])
def _get_stream_info(handle):
    key=py3.as_str(lib.PEAK_Device_GetKey(handle))
    sid=py3.as_str(lib.PEAK_Device_GetID(handle))
    tl_type=py3.as_str(lib.PEAK_Device_GetTLType(handle))
    return TIDSPeakStreamInfo(key,sid,tl_type)







class IIDSPeakDevice(devio_interface.IDevice):
    """Generic IDS peak object"""
    Error=IDSPeakError
    def __init__(self, handle=None):
        super().__init__()
        self.handle=handle
    def _get_connection_parameters(self):
        return ()


class IDSPeakAttributeManager:
    """Generic IDS peak attribute manager"""
    def __init__(self):
        self.attributes=dictionary.Dictionary()
        self.a=dictionary.ItemAccessor(self.get_attribute,missing_error=IDSPeakError)
        self.av=dictionary.ItemAccessor(self.get_attribute_value,self.set_attribute_value,missing_error=IDSPeakError)
    
    def __getitem__(self, key):
        return self.attributes[key]
    def __contains__(self, key):
        return key in self.attributes
    def _get_attribute(self, node):
        try:
            return GenericIDSPeakAttribute(node)
        except IDSPeakLibError:
            return None
    def _list_attributes(self, module):
        node_map=lib.PEAK_Module_GetNodeMap(module,0)
        num=lib.PEAK_NodeMap_GetNumNodes(node_map)
        attributes=[self._get_attribute(lib.PEAK_NodeMap_GetNode(node_map,i)) for i in range(num)]
        attributes=[a for a in attributes if a and a.kind in ["int","bool","float","str","enum","command"]]
        return attributes
    def update_attributes(self, module, replace=False):
        """Update ``attributes`` dictionary; if ``replace==True``, replace it entirely, otherwise, simply update it"""
        attrs=self._list_attributes(module)
        attrs_dict=dictionary.Dictionary(attrs if isinstance(attrs,dict) else {p.name:p for p in attrs})
        if replace:
            self.attributes=attrs_dict
        else:
            self.attributes.update(attrs_dict)
    def get_attribute(self, name, error_on_missing=True):
        """Get the camera attribute with the given name"""
        if name in self.attributes:
            return self.attributes[name]
        if error_on_missing:
            raise IDSPeakError("attribute {} is missing".format(name))
    def get_all_attributes(self, copy=False):
        """
        Return a dictionary of all available attributes.
        
        If ``copy==True``, copy the dictionary; otherwise, return the internal dictionary structure (should not be modified).
        """
        return self.attributes.copy() if copy else self.attributes

    def get_attribute_value(self, name, error_on_missing=True, default=None, **kwargs):
        """
        Get value of an attribute with the given name.
        
        If the value doesn't exist and ``error_on_missing==True``, raise error; otherwise, return `default`.
        If `default` is not ``None``, automatically assume that ``error_on_missing==False``.
        If `name` points at a dictionary branch, return a dictionary with all values in this branch.
        Additional arguments are passed to ``get_value`` methods of the individual attribute.
        """
        error_on_missing=error_on_missing and (default is None)
        attr=self.get_attribute(name,error_on_missing=error_on_missing)
        if dictionary.is_dictionary(attr):
            return self.get_all_attribute_values(root=name,**kwargs)
        return default if attr is None else attr.get_value(**kwargs)
    def set_attribute_value(self, name, value, error_on_missing=True, **kwargs):
        """
        Set value of an attribute with the given name.
        
        If the value doesn't exist and ``error_on_missing==True``, raise error; otherwise, do nothing.
        If `name` points at a dictionary branch, set all values in this branch (in this case `value` must be a dictionary).
        Additional arguments are passed to ``set_value`` methods of the individual attribute.
        """
        attr=self.get_attribute(name,error_on_missing=error_on_missing)
        if dictionary.is_dictionary(attr):
            return self.set_all_attribute_values(value,root=name,**kwargs)
        if attr is not None:
            attr.set_value(value,**kwargs)

    def call_command(self, name, error_on_missing=True, wait=False, wait_timeout=None):
        """
        Call a command with the given name.
        
        If the value doesn't exist and ``error_on_missing==True``, raise error; otherwise, do nothing.
        If ``wait==True``, wait until it is done for the given `wait_timeout` (``None`` means infinite timeout).
        """
        attr=self.get_attribute(name,error_on_missing=error_on_missing)
        if attr is not None:
            attr.call_command(wait=wait,wait_timeout=wait_timeout)
    def is_command_done(self, name, error_on_missing=True):
        """
        Check if the command with the given name is done.

        If the value doesn't exist and ``error_on_missing==True``, raise error; otherwise, do nothing.
        """
        attr=self.get_attribute(name,error_on_missing=error_on_missing)
        if attr is not None:
            return attr.is_command_done()
    def wait_command_done(self, name, error_on_missing=True, timeout=None):
        """
        Wait until the command with the given name is done.

        If the value doesn't exist and ``error_on_missing==True``, raise error; otherwise, do nothing.
        """
        attr=self.get_attribute(name,error_on_missing=error_on_missing)
        if attr is not None:
            return attr.wait_command_done(timeout=timeout)
    
    def get_all_attribute_values(self, root="", **kwargs):
        """
        Get values of all attributes with the given `root`.

        Additional arguments are passed to ``get_value`` methods of individual attributes.
        """
        attributes=self.get_attribute(root)
        values=dictionary.Dictionary()
        for k,a in attributes.iternodes(include_path=True):
            if a.readable:
                try:
                    values[k]=a.get_value(**kwargs)
                except IDSPeakLibError:
                    pass
        return values
    def set_all_attribute_values(self, settings, root="", **kwargs):
        """
        Set values of all attributes with the given `root`.

        Additional arguments are passed to ``set_value`` methods of individual attributes.
        """
        attributes=self.get_attribute(root)
        settings=dictionary.as_dict(settings,style="flat",copy=False)
        for k,v in settings.items():
            if k in attributes and attributes[k].writable:
                attributes[k].set_value(v,**kwargs)





class IIDSPeakAttributeDevice(IIDSPeakDevice):
    """
    Generic IDS peak device with attributes.
    """
    _attribute_variable="attributes"
    def __init__(self, handle=None):
        super().__init__(handle)
        self.attributes=IDSPeakAttributeManager()
        self._add_status_variable(self._attribute_variable,self.attributes.get_all_attribute_values,priority=-5)
        self.a=self.attributes.a
        self.av=self.attributes.av
    
    def _to_module(self):
        raise NotImplementedError("IIDSPeakAttributeDevice._to_module")
    def _update_attributes(self, replace=False):
        """Update ``attributes`` dictionary; if ``replace==True``, replace it entirely, otherwise, simply update it"""
        self.attributes.update_attributes(self._to_module(),replace=replace)
    def get_attribute(self, name, error_on_missing=True):
        """Get the camera attribute with the given name"""
        return self.attributes.get_attribute(name,error_on_missing=error_on_missing)
    def get_all_attributes(self, copy=False):
        """
        Return a dictionary of all available attributes.
        
        If ``copy==True``, copy the dictionary; otherwise, return the internal dictionary structure (should not be modified).
        """
        return self.attributes.get_all_attributes(copy=copy)

    def get_attribute_value(self, name, error_on_missing=True, default=None, **kwargs):
        """
        Get value of an attribute with the given name.
        
        If the value doesn't exist and ``error_on_missing==True``, raise error; otherwise, return `default`.
        If `default` is not ``None``, automatically assume that ``error_on_missing==False``.
        If `name` points at a dictionary branch, return a dictionary with all values in this branch.
        Additional arguments are passed to ``get_value`` methods of the individual attribute.
        """
        return self.attributes.get_attribute_value(name,error_on_missing=error_on_missing,default=default,**kwargs)
    def set_attribute_value(self, name, value, error_on_missing=True, **kwargs):
        """
        Set value of an attribute with the given name.
        
        If the value doesn't exist and ``error_on_missing==True``, raise error; otherwise, do nothing.
        If `name` points at a dictionary branch, set all values in this branch (in this case `value` must be a dictionary).
        Additional arguments are passed to ``set_value`` methods of the individual attribute.
        """
        return self.attributes.set_attribute_value(name,value,error_on_missing=error_on_missing,**kwargs)

    def call_command(self, name, error_on_missing=True, wait=False, wait_timeout=None):
        """
        Call a command with the given name.
        
        If the value doesn't exist and ``error_on_missing==True``, raise error; otherwise, do nothing.
        If ``wait==True``, wait until it is done for the given `wait_timeout` (``None`` means infinite timeout).
        """
        return self.attributes.call_command(name,error_on_missing=error_on_missing,wait=wait,wait_timeout=wait_timeout)
    def is_command_done(self, name, error_on_missing=True):
        """
        Check if the command with the given name is done.

        If the value doesn't exist and ``error_on_missing==True``, raise error; otherwise, do nothing.
        """
        return self.attributes.is_command_done(name,error_on_missing=error_on_missing)
    def wait_command_done(self, name, error_on_missing=True, timeout=None):
        """
        Wait until the command with the given name is done.

        If the value doesn't exist and ``error_on_missing==True``, raise error; otherwise, do nothing.
        """
        return self.attributes.wait_command_done(name,error_on_missing=error_on_missing,timeout=timeout)
    
    def get_all_attribute_values(self, root="", **kwargs):
        """
        Get values of all attributes with the given `root`.

        Additional arguments are passed to ``get_value`` methods of individual attributes.
        """
        return self.attributes.get_all_attribute_values(root=root,**kwargs)
    def set_all_attribute_values(self, settings, root="", **kwargs):
        """
        Set values of all attributes with the given `root`.

        Additional arguments are passed to ``set_value`` methods of individual attributes.
        """
        return self.attributes.set_all_attribute_values(settings,root=root,**kwargs)








class IDSPeakProducerLibrary(IIDSPeakDevice):
    """
    IDS peak producer library.

    Used to create an IDS peak system.
    
    Args:
        cti_path: path to the CTI file (use :func:`get_cti_paths` to get all paths)
    """
    def __init__(self, cti_path):
        super().__init__()
        self.cti_path=cti_path
        self._opid=None
        self.open()
    def open(self):
        if self.is_opened():
            return
        with libctl.temp_open():
            self.handle=lib.PEAK_ProducerLibrary_Construct(self.cti_path)
            self._opid=libctl.open().opid
        return super().open()
    def close(self):
        if self.handle is not None:
            lib.PEAK_ProducerLibrary_Destruct(self.handle)
            self.handle=None
            libctl.close(self._opid)
            self._opid=None
    def is_opened(self):
        return self.handle is not None
    def _get_connection_parameters(self):
        return (self.cti_path,)
    def get_system_info(self):
        """Get an IDS peak system descriptor info"""
        return _get_system_descriptor_info(lib.PEAK_ProducerLibrary_GetSystem(self.handle))
    def get_system(self):
        """Get an IDS peak system instance"""
        return IDSPeakSystem(self)




class IDSPeakSystem(IIDSPeakAttributeDevice):
    """
    IDS peak system.

    Used list and open interfaces.
    Has attributes (``.a`` and ``.av``) describing some properties (number of interfaces, GenTL version and properties, etc.)
    Typically created by an :class:`IDSPeakProducerLibrary` instance, does not need to be created explicitly.

    Args:
        producer: :class:`IDSPeakProducerLibrary` instance used to create the system
    """
    def __init__(self, producer):
        super().__init__()
        self.producer=producer
        self.dhandle=None
        self.open()
        self._update_attributes()
        self._add_info_variable("system_info",self.get_system_info)
    def _to_module(self):
        return lib.PEAK_System_ToModule(self.handle)
    def open(self):
        if self.is_opened():
            return
        self.dhandle=lib.PEAK_ProducerLibrary_GetSystem(self.producer.handle)
        self.handle=lib.PEAK_SystemDescriptor_OpenSystem(self.dhandle)
        return super().open()
    def close(self):
        if self.handle is not None:
            lib.PEAK_System_Destruct(self.handle)
            self.dhandle=None
            self.handle=None
        return super().close()
    def is_opened(self):
        return self.handle is not None
    def get_system_info(self):
        """Get system info as a :class:`TIDSPeakSystemInfo` tuple"""
        return _get_system_info(self.handle)
    def list_interfaces(self, update=False, update_timeout=1.):
        """
        List all interfaces available at this system.

        If ``update==True``, update the interfaces list with the given timeout before listing.
        """
        if update:
            lib.PEAK_System_UpdateInterfaces(self.handle,int(update_timeout*1000))
        num=lib.PEAK_System_GetNumInterfaces(self.handle)
        return [_get_interface_descriptor_info(lib.PEAK_System_GetInterface(self.handle,i)) for i in range(num)]
    def get_interface(self, idx=0, update=False, update_timeout=1.):
        """
        Get the interface with the given index (0-based, order given by :meth:`list_interfaces` method).

        If ``update==True``, update the interfaces list with the given timeout before listing and opening.
        """
        if update:
            lib.PEAK_System_UpdateInterfaces(self.handle,int(update_timeout*1000))
        return IDSPeakInterface(self,idx=idx)




class IDSPeakInterface(IIDSPeakAttributeDevice):
    """
    IDS peak interface.

    Used to list and open devices.
    Has attributes (``.a`` and ``.av``) describing some properties (number of devices, TL version and properties, etc.)
    Typically created by an :class:`IDSPeakSystem` instance, does not need to be created explicitly.

    Args:
        system: :class:`IDSPeakSystem` instance used to create the interface
        idx: index of the interface within the system
    """
    def __init__(self, system, idx=0):
        super().__init__()
        self.system=system
        self.idx=idx
        self.dhandle=None
        self.open()
        self._update_attributes()
        self._add_info_variable("interface_info",self.get_interface_info)
    def _to_module(self):
        return lib.PEAK_Interface_ToModule(self.handle)
    def open(self):
        if self.is_opened():
            return
        self.dhandle=lib.PEAK_System_GetInterface(self.system.handle,self.idx)
        self.handle=lib.PEAK_InterfaceDescriptor_OpenInterface(self.dhandle)
        return super().open()
    def close(self):
        if self.handle is not None:
            lib.PEAK_Interface_Destruct(self.handle)
            self.dhandle=None
            self.handle=None
        return super().close()
    def is_opened(self):
        return self.handle is not None
    def get_interface_info(self):
        """Get interface info as a :class:`TIDSPeakInterfaceInfo` tuple"""
        return _get_interface_info(self.handle)
    def list_devices(self, update=False, update_timeout=1.):
        """
        List all devices available at this system.

        If ``update==True``, update the devices list with the given timeout before listing.
        """
        if update:
            lib.PEAK_Interface_UpdateDevices(self.handle,int(update_timeout*1000))
        num=lib.PEAK_Interface_GetNumDevices(self.handle)
        return [_get_device_descriptor_info(lib.PEAK_Interface_GetDevice(self.handle,i)) for i in range(num)]
    def get_device(self, idx=0, update=False, update_timeout=1.):
        """
        Get the device with the given index (0-based, order given by :meth:`list_devices` method).

        If ``update==True``, update the devices list with the given timeout before listing and opening.
        """
        if update:
            lib.PEAK_Interface_UpdateDevices(self.handle,int(update_timeout*1000))
        return IDSPeakDevice(self,idx=idx)




class IDSPeakDevice(IIDSPeakAttributeDevice):
    """
    Generic IDS peak device.

    Used to control the camera.
    Has attributes (``.ca`` and ``.cav``) describing camera properties.
    In addition, it also gives access to GenTL (i.e., transport layer) properties via ``gentl_attributes`` attribute.
    Typically created by an :class:`IDSPeakInterface` instance, does not need to be created explicitly.

    Args:
        interface: :class:`IDSPeakInterface` instance used to create the device
        idx: index of the device within the interface
    """
    _device_access_types={"read_only":PEAK_DEVICE_ACCESS_TYPE_t.PEAK_DEVICE_ACCESS_TYPE_READ_ONLY,
                            "control":PEAK_DEVICE_ACCESS_TYPE_t.PEAK_DEVICE_ACCESS_TYPE_CONTROL,
                            "exclusive":PEAK_DEVICE_ACCESS_TYPE_t.PEAK_DEVICE_ACCESS_TYPE_EXCLUSIVE,
                            "custom":PEAK_DEVICE_ACCESS_TYPE_t.PEAK_DEVICE_ACCESS_TYPE_CUSTOM,}
    def __init__(self, interface, idx=0, access_type="control"):
        super().__init__()
        self.ca=self.a
        self.cav=self.av
        self.gentl_attributes=IDSPeakAttributeManager()
        self.interface=interface
        self.idx=idx
        self.access_type=self._device_access_types[access_type]
        self.dhandle=None
        self.open()
        self._update_attributes()
        self._add_info_variable("gentl_attributes",self.gentl_attributes.get_all_attribute_values,priority=-7)
        self._add_info_variable("device_info",self.get_device_info)
    def _to_module(self):
        return lib.PEAK_RemoteDevice_ToModule(self.rhandle)
    def _update_attributes(self, replace=False):
        self.gentl_attributes.update_attributes(lib.PEAK_Device_ToModule(self.handle),replace=replace)
        super()._update_attributes(replace=replace)
    def open(self):
        if self.is_opened():
            return
        self.dhandle=lib.PEAK_Interface_GetDevice(self.interface.handle,self.idx)
        self.handle=lib.PEAK_DeviceDescriptor_OpenDevice(self.dhandle,self.access_type)
        self.rhandle=lib.PEAK_Device_GetRemoteDevice(self.handle)
        return super().open()
    def close(self):
        if self.handle is not None:
            lib.PEAK_Device_Destruct(self.handle)
            self.dhandle=None
            self.handle=None
        return super().close()
    def is_opened(self):
        return self.handle is not None
    def get_device_info(self):
        """Get device info as a :class:`TIDSPeakDeviceInfo` tuple"""
        return _get_device_info(self.handle)
    def list_streams(self):
        """List the data streams of the device"""
        num=lib.PEAK_Device_GetNumDataStreams(self.handle)
        return [_get_stream_descriptor_info(lib.PEAK_Device_GetDataStream(self.handle,i)) for i in range(num)]
    def _get_stream(self, idx=0):
        """Get the data with the given index"""
        return IDSPeakStream(self,idx=idx)




TIDSPeakStreamBufferStat=collections.namedtuple("TIDSPeakStreamBufferStat",["announced","queued","awaiting","delivered","underruns","min_required","started"])
class IDSPeakStream(IIDSPeakAttributeDevice):
    """
    IDS peak stream.

    Used to control the camera readout.
    Has attributes (``.a`` and ``.av``) describing camera properties.
    In addition, it also gives access to GenTL (i.e., transport layer) properties via ``gentl_attributes`` attribute.
    Typically created by an :class:`IDSPeakInterface` instance, does not need to be created explicitly.

    Args:
        device: :class:`IDSPeakDevice` instance used to create the stream
        idx: index of the stream within the device
    """
    def __init__(self, device, idx=0):
        super().__init__()
        self.device=device
        self.idx=idx
        self.dhandle=None
        self.open()
        self._update_attributes()
        self._add_info_variable("stream_info",self.get_stream_info)
        self._buffer=None
        self._nbuff=None
        self._payload_size=None
        self._buff_handles=None
        self._queue_loop_thread=None
        self._looping=ctypes.c_uint()
    def _to_module(self):
        return lib.PEAK_DataStream_ToModule(self.handle)
    def open(self):
        if self.is_opened():
            return
        self.dhandle=lib.PEAK_Device_GetDataStream(self.device.handle,self.idx)
        self.handle=lib.PEAK_DataStreamDescriptor_OpenDataStream(self.dhandle)
        return super().open()
    def close(self):
        if self.handle is not None:
            self.unschedule_buffers()
            lib.PEAK_DataStream_Destruct(self.handle)
            self.dhandle=None
            self.handle=None
        return super().close()
    def is_opened(self):
        return self.handle is not None
    def get_stream_info(self):
        """Get stream info as a :class:`TIDSPeakStreamInfo` tuple"""
        return _get_stream_info(self.handle)
    def get_buffer_status(self):
        """
        Get buffer statistics.
        
        Return tuple ``(announced, queued, awaiting, delivered, under-runs, min_required, started)`` with the number of buffers which have been
        announced (scheduled), queued (waiting for reception), waiting to be read in the schedule loop, delivered (read in the scheduled loop),
        under-run (not delivered because the schedule loop is too slow), minimal number to be scheduled, and started (could be ``None`` if not supported).
        """
        announced=lib.PEAK_DataStream_GetNumBuffersAnnounced(self.handle)
        queued=lib.PEAK_DataStream_GetNumBuffersQueued(self.handle)
        awaiting=lib.PEAK_DataStream_GetNumBuffersAwaitDelivery(self.handle)
        delivered=lib.PEAK_DataStream_GetNumBuffersDelivered(self.handle)
        underruns=lib.PEAK_DataStream_GetNumUnderruns(self.handle)
        min_required=lib.PEAK_DataStream_GetNumBuffersAnnouncedMinRequired(self.handle)
        try:
            started=lib.PEAK_DataStream_GetNumBuffersStarted(self.handle)
        except IDSPeakLibError:
            started=None
        return TIDSPeakStreamBufferStat(announced,queued,awaiting,delivered,underruns,min_required,started)
    def is_grabbing(self):
        """Check if grabbing is in progress"""
        return bool(lib.PEAK_DataStream_GetIsGrabbing(self.handle))

    def _start_queue_loop(self):
        self._stop_queue_loop()
        self._queue_loop_thread=threading.Thread(target=self._run_queue_looper,daemon=True)
        self._looping.value=1
        self._queue_loop_thread.start()
        return True
    def _run_queue_looper(self):
        code=looper(self.handle.value,ctypes.addressof(self._looping),
                        funcaddressof(lib.lib.PEAK_DataStream_QueueBuffer),funcaddressof(lib.lib.PEAK_DataStream_WaitForFinishedBuffer))
        if code:
            func="PEAK_DataStream_WaitForFinishedBuffer" if code&0x10000 else "PEAK_DataStream_QueueBuffer"
            raise IDSPeakLibError(func,code&0xFFFF,lib=lib)
    def _stop_queue_loop(self):
        if self._queue_loop_thread is not None:
            self._looping.value=0
            self._queue_loop_thread.join()
            self._queue_loop_thread=None

    def _get_payload_size(self):
        payload_size=None
        try:
            if lib.PEAK_DataStream_GetDefinesPayloadSize(self.handle):
                payload_size=lib.PEAK_DataStream_GetPayloadSize(self.handle)
        except IDSPeakLibError:
            pass
        if payload_size is None:
            payload_size=self.device.cav["PayloadSize"]
        return payload_size
    def allocate_buffers(self, nbuff):
        """Allocate the given number of buffers (deallocate currently allocated if necessary)"""
        self.deallocate_buffers()
        self._payload_size=self._get_payload_size()
        self._nbuff=max(nbuff,self.get_buffer_status().min_required)
        self._buffer=ctypes.create_string_buffer(self._nbuff*self._payload_size)
    def schedule_buffers(self):
        """
        Schedule the allocated buffers (unschedule currently scheduled if necessary).
        
        Return ``True`` if could schedule, and ``False`` if no buffers are allocated.
        """
        self.unschedule_buffers()
        if self._buffer is None:
            return False
        self._buff_handles=[]
        baddr=ctypes.addressof(self._buffer)
        for i in range(self._nbuff):
            bh=lib.PEAK_DataStream_AnnounceBuffer(self.handle,baddr+i*self._payload_size,self._payload_size,None,None,None)
            self._buff_handles.append(bh)
        return True
    def start_acquisition(self, nacq=None):
        """
        Start the acquisition of the given number of frames (``None`` means infinite).
        
        Return ``True`` if could start, and ``False`` if no buffers are scheduled.
        """
        if self._buff_handles is None:
            return False
        self.stop_acquisition()
        for bh in self._buff_handles:
            lib.PEAK_DataStream_QueueBuffer(self.handle,bh)
        if nacq is not None:
            lib.PEAK_DataStream_StartAcquisition(self.handle,PEAK_ACQUISITION_START_MODE_t.PEAK_ACQUISITION_START_MODE_DEFAULT,nacq)
        else:
            lib.PEAK_DataStream_StartAcquisitionInfinite(self.handle,PEAK_ACQUISITION_START_MODE_t.PEAK_ACQUISITION_START_MODE_DEFAULT)
        self._start_queue_loop()
        return True
    def stop_acquisition(self):
        """Stop acquisition and scheduling loop"""
        try:
            lib.PEAK_DataStream_StopAcquisition(self.handle,PEAK_ACQUISITION_STOP_MODE_t.PEAK_ACQUISITION_STOP_MODE_DEFAULT)
        except IDSPeakLibError:
            pass
        self._stop_queue_loop()
        lib.PEAK_DataStream_Flush(self.handle,PEAK_DATA_STREAM_FLUSH_MODE_t.PEAK_DATA_STREAM_FLUSH_MODE_DISCARD_ALL)
    def unschedule_buffers(self):
        """Unschedule currently scheduled buffers"""
        if self._buff_handles is None:
            return
        self.stop_acquisition()
        for bh in self._buff_handles:
            lib.PEAK_DataStream_RevokeBuffer(self.handle,bh)
        self._buff_handles=None
    def deallocate_buffers(self):
        """Deallocate currently allocated buffers"""
        if self._buffer is None:
            return
        self.unschedule_buffers()
        self._buffer=None
        self._payload_size=None
        self._nbuff=None
    def get_buffers(self, start, end):
        """Get buffers located between the given indices as a list of 2D numpy array chunks"""
        if self._buffer is None:
            return None
        start=max(start,end-self._nbuff+1)
        sidx=start%self._nbuff
        eidx=(end-1)%self._nbuff+1
        if eidx>sidx:
            chunks=[(sidx,eidx-sidx)]
        else:
            chunks=[(sidx,self._nbuff-sidx),(0,eidx)]
        result=[]
        uint8_ptr=ctypes.POINTER(ctypes.c_uint8)
        for s,n in chunks:
            buff=ctypes.c_void_p(ctypes.addressof(self._buffer)+s*self._payload_size)
            arr=np.ctypeslib.as_array(ctypes.cast(buff,uint8_ptr),shape=(n,self._payload_size))
            result.append(arr.copy())
        return result








TIDSPeakCameraEnumeratorSystem=collections.namedtuple("TIDSPeakCameraEnumeratorSystem",["producer","system","interfaces"])
TIDSPeakCameraEnumeratorInterface=collections.namedtuple("TIDSPeakCameraEnumeratorInterface",["interface","devices"])
class IDSPeakCameraEnumerator:
    """
    IDS peak camera enumerator.

    Iterates over all connected systems, interfaces within systems, and cameras within interfaces.
    """
    def __init__(self):
        self.lock=threading.RLock()
        self._opid=None
        self.systems={}
        self.idgen=general_utils.UIDGenerator()
    def open(self):
        if self._opid is not None:
            return
        with self.lock:
            with libctl.temp_open():
                self._opid=libctl.open().opid
    def close(self):
        with self.lock:
            for s in self.systems.values():
                s.producer.close()
            self.systems={}
            if self._opid is not None:
                libctl.close(self._opid)
                self._opid=None
    def _get_system(self, cti_path):
        if cti_path not in self.systems:
            producer=IDSPeakProducerLibrary(cti_path)
            system=producer.get_system()
            system.list_interfaces(update=True)
            self.systems[cti_path]=TIDSPeakCameraEnumeratorSystem(producer,system,{})
        return self.systems[cti_path]
    def _get_interface(self, system, iidx):
        if iidx not in system.interfaces:
            interface=system.system.get_interface(iidx)
            interface.list_devices(update=True)
            system.interfaces[iidx]=TIDSPeakCameraEnumeratorInterface(interface,{})
        return system.interfaces[iidx]
    def _close_unused_interfaces(self, system):
        for iidx,interface in list(system.interfaces.items()):
            if not interface.devices:
                system.interfaces[iidx].interface.close()
                del system.interfaces[iidx]
    def _close_unused_systems(self):
        for cti_path,system in list(self.systems.items()):
            self._close_unused_interfaces(system)
            if not system.interfaces:
                self.systems[cti_path].producer.close()
                del self.systems[cti_path]
    def iterate_cameras(self, cti_paths=None, cleanup=True):
        """
        Iterate over all cameras.

        Yield tuple ``(cti_path, interface_id, camera_id, camera_desc)``, where the first 3 elements identify system, interface and camera,
        and the last provides the camera description.
        `cti_paths` can specify a custom list of IDS peak CTI files.
        If ``cleanup==True``, close all unused systems upon completion.
        """
        with self.lock:
            self.open()
            cti_paths=cti_paths or get_cti_paths()
            try:
                for p in cti_paths:
                    system=self._get_system(p)
                    for iidx in range(len(system.system.list_interfaces())):
                        interface=self._get_interface(system,iidx)
                        for cidx,cam in enumerate(interface.interface.list_devices()):
                            yield p,iidx,cidx,cam
            finally:
                if cleanup:
                    self._close_unused_systems()
    def list_all_cameras(self, cti_paths=None):
        """List all cameras and return their descriptors"""
        with self.lock:
            return [cd[-1] for cd in self.iterate_cameras(cti_paths=cti_paths)]
    def open_camera(self, cti_path, interface_idx, camera_idx):
        """
        Open a camera with the given full CTI path, interface id and camera id.
        
        Return tuple ``(interface, uid)`` used to identify and control the camera.
        """
        with self.lock:
            system=self._get_system(cti_path)
            interface=self._get_interface(system,interface_idx)
            if camera_idx in interface.devices:
                raise IDSPeakError("camera {} | {} | {} is already opened".format(cti_path,interface_idx,camera_idx))
            cid=interface.devices[camera_idx]=self.idgen()
            return interface.interface,cid
    def close_camera(self, cid, cleanup=True):
        """
        Close the camera with the given ID.
         
        If ``cleanup==True`` and that was the last opened camera in the system, close the system as well.
        """
        with self.lock:
            for system in self.systems.values():
                for interface in system.interfaces.values():
                    for cidx,ccid in list(interface.devices.items()):
                        if ccid==cid:
                            del interface.devices[cidx]
                            if cleanup:
                                self._close_unused_systems()
                            return
        raise IDSPeakError("could not close camera {}".format(cid))

_cam_enum=IDSPeakCameraEnumerator()

def list_cameras():
    """
    List all connected cameras.

    Return a list of camera information tuples ``(key, id, display_name, user_name, vendor, model, serial, version, tl_type)``.
    """
    return _cam_enum.list_all_cameras()







class IDSPeakCamera(IDSPeakDevice,camera.IROICamera,camera.IExposureCamera):
    """
    Generic IDS peak camera interface.

    Args:
        idx: camera index among the cameras listed using :func:`list_cameras`
        name: camera key (unique identifier withing the system); if specified, then `idx` is ignored and the camera is determined based on the provided key
        serial: camera serial number; if specified, then `idx` and `key` are ignored and the camera is determined based on the provided serial number
    """
    Error=IDSPeakError
    TimeoutError=IDSPeakTimeoutError
    def __init__(self, idx=0, key=None, serial=None):
        self._cam_path=self._find_camera(idx,key,serial)
        interface,self._cid=_cam_enum.open_camera(*self._cam_path)
        self._stream=None
        super().__init__(interface,self._cam_path[-1])
        di=self.get_device_info()
        self._connection_parameters=(idx,di.key,di.serial)
        self._raw_readout_format=False
        self._add_status_variable("camera_attributes",self.get_all_attribute_values,priority=-5)
        self._add_settings_variable("exposure",self.get_exposure,self.set_exposure,ignore_error=IDSPeakError)
        self._update_device_variable_order("exposure")
        self._add_settings_variable("frame_period",self.get_frame_period,self.set_frame_period,ignore_error=IDSPeakError)
    def _get_connection_parameters(self):
        return self._connection_parameters
    @classmethod
    def _find_camera(cls, idx, key, serial):
        for i,(path,iidx,cidx,cd) in enumerate(_cam_enum.iterate_cameras()):
            found=False
            if serial is not None:
                found=cd.serial==serial
            elif key is not None:
                found=cd.key==key
            else:
                found=i==idx
            if found:
                return path,iidx,cidx
        if serial is not None:
            raise IDSPeakError("could not find camera with serial {}".format(serial))
        if key is not None:
            raise IDSPeakError("could not find camera with key {}".format(key))
        raise IDSPeakError("could not find camera with index {}".format(idx))
    def _open_cam_enum(self):
        if self._cid is None:
            _,self._cid=_cam_enum.open_camera(*self._cam_path)
    def _close_cam_enum(self):
        if self._cid is not None:
            _cam_enum.close_camera(self._cid)
            self._cid=None
    def open(self):
        self._open_cam_enum()
        try:
            res=super().open()
            with self._close_on_error():
                self.select_stream()
            return res
        except IDSPeakError:
            self._close_cam_enum()
            raise
    def close(self):
        try:
            self._close_stream()
            return super().close()
        finally:
            self._close_cam_enum()
    
    def _close_stream(self):
        if self._stream is not None:
            self._stream.close()
            self._stream=None
    @camera.acqcleared
    def select_stream(self, idx=0):
        """Select stream out of the ones available, as listed by :meth:`list_streams`"""
        self._close_stream()
        self._stream=self._get_stream(idx)

    _exposure_time_properties=["ExposureTimeAbs","ExposureTime"]
    def get_exposure(self):
        for p in self._exposure_time_properties:
            exp=self.get_attribute_value(p,error_on_missing=False)
            if exp is not None:
                return exp/1E6  # in us by default
        raise IDSPeakError("camera does not support exposure")
    def set_exposure(self, exposure):
        for p in self._exposure_time_properties:
            if p in self.attributes:
                self.cav[p]=exposure*1E6
                return self.get_exposure()
        raise IDSPeakError("camera does not support exposure")
    def get_frame_period(self):
        fps=self.get_attribute_value("AcquisitionFrameRate",error_on_missing=False)
        if fps is not None:
            period=1./fps
            try:
                exposure=self.get_exposure()
                return max(exposure,period)
            except IDSPeakError:
                return period
        try:
            return self.get_exposure()
        except IDSPeakError:
            raise IDSPeakError("camera does not support frame period")
    def set_frame_period(self, frame_period):
        """Set frame period (time between two consecutive frames in the internal trigger mode)"""
        enable_period=frame_period>0
        if "AcquisitionFrameRate" in self.attributes:
            if "AcquisitionFrameRateEnable" in self.attributes:
                self.cav["AcquisitionFrameRateEnable"]=enable_period
            self.cav["AcquisitionFrameRate"]=1./frame_period if frame_period>0 else 1E12
        else:
            raise IDSPeakError("camera does not support frame period")
        return self.get_frame_period()
    def get_frame_timings(self):
        return self._TAcqTimings(self.get_exposure(),self.get_frame_period())

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
            if a not in self.ca or not self.ca[a].writable:
                return self.get_roi()
        det_size=self.get_detector_size()
        if hend is None:
            hend=det_size[0]
        if vend is None:
            vend=det_size[1]
        with self.pausing_acquisition():
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
    
    
    

    @devio_interface.use_parameters(mode="acq_mode")
    def setup_acquisition(self, mode="sequence", nframes=100):  # pylint: disable=arguments-differ
        """
        Setup acquisition mode.

        `mode` can be either ``"snap"`` (single frame or a fixed number of frames) or ``"sequence"`` (continuous acquisition).
        (note that :meth:`.IDSPeakCamera.acquisition_in_progress` would still return ``True`` in this case, even though new frames are no longer acquired).
        `nframes` sets up number of frame buffers.
        """
        self.clear_acquisition()
        nframes=max(nframes,self._stream.get_buffer_status().min_required)
        super().setup_acquisition(mode=mode,nframes=nframes)
        self._stream.allocate_buffers(nframes)
    def clear_acquisition(self):
        if self._stream is not None:
            self._stream.deallocate_buffers()
        return super().clear_acquisition()
    def start_acquisition(self, *args, **kwargs):
        self.stop_acquisition()
        super().start_acquisition(*args,**kwargs)
        self._stream.schedule_buffers()
        nbuff=self._stream._nbuff
        self._frame_counter.reset(nbuff)
        self._stream.start_acquisition(nacq=nbuff if self._acq_params["mode"]=="snap" else None)
        self.call_command("AcquisitionStart")
    def stop_acquisition(self):
        if self.acquisition_in_progress():
            self.call_command("AcquisitionStop")
            self._stream.stop_acquisition()
            self._frame_counter.update_acquired_frames(self._get_acquired_frames())
            self._stream.unschedule_buffers()
    def acquisition_in_progress(self):
        return self._stream is not None and self._stream.is_grabbing()
    def _get_acquired_frames(self):
        return self._stream.get_buffer_status().delivered
    def get_buffer_status(self):
        return self._stream.get_buffer_status()
    

    def enable_raw_readout(self, enable="rows"):
        """
        Enable raw frame transfer.

        Should be used if the camera uses unsupported pixel format.
        Can be ``"frame"`` (return the whole frame as a 1D ``"u1"`` numpy array),
        ``"rows"`` (return a 2D array, where each row corresponds to a single image row),
        or ``False`` (convert to image data, or raise an error if the format is not supported; default).
        In addition, for cameras which incorrectly implement ``"PayloadSize"`` parameter, one can explicitly specify the number
        of bytes per pixel (possibly fractional) which will be used to calculate the total byte size of the frame,
        or the total number of bytes per image (if specified, takes priority over `bytes_per_pixel`).
        Both `bytes_per_pixel` and `bytes_per_image` only apply if `enable` is set to ``"frame"`` or ``"rows"``.
        """
        funcargparse.check_parameter_range(enable,"enable",{False,"rows","frame"})
        self._raw_readout_format=enable

    def _parse_data(self, data, shape, pixel_format):
        fshape=(data.shape[0],)+shape
        if self._raw_readout_format=="frame":
            return data
        if self._raw_readout_format=="rows":
            return data.reshape(fshape[:2]+(-1,))
        supported_formats=["Mono8","Mono10","Mono12","Mono12p","Mono16","Mono32"]
        if pixel_format not in supported_formats:
            sf_string=", ".join(supported_formats)
            raise IDSPeakError("pixel format {} is not supported, only [{}] are supported; raw data readout can be enabled via enable_raw_readout method".format(pixel_format,sf_string))
        if pixel_format=="Mono8":
            return data.reshape(fshape)
        elif pixel_format in ["Mono10","Mono12","Mono16"]:
            return data.view("<u2").reshape(fshape)
        elif pixel_format =="Mono12p":
            return pf.convert_uint12(data.reshape(fshape[0],fshape[1],-1),mode="little_endian",width=fshape[2])
        else:
            return data.view("<u4").reshape(fshape)
    _support_chunks=True
    def _read_frames(self, rng, return_info=False):  # TODO: add parsing and pixel format
        shape=self._get_data_dimensions_rc()
        pixel_format=self.cav["PixelFormat"]
        chunks=self._stream.get_buffers(*rng)
        try:
            chunks=[self._parse_data(ch,shape,pixel_format) for ch in chunks]
        except ValueError:
            print(rng,shape,chunks)
            raise
        if not self._raw_readout_format:
            chunks=[self._convert_indexing(ch,"rct") for ch in chunks]
        return chunks,None