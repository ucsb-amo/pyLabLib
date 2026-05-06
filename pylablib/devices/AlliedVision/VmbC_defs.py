##########   This file is generated automatically based on VmbC.h   ##########

# pylint: disable=unused-import, unused-argument, wrong-spelling-in-comment


import ctypes
import enum
from ...core.utils import ctypes_wrap




def _int32(v): return (v+0x80000000)%0x100000000-0x80000000




##### TYPE DEFINITIONS #####


BOOL=ctypes.c_int
BYTE=ctypes.c_ubyte
PBYTE=ctypes.POINTER(BYTE)
CHAR=ctypes.c_char
PCHAR=ctypes.c_char_p
UCHAR=ctypes.c_ubyte
PUCHAR=ctypes.POINTER(UCHAR)
intptr_t=ctypes.POINTER(ctypes.c_int)
ULONG_PTR=ctypes.c_uint64
LONG_PTR=ctypes.c_int64
WORD=ctypes.c_ushort
DWORD=ctypes.c_ulong
LPWORD=ctypes.POINTER(WORD)
LONG=ctypes.c_long
LONGLONG=ctypes.c_int64
LPLONG=ctypes.POINTER(ctypes.c_long)
HANDLE=ctypes.c_void_p
LPHANDLE=ctypes.POINTER(HANDLE)
PHANDLE=ctypes.POINTER(HANDLE)
HWND=ctypes.c_void_p
HGLOBAL=ctypes.c_void_p
HINSTANCE=ctypes.c_void_p
HDC=ctypes.c_void_p
HMODULE=ctypes.c_void_p
HKEY=ctypes.c_void_p
PVOID=ctypes.c_void_p
LPVOID=ctypes.c_void_p
class RECT(ctypes.Structure):
    _fields_=[  ("left",LONG),
                ("top",LONG),
                ("right",LONG),
                ("bottom",LONG) ]
PRECT=ctypes.POINTER(RECT)
class CRECT(ctypes_wrap.CStructWrapper):
    _struct=RECT


class BITMAPINFOHEADER(ctypes.Structure):
    _fields_=[  ("biSize",DWORD),
                ("biWidth",LONG),
                ("biHeight",LONG),
                ("biPlanes",WORD),
                ("biBitCount",WORD),
                ("biCompression",DWORD),
                ("biSizeImage",DWORD),
                ("biXPelsPerMeter",LONG),
                ("biYPelsPerMeter",LONG),
                ("biClrUsed",DWORD),
                ("biClrImportant",DWORD) ]
PBITMAPINFOHEADER=ctypes.POINTER(BITMAPINFOHEADER)
class CBITMAPINFOHEADER(ctypes_wrap.CStructWrapper):
    _struct=BITMAPINFOHEADER


MirEGLNativeWindowType=ctypes.c_void_p
MirEGLNativeDisplayType=ctypes.c_void_p
VmbUint8_t=ctypes.c_ubyte
VmbInt32_t=ctypes.c_long
VmbUint32_t=ctypes.c_ulong
VmbInt64_t=ctypes.c_longlong
VmbUint64_t=ctypes.c_ulonglong
VmbHandle_t=ctypes.c_void_p
VmbBool_t=BOOL
class VmbBoolVal(enum.IntEnum):
    VmbBoolTrue =_int32(1)
    VmbBoolFalse=_int32(0)
dVmbBoolVal={a.name:a.value for a in VmbBoolVal}
drVmbBoolVal={a.value:a.name for a in VmbBoolVal}


VmbFilePathChar_t=ctypes.c_wchar
class VmbErrorType(enum.IntEnum):
    VmbErrorSuccess                =_int32(0)
    VmbErrorInternalFault          =_int32((-1))
    VmbErrorApiNotStarted          =_int32((-2))
    VmbErrorNotFound               =_int32((-3))
    VmbErrorBadHandle              =_int32((-4))
    VmbErrorDeviceNotOpen          =_int32((-5))
    VmbErrorInvalidAccess          =_int32((-6))
    VmbErrorBadParameter           =_int32((-7))
    VmbErrorStructSize             =_int32((-8))
    VmbErrorMoreData               =_int32((-9))
    VmbErrorWrongType              =_int32((-10))
    VmbErrorInvalidValue           =_int32((-11))
    VmbErrorTimeout                =_int32((-12))
    VmbErrorOther                  =_int32((-13))
    VmbErrorResources              =_int32((-14))
    VmbErrorInvalidCall            =_int32((-15))
    VmbErrorNoTL                   =_int32((-16))
    VmbErrorNotImplemented         =_int32((-17))
    VmbErrorNotSupported           =_int32((-18))
    VmbErrorIncomplete             =_int32((-19))
    VmbErrorIO                     =_int32((-20))
    VmbErrorValidValueSetNotPresent=_int32((-21))
    VmbErrorGenTLUnspecified       =_int32((-22))
    VmbErrorUnspecified            =_int32((-23))
    VmbErrorBusy                   =_int32((-24))
    VmbErrorNoData                 =_int32((-25))
    VmbErrorParsingChunkData       =_int32((-26))
    VmbErrorInUse                  =_int32((-27))
    VmbErrorUnknown                =_int32((-28))
    VmbErrorXml                    =_int32((-29))
    VmbErrorNotAvailable           =_int32((-30))
    VmbErrorNotInitialized         =_int32((-31))
    VmbErrorInvalidAddress         =_int32((-32))
    VmbErrorAlready                =_int32((-33))
    VmbErrorNoChunkData            =_int32((-34))
    VmbErrorUserCallbackException  =_int32((-35))
    VmbErrorFeaturesUnavailable    =_int32((-36))
    VmbErrorTLNotFound             =_int32((-37))
    VmbErrorAmbiguous              =_int32((-38))
    VmbErrorRetriesExceeded        =_int32((-39))
    VmbErrorInsufficientBufferCount=_int32((-40))
    VmbErrorCustom                 =_int32(1)
dVmbErrorType={a.name:a.value for a in VmbErrorType}
drVmbErrorType={a.value:a.name for a in VmbErrorType}


VmbError_t=VmbInt32_t
class VmbVersionInfo_t(ctypes.Structure):
    _fields_=[  ("major",VmbUint32_t),
                ("minor",VmbUint32_t),
                ("patch",VmbUint32_t) ]
PVmbVersionInfo_t=ctypes.POINTER(VmbVersionInfo_t)
class CVmbVersionInfo_t(ctypes_wrap.CStructWrapper):
    _struct=VmbVersionInfo_t


class VmbPixelType(enum.IntEnum):
    VmbPixelMono =_int32(0x01000000)
    VmbPixelColor=_int32(0x02000000)
dVmbPixelType={a.name:a.value for a in VmbPixelType}
drVmbPixelType={a.value:a.name for a in VmbPixelType}


class VmbPixelOccupyType(enum.IntEnum):
    VmbPixelOccupy8Bit =_int32(0x00080000)
    VmbPixelOccupy10Bit=_int32(0x000A0000)
    VmbPixelOccupy12Bit=_int32(0x000C0000)
    VmbPixelOccupy14Bit=_int32(0x000E0000)
    VmbPixelOccupy16Bit=_int32(0x00100000)
    VmbPixelOccupy24Bit=_int32(0x00180000)
    VmbPixelOccupy32Bit=_int32(0x00200000)
    VmbPixelOccupy48Bit=_int32(0x00300000)
    VmbPixelOccupy64Bit=_int32(0x00400000)
dVmbPixelOccupyType={a.name:a.value for a in VmbPixelOccupyType}
drVmbPixelOccupyType={a.value:a.name for a in VmbPixelOccupyType}


class VmbPixelFormatType(enum.IntEnum):
    VmbPixelFormatMono8                  =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy8Bit.value)|0x0001))
    VmbPixelFormatMono10                 =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0003))
    VmbPixelFormatMono10p                =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy10Bit.value)|0x0046))
    VmbPixelFormatMono12                 =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0005))
    VmbPixelFormatMono12Packed           =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x0006))
    VmbPixelFormatMono12p                =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x0047))
    VmbPixelFormatMono14                 =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0025))
    VmbPixelFormatMono16                 =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0007))
    VmbPixelFormatBayerGR8               =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy8Bit.value)|0x0008))
    VmbPixelFormatBayerRG8               =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy8Bit.value)|0x0009))
    VmbPixelFormatBayerGB8               =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy8Bit.value)|0x000A))
    VmbPixelFormatBayerBG8               =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy8Bit.value)|0x000B))
    VmbPixelFormatBayerGR10              =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x000C))
    VmbPixelFormatBayerRG10              =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x000D))
    VmbPixelFormatBayerGB10              =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x000E))
    VmbPixelFormatBayerBG10              =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x000F))
    VmbPixelFormatBayerGR12              =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0010))
    VmbPixelFormatBayerRG12              =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0011))
    VmbPixelFormatBayerGB12              =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0012))
    VmbPixelFormatBayerBG12              =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0013))
    VmbPixelFormatBayerGR12Packed        =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x002A))
    VmbPixelFormatBayerRG12Packed        =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x002B))
    VmbPixelFormatBayerGB12Packed        =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x002C))
    VmbPixelFormatBayerBG12Packed        =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x002D))
    VmbPixelFormatBayerGR10p             =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy10Bit.value)|0x0056))
    VmbPixelFormatBayerRG10p             =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy10Bit.value)|0x0058))
    VmbPixelFormatBayerGB10p             =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy10Bit.value)|0x0054))
    VmbPixelFormatBayerBG10p             =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy10Bit.value)|0x0052))
    VmbPixelFormatBayerGR12p             =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x0057))
    VmbPixelFormatBayerRG12p             =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x0059))
    VmbPixelFormatBayerGB12p             =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x0055))
    VmbPixelFormatBayerBG12p             =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x0053))
    VmbPixelFormatBayerGR16              =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x002E))
    VmbPixelFormatBayerRG16              =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x002F))
    VmbPixelFormatBayerGB16              =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0030))
    VmbPixelFormatBayerBG16              =_int32(((VmbPixelType.VmbPixelMono.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0031))
    VmbPixelFormatRgb8                   =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy24Bit.value)|0x0014))
    VmbPixelFormatBgr8                   =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy24Bit.value)|0x0015))
    VmbPixelFormatRgb10                  =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy48Bit.value)|0x0018))
    VmbPixelFormatBgr10                  =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy48Bit.value)|0x0019))
    VmbPixelFormatRgb12                  =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy48Bit.value)|0x001A))
    VmbPixelFormatBgr12                  =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy48Bit.value)|0x001B))
    VmbPixelFormatRgb14                  =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy48Bit.value)|0x005E))
    VmbPixelFormatBgr14                  =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy48Bit.value)|0x004A))
    VmbPixelFormatRgb16                  =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy48Bit.value)|0x0033))
    VmbPixelFormatBgr16                  =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy48Bit.value)|0x004B))
    VmbPixelFormatArgb8                  =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy32Bit.value)|0x0016))
    VmbPixelFormatRgba8                  =_int32(VmbPixelFormatArgb8)
    VmbPixelFormatBgra8                  =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy32Bit.value)|0x0017))
    VmbPixelFormatRgba10                 =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy64Bit.value)|0x005F))
    VmbPixelFormatBgra10                 =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy64Bit.value)|0x004C))
    VmbPixelFormatRgba12                 =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy64Bit.value)|0x0061))
    VmbPixelFormatBgra12                 =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy64Bit.value)|0x004E))
    VmbPixelFormatRgba14                 =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy64Bit.value)|0x0063))
    VmbPixelFormatBgra14                 =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy64Bit.value)|0x0050))
    VmbPixelFormatRgba16                 =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy64Bit.value)|0x0064))
    VmbPixelFormatBgra16                 =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy64Bit.value)|0x0051))
    VmbPixelFormatYuv411                 =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x001E))
    VmbPixelFormatYuv422                 =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x001F))
    VmbPixelFormatYuv444                 =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy24Bit.value)|0x0020))
    VmbPixelFormatYuv422_8               =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0032))
    VmbPixelFormatYCbCr8_CbYCr           =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy24Bit.value)|0x003A))
    VmbPixelFormatYCbCr422_8             =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x003B))
    VmbPixelFormatYCbCr411_8_CbYYCrYY    =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x003C))
    VmbPixelFormatYCbCr601_8_CbYCr       =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy24Bit.value)|0x003D))
    VmbPixelFormatYCbCr601_422_8         =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x003E))
    VmbPixelFormatYCbCr601_411_8_CbYYCrYY=_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x003F))
    VmbPixelFormatYCbCr709_8_CbYCr       =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy24Bit.value)|0x0040))
    VmbPixelFormatYCbCr709_422_8         =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0041))
    VmbPixelFormatYCbCr709_411_8_CbYYCrYY=_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x0042))
    VmbPixelFormatYCbCr422_8_CbYCrY      =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0043))
    VmbPixelFormatYCbCr601_422_8_CbYCrY  =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0044))
    VmbPixelFormatYCbCr709_422_8_CbYCrY  =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy16Bit.value)|0x0045))
    VmbPixelFormatYCbCr411_8             =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy12Bit.value)|0x005A))
    VmbPixelFormatYCbCr8                 =_int32(((VmbPixelType.VmbPixelColor.value|VmbPixelOccupyType.VmbPixelOccupy24Bit.value)|0x005B))
    VmbPixelFormatLast                   =_int32(VmbPixelFormatYCbCr8+1)
dVmbPixelFormatType={a.name:a.value for a in VmbPixelFormatType}
drVmbPixelFormatType={a.value:a.name for a in VmbPixelFormatType}


VmbPixelFormat_t=VmbUint32_t
class VmbTransportLayerType(enum.IntEnum):
    VmbTransportLayerTypeUnknown =_int32(0)
    VmbTransportLayerTypeGEV     =_int32(1)
    VmbTransportLayerTypeCL      =_int32(2)
    VmbTransportLayerTypeIIDC    =_int32(3)
    VmbTransportLayerTypeUVC     =_int32(4)
    VmbTransportLayerTypeCXP     =_int32(5)
    VmbTransportLayerTypeCLHS    =_int32(6)
    VmbTransportLayerTypeU3V     =_int32(7)
    VmbTransportLayerTypeEthernet=_int32(8)
    VmbTransportLayerTypePCI     =_int32(9)
    VmbTransportLayerTypeCustom  =_int32(10)
    VmbTransportLayerTypeMixed   =_int32(11)
dVmbTransportLayerType={a.name:a.value for a in VmbTransportLayerType}
drVmbTransportLayerType={a.value:a.name for a in VmbTransportLayerType}


VmbTransportLayerType_t=VmbUint32_t
class VmbTransportLayerInfo_t(ctypes.Structure):
    _fields_=[  ("transportLayerIdString",ctypes.c_char_p),
                ("transportLayerName",ctypes.c_char_p),
                ("transportLayerModelName",ctypes.c_char_p),
                ("transportLayerVendor",ctypes.c_char_p),
                ("transportLayerVersion",ctypes.c_char_p),
                ("transportLayerPath",ctypes.c_char_p),
                ("transportLayerHandle",VmbHandle_t),
                ("transportLayerType",VmbTransportLayerType_t) ]
PVmbTransportLayerInfo_t=ctypes.POINTER(VmbTransportLayerInfo_t)
class CVmbTransportLayerInfo_t(ctypes_wrap.CStructWrapper):
    _struct=VmbTransportLayerInfo_t


class VmbInterfaceInfo_t(ctypes.Structure):
    _fields_=[  ("interfaceIdString",ctypes.c_char_p),
                ("interfaceName",ctypes.c_char_p),
                ("interfaceHandle",VmbHandle_t),
                ("transportLayerHandle",VmbHandle_t),
                ("interfaceType",VmbTransportLayerType_t) ]
PVmbInterfaceInfo_t=ctypes.POINTER(VmbInterfaceInfo_t)
class CVmbInterfaceInfo_t(ctypes_wrap.CStructWrapper):
    _struct=VmbInterfaceInfo_t


class VmbAccessModeType(enum.IntEnum):
    VmbAccessModeNone     =_int32(0)
    VmbAccessModeFull     =_int32(1)
    VmbAccessModeRead     =_int32(2)
    VmbAccessModeUnknown  =_int32(4)
    VmbAccessModeExclusive=_int32(8)
dVmbAccessModeType={a.name:a.value for a in VmbAccessModeType}
drVmbAccessModeType={a.value:a.name for a in VmbAccessModeType}


VmbAccessMode_t=VmbUint32_t
class VmbCameraInfo_t(ctypes.Structure):
    _fields_=[  ("cameraIdString",ctypes.c_char_p),
                ("cameraIdExtended",ctypes.c_char_p),
                ("cameraName",ctypes.c_char_p),
                ("modelName",ctypes.c_char_p),
                ("serialString",ctypes.c_char_p),
                ("transportLayerHandle",VmbHandle_t),
                ("interfaceHandle",VmbHandle_t),
                ("localDeviceHandle",VmbHandle_t),
                ("streamHandles",ctypes.POINTER(VmbHandle_t)),
                ("streamCount",VmbUint32_t),
                ("permittedAccess",VmbAccessMode_t) ]
PVmbCameraInfo_t=ctypes.POINTER(VmbCameraInfo_t)
class CVmbCameraInfo_t(ctypes_wrap.CStructWrapper):
    _struct=VmbCameraInfo_t


class VmbFeatureDataType(enum.IntEnum):
    VmbFeatureDataUnknown=_int32(0)
    VmbFeatureDataInt    =_int32(1)
    VmbFeatureDataFloat  =_int32(2)
    VmbFeatureDataEnum   =_int32(3)
    VmbFeatureDataString =_int32(4)
    VmbFeatureDataBool   =_int32(5)
    VmbFeatureDataCommand=_int32(6)
    VmbFeatureDataRaw    =_int32(7)
    VmbFeatureDataNone   =_int32(8)
dVmbFeatureDataType={a.name:a.value for a in VmbFeatureDataType}
drVmbFeatureDataType={a.value:a.name for a in VmbFeatureDataType}


VmbFeatureData_t=VmbUint32_t
class VmbFeatureVisibilityType(enum.IntEnum):
    VmbFeatureVisibilityUnknown  =_int32(0)
    VmbFeatureVisibilityBeginner =_int32(1)
    VmbFeatureVisibilityExpert   =_int32(2)
    VmbFeatureVisibilityGuru     =_int32(3)
    VmbFeatureVisibilityInvisible=_int32(4)
dVmbFeatureVisibilityType={a.name:a.value for a in VmbFeatureVisibilityType}
drVmbFeatureVisibilityType={a.value:a.name for a in VmbFeatureVisibilityType}


VmbFeatureVisibility_t=VmbUint32_t
class VmbFeatureFlagsType(enum.IntEnum):
    VmbFeatureFlagsNone       =_int32(0)
    VmbFeatureFlagsRead       =_int32(1)
    VmbFeatureFlagsWrite      =_int32(2)
    VmbFeatureFlagsVolatile   =_int32(8)
    VmbFeatureFlagsModifyWrite=_int32(16)
dVmbFeatureFlagsType={a.name:a.value for a in VmbFeatureFlagsType}
drVmbFeatureFlagsType={a.value:a.name for a in VmbFeatureFlagsType}


VmbFeatureFlags_t=VmbUint32_t
class VmbFeatureInfo_t(ctypes.Structure):
    _fields_=[  ("name",ctypes.c_char_p),
                ("category",ctypes.c_char_p),
                ("displayName",ctypes.c_char_p),
                ("tooltip",ctypes.c_char_p),
                ("description",ctypes.c_char_p),
                ("sfncNamespace",ctypes.c_char_p),
                ("unit",ctypes.c_char_p),
                ("representation",ctypes.c_char_p),
                ("featureDataType",VmbFeatureData_t),
                ("featureFlags",VmbFeatureFlags_t),
                ("pollingTime",VmbUint32_t),
                ("visibility",VmbFeatureVisibility_t),
                ("isStreamable",VmbBool_t),
                ("hasSelectedFeatures",VmbBool_t) ]
PVmbFeatureInfo_t=ctypes.POINTER(VmbFeatureInfo_t)
class CVmbFeatureInfo_t(ctypes_wrap.CStructWrapper):
    _struct=VmbFeatureInfo_t


class VmbFeatureEnumEntry_t(ctypes.Structure):
    _fields_=[  ("name",ctypes.c_char_p),
                ("displayName",ctypes.c_char_p),
                ("tooltip",ctypes.c_char_p),
                ("description",ctypes.c_char_p),
                ("intValue",VmbInt64_t),
                ("sfncNamespace",ctypes.c_char_p),
                ("visibility",VmbFeatureVisibility_t) ]
PVmbFeatureEnumEntry_t=ctypes.POINTER(VmbFeatureEnumEntry_t)
class CVmbFeatureEnumEntry_t(ctypes_wrap.CStructWrapper):
    _struct=VmbFeatureEnumEntry_t


class VmbFrameStatusType(enum.IntEnum):
    VmbFrameStatusComplete  =_int32(0)
    VmbFrameStatusIncomplete=_int32((-1))
    VmbFrameStatusTooSmall  =_int32((-2))
    VmbFrameStatusInvalid   =_int32((-3))
dVmbFrameStatusType={a.name:a.value for a in VmbFrameStatusType}
drVmbFrameStatusType={a.value:a.name for a in VmbFrameStatusType}


VmbFrameStatus_t=VmbInt32_t
class VmbFrameFlagsType(enum.IntEnum):
    VmbFrameFlagsNone            =_int32(0)
    VmbFrameFlagsDimension       =_int32(1)
    VmbFrameFlagsOffset          =_int32(2)
    VmbFrameFlagsFrameID         =_int32(4)
    VmbFrameFlagsTimestamp       =_int32(8)
    VmbFrameFlagsImageData       =_int32(16)
    VmbFrameFlagsPayloadType     =_int32(32)
    VmbFrameFlagsChunkDataPresent=_int32(64)
dVmbFrameFlagsType={a.name:a.value for a in VmbFrameFlagsType}
drVmbFrameFlagsType={a.value:a.name for a in VmbFrameFlagsType}


VmbFrameFlags_t=VmbUint32_t
class VmbPayloadType(enum.IntEnum):
    VmbPayloadTypeUnknown       =_int32(0)
    VmbPayloadTypeImage         =_int32(1)
    VmbPayloadTypeRaw           =_int32(2)
    VmbPayloadTypeFile          =_int32(3)
    VmbPayloadTypeJPEG          =_int32(5)
    VmbPayloadTypJPEG2000       =_int32(6)
    VmbPayloadTypeH264          =_int32(7)
    VmbPayloadTypeChunkOnly     =_int32(8)
    VmbPayloadTypeDeviceSpecific=_int32(9)
    VmbPayloadTypeGenDC         =_int32(11)
dVmbPayloadType={a.name:a.value for a in VmbPayloadType}
drVmbPayloadType={a.value:a.name for a in VmbPayloadType}


VmbPayloadType_t=VmbUint32_t
VmbImageDimension_t=VmbUint32_t
class VmbFrame_t(ctypes.Structure):
    _fields_=[  ("buffer",ctypes.c_void_p),
                ("bufferSize",VmbUint32_t),
                ("context",ctypes.c_void_p*4),
                ("receiveStatus",VmbFrameStatus_t),
                ("frameID",VmbUint64_t),
                ("timestamp",VmbUint64_t),
                ("imageData",ctypes.POINTER(VmbUint8_t)),
                ("receiveFlags",VmbFrameFlags_t),
                ("pixelFormat",VmbPixelFormat_t),
                ("width",VmbImageDimension_t),
                ("height",VmbImageDimension_t),
                ("offsetX",VmbImageDimension_t),
                ("offsetY",VmbImageDimension_t),
                ("payloadType",VmbPayloadType_t),
                ("chunkDataPresent",VmbBool_t) ]
PVmbFrame_t=ctypes.POINTER(VmbFrame_t)
class CVmbFrame_t(ctypes_wrap.CStructWrapper):
    _struct=VmbFrame_t


class VmbFeaturePersistType(enum.IntEnum):
    VmbFeaturePersistAll       =_int32(0)
    VmbFeaturePersistStreamable=_int32(1)
    VmbFeaturePersistNoLUT     =_int32(2)
dVmbFeaturePersistType={a.name:a.value for a in VmbFeaturePersistType}
drVmbFeaturePersistType={a.value:a.name for a in VmbFeaturePersistType}


VmbFeaturePersist_t=VmbUint32_t
class VmbModulePersistFlagsType(enum.IntEnum):
    VmbModulePersistFlagsNone          =_int32(0x00)
    VmbModulePersistFlagsTransportLayer=_int32(0x01)
    VmbModulePersistFlagsInterface     =_int32(0x02)
    VmbModulePersistFlagsRemoteDevice  =_int32(0x04)
    VmbModulePersistFlagsLocalDevice   =_int32(0x08)
    VmbModulePersistFlagsStreams       =_int32(0x10)
    VmbModulePersistFlagsAll           =_int32(0xff)
dVmbModulePersistFlagsType={a.name:a.value for a in VmbModulePersistFlagsType}
drVmbModulePersistFlagsType={a.value:a.name for a in VmbModulePersistFlagsType}


VmbModulePersistFlags_t=VmbUint32_t
class VmbLogLevel(enum.IntEnum):
    VmbLogLevelNone =_int32(0)
    VmbLogLevelError=_int32(VmbLogLevelNone+1)
    VmbLogLevelDebug=_int32(VmbLogLevelError+1)
    VmbLogLevelWarn =_int32(VmbLogLevelDebug+1)
    VmbLogLevelTrace=_int32(VmbLogLevelWarn+1)
    VmbLogLevelAll  =_int32(VmbLogLevelTrace)
dVmbLogLevel={a.name:a.value for a in VmbLogLevel}
drVmbLogLevel={a.value:a.name for a in VmbLogLevel}


VmbLogLevel_t=VmbUint32_t
class VmbFeaturePersistSettings_t(ctypes.Structure):
    _fields_=[  ("persistType",VmbFeaturePersist_t),
                ("modulePersistFlags",VmbModulePersistFlags_t),
                ("maxIterations",VmbUint32_t),
                ("loggingLevel",VmbLogLevel_t) ]
PVmbFeaturePersistSettings_t=ctypes.POINTER(VmbFeaturePersistSettings_t)
class CVmbFeaturePersistSettings_t(ctypes_wrap.CStructWrapper):
    _struct=VmbFeaturePersistSettings_t


VmbInvalidationCallback=ctypes.c_void_p
VmbFrameCallback=ctypes.c_void_p
VmbChunkAccessCallback=ctypes.c_void_p



##### FUNCTION DEFINITIONS #####





def addfunc(lib, name, restype, argtypes=None, argnames=None):
    if getattr(lib,name,None) is None:
        setattr(lib,name,None)
    else:
        func=getattr(lib,name)
        func.restype=restype
        if argtypes is not None:
            func.argtypes=argtypes
        if argnames is not None:
            func.argnames=argnames

def define_functions(lib):
    #  VmbError_t VmbVersionQuery(ctypes.POINTER(VmbVersionInfo_t) versionInfo, VmbUint32_t sizeofVersionInfo)
    addfunc(lib, "VmbVersionQuery", restype = VmbError_t,
            argtypes = [ctypes.POINTER(VmbVersionInfo_t), VmbUint32_t],
            argnames = ["versionInfo", "sizeofVersionInfo"] )
    #  VmbError_t VmbStartup(ctypes.c_wchar_p pathConfiguration)
    addfunc(lib, "VmbStartup", restype = VmbError_t,
            argtypes = [ctypes.c_wchar_p],
            argnames = ["pathConfiguration"] )
    #  None VmbShutdown()
    addfunc(lib, "VmbShutdown", restype = None,
            argtypes = [],
            argnames = [] )
    #  VmbError_t VmbCamerasList(ctypes.POINTER(VmbCameraInfo_t) cameraInfo, VmbUint32_t listLength, ctypes.POINTER(VmbUint32_t) numFound, VmbUint32_t sizeofCameraInfo)
    addfunc(lib, "VmbCamerasList", restype = VmbError_t,
            argtypes = [ctypes.POINTER(VmbCameraInfo_t), VmbUint32_t, ctypes.POINTER(VmbUint32_t), VmbUint32_t],
            argnames = ["cameraInfo", "listLength", "numFound", "sizeofCameraInfo"] )
    #  VmbError_t VmbCameraInfoQueryByHandle(VmbHandle_t cameraHandle, ctypes.POINTER(VmbCameraInfo_t) info, VmbUint32_t sizeofCameraInfo)
    addfunc(lib, "VmbCameraInfoQueryByHandle", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.POINTER(VmbCameraInfo_t), VmbUint32_t],
            argnames = ["cameraHandle", "info", "sizeofCameraInfo"] )
    #  VmbError_t VmbCameraInfoQuery(ctypes.c_char_p idString, ctypes.POINTER(VmbCameraInfo_t) info, VmbUint32_t sizeofCameraInfo)
    addfunc(lib, "VmbCameraInfoQuery", restype = VmbError_t,
            argtypes = [ctypes.c_char_p, ctypes.POINTER(VmbCameraInfo_t), VmbUint32_t],
            argnames = ["idString", "info", "sizeofCameraInfo"] )
    #  VmbError_t VmbCameraOpen(ctypes.c_char_p idString, VmbAccessMode_t accessMode, ctypes.POINTER(VmbHandle_t) cameraHandle)
    addfunc(lib, "VmbCameraOpen", restype = VmbError_t,
            argtypes = [ctypes.c_char_p, VmbAccessMode_t, ctypes.POINTER(VmbHandle_t)],
            argnames = ["idString", "accessMode", "cameraHandle"] )
    #  VmbError_t VmbCameraClose(VmbHandle_t cameraHandle)
    addfunc(lib, "VmbCameraClose", restype = VmbError_t,
            argtypes = [VmbHandle_t],
            argnames = ["cameraHandle"] )
    #  VmbError_t VmbFeaturesList(VmbHandle_t handle, ctypes.POINTER(VmbFeatureInfo_t) featureInfoList, VmbUint32_t listLength, ctypes.POINTER(VmbUint32_t) numFound, VmbUint32_t sizeofFeatureInfo)
    addfunc(lib, "VmbFeaturesList", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.POINTER(VmbFeatureInfo_t), VmbUint32_t, ctypes.POINTER(VmbUint32_t), VmbUint32_t],
            argnames = ["handle", "featureInfoList", "listLength", "numFound", "sizeofFeatureInfo"] )
    #  VmbError_t VmbFeatureInfoQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbFeatureInfo_t) featureInfo, VmbUint32_t sizeofFeatureInfo)
    addfunc(lib, "VmbFeatureInfoQuery", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(VmbFeatureInfo_t), VmbUint32_t],
            argnames = ["handle", "name", "featureInfo", "sizeofFeatureInfo"] )
    #  VmbError_t VmbFeatureListSelected(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbFeatureInfo_t) featureInfoList, VmbUint32_t listLength, ctypes.POINTER(VmbUint32_t) numFound, VmbUint32_t sizeofFeatureInfo)
    addfunc(lib, "VmbFeatureListSelected", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(VmbFeatureInfo_t), VmbUint32_t, ctypes.POINTER(VmbUint32_t), VmbUint32_t],
            argnames = ["handle", "name", "featureInfoList", "listLength", "numFound", "sizeofFeatureInfo"] )
    #  VmbError_t VmbFeatureAccessQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbBool_t) isReadable, ctypes.POINTER(VmbBool_t) isWriteable)
    addfunc(lib, "VmbFeatureAccessQuery", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(VmbBool_t), ctypes.POINTER(VmbBool_t)],
            argnames = ["handle", "name", "isReadable", "isWriteable"] )
    #  VmbError_t VmbFeatureIntGet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbInt64_t) value)
    addfunc(lib, "VmbFeatureIntGet", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(VmbInt64_t)],
            argnames = ["handle", "name", "value"] )
    #  VmbError_t VmbFeatureIntSet(VmbHandle_t handle, ctypes.c_char_p name, VmbInt64_t value)
    addfunc(lib, "VmbFeatureIntSet", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, VmbInt64_t],
            argnames = ["handle", "name", "value"] )
    #  VmbError_t VmbFeatureIntRangeQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbInt64_t) min, ctypes.POINTER(VmbInt64_t) max)
    addfunc(lib, "VmbFeatureIntRangeQuery", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(VmbInt64_t), ctypes.POINTER(VmbInt64_t)],
            argnames = ["handle", "name", "min", "max"] )
    #  VmbError_t VmbFeatureIntIncrementQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbInt64_t) value)
    addfunc(lib, "VmbFeatureIntIncrementQuery", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(VmbInt64_t)],
            argnames = ["handle", "name", "value"] )
    #  VmbError_t VmbFeatureIntValidValueSetQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbInt64_t) buffer, VmbUint32_t bufferSize, ctypes.POINTER(VmbUint32_t) setSize)
    addfunc(lib, "VmbFeatureIntValidValueSetQuery", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(VmbInt64_t), VmbUint32_t, ctypes.POINTER(VmbUint32_t)],
            argnames = ["handle", "name", "buffer", "bufferSize", "setSize"] )
    #  VmbError_t VmbFeatureFloatGet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(ctypes.c_double) value)
    addfunc(lib, "VmbFeatureFloatGet", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)],
            argnames = ["handle", "name", "value"] )
    #  VmbError_t VmbFeatureFloatSet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_double value)
    addfunc(lib, "VmbFeatureFloatSet", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.c_double],
            argnames = ["handle", "name", "value"] )
    #  VmbError_t VmbFeatureFloatRangeQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(ctypes.c_double) min, ctypes.POINTER(ctypes.c_double) max)
    addfunc(lib, "VmbFeatureFloatRangeQuery", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)],
            argnames = ["handle", "name", "min", "max"] )
    #  VmbError_t VmbFeatureFloatIncrementQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbBool_t) hasIncrement, ctypes.POINTER(ctypes.c_double) value)
    addfunc(lib, "VmbFeatureFloatIncrementQuery", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(VmbBool_t), ctypes.POINTER(ctypes.c_double)],
            argnames = ["handle", "name", "hasIncrement", "value"] )
    #  VmbError_t VmbFeatureEnumGet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(ctypes.c_char_p) value)
    addfunc(lib, "VmbFeatureEnumGet", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p)],
            argnames = ["handle", "name", "value"] )
    #  VmbError_t VmbFeatureEnumSet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_char_p value)
    addfunc(lib, "VmbFeatureEnumSet", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.c_char_p],
            argnames = ["handle", "name", "value"] )
    #  VmbError_t VmbFeatureEnumRangeQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(ctypes.c_char_p) nameArray, VmbUint32_t arrayLength, ctypes.POINTER(VmbUint32_t) numFound)
    addfunc(lib, "VmbFeatureEnumRangeQuery", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), VmbUint32_t, ctypes.POINTER(VmbUint32_t)],
            argnames = ["handle", "name", "nameArray", "arrayLength", "numFound"] )
    #  VmbError_t VmbFeatureEnumIsAvailable(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_char_p value, ctypes.POINTER(VmbBool_t) isAvailable)
    addfunc(lib, "VmbFeatureEnumIsAvailable", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(VmbBool_t)],
            argnames = ["handle", "name", "value", "isAvailable"] )
    #  VmbError_t VmbFeatureEnumAsInt(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_char_p value, ctypes.POINTER(VmbInt64_t) intVal)
    addfunc(lib, "VmbFeatureEnumAsInt", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(VmbInt64_t)],
            argnames = ["handle", "name", "value", "intVal"] )
    #  VmbError_t VmbFeatureEnumAsString(VmbHandle_t handle, ctypes.c_char_p name, VmbInt64_t intValue, ctypes.POINTER(ctypes.c_char_p) stringValue)
    addfunc(lib, "VmbFeatureEnumAsString", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, VmbInt64_t, ctypes.POINTER(ctypes.c_char_p)],
            argnames = ["handle", "name", "intValue", "stringValue"] )
    #  VmbError_t VmbFeatureEnumEntryGet(VmbHandle_t handle, ctypes.c_char_p featureName, ctypes.c_char_p entryName, ctypes.POINTER(VmbFeatureEnumEntry_t) featureEnumEntry, VmbUint32_t sizeofFeatureEnumEntry)
    addfunc(lib, "VmbFeatureEnumEntryGet", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(VmbFeatureEnumEntry_t), VmbUint32_t],
            argnames = ["handle", "featureName", "entryName", "featureEnumEntry", "sizeofFeatureEnumEntry"] )
    #  VmbError_t VmbFeatureStringGet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_char_p buffer, VmbUint32_t bufferSize, ctypes.POINTER(VmbUint32_t) sizeFilled)
    addfunc(lib, "VmbFeatureStringGet", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.c_char_p, VmbUint32_t, ctypes.POINTER(VmbUint32_t)],
            argnames = ["handle", "name", "buffer", "bufferSize", "sizeFilled"] )
    #  VmbError_t VmbFeatureStringSet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_char_p value)
    addfunc(lib, "VmbFeatureStringSet", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.c_char_p],
            argnames = ["handle", "name", "value"] )
    #  VmbError_t VmbFeatureStringMaxlengthQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbUint32_t) maxLength)
    addfunc(lib, "VmbFeatureStringMaxlengthQuery", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(VmbUint32_t)],
            argnames = ["handle", "name", "maxLength"] )
    #  VmbError_t VmbFeatureBoolGet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbBool_t) value)
    addfunc(lib, "VmbFeatureBoolGet", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(VmbBool_t)],
            argnames = ["handle", "name", "value"] )
    #  VmbError_t VmbFeatureBoolSet(VmbHandle_t handle, ctypes.c_char_p name, VmbBool_t value)
    addfunc(lib, "VmbFeatureBoolSet", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, VmbBool_t],
            argnames = ["handle", "name", "value"] )
    #  VmbError_t VmbFeatureCommandRun(VmbHandle_t handle, ctypes.c_char_p name)
    addfunc(lib, "VmbFeatureCommandRun", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p],
            argnames = ["handle", "name"] )
    #  VmbError_t VmbFeatureCommandIsDone(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbBool_t) isDone)
    addfunc(lib, "VmbFeatureCommandIsDone", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(VmbBool_t)],
            argnames = ["handle", "name", "isDone"] )
    #  VmbError_t VmbFeatureRawGet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_char_p buffer, VmbUint32_t bufferSize, ctypes.POINTER(VmbUint32_t) sizeFilled)
    addfunc(lib, "VmbFeatureRawGet", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.c_char_p, VmbUint32_t, ctypes.POINTER(VmbUint32_t)],
            argnames = ["handle", "name", "buffer", "bufferSize", "sizeFilled"] )
    #  VmbError_t VmbFeatureRawSet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_char_p buffer, VmbUint32_t bufferSize)
    addfunc(lib, "VmbFeatureRawSet", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.c_char_p, VmbUint32_t],
            argnames = ["handle", "name", "buffer", "bufferSize"] )
    #  VmbError_t VmbFeatureRawLengthQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbUint32_t) length)
    addfunc(lib, "VmbFeatureRawLengthQuery", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, ctypes.POINTER(VmbUint32_t)],
            argnames = ["handle", "name", "length"] )
    #  VmbError_t VmbFeatureInvalidationRegister(VmbHandle_t handle, ctypes.c_char_p name, VmbInvalidationCallback callback, ctypes.c_void_p userContext)
    addfunc(lib, "VmbFeatureInvalidationRegister", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, VmbInvalidationCallback, ctypes.c_void_p],
            argnames = ["handle", "name", "callback", "userContext"] )
    #  VmbError_t VmbFeatureInvalidationUnregister(VmbHandle_t handle, ctypes.c_char_p name, VmbInvalidationCallback callback)
    addfunc(lib, "VmbFeatureInvalidationUnregister", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_char_p, VmbInvalidationCallback],
            argnames = ["handle", "name", "callback"] )
    #  VmbError_t VmbPayloadSizeGet(VmbHandle_t handle, ctypes.POINTER(VmbUint32_t) payloadSize)
    addfunc(lib, "VmbPayloadSizeGet", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.POINTER(VmbUint32_t)],
            argnames = ["handle", "payloadSize"] )
    #  VmbError_t VmbFrameAnnounce(VmbHandle_t handle, ctypes.POINTER(VmbFrame_t) frame, VmbUint32_t sizeofFrame)
    addfunc(lib, "VmbFrameAnnounce", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.POINTER(VmbFrame_t), VmbUint32_t],
            argnames = ["handle", "frame", "sizeofFrame"] )
    #  VmbError_t VmbFrameRevoke(VmbHandle_t handle, ctypes.POINTER(VmbFrame_t) frame)
    addfunc(lib, "VmbFrameRevoke", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.POINTER(VmbFrame_t)],
            argnames = ["handle", "frame"] )
    #  VmbError_t VmbFrameRevokeAll(VmbHandle_t handle)
    addfunc(lib, "VmbFrameRevokeAll", restype = VmbError_t,
            argtypes = [VmbHandle_t],
            argnames = ["handle"] )
    #  VmbError_t VmbCaptureStart(VmbHandle_t handle)
    addfunc(lib, "VmbCaptureStart", restype = VmbError_t,
            argtypes = [VmbHandle_t],
            argnames = ["handle"] )
    #  VmbError_t VmbCaptureEnd(VmbHandle_t handle)
    addfunc(lib, "VmbCaptureEnd", restype = VmbError_t,
            argtypes = [VmbHandle_t],
            argnames = ["handle"] )
    #  VmbError_t VmbCaptureFrameQueue(VmbHandle_t handle, ctypes.POINTER(VmbFrame_t) frame, VmbFrameCallback callback)
    addfunc(lib, "VmbCaptureFrameQueue", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.POINTER(VmbFrame_t), VmbFrameCallback],
            argnames = ["handle", "frame", "callback"] )
    #  VmbError_t VmbCaptureFrameWait(VmbHandle_t handle, ctypes.POINTER(VmbFrame_t) frame, VmbUint32_t timeout)
    addfunc(lib, "VmbCaptureFrameWait", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.POINTER(VmbFrame_t), VmbUint32_t],
            argnames = ["handle", "frame", "timeout"] )
    #  VmbError_t VmbCaptureQueueFlush(VmbHandle_t handle)
    addfunc(lib, "VmbCaptureQueueFlush", restype = VmbError_t,
            argtypes = [VmbHandle_t],
            argnames = ["handle"] )
    #  VmbError_t VmbTransportLayersList(ctypes.POINTER(VmbTransportLayerInfo_t) transportLayerInfo, VmbUint32_t listLength, ctypes.POINTER(VmbUint32_t) numFound, VmbUint32_t sizeofTransportLayerInfo)
    addfunc(lib, "VmbTransportLayersList", restype = VmbError_t,
            argtypes = [ctypes.POINTER(VmbTransportLayerInfo_t), VmbUint32_t, ctypes.POINTER(VmbUint32_t), VmbUint32_t],
            argnames = ["transportLayerInfo", "listLength", "numFound", "sizeofTransportLayerInfo"] )
    #  VmbError_t VmbInterfacesList(ctypes.POINTER(VmbInterfaceInfo_t) interfaceInfo, VmbUint32_t listLength, ctypes.POINTER(VmbUint32_t) numFound, VmbUint32_t sizeofInterfaceInfo)
    addfunc(lib, "VmbInterfacesList", restype = VmbError_t,
            argtypes = [ctypes.POINTER(VmbInterfaceInfo_t), VmbUint32_t, ctypes.POINTER(VmbUint32_t), VmbUint32_t],
            argnames = ["interfaceInfo", "listLength", "numFound", "sizeofInterfaceInfo"] )
    #  VmbError_t VmbMemoryRead(VmbHandle_t handle, VmbUint64_t address, VmbUint32_t bufferSize, ctypes.c_char_p dataBuffer, ctypes.POINTER(VmbUint32_t) sizeComplete)
    addfunc(lib, "VmbMemoryRead", restype = VmbError_t,
            argtypes = [VmbHandle_t, VmbUint64_t, VmbUint32_t, ctypes.c_char_p, ctypes.POINTER(VmbUint32_t)],
            argnames = ["handle", "address", "bufferSize", "dataBuffer", "sizeComplete"] )
    #  VmbError_t VmbMemoryWrite(VmbHandle_t handle, VmbUint64_t address, VmbUint32_t bufferSize, ctypes.c_char_p dataBuffer, ctypes.POINTER(VmbUint32_t) sizeComplete)
    addfunc(lib, "VmbMemoryWrite", restype = VmbError_t,
            argtypes = [VmbHandle_t, VmbUint64_t, VmbUint32_t, ctypes.c_char_p, ctypes.POINTER(VmbUint32_t)],
            argnames = ["handle", "address", "bufferSize", "dataBuffer", "sizeComplete"] )
    #  VmbError_t VmbSettingsSave(VmbHandle_t handle, ctypes.c_wchar_p filePath, ctypes.POINTER(VmbFeaturePersistSettings_t) settings, VmbUint32_t sizeofSettings)
    addfunc(lib, "VmbSettingsSave", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_wchar_p, ctypes.POINTER(VmbFeaturePersistSettings_t), VmbUint32_t],
            argnames = ["handle", "filePath", "settings", "sizeofSettings"] )
    #  VmbError_t VmbSettingsLoad(VmbHandle_t handle, ctypes.c_wchar_p filePath, ctypes.POINTER(VmbFeaturePersistSettings_t) settings, VmbUint32_t sizeofSettings)
    addfunc(lib, "VmbSettingsLoad", restype = VmbError_t,
            argtypes = [VmbHandle_t, ctypes.c_wchar_p, ctypes.POINTER(VmbFeaturePersistSettings_t), VmbUint32_t],
            argnames = ["handle", "filePath", "settings", "sizeofSettings"] )
    #  VmbError_t VmbChunkDataAccess(ctypes.POINTER(VmbFrame_t) frame, VmbChunkAccessCallback chunkAccessCallback, ctypes.c_void_p userContext)
    addfunc(lib, "VmbChunkDataAccess", restype = VmbError_t,
            argtypes = [ctypes.POINTER(VmbFrame_t), VmbChunkAccessCallback, ctypes.c_void_p],
            argnames = ["frame", "chunkAccessCallback", "userContext"] )


