##########   This file is generated automatically based on SpinnakerC.h   ##########

# pylint: disable=unused-import, unused-argument, wrong-spelling-in-comment


import ctypes
import enum
from ...core.utils import ctypes_wrap




def _int32(v): return (v+0x80000000)%0x100000000-0x80000000




##### TYPE DEFINITIONS #####


BYTE=ctypes.c_ubyte
PBYTE=ctypes.POINTER(BYTE)
CHAR=ctypes.c_char
PCHAR=ctypes.c_char_p
UCHAR=ctypes.c_ubyte
PUCHAR=ctypes.POINTER(UCHAR)
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
bool8_t=ctypes.c_uint8
spinSystem=ctypes.c_void_p
spinInterfaceList=ctypes.c_void_p
spinInterface=ctypes.c_void_p
spinCameraList=ctypes.c_void_p
spinCamera=ctypes.c_void_p
spinImage=ctypes.c_void_p
spinImageList=ctypes.c_void_p
spinImageProcessor=ctypes.c_void_p
spinImageStatistics=ctypes.c_void_p
spinDeviceEventHandler=ctypes.c_void_p
spinImageEventHandler=ctypes.c_void_p
spinImageListEventHandler=ctypes.c_void_p
spinDeviceArrivalEventHandler=ctypes.c_void_p
spinDeviceRemovalEventHandler=ctypes.c_void_p
spinInterfaceEventHandler=ctypes.c_void_p
spinLogEventHandler=ctypes.c_void_p
spinLogEventData=ctypes.c_void_p
spinDeviceEventData=ctypes.c_void_p
spinVideo=ctypes.c_void_p
spinDeviceEventFunction=ctypes.c_void_p
spinImageEventFunction=ctypes.c_void_p
spinImageListEventFunction=ctypes.c_void_p
spinArrivalEventFunction=ctypes.c_void_p
spinRemovalEventFunction=ctypes.c_void_p
spinLogEventFunction=ctypes.c_void_p
class spinError(enum.IntEnum):
    SPINNAKER_ERR_SUCCESS                 =_int32(0)
    SPINNAKER_ERR_ERROR                   =_int32((-1001))
    SPINNAKER_ERR_NOT_INITIALIZED         =_int32((-1002))
    SPINNAKER_ERR_NOT_IMPLEMENTED         =_int32((-1003))
    SPINNAKER_ERR_RESOURCE_IN_USE         =_int32((-1004))
    SPINNAKER_ERR_ACCESS_DENIED           =_int32((-1005))
    SPINNAKER_ERR_INVALID_HANDLE          =_int32((-1006))
    SPINNAKER_ERR_INVALID_ID              =_int32((-1007))
    SPINNAKER_ERR_NO_DATA                 =_int32((-1008))
    SPINNAKER_ERR_INVALID_PARAMETER       =_int32((-1009))
    SPINNAKER_ERR_IO                      =_int32((-1010))
    SPINNAKER_ERR_TIMEOUT                 =_int32((-1011))
    SPINNAKER_ERR_ABORT                   =_int32((-1012))
    SPINNAKER_ERR_INVALID_BUFFER          =_int32((-1013))
    SPINNAKER_ERR_NOT_AVAILABLE           =_int32((-1014))
    SPINNAKER_ERR_INVALID_ADDRESS         =_int32((-1015))
    SPINNAKER_ERR_BUFFER_TOO_SMALL        =_int32((-1016))
    SPINNAKER_ERR_INVALID_INDEX           =_int32((-1017))
    SPINNAKER_ERR_PARSING_CHUNK_DATA      =_int32((-1018))
    SPINNAKER_ERR_INVALID_VALUE           =_int32((-1019))
    SPINNAKER_ERR_RESOURCE_EXHAUSTED      =_int32((-1020))
    SPINNAKER_ERR_OUT_OF_MEMORY           =_int32((-1021))
    SPINNAKER_ERR_BUSY                    =_int32((-1022))
    SPINNAKER_ERR_GENICAM_INVALID_ARGUMENT=_int32((-2001))
    SPINNAKER_ERR_GENICAM_OUT_OF_RANGE    =_int32((-2002))
    SPINNAKER_ERR_GENICAM_PROPERTY        =_int32((-2003))
    SPINNAKER_ERR_GENICAM_RUN_TIME        =_int32((-2004))
    SPINNAKER_ERR_GENICAM_LOGICAL         =_int32((-2005))
    SPINNAKER_ERR_GENICAM_ACCESS          =_int32((-2006))
    SPINNAKER_ERR_GENICAM_TIMEOUT         =_int32((-2007))
    SPINNAKER_ERR_GENICAM_DYNAMIC_CAST    =_int32((-2008))
    SPINNAKER_ERR_GENICAM_GENERIC         =_int32((-2009))
    SPINNAKER_ERR_GENICAM_BAD_ALLOCATION  =_int32((-2010))
    SPINNAKER_ERR_IM_CONVERT              =_int32((-3001))
    SPINNAKER_ERR_IM_COPY                 =_int32((-3002))
    SPINNAKER_ERR_IM_MALLOC               =_int32((-3003))
    SPINNAKER_ERR_IM_NOT_SUPPORTED        =_int32((-3004))
    SPINNAKER_ERR_IM_HISTOGRAM_RANGE      =_int32((-3005))
    SPINNAKER_ERR_IM_HISTOGRAM_MEAN       =_int32((-3006))
    SPINNAKER_ERR_IM_MIN_MAX              =_int32((-3007))
    SPINNAKER_ERR_IM_COLOR_CONVERSION     =_int32((-3008))
    SPINNAKER_ERR_CUSTOM_ID               =_int32((-10000))
dspinError={a.name:a.value for a in spinError}
drspinError={a.value:a.name for a in spinError}


class spinColorProcessingAlgorithm(enum.IntEnum):
    SPINNAKER_COLOR_PROCESSING_ALGORITHM_NONE                       =_int32(0)
    SPINNAKER_COLOR_PROCESSING_ALGORITHM_NEAREST_NEIGHBOR           =_int32(1)
    SPINNAKER_COLOR_PROCESSING_ALGORITHM_NEAREST_NEIGHBOR_AVG       =_int32(2)
    SPINNAKER_COLOR_PROCESSING_ALGORITHM_BILINEAR                   =_int32(3)
    SPINNAKER_COLOR_PROCESSING_ALGORITHM_EDGE_SENSING               =_int32(4)
    SPINNAKER_COLOR_PROCESSING_ALGORITHM_HQ_LINEAR                  =_int32(5)
    SPINNAKER_COLOR_PROCESSING_ALGORITHM_IPP                        =_int32(6)
    SPINNAKER_COLOR_PROCESSING_ALGORITHM_DIRECTIONAL_FILTER         =_int32(7)
    SPINNAKER_COLOR_PROCESSING_ALGORITHM_RIGOROUS                   =_int32(8)
    SPINNAKER_COLOR_PROCESSING_ALGORITHM_WEIGHTED_DIRECTIONAL_FILTER=_int32(9)
dspinColorProcessingAlgorithm={a.name:a.value for a in spinColorProcessingAlgorithm}
drspinColorProcessingAlgorithm={a.value:a.name for a in spinColorProcessingAlgorithm}


class spinStatisticsChannel(enum.IntEnum):
    SPINNAKER_STATISTICS_CHANNEL_GREY        =_int32(0)
    SPINNAKER_STATISTICS_CHANNEL_RED         =_int32(1)
    SPINNAKER_STATISTICS_CHANNEL_GREEN       =_int32(2)
    SPINNAKER_STATISTICS_CHANNEL_BLUE        =_int32(3)
    SPINNAKER_STATISTICS_CHANNEL_HUE         =_int32(4)
    SPINNAKER_STATISTICS_CHANNEL_SATURATION  =_int32(5)
    SPINNAKER_STATISTICS_CHANNEL_LIGHTNESS   =_int32(6)
    SPINNAKER_STATISTICS_CHANNEL_NUM_CHANNELS=_int32(7)
dspinStatisticsChannel={a.name:a.value for a in spinStatisticsChannel}
drspinStatisticsChannel={a.value:a.name for a in spinStatisticsChannel}


class spinImageFileFormat(enum.IntEnum):
    SPINNAKER_IMAGE_FILE_FORMAT_FROM_FILE_EXT=_int32((-1))
    SPINNAKER_IMAGE_FILE_FORMAT_PGM          =_int32(0)
    SPINNAKER_IMAGE_FILE_FORMAT_PPM          =_int32(1)
    SPINNAKER_IMAGE_FILE_FORMAT_BMP          =_int32(2)
    SPINNAKER_IMAGE_FILE_FORMAT_JPEG         =_int32(3)
    SPINNAKER_IMAGE_FILE_FORMAT_JPEG2000     =_int32(4)
    SPINNAKER_IMAGE_FILE_FORMAT_TIFF         =_int32(5)
    SPINNAKER_IMAGE_FILE_FORMAT_PNG          =_int32(6)
    SPINNAKER_IMAGE_FILE_FORMAT_RAW          =_int32(7)
    SPINNAKER_IMAGE_FILE_FORMAT_FORCE_32BITS =_int32(0x7FFFFFFF)
dspinImageFileFormat={a.name:a.value for a in spinImageFileFormat}
drspinImageFileFormat={a.value:a.name for a in spinImageFileFormat}


class spinTLPixelFormatNamespace(enum.IntEnum):
    SPINNAKER_TLPIXELFORMAT_NAMESPACE_UNKNOWN   =_int32(0)
    SPINNAKER_TLPIXELFORMAT_NAMESPACE_GEV       =_int32(1)
    SPINNAKER_TLPIXELFORMAT_NAMESPACE_IIDC      =_int32(2)
    SPINNAKER_TLPIXELFORMAT_NAMESPACE_PFNC_16BIT=_int32(3)
    SPINNAKER_TLPIXELFORMAT_NAMESPACE_PFNC_32BIT=_int32(4)
    SPINNAKER_PIXELFORMAT_NAMESPACE_CUSTOM_ID   =_int32(1000)
dspinTLPixelFormatNamespace={a.name:a.value for a in spinTLPixelFormatNamespace}
drspinTLPixelFormatNamespace={a.value:a.name for a in spinTLPixelFormatNamespace}


class spinImageStatus(enum.IntEnum):
    SPINNAKER_IMAGE_STATUS_UNKNOWN_ERROR                   =_int32((-1))
    SPINNAKER_IMAGE_STATUS_NO_ERROR                        =_int32(0)
    SPINNAKER_IMAGE_STATUS_CRC_CHECK_FAILED                =_int32(1)
    SPINNAKER_IMAGE_STATUS_DATA_OVERFLOW                   =_int32(2)
    SPINNAKER_IMAGE_STATUS_MISSING_PACKETS                 =_int32(3)
    SPINNAKER_IMAGE_STATUS_LEADER_BUFFER_SIZE_INCONSISTENT =_int32(4)
    SPINNAKER_IMAGE_STATUS_TRAILER_BUFFER_SIZE_INCONSISTENT=_int32(5)
    SPINNAKER_IMAGE_STATUS_PACKETID_INCONSISTENT           =_int32(6)
    SPINNAKER_IMAGE_STATUS_MISSING_LEADER                  =_int32(7)
    SPINNAKER_IMAGE_STATUS_MISSING_TRAILER                 =_int32(8)
    SPINNAKER_IMAGE_STATUS_DATA_INCOMPLETE                 =_int32(9)
    SPINNAKER_IMAGE_STATUS_INFO_INCONSISTENT               =_int32(10)
    SPINNAKER_IMAGE_STATUS_CHUNK_DATA_INVALID              =_int32(11)
    SPINNAKER_IMAGE_STATUS_NO_SYSTEM_RESOURCES             =_int32(12)
dspinImageStatus={a.name:a.value for a in spinImageStatus}
drspinImageStatus={a.value:a.name for a in spinImageStatus}


class spinnakerLogLevel(enum.IntEnum):
    SPINNAKER_LOG_LEVEL_OFF   =_int32((-1))
    SPINNAKER_LOG_LEVEL_FATAL =_int32(0)
    SPINNAKER_LOG_LEVEL_ALERT =_int32(100)
    SPINNAKER_LOG_LEVEL_CRIT  =_int32(200)
    SPINNAKER_LOG_LEVEL_ERROR =_int32(300)
    SPINNAKER_LOG_LEVEL_WARN  =_int32(400)
    SPINNAKER_LOG_LEVEL_NOTICE=_int32(500)
    SPINNAKER_LOG_LEVEL_INFO  =_int32(600)
    SPINNAKER_LOG_LEVEL_DEBUG =_int32(700)
    SPINNAKER_LOG_LEVEL_NOTSET=_int32(800)
dspinnakerLogLevel={a.name:a.value for a in spinnakerLogLevel}
drspinnakerLogLevel={a.value:a.name for a in spinnakerLogLevel}


class spinTLPayloadType(enum.IntEnum):
    SPINNAKER_TLPAYLOAD_TYPE_UNKNOWN                 =_int32(0)
    SPINNAKER_TLPAYLOAD_TYPE_IMAGE                   =_int32(1)
    SPINNAKER_TLPAYLOAD_TYPE_RAW_DATA                =_int32(2)
    SPINNAKER_TLPAYLOAD_TYPE_FILE                    =_int32(3)
    SPINNAKER_TLPAYLOAD_TYPE_CHUNK_DATA              =_int32(4)
    SPINNAKER_TLPAYLOAD_TYPE_JPEG                    =_int32(5)
    SPINNAKER_TLPAYLOAD_TYPE_JPEG2000                =_int32(6)
    SPINNAKER_TLPAYLOAD_TYPE_H264                    =_int32(7)
    SPINNAKER_TLPAYLOAD_TYPE_CHUNK_ONLY              =_int32(8)
    SPINNAKER_TLPAYLOAD_TYPE_DEVICE_SPECIFIC         =_int32(9)
    SPINNAKER_TLPAYLOAD_TYPE_MULTI_PART              =_int32(10)
    SPINNAKER_TLPAYLOAD_TYPE_CUSTOM_ID               =_int32(1000)
    SPINNAKER_TLPAYLOAD_TYPE_LOSSLESS_COMPRESSED     =_int32((SPINNAKER_TLPAYLOAD_TYPE_CUSTOM_ID+1))
    SPINNAKER_TLPAYLOAD_TYPE_LOSSY_COMPRESSED        =_int32((SPINNAKER_TLPAYLOAD_TYPE_CUSTOM_ID+2))
    SPINNAKER_TLPAYLOAD_TYPE_JPEG_LOSSLESS_COMPRESSED=_int32((SPINNAKER_TLPAYLOAD_TYPE_CUSTOM_ID+3))
dspinTLPayloadType={a.name:a.value for a in spinTLPayloadType}
drspinTLPayloadType={a.value:a.name for a in spinTLPayloadType}


class spinTIFFCompressionMethod(enum.IntEnum):
    SPINNAKER_TIFF_COMPRESS_METHOD_NONE         =_int32(1)
    SPINNAKER_TIFF_COMPRESS_METHOD_PACKBITS     =_int32(2)
    SPINNAKER_TIFF_COMPRESS_METHOD_DEFLATE      =_int32(3)
    SPINNAKER_TIFF_COMPRESS_METHOD_ADOBE_DEFLATE=_int32(4)
    SPINNAKER_TIFF_COMPRESS_METHOD_CCITTFAX3    =_int32(5)
    SPINNAKER_TIFF_COMPRESS_METHOD_CCITTFAX4    =_int32(6)
    SPINNAKER_TIFF_COMPRESS_METHOD_LZW          =_int32(7)
    SPINNAKER_TIFF_COMPRESS_METHOD_JPG          =_int32(8)
dspinTIFFCompressionMethod={a.name:a.value for a in spinTIFFCompressionMethod}
drspinTIFFCompressionMethod={a.value:a.name for a in spinTIFFCompressionMethod}


class spinActionCommandStatus(enum.IntEnum):
    SPINNAKER_ACTION_COMMAND_STATUS_OK         =_int32(0)
    SPINNAKER_ACTION_COMMAND_STATUS_NO_REF_TIME=_int32(0x8013)
    SPINNAKER_ACTION_COMMAND_STATUS_OVERFLOW   =_int32(0x8015)
    SPINNAKER_ACTION_COMMAND_STATUS_ACTION_LATE=_int32(0x8016)
    SPINNAKER_ACTION_COMMAND_STATUS_ERROR      =_int32(0x8FFF)
dspinActionCommandStatus={a.name:a.value for a in spinActionCommandStatus}
drspinActionCommandStatus={a.value:a.name for a in spinActionCommandStatus}


class spinPNGOption(ctypes.Structure):
    _fields_=[  ("interlaced",bool8_t),
                ("compressionLevel",ctypes.c_uint),
                ("reserved",ctypes.c_uint*16) ]
PspinPNGOption=ctypes.POINTER(spinPNGOption)
class CspinPNGOption(ctypes_wrap.CStructWrapper):
    _struct=spinPNGOption


class spinPPMOption(ctypes.Structure):
    _fields_=[  ("binaryFile",bool8_t),
                ("reserved",ctypes.c_uint*16) ]
PspinPPMOption=ctypes.POINTER(spinPPMOption)
class CspinPPMOption(ctypes_wrap.CStructWrapper):
    _struct=spinPPMOption


class spinPGMOption(ctypes.Structure):
    _fields_=[  ("binaryFile",bool8_t),
                ("reserved",ctypes.c_uint*16) ]
PspinPGMOption=ctypes.POINTER(spinPGMOption)
class CspinPGMOption(ctypes_wrap.CStructWrapper):
    _struct=spinPGMOption


class spinTIFFOption(ctypes.Structure):
    _fields_=[  ("compression",ctypes.c_int),
                ("reserved",ctypes.c_uint*16) ]
PspinTIFFOption=ctypes.POINTER(spinTIFFOption)
class CspinTIFFOption(ctypes_wrap.CStructWrapper):
    _struct=spinTIFFOption


class spinJPEGOption(ctypes.Structure):
    _fields_=[  ("progressive",bool8_t),
                ("quality",ctypes.c_uint),
                ("reserved",ctypes.c_uint*16) ]
PspinJPEGOption=ctypes.POINTER(spinJPEGOption)
class CspinJPEGOption(ctypes_wrap.CStructWrapper):
    _struct=spinJPEGOption


class spinJPG2Option(ctypes.Structure):
    _fields_=[  ("quality",ctypes.c_uint),
                ("reserved",ctypes.c_uint*16) ]
PspinJPG2Option=ctypes.POINTER(spinJPG2Option)
class CspinJPG2Option(ctypes_wrap.CStructWrapper):
    _struct=spinJPG2Option


class spinBMPOption(ctypes.Structure):
    _fields_=[  ("indexedColor_8bit",bool8_t),
                ("reserved",ctypes.c_uint*16) ]
PspinBMPOption=ctypes.POINTER(spinBMPOption)
class CspinBMPOption(ctypes_wrap.CStructWrapper):
    _struct=spinBMPOption


class spinMJPGOption(ctypes.Structure):
    _fields_=[  ("frameRate",ctypes.c_float),
                ("quality",ctypes.c_uint),
                ("width",ctypes.c_uint),
                ("height",ctypes.c_uint),
                ("reserved",ctypes.c_uint*192) ]
PspinMJPGOption=ctypes.POINTER(spinMJPGOption)
class CspinMJPGOption(ctypes_wrap.CStructWrapper):
    _struct=spinMJPGOption


class spinH264Option(ctypes.Structure):
    _fields_=[  ("frameRate",ctypes.c_float),
                ("width",ctypes.c_uint),
                ("height",ctypes.c_uint),
                ("bitrate",ctypes.c_uint),
                ("reserved",ctypes.c_uint*256) ]
PspinH264Option=ctypes.POINTER(spinH264Option)
class CspinH264Option(ctypes_wrap.CStructWrapper):
    _struct=spinH264Option


class spinAVIOption(ctypes.Structure):
    _fields_=[  ("frameRate",ctypes.c_float),
                ("width",ctypes.c_uint),
                ("height",ctypes.c_uint),
                ("reserved",ctypes.c_uint*192) ]
PspinAVIOption=ctypes.POINTER(spinAVIOption)
class CspinAVIOption(ctypes_wrap.CStructWrapper):
    _struct=spinAVIOption


class spinLibraryVersion(ctypes.Structure):
    _fields_=[  ("major",ctypes.c_uint),
                ("minor",ctypes.c_uint),
                ("type",ctypes.c_uint),
                ("build",ctypes.c_uint) ]
PspinLibraryVersion=ctypes.POINTER(spinLibraryVersion)
class CspinLibraryVersion(ctypes_wrap.CStructWrapper):
    _struct=spinLibraryVersion


class actionCommandResult(ctypes.Structure):
    _fields_=[  ("DeviceAddress",ctypes.c_uint),
                ("Status",ctypes.c_int) ]
PactionCommandResult=ctypes.POINTER(actionCommandResult)
class CactionCommandResult(ctypes_wrap.CStructWrapper):
    _struct=actionCommandResult


class spinLUTSelectorEnums(enum.IntEnum):
    LUTSelector_LUT1=_int32(0)
    NUM_LUTSELECTOR =_int32(1)
dspinLUTSelectorEnums={a.name:a.value for a in spinLUTSelectorEnums}
drspinLUTSelectorEnums={a.value:a.name for a in spinLUTSelectorEnums}


class spinExposureModeEnums(enum.IntEnum):
    ExposureMode_Timed       =_int32(0)
    ExposureMode_TriggerWidth=_int32(1)
    NUM_EXPOSUREMODE         =_int32(2)
dspinExposureModeEnums={a.name:a.value for a in spinExposureModeEnums}
drspinExposureModeEnums={a.value:a.name for a in spinExposureModeEnums}


class spinAcquisitionModeEnums(enum.IntEnum):
    AcquisitionMode_Continuous =_int32(0)
    AcquisitionMode_SingleFrame=_int32(1)
    AcquisitionMode_MultiFrame =_int32(2)
    NUM_ACQUISITIONMODE        =_int32(3)
dspinAcquisitionModeEnums={a.name:a.value for a in spinAcquisitionModeEnums}
drspinAcquisitionModeEnums={a.value:a.name for a in spinAcquisitionModeEnums}


class spinTriggerSourceEnums(enum.IntEnum):
    TriggerSource_Software     =_int32(0)
    TriggerSource_Line0        =_int32(1)
    TriggerSource_Line1        =_int32(2)
    TriggerSource_Line2        =_int32(3)
    TriggerSource_Line3        =_int32(4)
    TriggerSource_UserOutput0  =_int32(5)
    TriggerSource_UserOutput1  =_int32(6)
    TriggerSource_UserOutput2  =_int32(7)
    TriggerSource_UserOutput3  =_int32(8)
    TriggerSource_Counter0Start=_int32(9)
    TriggerSource_Counter1Start=_int32(10)
    TriggerSource_Counter0End  =_int32(11)
    TriggerSource_Counter1End  =_int32(12)
    TriggerSource_LogicBlock0  =_int32(13)
    TriggerSource_LogicBlock1  =_int32(14)
    TriggerSource_Action0      =_int32(15)
    NUM_TRIGGERSOURCE          =_int32(16)
dspinTriggerSourceEnums={a.name:a.value for a in spinTriggerSourceEnums}
drspinTriggerSourceEnums={a.value:a.name for a in spinTriggerSourceEnums}


class spinTriggerActivationEnums(enum.IntEnum):
    TriggerActivation_LevelLow   =_int32(0)
    TriggerActivation_LevelHigh  =_int32(1)
    TriggerActivation_FallingEdge=_int32(2)
    TriggerActivation_RisingEdge =_int32(3)
    TriggerActivation_AnyEdge    =_int32(4)
    NUM_TRIGGERACTIVATION        =_int32(5)
dspinTriggerActivationEnums={a.name:a.value for a in spinTriggerActivationEnums}
drspinTriggerActivationEnums={a.value:a.name for a in spinTriggerActivationEnums}


class spinSensorShutterModeEnums(enum.IntEnum):
    SensorShutterMode_Global     =_int32(0)
    SensorShutterMode_Rolling    =_int32(1)
    SensorShutterMode_GlobalReset=_int32(2)
    NUM_SENSORSHUTTERMODE        =_int32(3)
dspinSensorShutterModeEnums={a.name:a.value for a in spinSensorShutterModeEnums}
drspinSensorShutterModeEnums={a.value:a.name for a in spinSensorShutterModeEnums}


class spinTriggerModeEnums(enum.IntEnum):
    TriggerMode_Off=_int32(0)
    TriggerMode_On =_int32(1)
    NUM_TRIGGERMODE=_int32(2)
dspinTriggerModeEnums={a.name:a.value for a in spinTriggerModeEnums}
drspinTriggerModeEnums={a.value:a.name for a in spinTriggerModeEnums}


class spinTriggerOverlapEnums(enum.IntEnum):
    TriggerOverlap_Off          =_int32(0)
    TriggerOverlap_ReadOut      =_int32(1)
    TriggerOverlap_PreviousFrame=_int32(2)
    NUM_TRIGGEROVERLAP          =_int32(3)
dspinTriggerOverlapEnums={a.name:a.value for a in spinTriggerOverlapEnums}
drspinTriggerOverlapEnums={a.value:a.name for a in spinTriggerOverlapEnums}


class spinTriggerSelectorEnums(enum.IntEnum):
    TriggerSelector_AcquisitionStart=_int32(0)
    TriggerSelector_FrameStart      =_int32(1)
    TriggerSelector_FrameBurstStart =_int32(2)
    NUM_TRIGGERSELECTOR             =_int32(3)
dspinTriggerSelectorEnums={a.name:a.value for a in spinTriggerSelectorEnums}
drspinTriggerSelectorEnums={a.value:a.name for a in spinTriggerSelectorEnums}


class spinExposureAutoEnums(enum.IntEnum):
    ExposureAuto_Off       =_int32(0)
    ExposureAuto_Once      =_int32(1)
    ExposureAuto_Continuous=_int32(2)
    NUM_EXPOSUREAUTO       =_int32(3)
dspinExposureAutoEnums={a.name:a.value for a in spinExposureAutoEnums}
drspinExposureAutoEnums={a.value:a.name for a in spinExposureAutoEnums}


class spinEventSelectorEnums(enum.IntEnum):
    EventSelector_Error            =_int32(0)
    EventSelector_ExposureEnd      =_int32(1)
    EventSelector_SerialPortReceive=_int32(2)
    NUM_EVENTSELECTOR              =_int32(3)
dspinEventSelectorEnums={a.name:a.value for a in spinEventSelectorEnums}
drspinEventSelectorEnums={a.value:a.name for a in spinEventSelectorEnums}


class spinEventNotificationEnums(enum.IntEnum):
    EventNotification_On =_int32(0)
    EventNotification_Off=_int32(1)
    NUM_EVENTNOTIFICATION=_int32(2)
dspinEventNotificationEnums={a.name:a.value for a in spinEventNotificationEnums}
drspinEventNotificationEnums={a.value:a.name for a in spinEventNotificationEnums}


class spinLogicBlockSelectorEnums(enum.IntEnum):
    LogicBlockSelector_LogicBlock0=_int32(0)
    LogicBlockSelector_LogicBlock1=_int32(1)
    NUM_LOGICBLOCKSELECTOR        =_int32(2)
dspinLogicBlockSelectorEnums={a.name:a.value for a in spinLogicBlockSelectorEnums}
drspinLogicBlockSelectorEnums={a.value:a.name for a in spinLogicBlockSelectorEnums}


class spinLogicBlockLUTInputActivationEnums(enum.IntEnum):
    LogicBlockLUTInputActivation_LevelLow   =_int32(0)
    LogicBlockLUTInputActivation_LevelHigh  =_int32(1)
    LogicBlockLUTInputActivation_FallingEdge=_int32(2)
    LogicBlockLUTInputActivation_RisingEdge =_int32(3)
    LogicBlockLUTInputActivation_AnyEdge    =_int32(4)
    NUM_LOGICBLOCKLUTINPUTACTIVATION        =_int32(5)
dspinLogicBlockLUTInputActivationEnums={a.name:a.value for a in spinLogicBlockLUTInputActivationEnums}
drspinLogicBlockLUTInputActivationEnums={a.value:a.name for a in spinLogicBlockLUTInputActivationEnums}


class spinLogicBlockLUTInputSelectorEnums(enum.IntEnum):
    LogicBlockLUTInputSelector_Input0=_int32(0)
    LogicBlockLUTInputSelector_Input1=_int32(1)
    LogicBlockLUTInputSelector_Input2=_int32(2)
    LogicBlockLUTInputSelector_Input3=_int32(3)
    NUM_LOGICBLOCKLUTINPUTSELECTOR   =_int32(4)
dspinLogicBlockLUTInputSelectorEnums={a.name:a.value for a in spinLogicBlockLUTInputSelectorEnums}
drspinLogicBlockLUTInputSelectorEnums={a.value:a.name for a in spinLogicBlockLUTInputSelectorEnums}


class spinLogicBlockLUTInputSourceEnums(enum.IntEnum):
    LogicBlockLUTInputSource_Zero             =_int32(0)
    LogicBlockLUTInputSource_Line0            =_int32(1)
    LogicBlockLUTInputSource_Line1            =_int32(2)
    LogicBlockLUTInputSource_Line2            =_int32(3)
    LogicBlockLUTInputSource_Line3            =_int32(4)
    LogicBlockLUTInputSource_UserOutput0      =_int32(5)
    LogicBlockLUTInputSource_UserOutput1      =_int32(6)
    LogicBlockLUTInputSource_UserOutput2      =_int32(7)
    LogicBlockLUTInputSource_UserOutput3      =_int32(8)
    LogicBlockLUTInputSource_Counter0Start    =_int32(9)
    LogicBlockLUTInputSource_Counter1Start    =_int32(10)
    LogicBlockLUTInputSource_Counter0End      =_int32(11)
    LogicBlockLUTInputSource_Counter1End      =_int32(12)
    LogicBlockLUTInputSource_LogicBlock0      =_int32(13)
    LogicBlockLUTInputSource_LogicBlock1      =_int32(14)
    LogicBlockLUTInputSource_ExposureStart    =_int32(15)
    LogicBlockLUTInputSource_ExposureEnd      =_int32(16)
    LogicBlockLUTInputSource_FrameTriggerWait =_int32(17)
    LogicBlockLUTInputSource_AcquisitionActive=_int32(18)
    NUM_LOGICBLOCKLUTINPUTSOURCE              =_int32(19)
dspinLogicBlockLUTInputSourceEnums={a.name:a.value for a in spinLogicBlockLUTInputSourceEnums}
drspinLogicBlockLUTInputSourceEnums={a.value:a.name for a in spinLogicBlockLUTInputSourceEnums}


class spinLogicBlockLUTSelectorEnums(enum.IntEnum):
    LogicBlockLUTSelector_Value =_int32(0)
    LogicBlockLUTSelector_Enable=_int32(1)
    NUM_LOGICBLOCKLUTSELECTOR   =_int32(2)
dspinLogicBlockLUTSelectorEnums={a.name:a.value for a in spinLogicBlockLUTSelectorEnums}
drspinLogicBlockLUTSelectorEnums={a.value:a.name for a in spinLogicBlockLUTSelectorEnums}


class spinColorTransformationSelectorEnums(enum.IntEnum):
    ColorTransformationSelector_RGBtoRGB=_int32(0)
    ColorTransformationSelector_RGBtoYUV=_int32(1)
    NUM_COLORTRANSFORMATIONSELECTOR     =_int32(2)
dspinColorTransformationSelectorEnums={a.name:a.value for a in spinColorTransformationSelectorEnums}
drspinColorTransformationSelectorEnums={a.value:a.name for a in spinColorTransformationSelectorEnums}


class spinRgbTransformLightSourceEnums(enum.IntEnum):
    RgbTransformLightSource_General             =_int32(0)
    RgbTransformLightSource_Tungsten2800K       =_int32(1)
    RgbTransformLightSource_WarmFluorescent3000K=_int32(2)
    RgbTransformLightSource_CoolFluorescent4000K=_int32(3)
    RgbTransformLightSource_Daylight5000K       =_int32(4)
    RgbTransformLightSource_Cloudy6500K         =_int32(5)
    RgbTransformLightSource_Shade8000K          =_int32(6)
    RgbTransformLightSource_Custom              =_int32(7)
    NUM_RGBTRANSFORMLIGHTSOURCE                 =_int32(8)
dspinRgbTransformLightSourceEnums={a.name:a.value for a in spinRgbTransformLightSourceEnums}
drspinRgbTransformLightSourceEnums={a.value:a.name for a in spinRgbTransformLightSourceEnums}


class spinColorTransformationValueSelectorEnums(enum.IntEnum):
    ColorTransformationValueSelector_Gain00 =_int32(0)
    ColorTransformationValueSelector_Gain01 =_int32(1)
    ColorTransformationValueSelector_Gain02 =_int32(2)
    ColorTransformationValueSelector_Gain10 =_int32(3)
    ColorTransformationValueSelector_Gain11 =_int32(4)
    ColorTransformationValueSelector_Gain12 =_int32(5)
    ColorTransformationValueSelector_Gain20 =_int32(6)
    ColorTransformationValueSelector_Gain21 =_int32(7)
    ColorTransformationValueSelector_Gain22 =_int32(8)
    ColorTransformationValueSelector_Offset0=_int32(9)
    ColorTransformationValueSelector_Offset1=_int32(10)
    ColorTransformationValueSelector_Offset2=_int32(11)
    NUM_COLORTRANSFORMATIONVALUESELECTOR    =_int32(12)
dspinColorTransformationValueSelectorEnums={a.name:a.value for a in spinColorTransformationValueSelectorEnums}
drspinColorTransformationValueSelectorEnums={a.value:a.name for a in spinColorTransformationValueSelectorEnums}


class spinDeviceRegistersEndiannessEnums(enum.IntEnum):
    DeviceRegistersEndianness_Little=_int32(0)
    DeviceRegistersEndianness_Big   =_int32(1)
    NUM_DEVICEREGISTERSENDIANNESS   =_int32(2)
dspinDeviceRegistersEndiannessEnums={a.name:a.value for a in spinDeviceRegistersEndiannessEnums}
drspinDeviceRegistersEndiannessEnums={a.value:a.name for a in spinDeviceRegistersEndiannessEnums}


class spinDeviceScanTypeEnums(enum.IntEnum):
    DeviceScanType_Areascan=_int32(0)
    NUM_DEVICESCANTYPE     =_int32(1)
dspinDeviceScanTypeEnums={a.name:a.value for a in spinDeviceScanTypeEnums}
drspinDeviceScanTypeEnums={a.value:a.name for a in spinDeviceScanTypeEnums}


class spinDeviceCharacterSetEnums(enum.IntEnum):
    DeviceCharacterSet_UTF8 =_int32(0)
    DeviceCharacterSet_ASCII=_int32(1)
    NUM_DEVICECHARACTERSET  =_int32(2)
dspinDeviceCharacterSetEnums={a.name:a.value for a in spinDeviceCharacterSetEnums}
drspinDeviceCharacterSetEnums={a.value:a.name for a in spinDeviceCharacterSetEnums}


class spinDeviceTLTypeEnums(enum.IntEnum):
    DeviceTLType_GigEVision  =_int32(0)
    DeviceTLType_CameraLink  =_int32(1)
    DeviceTLType_CameraLinkHS=_int32(2)
    DeviceTLType_CoaXPress   =_int32(3)
    DeviceTLType_USB3Vision  =_int32(4)
    DeviceTLType_Custom      =_int32(5)
    NUM_DEVICETLTYPE         =_int32(6)
dspinDeviceTLTypeEnums={a.name:a.value for a in spinDeviceTLTypeEnums}
drspinDeviceTLTypeEnums={a.value:a.name for a in spinDeviceTLTypeEnums}


class spinDevicePowerSupplySelectorEnums(enum.IntEnum):
    DevicePowerSupplySelector_External=_int32(0)
    NUM_DEVICEPOWERSUPPLYSELECTOR     =_int32(1)
dspinDevicePowerSupplySelectorEnums={a.name:a.value for a in spinDevicePowerSupplySelectorEnums}
drspinDevicePowerSupplySelectorEnums={a.value:a.name for a in spinDevicePowerSupplySelectorEnums}


class spinDeviceTemperatureSelectorEnums(enum.IntEnum):
    DeviceTemperatureSelector_Sensor=_int32(0)
    NUM_DEVICETEMPERATURESELECTOR   =_int32(1)
dspinDeviceTemperatureSelectorEnums={a.name:a.value for a in spinDeviceTemperatureSelectorEnums}
drspinDeviceTemperatureSelectorEnums={a.value:a.name for a in spinDeviceTemperatureSelectorEnums}


class spinDeviceIndicatorModeEnums(enum.IntEnum):
    DeviceIndicatorMode_Inactive   =_int32(0)
    DeviceIndicatorMode_Active     =_int32(1)
    DeviceIndicatorMode_ErrorStatus=_int32(2)
    NUM_DEVICEINDICATORMODE        =_int32(3)
dspinDeviceIndicatorModeEnums={a.name:a.value for a in spinDeviceIndicatorModeEnums}
drspinDeviceIndicatorModeEnums={a.value:a.name for a in spinDeviceIndicatorModeEnums}


class spinAutoExposureControlPriorityEnums(enum.IntEnum):
    AutoExposureControlPriority_Gain        =_int32(0)
    AutoExposureControlPriority_ExposureTime=_int32(1)
    NUM_AUTOEXPOSURECONTROLPRIORITY         =_int32(2)
dspinAutoExposureControlPriorityEnums={a.name:a.value for a in spinAutoExposureControlPriorityEnums}
drspinAutoExposureControlPriorityEnums={a.value:a.name for a in spinAutoExposureControlPriorityEnums}


class spinAutoExposureMeteringModeEnums(enum.IntEnum):
    AutoExposureMeteringMode_Average       =_int32(0)
    AutoExposureMeteringMode_Spot          =_int32(1)
    AutoExposureMeteringMode_Partial       =_int32(2)
    AutoExposureMeteringMode_CenterWeighted=_int32(3)
    AutoExposureMeteringMode_HistgramPeak  =_int32(4)
    NUM_AUTOEXPOSUREMETERINGMODE           =_int32(5)
dspinAutoExposureMeteringModeEnums={a.name:a.value for a in spinAutoExposureMeteringModeEnums}
drspinAutoExposureMeteringModeEnums={a.value:a.name for a in spinAutoExposureMeteringModeEnums}


class spinBalanceWhiteAutoProfileEnums(enum.IntEnum):
    BalanceWhiteAutoProfile_Indoor =_int32(0)
    BalanceWhiteAutoProfile_Outdoor=_int32(1)
    NUM_BALANCEWHITEAUTOPROFILE    =_int32(2)
dspinBalanceWhiteAutoProfileEnums={a.name:a.value for a in spinBalanceWhiteAutoProfileEnums}
drspinBalanceWhiteAutoProfileEnums={a.value:a.name for a in spinBalanceWhiteAutoProfileEnums}


class spinAutoAlgorithmSelectorEnums(enum.IntEnum):
    AutoAlgorithmSelector_Awb=_int32(0)
    AutoAlgorithmSelector_Ae =_int32(1)
    NUM_AUTOALGORITHMSELECTOR=_int32(2)
dspinAutoAlgorithmSelectorEnums={a.name:a.value for a in spinAutoAlgorithmSelectorEnums}
drspinAutoAlgorithmSelectorEnums={a.value:a.name for a in spinAutoAlgorithmSelectorEnums}


class spinAutoExposureTargetGreyValueAutoEnums(enum.IntEnum):
    AutoExposureTargetGreyValueAuto_Off       =_int32(0)
    AutoExposureTargetGreyValueAuto_Continuous=_int32(1)
    NUM_AUTOEXPOSURETARGETGREYVALUEAUTO       =_int32(2)
dspinAutoExposureTargetGreyValueAutoEnums={a.name:a.value for a in spinAutoExposureTargetGreyValueAutoEnums}
drspinAutoExposureTargetGreyValueAutoEnums={a.value:a.name for a in spinAutoExposureTargetGreyValueAutoEnums}


class spinAutoExposureLightingModeEnums(enum.IntEnum):
    AutoExposureLightingMode_AutoDetect=_int32(0)
    AutoExposureLightingMode_Backlight =_int32(1)
    AutoExposureLightingMode_Frontlight=_int32(2)
    AutoExposureLightingMode_Normal    =_int32(3)
    NUM_AUTOEXPOSURELIGHTINGMODE       =_int32(4)
dspinAutoExposureLightingModeEnums={a.name:a.value for a in spinAutoExposureLightingModeEnums}
drspinAutoExposureLightingModeEnums={a.value:a.name for a in spinAutoExposureLightingModeEnums}


class spinGevIEEE1588StatusEnums(enum.IntEnum):
    GevIEEE1588Status_Initializing=_int32(0)
    GevIEEE1588Status_Faulty      =_int32(1)
    GevIEEE1588Status_Disabled    =_int32(2)
    GevIEEE1588Status_Listening   =_int32(3)
    GevIEEE1588Status_PreMaster   =_int32(4)
    GevIEEE1588Status_Master      =_int32(5)
    GevIEEE1588Status_Passive     =_int32(6)
    GevIEEE1588Status_Uncalibrated=_int32(7)
    GevIEEE1588Status_Slave       =_int32(8)
    NUM_GEVIEEE1588STATUS         =_int32(9)
dspinGevIEEE1588StatusEnums={a.name:a.value for a in spinGevIEEE1588StatusEnums}
drspinGevIEEE1588StatusEnums={a.value:a.name for a in spinGevIEEE1588StatusEnums}


class spinGevIEEE1588ModeEnums(enum.IntEnum):
    GevIEEE1588Mode_Auto     =_int32(0)
    GevIEEE1588Mode_SlaveOnly=_int32(1)
    NUM_GEVIEEE1588MODE      =_int32(2)
dspinGevIEEE1588ModeEnums={a.name:a.value for a in spinGevIEEE1588ModeEnums}
drspinGevIEEE1588ModeEnums={a.value:a.name for a in spinGevIEEE1588ModeEnums}


class spinGevIEEE1588ClockAccuracyEnums(enum.IntEnum):
    GevIEEE1588ClockAccuracy_Unknown=_int32(0)
    NUM_GEVIEEE1588CLOCKACCURACY    =_int32(1)
dspinGevIEEE1588ClockAccuracyEnums={a.name:a.value for a in spinGevIEEE1588ClockAccuracyEnums}
drspinGevIEEE1588ClockAccuracyEnums={a.value:a.name for a in spinGevIEEE1588ClockAccuracyEnums}


class spinGevCCPEnums(enum.IntEnum):
    GevCCP_OpenAccess     =_int32(0)
    GevCCP_ExclusiveAccess=_int32(1)
    GevCCP_ControlAccess  =_int32(2)
    NUM_GEVCCP            =_int32(3)
dspinGevCCPEnums={a.name:a.value for a in spinGevCCPEnums}
drspinGevCCPEnums={a.value:a.name for a in spinGevCCPEnums}


class spinGevSupportedOptionSelectorEnums(enum.IntEnum):
    GevSupportedOptionSelector_UserDefinedName            =_int32(0)
    GevSupportedOptionSelector_SerialNumber               =_int32(1)
    GevSupportedOptionSelector_HeartbeatDisable           =_int32(2)
    GevSupportedOptionSelector_LinkSpeed                  =_int32(3)
    GevSupportedOptionSelector_CCPApplicationSocket       =_int32(4)
    GevSupportedOptionSelector_ManifestTable              =_int32(5)
    GevSupportedOptionSelector_TestData                   =_int32(6)
    GevSupportedOptionSelector_DiscoveryAckDelay          =_int32(7)
    GevSupportedOptionSelector_DiscoveryAckDelayWritable  =_int32(8)
    GevSupportedOptionSelector_ExtendedStatusCodes        =_int32(9)
    GevSupportedOptionSelector_Action                     =_int32(10)
    GevSupportedOptionSelector_PendingAck                 =_int32(11)
    GevSupportedOptionSelector_EventData                  =_int32(12)
    GevSupportedOptionSelector_Event                      =_int32(13)
    GevSupportedOptionSelector_PacketResend               =_int32(14)
    GevSupportedOptionSelector_WriteMem                   =_int32(15)
    GevSupportedOptionSelector_CommandsConcatenation      =_int32(16)
    GevSupportedOptionSelector_IPConfigurationLLA         =_int32(17)
    GevSupportedOptionSelector_IPConfigurationDHCP        =_int32(18)
    GevSupportedOptionSelector_IPConfigurationPersistentIP=_int32(19)
    GevSupportedOptionSelector_StreamChannelSourceSocket  =_int32(20)
    GevSupportedOptionSelector_MessageChannelSourceSocket =_int32(21)
    NUM_GEVSUPPORTEDOPTIONSELECTOR                        =_int32(22)
dspinGevSupportedOptionSelectorEnums={a.name:a.value for a in spinGevSupportedOptionSelectorEnums}
drspinGevSupportedOptionSelectorEnums={a.value:a.name for a in spinGevSupportedOptionSelectorEnums}


class spinBlackLevelSelectorEnums(enum.IntEnum):
    BlackLevelSelector_All    =_int32(0)
    BlackLevelSelector_Analog =_int32(1)
    BlackLevelSelector_Digital=_int32(2)
    NUM_BLACKLEVELSELECTOR    =_int32(3)
dspinBlackLevelSelectorEnums={a.name:a.value for a in spinBlackLevelSelectorEnums}
drspinBlackLevelSelectorEnums={a.value:a.name for a in spinBlackLevelSelectorEnums}


class spinBalanceWhiteAutoEnums(enum.IntEnum):
    BalanceWhiteAuto_Off       =_int32(0)
    BalanceWhiteAuto_Once      =_int32(1)
    BalanceWhiteAuto_Continuous=_int32(2)
    NUM_BALANCEWHITEAUTO       =_int32(3)
dspinBalanceWhiteAutoEnums={a.name:a.value for a in spinBalanceWhiteAutoEnums}
drspinBalanceWhiteAutoEnums={a.value:a.name for a in spinBalanceWhiteAutoEnums}


class spinGainAutoEnums(enum.IntEnum):
    GainAuto_Off       =_int32(0)
    GainAuto_Once      =_int32(1)
    GainAuto_Continuous=_int32(2)
    NUM_GAINAUTO       =_int32(3)
dspinGainAutoEnums={a.name:a.value for a in spinGainAutoEnums}
drspinGainAutoEnums={a.value:a.name for a in spinGainAutoEnums}


class spinBalanceRatioSelectorEnums(enum.IntEnum):
    BalanceRatioSelector_Red =_int32(0)
    BalanceRatioSelector_Blue=_int32(1)
    NUM_BALANCERATIOSELECTOR =_int32(2)
dspinBalanceRatioSelectorEnums={a.name:a.value for a in spinBalanceRatioSelectorEnums}
drspinBalanceRatioSelectorEnums={a.value:a.name for a in spinBalanceRatioSelectorEnums}


class spinGainSelectorEnums(enum.IntEnum):
    GainSelector_All=_int32(0)
    NUM_GAINSELECTOR=_int32(1)
dspinGainSelectorEnums={a.name:a.value for a in spinGainSelectorEnums}
drspinGainSelectorEnums={a.value:a.name for a in spinGainSelectorEnums}


class spinDefectCorrectionModeEnums(enum.IntEnum):
    DefectCorrectionMode_Average  =_int32(0)
    DefectCorrectionMode_Highlight=_int32(1)
    DefectCorrectionMode_Zero     =_int32(2)
    NUM_DEFECTCORRECTIONMODE      =_int32(3)
dspinDefectCorrectionModeEnums={a.name:a.value for a in spinDefectCorrectionModeEnums}
drspinDefectCorrectionModeEnums={a.value:a.name for a in spinDefectCorrectionModeEnums}


class spinUserSetSelectorEnums(enum.IntEnum):
    UserSetSelector_Default =_int32(0)
    UserSetSelector_UserSet0=_int32(1)
    UserSetSelector_UserSet1=_int32(2)
    NUM_USERSETSELECTOR     =_int32(3)
dspinUserSetSelectorEnums={a.name:a.value for a in spinUserSetSelectorEnums}
drspinUserSetSelectorEnums={a.value:a.name for a in spinUserSetSelectorEnums}


class spinUserSetDefaultEnums(enum.IntEnum):
    UserSetDefault_Default =_int32(0)
    UserSetDefault_UserSet0=_int32(1)
    UserSetDefault_UserSet1=_int32(2)
    NUM_USERSETDEFAULT     =_int32(3)
dspinUserSetDefaultEnums={a.name:a.value for a in spinUserSetDefaultEnums}
drspinUserSetDefaultEnums={a.value:a.name for a in spinUserSetDefaultEnums}


class spinSerialPortBaudRateEnums(enum.IntEnum):
    SerialPortBaudRate_Baud300   =_int32(0)
    SerialPortBaudRate_Baud600   =_int32(1)
    SerialPortBaudRate_Baud1200  =_int32(2)
    SerialPortBaudRate_Baud2400  =_int32(3)
    SerialPortBaudRate_Baud4800  =_int32(4)
    SerialPortBaudRate_Baud9600  =_int32(5)
    SerialPortBaudRate_Baud14400 =_int32(6)
    SerialPortBaudRate_Baud19200 =_int32(7)
    SerialPortBaudRate_Baud38400 =_int32(8)
    SerialPortBaudRate_Baud57600 =_int32(9)
    SerialPortBaudRate_Baud115200=_int32(10)
    SerialPortBaudRate_Baud230400=_int32(11)
    SerialPortBaudRate_Baud460800=_int32(12)
    SerialPortBaudRate_Baud921600=_int32(13)
    NUM_SERIALPORTBAUDRATE       =_int32(14)
dspinSerialPortBaudRateEnums={a.name:a.value for a in spinSerialPortBaudRateEnums}
drspinSerialPortBaudRateEnums={a.value:a.name for a in spinSerialPortBaudRateEnums}


class spinSerialPortParityEnums(enum.IntEnum):
    SerialPortParity_None =_int32(0)
    SerialPortParity_Odd  =_int32(1)
    SerialPortParity_Even =_int32(2)
    SerialPortParity_Mark =_int32(3)
    SerialPortParity_Space=_int32(4)
    NUM_SERIALPORTPARITY  =_int32(5)
dspinSerialPortParityEnums={a.name:a.value for a in spinSerialPortParityEnums}
drspinSerialPortParityEnums={a.value:a.name for a in spinSerialPortParityEnums}


class spinSerialPortSelectorEnums(enum.IntEnum):
    SerialPortSelector_SerialPort0=_int32(0)
    NUM_SERIALPORTSELECTOR        =_int32(1)
dspinSerialPortSelectorEnums={a.name:a.value for a in spinSerialPortSelectorEnums}
drspinSerialPortSelectorEnums={a.value:a.name for a in spinSerialPortSelectorEnums}


class spinSerialPortStopBitsEnums(enum.IntEnum):
    SerialPortStopBits_Bits1        =_int32(0)
    SerialPortStopBits_Bits1AndAHalf=_int32(1)
    SerialPortStopBits_Bits2        =_int32(2)
    NUM_SERIALPORTSTOPBITS          =_int32(3)
dspinSerialPortStopBitsEnums={a.name:a.value for a in spinSerialPortStopBitsEnums}
drspinSerialPortStopBitsEnums={a.value:a.name for a in spinSerialPortStopBitsEnums}


class spinSerialPortSourceEnums(enum.IntEnum):
    SerialPortSource_Line0=_int32(0)
    SerialPortSource_Line1=_int32(1)
    SerialPortSource_Line2=_int32(2)
    SerialPortSource_Line3=_int32(3)
    SerialPortSource_Off  =_int32(4)
    NUM_SERIALPORTSOURCE  =_int32(5)
dspinSerialPortSourceEnums={a.name:a.value for a in spinSerialPortSourceEnums}
drspinSerialPortSourceEnums={a.value:a.name for a in spinSerialPortSourceEnums}


class spinSequencerModeEnums(enum.IntEnum):
    SequencerMode_Off=_int32(0)
    SequencerMode_On =_int32(1)
    NUM_SEQUENCERMODE=_int32(2)
dspinSequencerModeEnums={a.name:a.value for a in spinSequencerModeEnums}
drspinSequencerModeEnums={a.value:a.name for a in spinSequencerModeEnums}


class spinSequencerConfigurationValidEnums(enum.IntEnum):
    SequencerConfigurationValid_No =_int32(0)
    SequencerConfigurationValid_Yes=_int32(1)
    NUM_SEQUENCERCONFIGURATIONVALID=_int32(2)
dspinSequencerConfigurationValidEnums={a.name:a.value for a in spinSequencerConfigurationValidEnums}
drspinSequencerConfigurationValidEnums={a.value:a.name for a in spinSequencerConfigurationValidEnums}


class spinSequencerSetValidEnums(enum.IntEnum):
    SequencerSetValid_No =_int32(0)
    SequencerSetValid_Yes=_int32(1)
    NUM_SEQUENCERSETVALID=_int32(2)
dspinSequencerSetValidEnums={a.name:a.value for a in spinSequencerSetValidEnums}
drspinSequencerSetValidEnums={a.value:a.name for a in spinSequencerSetValidEnums}


class spinSequencerTriggerActivationEnums(enum.IntEnum):
    SequencerTriggerActivation_RisingEdge =_int32(0)
    SequencerTriggerActivation_FallingEdge=_int32(1)
    SequencerTriggerActivation_AnyEdge    =_int32(2)
    SequencerTriggerActivation_LevelHigh  =_int32(3)
    SequencerTriggerActivation_LevelLow   =_int32(4)
    NUM_SEQUENCERTRIGGERACTIVATION        =_int32(5)
dspinSequencerTriggerActivationEnums={a.name:a.value for a in spinSequencerTriggerActivationEnums}
drspinSequencerTriggerActivationEnums={a.value:a.name for a in spinSequencerTriggerActivationEnums}


class spinSequencerConfigurationModeEnums(enum.IntEnum):
    SequencerConfigurationMode_Off=_int32(0)
    SequencerConfigurationMode_On =_int32(1)
    NUM_SEQUENCERCONFIGURATIONMODE=_int32(2)
dspinSequencerConfigurationModeEnums={a.name:a.value for a in spinSequencerConfigurationModeEnums}
drspinSequencerConfigurationModeEnums={a.value:a.name for a in spinSequencerConfigurationModeEnums}


class spinSequencerTriggerSourceEnums(enum.IntEnum):
    SequencerTriggerSource_Off       =_int32(0)
    SequencerTriggerSource_FrameStart=_int32(1)
    NUM_SEQUENCERTRIGGERSOURCE       =_int32(2)
dspinSequencerTriggerSourceEnums={a.name:a.value for a in spinSequencerTriggerSourceEnums}
drspinSequencerTriggerSourceEnums={a.value:a.name for a in spinSequencerTriggerSourceEnums}


class spinTransferQueueModeEnums(enum.IntEnum):
    TransferQueueMode_FirstInFirstOut=_int32(0)
    NUM_TRANSFERQUEUEMODE            =_int32(1)
dspinTransferQueueModeEnums={a.name:a.value for a in spinTransferQueueModeEnums}
drspinTransferQueueModeEnums={a.value:a.name for a in spinTransferQueueModeEnums}


class spinTransferOperationModeEnums(enum.IntEnum):
    TransferOperationMode_Continuous=_int32(0)
    TransferOperationMode_MultiBlock=_int32(1)
    NUM_TRANSFEROPERATIONMODE       =_int32(2)
dspinTransferOperationModeEnums={a.name:a.value for a in spinTransferOperationModeEnums}
drspinTransferOperationModeEnums={a.value:a.name for a in spinTransferOperationModeEnums}


class spinTransferControlModeEnums(enum.IntEnum):
    TransferControlMode_Basic         =_int32(0)
    TransferControlMode_Automatic     =_int32(1)
    TransferControlMode_UserControlled=_int32(2)
    NUM_TRANSFERCONTROLMODE           =_int32(3)
dspinTransferControlModeEnums={a.name:a.value for a in spinTransferControlModeEnums}
drspinTransferControlModeEnums={a.value:a.name for a in spinTransferControlModeEnums}


class spinChunkGainSelectorEnums(enum.IntEnum):
    ChunkGainSelector_All  =_int32(0)
    ChunkGainSelector_Red  =_int32(1)
    ChunkGainSelector_Green=_int32(2)
    ChunkGainSelector_Blue =_int32(3)
    NUM_CHUNKGAINSELECTOR  =_int32(4)
dspinChunkGainSelectorEnums={a.name:a.value for a in spinChunkGainSelectorEnums}
drspinChunkGainSelectorEnums={a.value:a.name for a in spinChunkGainSelectorEnums}


class spinChunkSelectorEnums(enum.IntEnum):
    ChunkSelector_Image                   =_int32(0)
    ChunkSelector_CRC                     =_int32(1)
    ChunkSelector_FrameID                 =_int32(2)
    ChunkSelector_OffsetX                 =_int32(3)
    ChunkSelector_OffsetY                 =_int32(4)
    ChunkSelector_Width                   =_int32(5)
    ChunkSelector_Height                  =_int32(6)
    ChunkSelector_ExposureTime            =_int32(7)
    ChunkSelector_Gain                    =_int32(8)
    ChunkSelector_BlackLevel              =_int32(9)
    ChunkSelector_PixelFormat             =_int32(10)
    ChunkSelector_Timestamp               =_int32(11)
    ChunkSelector_SequencerSetActive      =_int32(12)
    ChunkSelector_SerialData              =_int32(13)
    ChunkSelector_ExposureEndLineStatusAll=_int32(14)
    NUM_CHUNKSELECTOR                     =_int32(15)
dspinChunkSelectorEnums={a.name:a.value for a in spinChunkSelectorEnums}
drspinChunkSelectorEnums={a.value:a.name for a in spinChunkSelectorEnums}


class spinChunkBlackLevelSelectorEnums(enum.IntEnum):
    ChunkBlackLevelSelector_All=_int32(0)
    NUM_CHUNKBLACKLEVELSELECTOR=_int32(1)
dspinChunkBlackLevelSelectorEnums={a.name:a.value for a in spinChunkBlackLevelSelectorEnums}
drspinChunkBlackLevelSelectorEnums={a.value:a.name for a in spinChunkBlackLevelSelectorEnums}


class spinChunkPixelFormatEnums(enum.IntEnum):
    ChunkPixelFormat_Mono8                =_int32(0)
    ChunkPixelFormat_Mono12Packed         =_int32(1)
    ChunkPixelFormat_Mono16               =_int32(2)
    ChunkPixelFormat_RGB8Packed           =_int32(3)
    ChunkPixelFormat_YUV422Packed         =_int32(4)
    ChunkPixelFormat_BayerGR8             =_int32(5)
    ChunkPixelFormat_BayerRG8             =_int32(6)
    ChunkPixelFormat_BayerGB8             =_int32(7)
    ChunkPixelFormat_BayerBG8             =_int32(8)
    ChunkPixelFormat_YCbCr601_422_8_CbYCrY=_int32(9)
    NUM_CHUNKPIXELFORMAT                  =_int32(10)
dspinChunkPixelFormatEnums={a.name:a.value for a in spinChunkPixelFormatEnums}
drspinChunkPixelFormatEnums={a.value:a.name for a in spinChunkPixelFormatEnums}


class spinFileOperationStatusEnums(enum.IntEnum):
    FileOperationStatus_Success =_int32(0)
    FileOperationStatus_Failure =_int32(1)
    FileOperationStatus_Overflow=_int32(2)
    NUM_FILEOPERATIONSTATUS     =_int32(3)
dspinFileOperationStatusEnums={a.name:a.value for a in spinFileOperationStatusEnums}
drspinFileOperationStatusEnums={a.value:a.name for a in spinFileOperationStatusEnums}


class spinFileOpenModeEnums(enum.IntEnum):
    FileOpenMode_Read     =_int32(0)
    FileOpenMode_Write    =_int32(1)
    FileOpenMode_ReadWrite=_int32(2)
    NUM_FILEOPENMODE      =_int32(3)
dspinFileOpenModeEnums={a.name:a.value for a in spinFileOpenModeEnums}
drspinFileOpenModeEnums={a.value:a.name for a in spinFileOpenModeEnums}


class spinFileOperationSelectorEnums(enum.IntEnum):
    FileOperationSelector_Open  =_int32(0)
    FileOperationSelector_Close =_int32(1)
    FileOperationSelector_Read  =_int32(2)
    FileOperationSelector_Write =_int32(3)
    FileOperationSelector_Delete=_int32(4)
    NUM_FILEOPERATIONSELECTOR   =_int32(5)
dspinFileOperationSelectorEnums={a.name:a.value for a in spinFileOperationSelectorEnums}
drspinFileOperationSelectorEnums={a.value:a.name for a in spinFileOperationSelectorEnums}


class spinFileSelectorEnums(enum.IntEnum):
    FileSelector_UserSetDefault=_int32(0)
    FileSelector_UserSet0      =_int32(1)
    FileSelector_UserSet1      =_int32(2)
    FileSelector_UserFile1     =_int32(3)
    FileSelector_SerialPort0   =_int32(4)
    NUM_FILESELECTOR           =_int32(5)
dspinFileSelectorEnums={a.name:a.value for a in spinFileSelectorEnums}
drspinFileSelectorEnums={a.value:a.name for a in spinFileSelectorEnums}


class spinBinningSelectorEnums(enum.IntEnum):
    BinningSelector_All   =_int32(0)
    BinningSelector_Sensor=_int32(1)
    BinningSelector_ISP   =_int32(2)
    NUM_BINNINGSELECTOR   =_int32(3)
dspinBinningSelectorEnums={a.name:a.value for a in spinBinningSelectorEnums}
drspinBinningSelectorEnums={a.value:a.name for a in spinBinningSelectorEnums}


class spinTestPatternGeneratorSelectorEnums(enum.IntEnum):
    TestPatternGeneratorSelector_Sensor       =_int32(0)
    TestPatternGeneratorSelector_PipelineStart=_int32(1)
    NUM_TESTPATTERNGENERATORSELECTOR          =_int32(2)
dspinTestPatternGeneratorSelectorEnums={a.name:a.value for a in spinTestPatternGeneratorSelectorEnums}
drspinTestPatternGeneratorSelectorEnums={a.value:a.name for a in spinTestPatternGeneratorSelectorEnums}


class spinCompressionSaturationPriorityEnums(enum.IntEnum):
    CompressionSaturationPriority_DropFrame      =_int32(0)
    CompressionSaturationPriority_ReduceFrameRate=_int32(1)
    NUM_COMPRESSIONSATURATIONPRIORITY            =_int32(2)
dspinCompressionSaturationPriorityEnums={a.name:a.value for a in spinCompressionSaturationPriorityEnums}
drspinCompressionSaturationPriorityEnums={a.value:a.name for a in spinCompressionSaturationPriorityEnums}


class spinTestPatternEnums(enum.IntEnum):
    TestPattern_Off              =_int32(0)
    TestPattern_Increment        =_int32(1)
    TestPattern_SensorTestPattern=_int32(2)
    NUM_TESTPATTERN              =_int32(3)
dspinTestPatternEnums={a.name:a.value for a in spinTestPatternEnums}
drspinTestPatternEnums={a.value:a.name for a in spinTestPatternEnums}


class spinPixelColorFilterEnums(enum.IntEnum):
    PixelColorFilter_None   =_int32(0)
    PixelColorFilter_BayerRG=_int32(1)
    PixelColorFilter_BayerGB=_int32(2)
    PixelColorFilter_BayerGR=_int32(3)
    PixelColorFilter_BayerBG=_int32(4)
    NUM_PIXELCOLORFILTER    =_int32(5)
dspinPixelColorFilterEnums={a.name:a.value for a in spinPixelColorFilterEnums}
drspinPixelColorFilterEnums={a.value:a.name for a in spinPixelColorFilterEnums}


class spinAdcBitDepthEnums(enum.IntEnum):
    AdcBitDepth_Bit8 =_int32(0)
    AdcBitDepth_Bit10=_int32(1)
    AdcBitDepth_Bit12=_int32(2)
    AdcBitDepth_Bit14=_int32(3)
    NUM_ADCBITDEPTH  =_int32(4)
dspinAdcBitDepthEnums={a.name:a.value for a in spinAdcBitDepthEnums}
drspinAdcBitDepthEnums={a.value:a.name for a in spinAdcBitDepthEnums}


class spinDecimationHorizontalModeEnums(enum.IntEnum):
    DecimationHorizontalMode_Discard=_int32(0)
    NUM_DECIMATIONHORIZONTALMODE    =_int32(1)
dspinDecimationHorizontalModeEnums={a.name:a.value for a in spinDecimationHorizontalModeEnums}
drspinDecimationHorizontalModeEnums={a.value:a.name for a in spinDecimationHorizontalModeEnums}


class spinBinningVerticalModeEnums(enum.IntEnum):
    BinningVerticalMode_Sum    =_int32(0)
    BinningVerticalMode_Average=_int32(1)
    NUM_BINNINGVERTICALMODE    =_int32(2)
dspinBinningVerticalModeEnums={a.name:a.value for a in spinBinningVerticalModeEnums}
drspinBinningVerticalModeEnums={a.value:a.name for a in spinBinningVerticalModeEnums}


class spinPixelSizeEnums(enum.IntEnum):
    PixelSize_Bpp1 =_int32(0)
    PixelSize_Bpp2 =_int32(1)
    PixelSize_Bpp4 =_int32(2)
    PixelSize_Bpp8 =_int32(3)
    PixelSize_Bpp10=_int32(4)
    PixelSize_Bpp12=_int32(5)
    PixelSize_Bpp14=_int32(6)
    PixelSize_Bpp16=_int32(7)
    PixelSize_Bpp20=_int32(8)
    PixelSize_Bpp24=_int32(9)
    PixelSize_Bpp30=_int32(10)
    PixelSize_Bpp32=_int32(11)
    PixelSize_Bpp36=_int32(12)
    PixelSize_Bpp48=_int32(13)
    PixelSize_Bpp64=_int32(14)
    PixelSize_Bpp96=_int32(15)
    NUM_PIXELSIZE  =_int32(16)
dspinPixelSizeEnums={a.name:a.value for a in spinPixelSizeEnums}
drspinPixelSizeEnums={a.value:a.name for a in spinPixelSizeEnums}


class spinDecimationSelectorEnums(enum.IntEnum):
    DecimationSelector_All   =_int32(0)
    DecimationSelector_Sensor=_int32(1)
    NUM_DECIMATIONSELECTOR   =_int32(2)
dspinDecimationSelectorEnums={a.name:a.value for a in spinDecimationSelectorEnums}
drspinDecimationSelectorEnums={a.value:a.name for a in spinDecimationSelectorEnums}


class spinImageCompressionModeEnums(enum.IntEnum):
    ImageCompressionMode_Off     =_int32(0)
    ImageCompressionMode_Lossless=_int32(1)
    NUM_IMAGECOMPRESSIONMODE     =_int32(2)
dspinImageCompressionModeEnums={a.name:a.value for a in spinImageCompressionModeEnums}
drspinImageCompressionModeEnums={a.value:a.name for a in spinImageCompressionModeEnums}


class spinBinningHorizontalModeEnums(enum.IntEnum):
    BinningHorizontalMode_Sum    =_int32(0)
    BinningHorizontalMode_Average=_int32(1)
    NUM_BINNINGHORIZONTALMODE    =_int32(2)
dspinBinningHorizontalModeEnums={a.name:a.value for a in spinBinningHorizontalModeEnums}
drspinBinningHorizontalModeEnums={a.value:a.name for a in spinBinningHorizontalModeEnums}


class spinPixelFormatEnums(enum.IntEnum):
    PixelFormat_Mono8                  =_int32(0)
    PixelFormat_Mono16                 =_int32(1)
    PixelFormat_RGB8Packed             =_int32(2)
    PixelFormat_BayerGR8               =_int32(3)
    PixelFormat_BayerRG8               =_int32(4)
    PixelFormat_BayerGB8               =_int32(5)
    PixelFormat_BayerBG8               =_int32(6)
    PixelFormat_BayerGR16              =_int32(7)
    PixelFormat_BayerRG16              =_int32(8)
    PixelFormat_BayerGB16              =_int32(9)
    PixelFormat_BayerBG16              =_int32(10)
    PixelFormat_Mono12Packed           =_int32(11)
    PixelFormat_BayerGR12Packed        =_int32(12)
    PixelFormat_BayerRG12Packed        =_int32(13)
    PixelFormat_BayerGB12Packed        =_int32(14)
    PixelFormat_BayerBG12Packed        =_int32(15)
    PixelFormat_YUV411Packed           =_int32(16)
    PixelFormat_YUV422Packed           =_int32(17)
    PixelFormat_YUV444Packed           =_int32(18)
    PixelFormat_Mono12p                =_int32(19)
    PixelFormat_BayerGR12p             =_int32(20)
    PixelFormat_BayerRG12p             =_int32(21)
    PixelFormat_BayerGB12p             =_int32(22)
    PixelFormat_BayerBG12p             =_int32(23)
    PixelFormat_YCbCr8                 =_int32(24)
    PixelFormat_YCbCr422_8             =_int32(25)
    PixelFormat_YCbCr411_8             =_int32(26)
    PixelFormat_BGR8                   =_int32(27)
    PixelFormat_BGRa8                  =_int32(28)
    PixelFormat_Mono10Packed           =_int32(29)
    PixelFormat_BayerGR10Packed        =_int32(30)
    PixelFormat_BayerRG10Packed        =_int32(31)
    PixelFormat_BayerGB10Packed        =_int32(32)
    PixelFormat_BayerBG10Packed        =_int32(33)
    PixelFormat_Mono10p                =_int32(34)
    PixelFormat_BayerGR10p             =_int32(35)
    PixelFormat_BayerRG10p             =_int32(36)
    PixelFormat_BayerGB10p             =_int32(37)
    PixelFormat_BayerBG10p             =_int32(38)
    PixelFormat_Mono1p                 =_int32(39)
    PixelFormat_Mono2p                 =_int32(40)
    PixelFormat_Mono4p                 =_int32(41)
    PixelFormat_Mono8s                 =_int32(42)
    PixelFormat_Mono10                 =_int32(43)
    PixelFormat_Mono12                 =_int32(44)
    PixelFormat_Mono14                 =_int32(45)
    PixelFormat_Mono16s                =_int32(46)
    PixelFormat_Mono32f                =_int32(47)
    PixelFormat_BayerBG10              =_int32(48)
    PixelFormat_BayerBG12              =_int32(49)
    PixelFormat_BayerGB10              =_int32(50)
    PixelFormat_BayerGB12              =_int32(51)
    PixelFormat_BayerGR10              =_int32(52)
    PixelFormat_BayerGR12              =_int32(53)
    PixelFormat_BayerRG10              =_int32(54)
    PixelFormat_BayerRG12              =_int32(55)
    PixelFormat_RGBa8                  =_int32(56)
    PixelFormat_RGBa10                 =_int32(57)
    PixelFormat_RGBa10p                =_int32(58)
    PixelFormat_RGBa12                 =_int32(59)
    PixelFormat_RGBa12p                =_int32(60)
    PixelFormat_RGBa14                 =_int32(61)
    PixelFormat_RGBa16                 =_int32(62)
    PixelFormat_RGB8                   =_int32(63)
    PixelFormat_RGB8_Planar            =_int32(64)
    PixelFormat_RGB10                  =_int32(65)
    PixelFormat_RGB10_Planar           =_int32(66)
    PixelFormat_RGB10p                 =_int32(67)
    PixelFormat_RGB10p32               =_int32(68)
    PixelFormat_RGB12                  =_int32(69)
    PixelFormat_RGB12_Planar           =_int32(70)
    PixelFormat_RGB12p                 =_int32(71)
    PixelFormat_RGB14                  =_int32(72)
    PixelFormat_RGB16                  =_int32(73)
    PixelFormat_RGB16s                 =_int32(74)
    PixelFormat_RGB32f                 =_int32(75)
    PixelFormat_RGB16_Planar           =_int32(76)
    PixelFormat_RGB565p                =_int32(77)
    PixelFormat_BGRa10                 =_int32(78)
    PixelFormat_BGRa10p                =_int32(79)
    PixelFormat_BGRa12                 =_int32(80)
    PixelFormat_BGRa12p                =_int32(81)
    PixelFormat_BGRa14                 =_int32(82)
    PixelFormat_BGRa16                 =_int32(83)
    PixelFormat_RGBa32f                =_int32(84)
    PixelFormat_BGR10                  =_int32(85)
    PixelFormat_BGR10p                 =_int32(86)
    PixelFormat_BGR12                  =_int32(87)
    PixelFormat_BGR12p                 =_int32(88)
    PixelFormat_BGR14                  =_int32(89)
    PixelFormat_BGR16                  =_int32(90)
    PixelFormat_BGR565p                =_int32(91)
    PixelFormat_R8                     =_int32(92)
    PixelFormat_R10                    =_int32(93)
    PixelFormat_R12                    =_int32(94)
    PixelFormat_R16                    =_int32(95)
    PixelFormat_G8                     =_int32(96)
    PixelFormat_G10                    =_int32(97)
    PixelFormat_G12                    =_int32(98)
    PixelFormat_G16                    =_int32(99)
    PixelFormat_B8                     =_int32(100)
    PixelFormat_B10                    =_int32(101)
    PixelFormat_B12                    =_int32(102)
    PixelFormat_B16                    =_int32(103)
    PixelFormat_Coord3D_ABC8           =_int32(104)
    PixelFormat_Coord3D_ABC8_Planar    =_int32(105)
    PixelFormat_Coord3D_ABC10p         =_int32(106)
    PixelFormat_Coord3D_ABC10p_Planar  =_int32(107)
    PixelFormat_Coord3D_ABC12p         =_int32(108)
    PixelFormat_Coord3D_ABC12p_Planar  =_int32(109)
    PixelFormat_Coord3D_ABC16          =_int32(110)
    PixelFormat_Coord3D_ABC16_Planar   =_int32(111)
    PixelFormat_Coord3D_ABC32f         =_int32(112)
    PixelFormat_Coord3D_ABC32f_Planar  =_int32(113)
    PixelFormat_Coord3D_AC8            =_int32(114)
    PixelFormat_Coord3D_AC8_Planar     =_int32(115)
    PixelFormat_Coord3D_AC10p          =_int32(116)
    PixelFormat_Coord3D_AC10p_Planar   =_int32(117)
    PixelFormat_Coord3D_AC12p          =_int32(118)
    PixelFormat_Coord3D_AC12p_Planar   =_int32(119)
    PixelFormat_Coord3D_AC16           =_int32(120)
    PixelFormat_Coord3D_AC16_Planar    =_int32(121)
    PixelFormat_Coord3D_AC32f          =_int32(122)
    PixelFormat_Coord3D_AC32f_Planar   =_int32(123)
    PixelFormat_Coord3D_A8             =_int32(124)
    PixelFormat_Coord3D_A10p           =_int32(125)
    PixelFormat_Coord3D_A12p           =_int32(126)
    PixelFormat_Coord3D_A16            =_int32(127)
    PixelFormat_Coord3D_A32f           =_int32(128)
    PixelFormat_Coord3D_B8             =_int32(129)
    PixelFormat_Coord3D_B10p           =_int32(130)
    PixelFormat_Coord3D_B12p           =_int32(131)
    PixelFormat_Coord3D_B16            =_int32(132)
    PixelFormat_Coord3D_B32f           =_int32(133)
    PixelFormat_Coord3D_C8             =_int32(134)
    PixelFormat_Coord3D_C10p           =_int32(135)
    PixelFormat_Coord3D_C12p           =_int32(136)
    PixelFormat_Coord3D_C16            =_int32(137)
    PixelFormat_Coord3D_C32f           =_int32(138)
    PixelFormat_Confidence1            =_int32(139)
    PixelFormat_Confidence1p           =_int32(140)
    PixelFormat_Confidence8            =_int32(141)
    PixelFormat_Confidence16           =_int32(142)
    PixelFormat_Confidence32f          =_int32(143)
    PixelFormat_BiColorBGRG8           =_int32(144)
    PixelFormat_BiColorBGRG10          =_int32(145)
    PixelFormat_BiColorBGRG10p         =_int32(146)
    PixelFormat_BiColorBGRG12          =_int32(147)
    PixelFormat_BiColorBGRG12p         =_int32(148)
    PixelFormat_BiColorRGBG8           =_int32(149)
    PixelFormat_BiColorRGBG10          =_int32(150)
    PixelFormat_BiColorRGBG10p         =_int32(151)
    PixelFormat_BiColorRGBG12          =_int32(152)
    PixelFormat_BiColorRGBG12p         =_int32(153)
    PixelFormat_SCF1WBWG8              =_int32(154)
    PixelFormat_SCF1WBWG10             =_int32(155)
    PixelFormat_SCF1WBWG10p            =_int32(156)
    PixelFormat_SCF1WBWG12             =_int32(157)
    PixelFormat_SCF1WBWG12p            =_int32(158)
    PixelFormat_SCF1WBWG14             =_int32(159)
    PixelFormat_SCF1WBWG16             =_int32(160)
    PixelFormat_SCF1WGWB8              =_int32(161)
    PixelFormat_SCF1WGWB10             =_int32(162)
    PixelFormat_SCF1WGWB10p            =_int32(163)
    PixelFormat_SCF1WGWB12             =_int32(164)
    PixelFormat_SCF1WGWB12p            =_int32(165)
    PixelFormat_SCF1WGWB14             =_int32(166)
    PixelFormat_SCF1WGWB16             =_int32(167)
    PixelFormat_SCF1WGWR8              =_int32(168)
    PixelFormat_SCF1WGWR10             =_int32(169)
    PixelFormat_SCF1WGWR10p            =_int32(170)
    PixelFormat_SCF1WGWR12             =_int32(171)
    PixelFormat_SCF1WGWR12p            =_int32(172)
    PixelFormat_SCF1WGWR14             =_int32(173)
    PixelFormat_SCF1WGWR16             =_int32(174)
    PixelFormat_SCF1WRWG8              =_int32(175)
    PixelFormat_SCF1WRWG10             =_int32(176)
    PixelFormat_SCF1WRWG10p            =_int32(177)
    PixelFormat_SCF1WRWG12             =_int32(178)
    PixelFormat_SCF1WRWG12p            =_int32(179)
    PixelFormat_SCF1WRWG14             =_int32(180)
    PixelFormat_SCF1WRWG16             =_int32(181)
    PixelFormat_YCbCr8_CbYCr           =_int32(182)
    PixelFormat_YCbCr10_CbYCr          =_int32(183)
    PixelFormat_YCbCr10p_CbYCr         =_int32(184)
    PixelFormat_YCbCr12_CbYCr          =_int32(185)
    PixelFormat_YCbCr12p_CbYCr         =_int32(186)
    PixelFormat_YCbCr411_8_CbYYCrYY    =_int32(187)
    PixelFormat_YCbCr422_8_CbYCrY      =_int32(188)
    PixelFormat_YCbCr422_10            =_int32(189)
    PixelFormat_YCbCr422_10_CbYCrY     =_int32(190)
    PixelFormat_YCbCr422_10p           =_int32(191)
    PixelFormat_YCbCr422_10p_CbYCrY    =_int32(192)
    PixelFormat_YCbCr422_12            =_int32(193)
    PixelFormat_YCbCr422_12_CbYCrY     =_int32(194)
    PixelFormat_YCbCr422_12p           =_int32(195)
    PixelFormat_YCbCr422_12p_CbYCrY    =_int32(196)
    PixelFormat_YCbCr601_8_CbYCr       =_int32(197)
    PixelFormat_YCbCr601_10_CbYCr      =_int32(198)
    PixelFormat_YCbCr601_10p_CbYCr     =_int32(199)
    PixelFormat_YCbCr601_12_CbYCr      =_int32(200)
    PixelFormat_YCbCr601_12p_CbYCr     =_int32(201)
    PixelFormat_YCbCr601_411_8_CbYYCrYY=_int32(202)
    PixelFormat_YCbCr601_422_8         =_int32(203)
    PixelFormat_YCbCr601_422_8_CbYCrY  =_int32(204)
    PixelFormat_YCbCr601_422_10        =_int32(205)
    PixelFormat_YCbCr601_422_10_CbYCrY =_int32(206)
    PixelFormat_YCbCr601_422_10p       =_int32(207)
    PixelFormat_YCbCr601_422_10p_CbYCrY=_int32(208)
    PixelFormat_YCbCr601_422_12        =_int32(209)
    PixelFormat_YCbCr601_422_12_CbYCrY =_int32(210)
    PixelFormat_YCbCr601_422_12p       =_int32(211)
    PixelFormat_YCbCr601_422_12p_CbYCrY=_int32(212)
    PixelFormat_YCbCr709_8_CbYCr       =_int32(213)
    PixelFormat_YCbCr709_10_CbYCr      =_int32(214)
    PixelFormat_YCbCr709_10p_CbYCr     =_int32(215)
    PixelFormat_YCbCr709_12_CbYCr      =_int32(216)
    PixelFormat_YCbCr709_12p_CbYCr     =_int32(217)
    PixelFormat_YCbCr709_411_8_CbYYCrYY=_int32(218)
    PixelFormat_YCbCr709_422_8         =_int32(219)
    PixelFormat_YCbCr709_422_8_CbYCrY  =_int32(220)
    PixelFormat_YCbCr709_422_10        =_int32(221)
    PixelFormat_YCbCr709_422_10_CbYCrY =_int32(222)
    PixelFormat_YCbCr709_422_10p       =_int32(223)
    PixelFormat_YCbCr709_422_10p_CbYCrY=_int32(224)
    PixelFormat_YCbCr709_422_12        =_int32(225)
    PixelFormat_YCbCr709_422_12_CbYCrY =_int32(226)
    PixelFormat_YCbCr709_422_12p       =_int32(227)
    PixelFormat_YCbCr709_422_12p_CbYCrY=_int32(228)
    PixelFormat_YUV8_UYV               =_int32(229)
    PixelFormat_YUV411_8_UYYVYY        =_int32(230)
    PixelFormat_YUV422_8               =_int32(231)
    PixelFormat_YUV422_8_UYVY          =_int32(232)
    PixelFormat_Polarized8             =_int32(233)
    PixelFormat_Polarized10p           =_int32(234)
    PixelFormat_Polarized12p           =_int32(235)
    PixelFormat_Polarized16            =_int32(236)
    PixelFormat_BayerRGPolarized8      =_int32(237)
    PixelFormat_BayerRGPolarized10p    =_int32(238)
    PixelFormat_BayerRGPolarized12p    =_int32(239)
    PixelFormat_BayerRGPolarized16     =_int32(240)
    PixelFormat_LLCMono8               =_int32(241)
    PixelFormat_LLCBayerRG8            =_int32(242)
    PixelFormat_JPEGMono8              =_int32(243)
    PixelFormat_JPEGColor8             =_int32(244)
    PixelFormat_Raw16                  =_int32(245)
    PixelFormat_Raw8                   =_int32(246)
    PixelFormat_R12_Jpeg               =_int32(247)
    PixelFormat_GR12_Jpeg              =_int32(248)
    PixelFormat_GB12_Jpeg              =_int32(249)
    PixelFormat_B12_Jpeg               =_int32(250)
    PixelFormat_GR12                   =_int32(251)
    PixelFormat_GB12                   =_int32(252)
    UNKNOWN_PIXELFORMAT                =_int32(253)
    NUM_PIXELFORMAT                    =_int32(254)
dspinPixelFormatEnums={a.name:a.value for a in spinPixelFormatEnums}
drspinPixelFormatEnums={a.value:a.name for a in spinPixelFormatEnums}


class spinDecimationVerticalModeEnums(enum.IntEnum):
    DecimationVerticalMode_Discard=_int32(0)
    NUM_DECIMATIONVERTICALMODE    =_int32(1)
dspinDecimationVerticalModeEnums={a.name:a.value for a in spinDecimationVerticalModeEnums}
drspinDecimationVerticalModeEnums={a.value:a.name for a in spinDecimationVerticalModeEnums}


class spinLineModeEnums(enum.IntEnum):
    LineMode_Input =_int32(0)
    LineMode_Output=_int32(1)
    NUM_LINEMODE   =_int32(2)
dspinLineModeEnums={a.name:a.value for a in spinLineModeEnums}
drspinLineModeEnums={a.value:a.name for a in spinLineModeEnums}


class spinLineSourceEnums(enum.IntEnum):
    LineSource_Off             =_int32(0)
    LineSource_Line0           =_int32(1)
    LineSource_Line1           =_int32(2)
    LineSource_Line2           =_int32(3)
    LineSource_Line3           =_int32(4)
    LineSource_UserOutput0     =_int32(5)
    LineSource_UserOutput1     =_int32(6)
    LineSource_UserOutput2     =_int32(7)
    LineSource_UserOutput3     =_int32(8)
    LineSource_Counter0Active  =_int32(9)
    LineSource_Counter1Active  =_int32(10)
    LineSource_LogicBlock0     =_int32(11)
    LineSource_LogicBlock1     =_int32(12)
    LineSource_ExposureActive  =_int32(13)
    LineSource_FrameTriggerWait=_int32(14)
    LineSource_SerialPort0     =_int32(15)
    LineSource_PPSSignal       =_int32(16)
    LineSource_AllPixel        =_int32(17)
    LineSource_AnyPixel        =_int32(18)
    NUM_LINESOURCE             =_int32(19)
dspinLineSourceEnums={a.name:a.value for a in spinLineSourceEnums}
drspinLineSourceEnums={a.value:a.name for a in spinLineSourceEnums}


class spinLineInputFilterSelectorEnums(enum.IntEnum):
    LineInputFilterSelector_Deglitch=_int32(0)
    LineInputFilterSelector_Debounce=_int32(1)
    NUM_LINEINPUTFILTERSELECTOR     =_int32(2)
dspinLineInputFilterSelectorEnums={a.name:a.value for a in spinLineInputFilterSelectorEnums}
drspinLineInputFilterSelectorEnums={a.value:a.name for a in spinLineInputFilterSelectorEnums}


class spinUserOutputSelectorEnums(enum.IntEnum):
    UserOutputSelector_UserOutput0=_int32(0)
    UserOutputSelector_UserOutput1=_int32(1)
    UserOutputSelector_UserOutput2=_int32(2)
    UserOutputSelector_UserOutput3=_int32(3)
    NUM_USEROUTPUTSELECTOR        =_int32(4)
dspinUserOutputSelectorEnums={a.name:a.value for a in spinUserOutputSelectorEnums}
drspinUserOutputSelectorEnums={a.value:a.name for a in spinUserOutputSelectorEnums}


class spinLineFormatEnums(enum.IntEnum):
    LineFormat_NoConnect  =_int32(0)
    LineFormat_TriState   =_int32(1)
    LineFormat_TTL        =_int32(2)
    LineFormat_LVDS       =_int32(3)
    LineFormat_RS422      =_int32(4)
    LineFormat_OptoCoupled=_int32(5)
    LineFormat_OpenDrain  =_int32(6)
    NUM_LINEFORMAT        =_int32(7)
dspinLineFormatEnums={a.name:a.value for a in spinLineFormatEnums}
drspinLineFormatEnums={a.value:a.name for a in spinLineFormatEnums}


class spinLineSelectorEnums(enum.IntEnum):
    LineSelector_Line0=_int32(0)
    LineSelector_Line1=_int32(1)
    LineSelector_Line2=_int32(2)
    LineSelector_Line3=_int32(3)
    NUM_LINESELECTOR  =_int32(4)
dspinLineSelectorEnums={a.name:a.value for a in spinLineSelectorEnums}
drspinLineSelectorEnums={a.value:a.name for a in spinLineSelectorEnums}


class spinExposureActiveModeEnums(enum.IntEnum):
    ExposureActiveMode_Line1    =_int32(0)
    ExposureActiveMode_AnyPixels=_int32(1)
    ExposureActiveMode_AllPixels=_int32(2)
    NUM_EXPOSUREACTIVEMODE      =_int32(3)
dspinExposureActiveModeEnums={a.name:a.value for a in spinExposureActiveModeEnums}
drspinExposureActiveModeEnums={a.value:a.name for a in spinExposureActiveModeEnums}


class spinCounterTriggerActivationEnums(enum.IntEnum):
    CounterTriggerActivation_LevelLow   =_int32(0)
    CounterTriggerActivation_LevelHigh  =_int32(1)
    CounterTriggerActivation_FallingEdge=_int32(2)
    CounterTriggerActivation_RisingEdge =_int32(3)
    CounterTriggerActivation_AnyEdge    =_int32(4)
    NUM_COUNTERTRIGGERACTIVATION        =_int32(5)
dspinCounterTriggerActivationEnums={a.name:a.value for a in spinCounterTriggerActivationEnums}
drspinCounterTriggerActivationEnums={a.value:a.name for a in spinCounterTriggerActivationEnums}


class spinCounterSelectorEnums(enum.IntEnum):
    CounterSelector_Counter0=_int32(0)
    CounterSelector_Counter1=_int32(1)
    NUM_COUNTERSELECTOR     =_int32(2)
dspinCounterSelectorEnums={a.name:a.value for a in spinCounterSelectorEnums}
drspinCounterSelectorEnums={a.value:a.name for a in spinCounterSelectorEnums}


class spinCounterStatusEnums(enum.IntEnum):
    CounterStatus_CounterIdle       =_int32(0)
    CounterStatus_CounterTriggerWait=_int32(1)
    CounterStatus_CounterActive     =_int32(2)
    CounterStatus_CounterCompleted  =_int32(3)
    CounterStatus_CounterOverflow   =_int32(4)
    NUM_COUNTERSTATUS               =_int32(5)
dspinCounterStatusEnums={a.name:a.value for a in spinCounterStatusEnums}
drspinCounterStatusEnums={a.value:a.name for a in spinCounterStatusEnums}


class spinCounterTriggerSourceEnums(enum.IntEnum):
    CounterTriggerSource_Off             =_int32(0)
    CounterTriggerSource_Line0           =_int32(1)
    CounterTriggerSource_Line1           =_int32(2)
    CounterTriggerSource_Line2           =_int32(3)
    CounterTriggerSource_Line3           =_int32(4)
    CounterTriggerSource_UserOutput0     =_int32(5)
    CounterTriggerSource_UserOutput1     =_int32(6)
    CounterTriggerSource_UserOutput2     =_int32(7)
    CounterTriggerSource_UserOutput3     =_int32(8)
    CounterTriggerSource_Counter0Start   =_int32(9)
    CounterTriggerSource_Counter1Start   =_int32(10)
    CounterTriggerSource_Counter0End     =_int32(11)
    CounterTriggerSource_Counter1End     =_int32(12)
    CounterTriggerSource_LogicBlock0     =_int32(13)
    CounterTriggerSource_LogicBlock1     =_int32(14)
    CounterTriggerSource_ExposureStart   =_int32(15)
    CounterTriggerSource_ExposureEnd     =_int32(16)
    CounterTriggerSource_FrameTriggerWait=_int32(17)
    NUM_COUNTERTRIGGERSOURCE             =_int32(18)
dspinCounterTriggerSourceEnums={a.name:a.value for a in spinCounterTriggerSourceEnums}
drspinCounterTriggerSourceEnums={a.value:a.name for a in spinCounterTriggerSourceEnums}


class spinCounterResetSourceEnums(enum.IntEnum):
    CounterResetSource_Off             =_int32(0)
    CounterResetSource_Line0           =_int32(1)
    CounterResetSource_Line1           =_int32(2)
    CounterResetSource_Line2           =_int32(3)
    CounterResetSource_Line3           =_int32(4)
    CounterResetSource_UserOutput0     =_int32(5)
    CounterResetSource_UserOutput1     =_int32(6)
    CounterResetSource_UserOutput2     =_int32(7)
    CounterResetSource_UserOutput3     =_int32(8)
    CounterResetSource_Counter0Start   =_int32(9)
    CounterResetSource_Counter1Start   =_int32(10)
    CounterResetSource_Counter0End     =_int32(11)
    CounterResetSource_Counter1End     =_int32(12)
    CounterResetSource_LogicBlock0     =_int32(13)
    CounterResetSource_LogicBlock1     =_int32(14)
    CounterResetSource_ExposureStart   =_int32(15)
    CounterResetSource_ExposureEnd     =_int32(16)
    CounterResetSource_FrameTriggerWait=_int32(17)
    NUM_COUNTERRESETSOURCE             =_int32(18)
dspinCounterResetSourceEnums={a.name:a.value for a in spinCounterResetSourceEnums}
drspinCounterResetSourceEnums={a.value:a.name for a in spinCounterResetSourceEnums}


class spinCounterEventSourceEnums(enum.IntEnum):
    CounterEventSource_Off             =_int32(0)
    CounterEventSource_MHzTick         =_int32(1)
    CounterEventSource_Line0           =_int32(2)
    CounterEventSource_Line1           =_int32(3)
    CounterEventSource_Line2           =_int32(4)
    CounterEventSource_Line3           =_int32(5)
    CounterEventSource_UserOutput0     =_int32(6)
    CounterEventSource_UserOutput1     =_int32(7)
    CounterEventSource_UserOutput2     =_int32(8)
    CounterEventSource_UserOutput3     =_int32(9)
    CounterEventSource_Counter0Start   =_int32(10)
    CounterEventSource_Counter1Start   =_int32(11)
    CounterEventSource_Counter0End     =_int32(12)
    CounterEventSource_Counter1End     =_int32(13)
    CounterEventSource_LogicBlock0     =_int32(14)
    CounterEventSource_LogicBlock1     =_int32(15)
    CounterEventSource_ExposureStart   =_int32(16)
    CounterEventSource_ExposureEnd     =_int32(17)
    CounterEventSource_FrameTriggerWait=_int32(18)
    NUM_COUNTEREVENTSOURCE             =_int32(19)
dspinCounterEventSourceEnums={a.name:a.value for a in spinCounterEventSourceEnums}
drspinCounterEventSourceEnums={a.value:a.name for a in spinCounterEventSourceEnums}


class spinCounterEventActivationEnums(enum.IntEnum):
    CounterEventActivation_LevelLow   =_int32(0)
    CounterEventActivation_LevelHigh  =_int32(1)
    CounterEventActivation_FallingEdge=_int32(2)
    CounterEventActivation_RisingEdge =_int32(3)
    CounterEventActivation_AnyEdge    =_int32(4)
    NUM_COUNTEREVENTACTIVATION        =_int32(5)
dspinCounterEventActivationEnums={a.name:a.value for a in spinCounterEventActivationEnums}
drspinCounterEventActivationEnums={a.value:a.name for a in spinCounterEventActivationEnums}


class spinCounterResetActivationEnums(enum.IntEnum):
    CounterResetActivation_LevelLow   =_int32(0)
    CounterResetActivation_LevelHigh  =_int32(1)
    CounterResetActivation_FallingEdge=_int32(2)
    CounterResetActivation_RisingEdge =_int32(3)
    CounterResetActivation_AnyEdge    =_int32(4)
    NUM_COUNTERRESETACTIVATION        =_int32(5)
dspinCounterResetActivationEnums={a.name:a.value for a in spinCounterResetActivationEnums}
drspinCounterResetActivationEnums={a.value:a.name for a in spinCounterResetActivationEnums}


class spinDeviceTypeEnums(enum.IntEnum):
    DeviceType_Transmitter=_int32(0)
    DeviceType_Receiver   =_int32(1)
    DeviceType_Transceiver=_int32(2)
    DeviceType_Peripheral =_int32(3)
    NUM_DEVICETYPE        =_int32(4)
dspinDeviceTypeEnums={a.name:a.value for a in spinDeviceTypeEnums}
drspinDeviceTypeEnums={a.value:a.name for a in spinDeviceTypeEnums}


class spinDeviceConnectionStatusEnums(enum.IntEnum):
    DeviceConnectionStatus_Active  =_int32(0)
    DeviceConnectionStatus_Inactive=_int32(1)
    NUM_DEVICECONNECTIONSTATUS     =_int32(2)
dspinDeviceConnectionStatusEnums={a.name:a.value for a in spinDeviceConnectionStatusEnums}
drspinDeviceConnectionStatusEnums={a.value:a.name for a in spinDeviceConnectionStatusEnums}


class spinDeviceLinkThroughputLimitModeEnums(enum.IntEnum):
    DeviceLinkThroughputLimitMode_On =_int32(0)
    DeviceLinkThroughputLimitMode_Off=_int32(1)
    NUM_DEVICELINKTHROUGHPUTLIMITMODE=_int32(2)
dspinDeviceLinkThroughputLimitModeEnums={a.name:a.value for a in spinDeviceLinkThroughputLimitModeEnums}
drspinDeviceLinkThroughputLimitModeEnums={a.value:a.name for a in spinDeviceLinkThroughputLimitModeEnums}


class spinDeviceLinkHeartbeatModeEnums(enum.IntEnum):
    DeviceLinkHeartbeatMode_On =_int32(0)
    DeviceLinkHeartbeatMode_Off=_int32(1)
    NUM_DEVICELINKHEARTBEATMODE=_int32(2)
dspinDeviceLinkHeartbeatModeEnums={a.name:a.value for a in spinDeviceLinkHeartbeatModeEnums}
drspinDeviceLinkHeartbeatModeEnums={a.value:a.name for a in spinDeviceLinkHeartbeatModeEnums}


class spinDeviceStreamChannelTypeEnums(enum.IntEnum):
    DeviceStreamChannelType_Transmitter=_int32(0)
    DeviceStreamChannelType_Receiver   =_int32(1)
    NUM_DEVICESTREAMCHANNELTYPE        =_int32(2)
dspinDeviceStreamChannelTypeEnums={a.name:a.value for a in spinDeviceStreamChannelTypeEnums}
drspinDeviceStreamChannelTypeEnums={a.value:a.name for a in spinDeviceStreamChannelTypeEnums}


class spinDeviceStreamChannelEndiannessEnums(enum.IntEnum):
    DeviceStreamChannelEndianness_Big   =_int32(0)
    DeviceStreamChannelEndianness_Little=_int32(1)
    NUM_DEVICESTREAMCHANNELENDIANNESS   =_int32(2)
dspinDeviceStreamChannelEndiannessEnums={a.name:a.value for a in spinDeviceStreamChannelEndiannessEnums}
drspinDeviceStreamChannelEndiannessEnums={a.value:a.name for a in spinDeviceStreamChannelEndiannessEnums}


class spinDeviceClockSelectorEnums(enum.IntEnum):
    DeviceClockSelector_Sensor            =_int32(0)
    DeviceClockSelector_SensorDigitization=_int32(1)
    DeviceClockSelector_CameraLink        =_int32(2)
    NUM_DEVICECLOCKSELECTOR               =_int32(3)
dspinDeviceClockSelectorEnums={a.name:a.value for a in spinDeviceClockSelectorEnums}
drspinDeviceClockSelectorEnums={a.value:a.name for a in spinDeviceClockSelectorEnums}


class spinDeviceSerialPortSelectorEnums(enum.IntEnum):
    DeviceSerialPortSelector_CameraLink=_int32(0)
    NUM_DEVICESERIALPORTSELECTOR       =_int32(1)
dspinDeviceSerialPortSelectorEnums={a.name:a.value for a in spinDeviceSerialPortSelectorEnums}
drspinDeviceSerialPortSelectorEnums={a.value:a.name for a in spinDeviceSerialPortSelectorEnums}


class spinDeviceSerialPortBaudRateEnums(enum.IntEnum):
    DeviceSerialPortBaudRate_Baud9600  =_int32(0)
    DeviceSerialPortBaudRate_Baud19200 =_int32(1)
    DeviceSerialPortBaudRate_Baud38400 =_int32(2)
    DeviceSerialPortBaudRate_Baud57600 =_int32(3)
    DeviceSerialPortBaudRate_Baud115200=_int32(4)
    DeviceSerialPortBaudRate_Baud230400=_int32(5)
    DeviceSerialPortBaudRate_Baud460800=_int32(6)
    DeviceSerialPortBaudRate_Baud921600=_int32(7)
    NUM_DEVICESERIALPORTBAUDRATE       =_int32(8)
dspinDeviceSerialPortBaudRateEnums={a.name:a.value for a in spinDeviceSerialPortBaudRateEnums}
drspinDeviceSerialPortBaudRateEnums={a.value:a.name for a in spinDeviceSerialPortBaudRateEnums}


class spinSensorTapsEnums(enum.IntEnum):
    SensorTaps_One  =_int32(0)
    SensorTaps_Two  =_int32(1)
    SensorTaps_Three=_int32(2)
    SensorTaps_Four =_int32(3)
    SensorTaps_Eight=_int32(4)
    SensorTaps_Ten  =_int32(5)
    NUM_SENSORTAPS  =_int32(6)
dspinSensorTapsEnums={a.name:a.value for a in spinSensorTapsEnums}
drspinSensorTapsEnums={a.value:a.name for a in spinSensorTapsEnums}


class spinSensorDigitizationTapsEnums(enum.IntEnum):
    SensorDigitizationTaps_One  =_int32(0)
    SensorDigitizationTaps_Two  =_int32(1)
    SensorDigitizationTaps_Three=_int32(2)
    SensorDigitizationTaps_Four =_int32(3)
    SensorDigitizationTaps_Eight=_int32(4)
    SensorDigitizationTaps_Ten  =_int32(5)
    NUM_SENSORDIGITIZATIONTAPS  =_int32(6)
dspinSensorDigitizationTapsEnums={a.name:a.value for a in spinSensorDigitizationTapsEnums}
drspinSensorDigitizationTapsEnums={a.value:a.name for a in spinSensorDigitizationTapsEnums}


class spinRegionSelectorEnums(enum.IntEnum):
    RegionSelector_Region0=_int32(0)
    RegionSelector_Region1=_int32(1)
    RegionSelector_Region2=_int32(2)
    RegionSelector_All    =_int32(3)
    NUM_REGIONSELECTOR    =_int32(4)
dspinRegionSelectorEnums={a.name:a.value for a in spinRegionSelectorEnums}
drspinRegionSelectorEnums={a.value:a.name for a in spinRegionSelectorEnums}


class spinRegionModeEnums(enum.IntEnum):
    RegionMode_Off=_int32(0)
    RegionMode_On =_int32(1)
    NUM_REGIONMODE=_int32(2)
dspinRegionModeEnums={a.name:a.value for a in spinRegionModeEnums}
drspinRegionModeEnums={a.value:a.name for a in spinRegionModeEnums}


class spinRegionDestinationEnums(enum.IntEnum):
    RegionDestination_Stream0=_int32(0)
    RegionDestination_Stream1=_int32(1)
    RegionDestination_Stream2=_int32(2)
    NUM_REGIONDESTINATION    =_int32(3)
dspinRegionDestinationEnums={a.name:a.value for a in spinRegionDestinationEnums}
drspinRegionDestinationEnums={a.value:a.name for a in spinRegionDestinationEnums}


class spinImageComponentSelectorEnums(enum.IntEnum):
    ImageComponentSelector_Intensity  =_int32(0)
    ImageComponentSelector_Color      =_int32(1)
    ImageComponentSelector_Infrared   =_int32(2)
    ImageComponentSelector_Ultraviolet=_int32(3)
    ImageComponentSelector_Range      =_int32(4)
    ImageComponentSelector_Disparity  =_int32(5)
    ImageComponentSelector_Confidence =_int32(6)
    ImageComponentSelector_Scatter    =_int32(7)
    NUM_IMAGECOMPONENTSELECTOR        =_int32(8)
dspinImageComponentSelectorEnums={a.name:a.value for a in spinImageComponentSelectorEnums}
drspinImageComponentSelectorEnums={a.value:a.name for a in spinImageComponentSelectorEnums}


class spinPixelFormatInfoSelectorEnums(enum.IntEnum):
    PixelFormatInfoSelector_Mono1p                 =_int32(0)
    PixelFormatInfoSelector_Mono2p                 =_int32(1)
    PixelFormatInfoSelector_Mono4p                 =_int32(2)
    PixelFormatInfoSelector_Mono8                  =_int32(3)
    PixelFormatInfoSelector_Mono8s                 =_int32(4)
    PixelFormatInfoSelector_Mono10                 =_int32(5)
    PixelFormatInfoSelector_Mono10p                =_int32(6)
    PixelFormatInfoSelector_Mono12                 =_int32(7)
    PixelFormatInfoSelector_Mono12p                =_int32(8)
    PixelFormatInfoSelector_Mono14                 =_int32(9)
    PixelFormatInfoSelector_Mono16                 =_int32(10)
    PixelFormatInfoSelector_Mono16s                =_int32(11)
    PixelFormatInfoSelector_Mono32f                =_int32(12)
    PixelFormatInfoSelector_BayerBG8               =_int32(13)
    PixelFormatInfoSelector_BayerBG10              =_int32(14)
    PixelFormatInfoSelector_BayerBG10p             =_int32(15)
    PixelFormatInfoSelector_BayerBG12              =_int32(16)
    PixelFormatInfoSelector_BayerBG12p             =_int32(17)
    PixelFormatInfoSelector_BayerBG16              =_int32(18)
    PixelFormatInfoSelector_BayerGB8               =_int32(19)
    PixelFormatInfoSelector_BayerGB10              =_int32(20)
    PixelFormatInfoSelector_BayerGB10p             =_int32(21)
    PixelFormatInfoSelector_BayerGB12              =_int32(22)
    PixelFormatInfoSelector_BayerGB12p             =_int32(23)
    PixelFormatInfoSelector_BayerGB16              =_int32(24)
    PixelFormatInfoSelector_BayerGR8               =_int32(25)
    PixelFormatInfoSelector_BayerGR10              =_int32(26)
    PixelFormatInfoSelector_BayerGR10p             =_int32(27)
    PixelFormatInfoSelector_BayerGR12              =_int32(28)
    PixelFormatInfoSelector_BayerGR12p             =_int32(29)
    PixelFormatInfoSelector_BayerGR16              =_int32(30)
    PixelFormatInfoSelector_BayerRG8               =_int32(31)
    PixelFormatInfoSelector_BayerRG10              =_int32(32)
    PixelFormatInfoSelector_BayerRG10p             =_int32(33)
    PixelFormatInfoSelector_BayerRG12              =_int32(34)
    PixelFormatInfoSelector_BayerRG12p             =_int32(35)
    PixelFormatInfoSelector_BayerRG16              =_int32(36)
    PixelFormatInfoSelector_RGBa8                  =_int32(37)
    PixelFormatInfoSelector_RGBa10                 =_int32(38)
    PixelFormatInfoSelector_RGBa10p                =_int32(39)
    PixelFormatInfoSelector_RGBa12                 =_int32(40)
    PixelFormatInfoSelector_RGBa12p                =_int32(41)
    PixelFormatInfoSelector_RGBa14                 =_int32(42)
    PixelFormatInfoSelector_RGBa16                 =_int32(43)
    PixelFormatInfoSelector_RGB8                   =_int32(44)
    PixelFormatInfoSelector_RGB8_Planar            =_int32(45)
    PixelFormatInfoSelector_RGB10                  =_int32(46)
    PixelFormatInfoSelector_RGB10_Planar           =_int32(47)
    PixelFormatInfoSelector_RGB10p                 =_int32(48)
    PixelFormatInfoSelector_RGB10p32               =_int32(49)
    PixelFormatInfoSelector_RGB12                  =_int32(50)
    PixelFormatInfoSelector_RGB12_Planar           =_int32(51)
    PixelFormatInfoSelector_RGB12p                 =_int32(52)
    PixelFormatInfoSelector_RGB14                  =_int32(53)
    PixelFormatInfoSelector_RGB16                  =_int32(54)
    PixelFormatInfoSelector_RGB16s                 =_int32(55)
    PixelFormatInfoSelector_RGB32f                 =_int32(56)
    PixelFormatInfoSelector_RGB16_Planar           =_int32(57)
    PixelFormatInfoSelector_RGB565p                =_int32(58)
    PixelFormatInfoSelector_BGRa8                  =_int32(59)
    PixelFormatInfoSelector_BGRa10                 =_int32(60)
    PixelFormatInfoSelector_BGRa10p                =_int32(61)
    PixelFormatInfoSelector_BGRa12                 =_int32(62)
    PixelFormatInfoSelector_BGRa12p                =_int32(63)
    PixelFormatInfoSelector_BGRa14                 =_int32(64)
    PixelFormatInfoSelector_BGRa16                 =_int32(65)
    PixelFormatInfoSelector_RGBa32f                =_int32(66)
    PixelFormatInfoSelector_BGR8                   =_int32(67)
    PixelFormatInfoSelector_BGR10                  =_int32(68)
    PixelFormatInfoSelector_BGR10p                 =_int32(69)
    PixelFormatInfoSelector_BGR12                  =_int32(70)
    PixelFormatInfoSelector_BGR12p                 =_int32(71)
    PixelFormatInfoSelector_BGR14                  =_int32(72)
    PixelFormatInfoSelector_BGR16                  =_int32(73)
    PixelFormatInfoSelector_BGR565p                =_int32(74)
    PixelFormatInfoSelector_R8                     =_int32(75)
    PixelFormatInfoSelector_R10                    =_int32(76)
    PixelFormatInfoSelector_R12                    =_int32(77)
    PixelFormatInfoSelector_R16                    =_int32(78)
    PixelFormatInfoSelector_G8                     =_int32(79)
    PixelFormatInfoSelector_G10                    =_int32(80)
    PixelFormatInfoSelector_G12                    =_int32(81)
    PixelFormatInfoSelector_G16                    =_int32(82)
    PixelFormatInfoSelector_B8                     =_int32(83)
    PixelFormatInfoSelector_B10                    =_int32(84)
    PixelFormatInfoSelector_B12                    =_int32(85)
    PixelFormatInfoSelector_B16                    =_int32(86)
    PixelFormatInfoSelector_Coord3D_ABC8           =_int32(87)
    PixelFormatInfoSelector_Coord3D_ABC8_Planar    =_int32(88)
    PixelFormatInfoSelector_Coord3D_ABC10p         =_int32(89)
    PixelFormatInfoSelector_Coord3D_ABC10p_Planar  =_int32(90)
    PixelFormatInfoSelector_Coord3D_ABC12p         =_int32(91)
    PixelFormatInfoSelector_Coord3D_ABC12p_Planar  =_int32(92)
    PixelFormatInfoSelector_Coord3D_ABC16          =_int32(93)
    PixelFormatInfoSelector_Coord3D_ABC16_Planar   =_int32(94)
    PixelFormatInfoSelector_Coord3D_ABC32f         =_int32(95)
    PixelFormatInfoSelector_Coord3D_ABC32f_Planar  =_int32(96)
    PixelFormatInfoSelector_Coord3D_AC8            =_int32(97)
    PixelFormatInfoSelector_Coord3D_AC8_Planar     =_int32(98)
    PixelFormatInfoSelector_Coord3D_AC10p          =_int32(99)
    PixelFormatInfoSelector_Coord3D_AC10p_Planar   =_int32(100)
    PixelFormatInfoSelector_Coord3D_AC12p          =_int32(101)
    PixelFormatInfoSelector_Coord3D_AC12p_Planar   =_int32(102)
    PixelFormatInfoSelector_Coord3D_AC16           =_int32(103)
    PixelFormatInfoSelector_Coord3D_AC16_Planar    =_int32(104)
    PixelFormatInfoSelector_Coord3D_AC32f          =_int32(105)
    PixelFormatInfoSelector_Coord3D_AC32f_Planar   =_int32(106)
    PixelFormatInfoSelector_Coord3D_A8             =_int32(107)
    PixelFormatInfoSelector_Coord3D_A10p           =_int32(108)
    PixelFormatInfoSelector_Coord3D_A12p           =_int32(109)
    PixelFormatInfoSelector_Coord3D_A16            =_int32(110)
    PixelFormatInfoSelector_Coord3D_A32f           =_int32(111)
    PixelFormatInfoSelector_Coord3D_B8             =_int32(112)
    PixelFormatInfoSelector_Coord3D_B10p           =_int32(113)
    PixelFormatInfoSelector_Coord3D_B12p           =_int32(114)
    PixelFormatInfoSelector_Coord3D_B16            =_int32(115)
    PixelFormatInfoSelector_Coord3D_B32f           =_int32(116)
    PixelFormatInfoSelector_Coord3D_C8             =_int32(117)
    PixelFormatInfoSelector_Coord3D_C10p           =_int32(118)
    PixelFormatInfoSelector_Coord3D_C12p           =_int32(119)
    PixelFormatInfoSelector_Coord3D_C16            =_int32(120)
    PixelFormatInfoSelector_Coord3D_C32f           =_int32(121)
    PixelFormatInfoSelector_Confidence1            =_int32(122)
    PixelFormatInfoSelector_Confidence1p           =_int32(123)
    PixelFormatInfoSelector_Confidence8            =_int32(124)
    PixelFormatInfoSelector_Confidence16           =_int32(125)
    PixelFormatInfoSelector_Confidence32f          =_int32(126)
    PixelFormatInfoSelector_BiColorBGRG8           =_int32(127)
    PixelFormatInfoSelector_BiColorBGRG10          =_int32(128)
    PixelFormatInfoSelector_BiColorBGRG10p         =_int32(129)
    PixelFormatInfoSelector_BiColorBGRG12          =_int32(130)
    PixelFormatInfoSelector_BiColorBGRG12p         =_int32(131)
    PixelFormatInfoSelector_BiColorRGBG8           =_int32(132)
    PixelFormatInfoSelector_BiColorRGBG10          =_int32(133)
    PixelFormatInfoSelector_BiColorRGBG10p         =_int32(134)
    PixelFormatInfoSelector_BiColorRGBG12          =_int32(135)
    PixelFormatInfoSelector_BiColorRGBG12p         =_int32(136)
    PixelFormatInfoSelector_SCF1WBWG8              =_int32(137)
    PixelFormatInfoSelector_SCF1WBWG10             =_int32(138)
    PixelFormatInfoSelector_SCF1WBWG10p            =_int32(139)
    PixelFormatInfoSelector_SCF1WBWG12             =_int32(140)
    PixelFormatInfoSelector_SCF1WBWG12p            =_int32(141)
    PixelFormatInfoSelector_SCF1WBWG14             =_int32(142)
    PixelFormatInfoSelector_SCF1WBWG16             =_int32(143)
    PixelFormatInfoSelector_SCF1WGWB8              =_int32(144)
    PixelFormatInfoSelector_SCF1WGWB10             =_int32(145)
    PixelFormatInfoSelector_SCF1WGWB10p            =_int32(146)
    PixelFormatInfoSelector_SCF1WGWB12             =_int32(147)
    PixelFormatInfoSelector_SCF1WGWB12p            =_int32(148)
    PixelFormatInfoSelector_SCF1WGWB14             =_int32(149)
    PixelFormatInfoSelector_SCF1WGWB16             =_int32(150)
    PixelFormatInfoSelector_SCF1WGWR8              =_int32(151)
    PixelFormatInfoSelector_SCF1WGWR10             =_int32(152)
    PixelFormatInfoSelector_SCF1WGWR10p            =_int32(153)
    PixelFormatInfoSelector_SCF1WGWR12             =_int32(154)
    PixelFormatInfoSelector_SCF1WGWR12p            =_int32(155)
    PixelFormatInfoSelector_SCF1WGWR14             =_int32(156)
    PixelFormatInfoSelector_SCF1WGWR16             =_int32(157)
    PixelFormatInfoSelector_SCF1WRWG8              =_int32(158)
    PixelFormatInfoSelector_SCF1WRWG10             =_int32(159)
    PixelFormatInfoSelector_SCF1WRWG10p            =_int32(160)
    PixelFormatInfoSelector_SCF1WRWG12             =_int32(161)
    PixelFormatInfoSelector_SCF1WRWG12p            =_int32(162)
    PixelFormatInfoSelector_SCF1WRWG14             =_int32(163)
    PixelFormatInfoSelector_SCF1WRWG16             =_int32(164)
    PixelFormatInfoSelector_YCbCr8                 =_int32(165)
    PixelFormatInfoSelector_YCbCr8_CbYCr           =_int32(166)
    PixelFormatInfoSelector_YCbCr10_CbYCr          =_int32(167)
    PixelFormatInfoSelector_YCbCr10p_CbYCr         =_int32(168)
    PixelFormatInfoSelector_YCbCr12_CbYCr          =_int32(169)
    PixelFormatInfoSelector_YCbCr12p_CbYCr         =_int32(170)
    PixelFormatInfoSelector_YCbCr411_8             =_int32(171)
    PixelFormatInfoSelector_YCbCr411_8_CbYYCrYY    =_int32(172)
    PixelFormatInfoSelector_YCbCr422_8             =_int32(173)
    PixelFormatInfoSelector_YCbCr422_8_CbYCrY      =_int32(174)
    PixelFormatInfoSelector_YCbCr422_10            =_int32(175)
    PixelFormatInfoSelector_YCbCr422_10_CbYCrY     =_int32(176)
    PixelFormatInfoSelector_YCbCr422_10p           =_int32(177)
    PixelFormatInfoSelector_YCbCr422_10p_CbYCrY    =_int32(178)
    PixelFormatInfoSelector_YCbCr422_12            =_int32(179)
    PixelFormatInfoSelector_YCbCr422_12_CbYCrY     =_int32(180)
    PixelFormatInfoSelector_YCbCr422_12p           =_int32(181)
    PixelFormatInfoSelector_YCbCr422_12p_CbYCrY    =_int32(182)
    PixelFormatInfoSelector_YCbCr601_8_CbYCr       =_int32(183)
    PixelFormatInfoSelector_YCbCr601_10_CbYCr      =_int32(184)
    PixelFormatInfoSelector_YCbCr601_10p_CbYCr     =_int32(185)
    PixelFormatInfoSelector_YCbCr601_12_CbYCr      =_int32(186)
    PixelFormatInfoSelector_YCbCr601_12p_CbYCr     =_int32(187)
    PixelFormatInfoSelector_YCbCr601_411_8_CbYYCrYY=_int32(188)
    PixelFormatInfoSelector_YCbCr601_422_8         =_int32(189)
    PixelFormatInfoSelector_YCbCr601_422_8_CbYCrY  =_int32(190)
    PixelFormatInfoSelector_YCbCr601_422_10        =_int32(191)
    PixelFormatInfoSelector_YCbCr601_422_10_CbYCrY =_int32(192)
    PixelFormatInfoSelector_YCbCr601_422_10p       =_int32(193)
    PixelFormatInfoSelector_YCbCr601_422_10p_CbYCrY=_int32(194)
    PixelFormatInfoSelector_YCbCr601_422_12        =_int32(195)
    PixelFormatInfoSelector_YCbCr601_422_12_CbYCrY =_int32(196)
    PixelFormatInfoSelector_YCbCr601_422_12p       =_int32(197)
    PixelFormatInfoSelector_YCbCr601_422_12p_CbYCrY=_int32(198)
    PixelFormatInfoSelector_YCbCr709_8_CbYCr       =_int32(199)
    PixelFormatInfoSelector_YCbCr709_10_CbYCr      =_int32(200)
    PixelFormatInfoSelector_YCbCr709_10p_CbYCr     =_int32(201)
    PixelFormatInfoSelector_YCbCr709_12_CbYCr      =_int32(202)
    PixelFormatInfoSelector_YCbCr709_12p_CbYCr     =_int32(203)
    PixelFormatInfoSelector_YCbCr709_411_8_CbYYCrYY=_int32(204)
    PixelFormatInfoSelector_YCbCr709_422_8         =_int32(205)
    PixelFormatInfoSelector_YCbCr709_422_8_CbYCrY  =_int32(206)
    PixelFormatInfoSelector_YCbCr709_422_10        =_int32(207)
    PixelFormatInfoSelector_YCbCr709_422_10_CbYCrY =_int32(208)
    PixelFormatInfoSelector_YCbCr709_422_10p       =_int32(209)
    PixelFormatInfoSelector_YCbCr709_422_10p_CbYCrY=_int32(210)
    PixelFormatInfoSelector_YCbCr709_422_12        =_int32(211)
    PixelFormatInfoSelector_YCbCr709_422_12_CbYCrY =_int32(212)
    PixelFormatInfoSelector_YCbCr709_422_12p       =_int32(213)
    PixelFormatInfoSelector_YCbCr709_422_12p_CbYCrY=_int32(214)
    PixelFormatInfoSelector_YUV8_UYV               =_int32(215)
    PixelFormatInfoSelector_YUV411_8_UYYVYY        =_int32(216)
    PixelFormatInfoSelector_YUV422_8               =_int32(217)
    PixelFormatInfoSelector_YUV422_8_UYVY          =_int32(218)
    PixelFormatInfoSelector_Polarized8             =_int32(219)
    PixelFormatInfoSelector_Polarized10p           =_int32(220)
    PixelFormatInfoSelector_Polarized12p           =_int32(221)
    PixelFormatInfoSelector_Polarized16            =_int32(222)
    PixelFormatInfoSelector_BayerRGPolarized8      =_int32(223)
    PixelFormatInfoSelector_BayerRGPolarized10p    =_int32(224)
    PixelFormatInfoSelector_BayerRGPolarized12p    =_int32(225)
    PixelFormatInfoSelector_BayerRGPolarized16     =_int32(226)
    PixelFormatInfoSelector_LLCMono8               =_int32(227)
    PixelFormatInfoSelector_LLCBayerRG8            =_int32(228)
    PixelFormatInfoSelector_JPEGMono8              =_int32(229)
    PixelFormatInfoSelector_JPEGColor8             =_int32(230)
    NUM_PIXELFORMATINFOSELECTOR                    =_int32(231)
dspinPixelFormatInfoSelectorEnums={a.name:a.value for a in spinPixelFormatInfoSelectorEnums}
drspinPixelFormatInfoSelectorEnums={a.value:a.name for a in spinPixelFormatInfoSelectorEnums}


class spinDeinterlacingEnums(enum.IntEnum):
    Deinterlacing_Off            =_int32(0)
    Deinterlacing_LineDuplication=_int32(1)
    Deinterlacing_Weave          =_int32(2)
    NUM_DEINTERLACING            =_int32(3)
dspinDeinterlacingEnums={a.name:a.value for a in spinDeinterlacingEnums}
drspinDeinterlacingEnums={a.value:a.name for a in spinDeinterlacingEnums}


class spinImageCompressionRateOptionEnums(enum.IntEnum):
    ImageCompressionRateOption_FixBitrate=_int32(0)
    ImageCompressionRateOption_FixQuality=_int32(1)
    NUM_IMAGECOMPRESSIONRATEOPTION       =_int32(2)
dspinImageCompressionRateOptionEnums={a.name:a.value for a in spinImageCompressionRateOptionEnums}
drspinImageCompressionRateOptionEnums={a.value:a.name for a in spinImageCompressionRateOptionEnums}


class spinImageCompressionJPEGFormatOptionEnums(enum.IntEnum):
    ImageCompressionJPEGFormatOption_Lossless         =_int32(0)
    ImageCompressionJPEGFormatOption_BaselineStandard =_int32(1)
    ImageCompressionJPEGFormatOption_BaselineOptimized=_int32(2)
    ImageCompressionJPEGFormatOption_Progressive      =_int32(3)
    NUM_IMAGECOMPRESSIONJPEGFORMATOPTION              =_int32(4)
dspinImageCompressionJPEGFormatOptionEnums={a.name:a.value for a in spinImageCompressionJPEGFormatOptionEnums}
drspinImageCompressionJPEGFormatOptionEnums={a.value:a.name for a in spinImageCompressionJPEGFormatOptionEnums}


class spinAcquisitionStatusSelectorEnums(enum.IntEnum):
    AcquisitionStatusSelector_AcquisitionTriggerWait=_int32(0)
    AcquisitionStatusSelector_AcquisitionActive     =_int32(1)
    AcquisitionStatusSelector_AcquisitionTransfer   =_int32(2)
    AcquisitionStatusSelector_FrameTriggerWait      =_int32(3)
    AcquisitionStatusSelector_FrameActive           =_int32(4)
    AcquisitionStatusSelector_ExposureActive        =_int32(5)
    NUM_ACQUISITIONSTATUSSELECTOR                   =_int32(6)
dspinAcquisitionStatusSelectorEnums={a.name:a.value for a in spinAcquisitionStatusSelectorEnums}
drspinAcquisitionStatusSelectorEnums={a.value:a.name for a in spinAcquisitionStatusSelectorEnums}


class spinExposureTimeModeEnums(enum.IntEnum):
    ExposureTimeMode_Common    =_int32(0)
    ExposureTimeMode_Individual=_int32(1)
    NUM_EXPOSURETIMEMODE       =_int32(2)
dspinExposureTimeModeEnums={a.name:a.value for a in spinExposureTimeModeEnums}
drspinExposureTimeModeEnums={a.value:a.name for a in spinExposureTimeModeEnums}


class spinExposureTimeSelectorEnums(enum.IntEnum):
    ExposureTimeSelector_Common     =_int32(0)
    ExposureTimeSelector_Red        =_int32(1)
    ExposureTimeSelector_Green      =_int32(2)
    ExposureTimeSelector_Blue       =_int32(3)
    ExposureTimeSelector_Cyan       =_int32(4)
    ExposureTimeSelector_Magenta    =_int32(5)
    ExposureTimeSelector_Yellow     =_int32(6)
    ExposureTimeSelector_Infrared   =_int32(7)
    ExposureTimeSelector_Ultraviolet=_int32(8)
    ExposureTimeSelector_Stage1     =_int32(9)
    ExposureTimeSelector_Stage2     =_int32(10)
    NUM_EXPOSURETIMESELECTOR        =_int32(11)
dspinExposureTimeSelectorEnums={a.name:a.value for a in spinExposureTimeSelectorEnums}
drspinExposureTimeSelectorEnums={a.value:a.name for a in spinExposureTimeSelectorEnums}


class spinGainAutoBalanceEnums(enum.IntEnum):
    GainAutoBalance_Off       =_int32(0)
    GainAutoBalance_Once      =_int32(1)
    GainAutoBalance_Continuous=_int32(2)
    NUM_GAINAUTOBALANCE       =_int32(3)
dspinGainAutoBalanceEnums={a.name:a.value for a in spinGainAutoBalanceEnums}
drspinGainAutoBalanceEnums={a.value:a.name for a in spinGainAutoBalanceEnums}


class spinBlackLevelAutoEnums(enum.IntEnum):
    BlackLevelAuto_Off       =_int32(0)
    BlackLevelAuto_Once      =_int32(1)
    BlackLevelAuto_Continuous=_int32(2)
    NUM_BLACKLEVELAUTO       =_int32(3)
dspinBlackLevelAutoEnums={a.name:a.value for a in spinBlackLevelAutoEnums}
drspinBlackLevelAutoEnums={a.value:a.name for a in spinBlackLevelAutoEnums}


class spinBlackLevelAutoBalanceEnums(enum.IntEnum):
    BlackLevelAutoBalance_Off       =_int32(0)
    BlackLevelAutoBalance_Once      =_int32(1)
    BlackLevelAutoBalance_Continuous=_int32(2)
    NUM_BLACKLEVELAUTOBALANCE       =_int32(3)
dspinBlackLevelAutoBalanceEnums={a.name:a.value for a in spinBlackLevelAutoBalanceEnums}
drspinBlackLevelAutoBalanceEnums={a.value:a.name for a in spinBlackLevelAutoBalanceEnums}


class spinWhiteClipSelectorEnums(enum.IntEnum):
    WhiteClipSelector_All  =_int32(0)
    WhiteClipSelector_Red  =_int32(1)
    WhiteClipSelector_Green=_int32(2)
    WhiteClipSelector_Blue =_int32(3)
    WhiteClipSelector_Y    =_int32(4)
    WhiteClipSelector_U    =_int32(5)
    WhiteClipSelector_V    =_int32(6)
    WhiteClipSelector_Tap1 =_int32(7)
    WhiteClipSelector_Tap2 =_int32(8)
    NUM_WHITECLIPSELECTOR  =_int32(9)
dspinWhiteClipSelectorEnums={a.name:a.value for a in spinWhiteClipSelectorEnums}
drspinWhiteClipSelectorEnums={a.value:a.name for a in spinWhiteClipSelectorEnums}


class spinTimerSelectorEnums(enum.IntEnum):
    TimerSelector_Timer0=_int32(0)
    TimerSelector_Timer1=_int32(1)
    TimerSelector_Timer2=_int32(2)
    NUM_TIMERSELECTOR   =_int32(3)
dspinTimerSelectorEnums={a.name:a.value for a in spinTimerSelectorEnums}
drspinTimerSelectorEnums={a.value:a.name for a in spinTimerSelectorEnums}


class spinTimerStatusEnums(enum.IntEnum):
    TimerStatus_TimerIdle       =_int32(0)
    TimerStatus_TimerTriggerWait=_int32(1)
    TimerStatus_TimerActive     =_int32(2)
    TimerStatus_TimerCompleted  =_int32(3)
    NUM_TIMERSTATUS             =_int32(4)
dspinTimerStatusEnums={a.name:a.value for a in spinTimerStatusEnums}
drspinTimerStatusEnums={a.value:a.name for a in spinTimerStatusEnums}


class spinTimerTriggerSourceEnums(enum.IntEnum):
    TimerTriggerSource_Off               =_int32(0)
    TimerTriggerSource_AcquisitionTrigger=_int32(1)
    TimerTriggerSource_AcquisitionStart  =_int32(2)
    TimerTriggerSource_AcquisitionEnd    =_int32(3)
    TimerTriggerSource_FrameTrigger      =_int32(4)
    TimerTriggerSource_FrameStart        =_int32(5)
    TimerTriggerSource_FrameEnd          =_int32(6)
    TimerTriggerSource_FrameBurstStart   =_int32(7)
    TimerTriggerSource_FrameBurstEnd     =_int32(8)
    TimerTriggerSource_LineTrigger       =_int32(9)
    TimerTriggerSource_LineStart         =_int32(10)
    TimerTriggerSource_LineEnd           =_int32(11)
    TimerTriggerSource_ExposureStart     =_int32(12)
    TimerTriggerSource_ExposureEnd       =_int32(13)
    TimerTriggerSource_Line0             =_int32(14)
    TimerTriggerSource_Line1             =_int32(15)
    TimerTriggerSource_Line2             =_int32(16)
    TimerTriggerSource_UserOutput0       =_int32(17)
    TimerTriggerSource_UserOutput1       =_int32(18)
    TimerTriggerSource_UserOutput2       =_int32(19)
    TimerTriggerSource_Counter0Start     =_int32(20)
    TimerTriggerSource_Counter1Start     =_int32(21)
    TimerTriggerSource_Counter2Start     =_int32(22)
    TimerTriggerSource_Counter0End       =_int32(23)
    TimerTriggerSource_Counter1End       =_int32(24)
    TimerTriggerSource_Counter2End       =_int32(25)
    TimerTriggerSource_Timer0Start       =_int32(26)
    TimerTriggerSource_Timer1Start       =_int32(27)
    TimerTriggerSource_Timer2Start       =_int32(28)
    TimerTriggerSource_Timer0End         =_int32(29)
    TimerTriggerSource_Timer1End         =_int32(30)
    TimerTriggerSource_Timer2End         =_int32(31)
    TimerTriggerSource_Encoder0          =_int32(32)
    TimerTriggerSource_Encoder1          =_int32(33)
    TimerTriggerSource_Encoder2          =_int32(34)
    TimerTriggerSource_SoftwareSignal0   =_int32(35)
    TimerTriggerSource_SoftwareSignal1   =_int32(36)
    TimerTriggerSource_SoftwareSignal2   =_int32(37)
    TimerTriggerSource_Action0           =_int32(38)
    TimerTriggerSource_Action1           =_int32(39)
    TimerTriggerSource_Action2           =_int32(40)
    TimerTriggerSource_LinkTrigger0      =_int32(41)
    TimerTriggerSource_LinkTrigger1      =_int32(42)
    TimerTriggerSource_LinkTrigger2      =_int32(43)
    NUM_TIMERTRIGGERSOURCE               =_int32(44)
dspinTimerTriggerSourceEnums={a.name:a.value for a in spinTimerTriggerSourceEnums}
drspinTimerTriggerSourceEnums={a.value:a.name for a in spinTimerTriggerSourceEnums}


class spinTimerTriggerActivationEnums(enum.IntEnum):
    TimerTriggerActivation_RisingEdge =_int32(0)
    TimerTriggerActivation_FallingEdge=_int32(1)
    TimerTriggerActivation_AnyEdge    =_int32(2)
    TimerTriggerActivation_LevelHigh  =_int32(3)
    TimerTriggerActivation_LevelLow   =_int32(4)
    NUM_TIMERTRIGGERACTIVATION        =_int32(5)
dspinTimerTriggerActivationEnums={a.name:a.value for a in spinTimerTriggerActivationEnums}
drspinTimerTriggerActivationEnums={a.value:a.name for a in spinTimerTriggerActivationEnums}


class spinEncoderSelectorEnums(enum.IntEnum):
    EncoderSelector_Encoder0=_int32(0)
    EncoderSelector_Encoder1=_int32(1)
    EncoderSelector_Encoder2=_int32(2)
    NUM_ENCODERSELECTOR     =_int32(3)
dspinEncoderSelectorEnums={a.name:a.value for a in spinEncoderSelectorEnums}
drspinEncoderSelectorEnums={a.value:a.name for a in spinEncoderSelectorEnums}


class spinEncoderSourceAEnums(enum.IntEnum):
    EncoderSourceA_Off  =_int32(0)
    EncoderSourceA_Line0=_int32(1)
    EncoderSourceA_Line1=_int32(2)
    EncoderSourceA_Line2=_int32(3)
    NUM_ENCODERSOURCEA  =_int32(4)
dspinEncoderSourceAEnums={a.name:a.value for a in spinEncoderSourceAEnums}
drspinEncoderSourceAEnums={a.value:a.name for a in spinEncoderSourceAEnums}


class spinEncoderSourceBEnums(enum.IntEnum):
    EncoderSourceB_Off  =_int32(0)
    EncoderSourceB_Line0=_int32(1)
    EncoderSourceB_Line1=_int32(2)
    EncoderSourceB_Line2=_int32(3)
    NUM_ENCODERSOURCEB  =_int32(4)
dspinEncoderSourceBEnums={a.name:a.value for a in spinEncoderSourceBEnums}
drspinEncoderSourceBEnums={a.value:a.name for a in spinEncoderSourceBEnums}


class spinEncoderModeEnums(enum.IntEnum):
    EncoderMode_FourPhase     =_int32(0)
    EncoderMode_HighResolution=_int32(1)
    NUM_ENCODERMODE           =_int32(2)
dspinEncoderModeEnums={a.name:a.value for a in spinEncoderModeEnums}
drspinEncoderModeEnums={a.value:a.name for a in spinEncoderModeEnums}


class spinEncoderOutputModeEnums(enum.IntEnum):
    EncoderOutputMode_Off          =_int32(0)
    EncoderOutputMode_PositionUp   =_int32(1)
    EncoderOutputMode_PositionDown =_int32(2)
    EncoderOutputMode_DirectionUp  =_int32(3)
    EncoderOutputMode_DirectionDown=_int32(4)
    EncoderOutputMode_Motion       =_int32(5)
    NUM_ENCODEROUTPUTMODE          =_int32(6)
dspinEncoderOutputModeEnums={a.name:a.value for a in spinEncoderOutputModeEnums}
drspinEncoderOutputModeEnums={a.value:a.name for a in spinEncoderOutputModeEnums}


class spinEncoderStatusEnums(enum.IntEnum):
    EncoderStatus_EncoderUp    =_int32(0)
    EncoderStatus_EncoderDown  =_int32(1)
    EncoderStatus_EncoderIdle  =_int32(2)
    EncoderStatus_EncoderStatic=_int32(3)
    NUM_ENCODERSTATUS          =_int32(4)
dspinEncoderStatusEnums={a.name:a.value for a in spinEncoderStatusEnums}
drspinEncoderStatusEnums={a.value:a.name for a in spinEncoderStatusEnums}


class spinEncoderResetSourceEnums(enum.IntEnum):
    EncoderResetSource_Off               =_int32(0)
    EncoderResetSource_AcquisitionTrigger=_int32(1)
    EncoderResetSource_AcquisitionStart  =_int32(2)
    EncoderResetSource_AcquisitionEnd    =_int32(3)
    EncoderResetSource_FrameTrigger      =_int32(4)
    EncoderResetSource_FrameStart        =_int32(5)
    EncoderResetSource_FrameEnd          =_int32(6)
    EncoderResetSource_ExposureStart     =_int32(7)
    EncoderResetSource_ExposureEnd       =_int32(8)
    EncoderResetSource_Line0             =_int32(9)
    EncoderResetSource_Line1             =_int32(10)
    EncoderResetSource_Line2             =_int32(11)
    EncoderResetSource_Counter0Start     =_int32(12)
    EncoderResetSource_Counter1Start     =_int32(13)
    EncoderResetSource_Counter2Start     =_int32(14)
    EncoderResetSource_Counter0End       =_int32(15)
    EncoderResetSource_Counter1End       =_int32(16)
    EncoderResetSource_Counter2End       =_int32(17)
    EncoderResetSource_Timer0Start       =_int32(18)
    EncoderResetSource_Timer1Start       =_int32(19)
    EncoderResetSource_Timer2Start       =_int32(20)
    EncoderResetSource_Timer0End         =_int32(21)
    EncoderResetSource_Timer1End         =_int32(22)
    EncoderResetSource_Timer2End         =_int32(23)
    EncoderResetSource_UserOutput0       =_int32(24)
    EncoderResetSource_UserOutput1       =_int32(25)
    EncoderResetSource_UserOutput2       =_int32(26)
    EncoderResetSource_SoftwareSignal0   =_int32(27)
    EncoderResetSource_SoftwareSignal1   =_int32(28)
    EncoderResetSource_SoftwareSignal2   =_int32(29)
    EncoderResetSource_Action0           =_int32(30)
    EncoderResetSource_Action1           =_int32(31)
    EncoderResetSource_Action2           =_int32(32)
    EncoderResetSource_LinkTrigger0      =_int32(33)
    EncoderResetSource_LinkTrigger1      =_int32(34)
    EncoderResetSource_LinkTrigger2      =_int32(35)
    NUM_ENCODERRESETSOURCE               =_int32(36)
dspinEncoderResetSourceEnums={a.name:a.value for a in spinEncoderResetSourceEnums}
drspinEncoderResetSourceEnums={a.value:a.name for a in spinEncoderResetSourceEnums}


class spinEncoderResetActivationEnums(enum.IntEnum):
    EncoderResetActivation_RisingEdge =_int32(0)
    EncoderResetActivation_FallingEdge=_int32(1)
    EncoderResetActivation_AnyEdge    =_int32(2)
    EncoderResetActivation_LevelHigh  =_int32(3)
    EncoderResetActivation_LevelLow   =_int32(4)
    NUM_ENCODERRESETACTIVATION        =_int32(5)
dspinEncoderResetActivationEnums={a.name:a.value for a in spinEncoderResetActivationEnums}
drspinEncoderResetActivationEnums={a.value:a.name for a in spinEncoderResetActivationEnums}


class spinSoftwareSignalSelectorEnums(enum.IntEnum):
    SoftwareSignalSelector_SoftwareSignal0=_int32(0)
    SoftwareSignalSelector_SoftwareSignal1=_int32(1)
    SoftwareSignalSelector_SoftwareSignal2=_int32(2)
    NUM_SOFTWARESIGNALSELECTOR            =_int32(3)
dspinSoftwareSignalSelectorEnums={a.name:a.value for a in spinSoftwareSignalSelectorEnums}
drspinSoftwareSignalSelectorEnums={a.value:a.name for a in spinSoftwareSignalSelectorEnums}


class spinActionUnconditionalModeEnums(enum.IntEnum):
    ActionUnconditionalMode_Off=_int32(0)
    ActionUnconditionalMode_On =_int32(1)
    NUM_ACTIONUNCONDITIONALMODE=_int32(2)
dspinActionUnconditionalModeEnums={a.name:a.value for a in spinActionUnconditionalModeEnums}
drspinActionUnconditionalModeEnums={a.value:a.name for a in spinActionUnconditionalModeEnums}


class spinSourceSelectorEnums(enum.IntEnum):
    SourceSelector_Source0=_int32(0)
    SourceSelector_Source1=_int32(1)
    SourceSelector_Source2=_int32(2)
    SourceSelector_All    =_int32(3)
    NUM_SOURCESELECTOR    =_int32(4)
dspinSourceSelectorEnums={a.name:a.value for a in spinSourceSelectorEnums}
drspinSourceSelectorEnums={a.value:a.name for a in spinSourceSelectorEnums}


class spinTransferSelectorEnums(enum.IntEnum):
    TransferSelector_Stream0=_int32(0)
    TransferSelector_Stream1=_int32(1)
    TransferSelector_Stream2=_int32(2)
    TransferSelector_All    =_int32(3)
    NUM_TRANSFERSELECTOR    =_int32(4)
dspinTransferSelectorEnums={a.name:a.value for a in spinTransferSelectorEnums}
drspinTransferSelectorEnums={a.value:a.name for a in spinTransferSelectorEnums}


class spinTransferTriggerSelectorEnums(enum.IntEnum):
    TransferTriggerSelector_TransferStart     =_int32(0)
    TransferTriggerSelector_TransferStop      =_int32(1)
    TransferTriggerSelector_TransferAbort     =_int32(2)
    TransferTriggerSelector_TransferPause     =_int32(3)
    TransferTriggerSelector_TransferResume    =_int32(4)
    TransferTriggerSelector_TransferActive    =_int32(5)
    TransferTriggerSelector_TransferBurstStart=_int32(6)
    TransferTriggerSelector_TransferBurstStop =_int32(7)
    NUM_TRANSFERTRIGGERSELECTOR               =_int32(8)
dspinTransferTriggerSelectorEnums={a.name:a.value for a in spinTransferTriggerSelectorEnums}
drspinTransferTriggerSelectorEnums={a.value:a.name for a in spinTransferTriggerSelectorEnums}


class spinTransferTriggerModeEnums(enum.IntEnum):
    TransferTriggerMode_Off=_int32(0)
    TransferTriggerMode_On =_int32(1)
    NUM_TRANSFERTRIGGERMODE=_int32(2)
dspinTransferTriggerModeEnums={a.name:a.value for a in spinTransferTriggerModeEnums}
drspinTransferTriggerModeEnums={a.value:a.name for a in spinTransferTriggerModeEnums}


class spinTransferTriggerSourceEnums(enum.IntEnum):
    TransferTriggerSource_Line0          =_int32(0)
    TransferTriggerSource_Line1          =_int32(1)
    TransferTriggerSource_Line2          =_int32(2)
    TransferTriggerSource_Counter0Start  =_int32(3)
    TransferTriggerSource_Counter1Start  =_int32(4)
    TransferTriggerSource_Counter2Start  =_int32(5)
    TransferTriggerSource_Counter0End    =_int32(6)
    TransferTriggerSource_Counter1End    =_int32(7)
    TransferTriggerSource_Counter2End    =_int32(8)
    TransferTriggerSource_Timer0Start    =_int32(9)
    TransferTriggerSource_Timer1Start    =_int32(10)
    TransferTriggerSource_Timer2Start    =_int32(11)
    TransferTriggerSource_Timer0End      =_int32(12)
    TransferTriggerSource_Timer1End      =_int32(13)
    TransferTriggerSource_Timer2End      =_int32(14)
    TransferTriggerSource_SoftwareSignal0=_int32(15)
    TransferTriggerSource_SoftwareSignal1=_int32(16)
    TransferTriggerSource_SoftwareSignal2=_int32(17)
    TransferTriggerSource_Action0        =_int32(18)
    TransferTriggerSource_Action1        =_int32(19)
    TransferTriggerSource_Action2        =_int32(20)
    NUM_TRANSFERTRIGGERSOURCE            =_int32(21)
dspinTransferTriggerSourceEnums={a.name:a.value for a in spinTransferTriggerSourceEnums}
drspinTransferTriggerSourceEnums={a.value:a.name for a in spinTransferTriggerSourceEnums}


class spinTransferTriggerActivationEnums(enum.IntEnum):
    TransferTriggerActivation_RisingEdge =_int32(0)
    TransferTriggerActivation_FallingEdge=_int32(1)
    TransferTriggerActivation_AnyEdge    =_int32(2)
    TransferTriggerActivation_LevelHigh  =_int32(3)
    TransferTriggerActivation_LevelLow   =_int32(4)
    NUM_TRANSFERTRIGGERACTIVATION        =_int32(5)
dspinTransferTriggerActivationEnums={a.name:a.value for a in spinTransferTriggerActivationEnums}
drspinTransferTriggerActivationEnums={a.value:a.name for a in spinTransferTriggerActivationEnums}


class spinTransferStatusSelectorEnums(enum.IntEnum):
    TransferStatusSelector_Streaming    =_int32(0)
    TransferStatusSelector_Paused       =_int32(1)
    TransferStatusSelector_Stopping     =_int32(2)
    TransferStatusSelector_Stopped      =_int32(3)
    TransferStatusSelector_QueueOverflow=_int32(4)
    NUM_TRANSFERSTATUSSELECTOR          =_int32(5)
dspinTransferStatusSelectorEnums={a.name:a.value for a in spinTransferStatusSelectorEnums}
drspinTransferStatusSelectorEnums={a.value:a.name for a in spinTransferStatusSelectorEnums}


class spinTransferComponentSelectorEnums(enum.IntEnum):
    TransferComponentSelector_Red  =_int32(0)
    TransferComponentSelector_Green=_int32(1)
    TransferComponentSelector_Blue =_int32(2)
    TransferComponentSelector_All  =_int32(3)
    NUM_TRANSFERCOMPONENTSELECTOR  =_int32(4)
dspinTransferComponentSelectorEnums={a.name:a.value for a in spinTransferComponentSelectorEnums}
drspinTransferComponentSelectorEnums={a.value:a.name for a in spinTransferComponentSelectorEnums}


class spinScan3dDistanceUnitEnums(enum.IntEnum):
    Scan3dDistanceUnit_Millimeter=_int32(0)
    Scan3dDistanceUnit_Inch      =_int32(1)
    NUM_SCAN3DDISTANCEUNIT       =_int32(2)
dspinScan3dDistanceUnitEnums={a.name:a.value for a in spinScan3dDistanceUnitEnums}
drspinScan3dDistanceUnitEnums={a.value:a.name for a in spinScan3dDistanceUnitEnums}


class spinScan3dCoordinateSystemEnums(enum.IntEnum):
    Scan3dCoordinateSystem_Cartesian  =_int32(0)
    Scan3dCoordinateSystem_Spherical  =_int32(1)
    Scan3dCoordinateSystem_Cylindrical=_int32(2)
    NUM_SCAN3DCOORDINATESYSTEM        =_int32(3)
dspinScan3dCoordinateSystemEnums={a.name:a.value for a in spinScan3dCoordinateSystemEnums}
drspinScan3dCoordinateSystemEnums={a.value:a.name for a in spinScan3dCoordinateSystemEnums}


class spinScan3dOutputModeEnums(enum.IntEnum):
    Scan3dOutputMode_UncalibratedC           =_int32(0)
    Scan3dOutputMode_CalibratedABC_Grid      =_int32(1)
    Scan3dOutputMode_CalibratedABC_PointCloud=_int32(2)
    Scan3dOutputMode_CalibratedAC            =_int32(3)
    Scan3dOutputMode_CalibratedAC_Linescan   =_int32(4)
    Scan3dOutputMode_CalibratedC             =_int32(5)
    Scan3dOutputMode_CalibratedC_Linescan    =_int32(6)
    Scan3dOutputMode_RectifiedC              =_int32(7)
    Scan3dOutputMode_RectifiedC_Linescan     =_int32(8)
    Scan3dOutputMode_DisparityC              =_int32(9)
    Scan3dOutputMode_DisparityC_Linescan     =_int32(10)
    NUM_SCAN3DOUTPUTMODE                     =_int32(11)
dspinScan3dOutputModeEnums={a.name:a.value for a in spinScan3dOutputModeEnums}
drspinScan3dOutputModeEnums={a.value:a.name for a in spinScan3dOutputModeEnums}


class spinScan3dCoordinateSystemReferenceEnums(enum.IntEnum):
    Scan3dCoordinateSystemReference_Anchor     =_int32(0)
    Scan3dCoordinateSystemReference_Transformed=_int32(1)
    NUM_SCAN3DCOORDINATESYSTEMREFERENCE        =_int32(2)
dspinScan3dCoordinateSystemReferenceEnums={a.name:a.value for a in spinScan3dCoordinateSystemReferenceEnums}
drspinScan3dCoordinateSystemReferenceEnums={a.value:a.name for a in spinScan3dCoordinateSystemReferenceEnums}


class spinScan3dCoordinateSelectorEnums(enum.IntEnum):
    Scan3dCoordinateSelector_CoordinateA=_int32(0)
    Scan3dCoordinateSelector_CoordinateB=_int32(1)
    Scan3dCoordinateSelector_CoordinateC=_int32(2)
    NUM_SCAN3DCOORDINATESELECTOR        =_int32(3)
dspinScan3dCoordinateSelectorEnums={a.name:a.value for a in spinScan3dCoordinateSelectorEnums}
drspinScan3dCoordinateSelectorEnums={a.value:a.name for a in spinScan3dCoordinateSelectorEnums}


class spinScan3dCoordinateTransformSelectorEnums(enum.IntEnum):
    Scan3dCoordinateTransformSelector_RotationX   =_int32(0)
    Scan3dCoordinateTransformSelector_RotationY   =_int32(1)
    Scan3dCoordinateTransformSelector_RotationZ   =_int32(2)
    Scan3dCoordinateTransformSelector_TranslationX=_int32(3)
    Scan3dCoordinateTransformSelector_TranslationY=_int32(4)
    Scan3dCoordinateTransformSelector_TranslationZ=_int32(5)
    NUM_SCAN3DCOORDINATETRANSFORMSELECTOR         =_int32(6)
dspinScan3dCoordinateTransformSelectorEnums={a.name:a.value for a in spinScan3dCoordinateTransformSelectorEnums}
drspinScan3dCoordinateTransformSelectorEnums={a.value:a.name for a in spinScan3dCoordinateTransformSelectorEnums}


class spinScan3dCoordinateReferenceSelectorEnums(enum.IntEnum):
    Scan3dCoordinateReferenceSelector_RotationX   =_int32(0)
    Scan3dCoordinateReferenceSelector_RotationY   =_int32(1)
    Scan3dCoordinateReferenceSelector_RotationZ   =_int32(2)
    Scan3dCoordinateReferenceSelector_TranslationX=_int32(3)
    Scan3dCoordinateReferenceSelector_TranslationY=_int32(4)
    Scan3dCoordinateReferenceSelector_TranslationZ=_int32(5)
    NUM_SCAN3DCOORDINATEREFERENCESELECTOR         =_int32(6)
dspinScan3dCoordinateReferenceSelectorEnums={a.name:a.value for a in spinScan3dCoordinateReferenceSelectorEnums}
drspinScan3dCoordinateReferenceSelectorEnums={a.value:a.name for a in spinScan3dCoordinateReferenceSelectorEnums}


class spinChunkImageComponentEnums(enum.IntEnum):
    ChunkImageComponent_Intensity  =_int32(0)
    ChunkImageComponent_Color      =_int32(1)
    ChunkImageComponent_Infrared   =_int32(2)
    ChunkImageComponent_Ultraviolet=_int32(3)
    ChunkImageComponent_Range      =_int32(4)
    ChunkImageComponent_Disparity  =_int32(5)
    ChunkImageComponent_Confidence =_int32(6)
    ChunkImageComponent_Scatter    =_int32(7)
    NUM_CHUNKIMAGECOMPONENT        =_int32(8)
dspinChunkImageComponentEnums={a.name:a.value for a in spinChunkImageComponentEnums}
drspinChunkImageComponentEnums={a.value:a.name for a in spinChunkImageComponentEnums}


class spinChunkCounterSelectorEnums(enum.IntEnum):
    ChunkCounterSelector_Counter0=_int32(0)
    ChunkCounterSelector_Counter1=_int32(1)
    ChunkCounterSelector_Counter2=_int32(2)
    NUM_CHUNKCOUNTERSELECTOR     =_int32(3)
dspinChunkCounterSelectorEnums={a.name:a.value for a in spinChunkCounterSelectorEnums}
drspinChunkCounterSelectorEnums={a.value:a.name for a in spinChunkCounterSelectorEnums}


class spinChunkTimerSelectorEnums(enum.IntEnum):
    ChunkTimerSelector_Timer0=_int32(0)
    ChunkTimerSelector_Timer1=_int32(1)
    ChunkTimerSelector_Timer2=_int32(2)
    NUM_CHUNKTIMERSELECTOR   =_int32(3)
dspinChunkTimerSelectorEnums={a.name:a.value for a in spinChunkTimerSelectorEnums}
drspinChunkTimerSelectorEnums={a.value:a.name for a in spinChunkTimerSelectorEnums}


class spinChunkEncoderSelectorEnums(enum.IntEnum):
    ChunkEncoderSelector_Encoder0=_int32(0)
    ChunkEncoderSelector_Encoder1=_int32(1)
    ChunkEncoderSelector_Encoder2=_int32(2)
    NUM_CHUNKENCODERSELECTOR     =_int32(3)
dspinChunkEncoderSelectorEnums={a.name:a.value for a in spinChunkEncoderSelectorEnums}
drspinChunkEncoderSelectorEnums={a.value:a.name for a in spinChunkEncoderSelectorEnums}


class spinChunkEncoderStatusEnums(enum.IntEnum):
    ChunkEncoderStatus_EncoderUp    =_int32(0)
    ChunkEncoderStatus_EncoderDown  =_int32(1)
    ChunkEncoderStatus_EncoderIdle  =_int32(2)
    ChunkEncoderStatus_EncoderStatic=_int32(3)
    NUM_CHUNKENCODERSTATUS          =_int32(4)
dspinChunkEncoderStatusEnums={a.name:a.value for a in spinChunkEncoderStatusEnums}
drspinChunkEncoderStatusEnums={a.value:a.name for a in spinChunkEncoderStatusEnums}


class spinChunkExposureTimeSelectorEnums(enum.IntEnum):
    ChunkExposureTimeSelector_Common     =_int32(0)
    ChunkExposureTimeSelector_Red        =_int32(1)
    ChunkExposureTimeSelector_Green      =_int32(2)
    ChunkExposureTimeSelector_Blue       =_int32(3)
    ChunkExposureTimeSelector_Cyan       =_int32(4)
    ChunkExposureTimeSelector_Magenta    =_int32(5)
    ChunkExposureTimeSelector_Yellow     =_int32(6)
    ChunkExposureTimeSelector_Infrared   =_int32(7)
    ChunkExposureTimeSelector_Ultraviolet=_int32(8)
    ChunkExposureTimeSelector_Stage1     =_int32(9)
    ChunkExposureTimeSelector_Stage2     =_int32(10)
    NUM_CHUNKEXPOSURETIMESELECTOR        =_int32(11)
dspinChunkExposureTimeSelectorEnums={a.name:a.value for a in spinChunkExposureTimeSelectorEnums}
drspinChunkExposureTimeSelectorEnums={a.value:a.name for a in spinChunkExposureTimeSelectorEnums}


class spinChunkSourceIDEnums(enum.IntEnum):
    ChunkSourceID_Source0=_int32(0)
    ChunkSourceID_Source1=_int32(1)
    ChunkSourceID_Source2=_int32(2)
    NUM_CHUNKSOURCEID    =_int32(3)
dspinChunkSourceIDEnums={a.name:a.value for a in spinChunkSourceIDEnums}
drspinChunkSourceIDEnums={a.value:a.name for a in spinChunkSourceIDEnums}


class spinChunkRegionIDEnums(enum.IntEnum):
    ChunkRegionID_Region0=_int32(0)
    ChunkRegionID_Region1=_int32(1)
    ChunkRegionID_Region2=_int32(2)
    NUM_CHUNKREGIONID    =_int32(3)
dspinChunkRegionIDEnums={a.name:a.value for a in spinChunkRegionIDEnums}
drspinChunkRegionIDEnums={a.value:a.name for a in spinChunkRegionIDEnums}


class spinChunkTransferStreamIDEnums(enum.IntEnum):
    ChunkTransferStreamID_Stream0=_int32(0)
    ChunkTransferStreamID_Stream1=_int32(1)
    ChunkTransferStreamID_Stream2=_int32(2)
    ChunkTransferStreamID_Stream3=_int32(3)
    NUM_CHUNKTRANSFERSTREAMID    =_int32(4)
dspinChunkTransferStreamIDEnums={a.name:a.value for a in spinChunkTransferStreamIDEnums}
drspinChunkTransferStreamIDEnums={a.value:a.name for a in spinChunkTransferStreamIDEnums}


class spinChunkScan3dDistanceUnitEnums(enum.IntEnum):
    ChunkScan3dDistanceUnit_Millimeter=_int32(0)
    ChunkScan3dDistanceUnit_Inch      =_int32(1)
    NUM_CHUNKSCAN3DDISTANCEUNIT       =_int32(2)
dspinChunkScan3dDistanceUnitEnums={a.name:a.value for a in spinChunkScan3dDistanceUnitEnums}
drspinChunkScan3dDistanceUnitEnums={a.value:a.name for a in spinChunkScan3dDistanceUnitEnums}


class spinChunkScan3dOutputModeEnums(enum.IntEnum):
    ChunkScan3dOutputMode_UncalibratedC           =_int32(0)
    ChunkScan3dOutputMode_CalibratedABC_Grid      =_int32(1)
    ChunkScan3dOutputMode_CalibratedABC_PointCloud=_int32(2)
    ChunkScan3dOutputMode_CalibratedAC            =_int32(3)
    ChunkScan3dOutputMode_CalibratedAC_Linescan   =_int32(4)
    ChunkScan3dOutputMode_CalibratedC             =_int32(5)
    ChunkScan3dOutputMode_CalibratedC_Linescan    =_int32(6)
    ChunkScan3dOutputMode_RectifiedC              =_int32(7)
    ChunkScan3dOutputMode_RectifiedC_Linescan     =_int32(8)
    ChunkScan3dOutputMode_DisparityC              =_int32(9)
    ChunkScan3dOutputMode_DisparityC_Linescan     =_int32(10)
    NUM_CHUNKSCAN3DOUTPUTMODE                     =_int32(11)
dspinChunkScan3dOutputModeEnums={a.name:a.value for a in spinChunkScan3dOutputModeEnums}
drspinChunkScan3dOutputModeEnums={a.value:a.name for a in spinChunkScan3dOutputModeEnums}


class spinChunkScan3dCoordinateSystemEnums(enum.IntEnum):
    ChunkScan3dCoordinateSystem_Cartesian  =_int32(0)
    ChunkScan3dCoordinateSystem_Spherical  =_int32(1)
    ChunkScan3dCoordinateSystem_Cylindrical=_int32(2)
    NUM_CHUNKSCAN3DCOORDINATESYSTEM        =_int32(3)
dspinChunkScan3dCoordinateSystemEnums={a.name:a.value for a in spinChunkScan3dCoordinateSystemEnums}
drspinChunkScan3dCoordinateSystemEnums={a.value:a.name for a in spinChunkScan3dCoordinateSystemEnums}


class spinChunkScan3dCoordinateSystemReferenceEnums(enum.IntEnum):
    ChunkScan3dCoordinateSystemReference_Anchor     =_int32(0)
    ChunkScan3dCoordinateSystemReference_Transformed=_int32(1)
    NUM_CHUNKSCAN3DCOORDINATESYSTEMREFERENCE        =_int32(2)
dspinChunkScan3dCoordinateSystemReferenceEnums={a.name:a.value for a in spinChunkScan3dCoordinateSystemReferenceEnums}
drspinChunkScan3dCoordinateSystemReferenceEnums={a.value:a.name for a in spinChunkScan3dCoordinateSystemReferenceEnums}


class spinChunkScan3dCoordinateSelectorEnums(enum.IntEnum):
    ChunkScan3dCoordinateSelector_CoordinateA=_int32(0)
    ChunkScan3dCoordinateSelector_CoordinateB=_int32(1)
    ChunkScan3dCoordinateSelector_CoordinateC=_int32(2)
    NUM_CHUNKSCAN3DCOORDINATESELECTOR        =_int32(3)
dspinChunkScan3dCoordinateSelectorEnums={a.name:a.value for a in spinChunkScan3dCoordinateSelectorEnums}
drspinChunkScan3dCoordinateSelectorEnums={a.value:a.name for a in spinChunkScan3dCoordinateSelectorEnums}


class spinChunkScan3dCoordinateTransformSelectorEnums(enum.IntEnum):
    ChunkScan3dCoordinateTransformSelector_RotationX   =_int32(0)
    ChunkScan3dCoordinateTransformSelector_RotationY   =_int32(1)
    ChunkScan3dCoordinateTransformSelector_RotationZ   =_int32(2)
    ChunkScan3dCoordinateTransformSelector_TranslationX=_int32(3)
    ChunkScan3dCoordinateTransformSelector_TranslationY=_int32(4)
    ChunkScan3dCoordinateTransformSelector_TranslationZ=_int32(5)
    NUM_CHUNKSCAN3DCOORDINATETRANSFORMSELECTOR         =_int32(6)
dspinChunkScan3dCoordinateTransformSelectorEnums={a.name:a.value for a in spinChunkScan3dCoordinateTransformSelectorEnums}
drspinChunkScan3dCoordinateTransformSelectorEnums={a.value:a.name for a in spinChunkScan3dCoordinateTransformSelectorEnums}


class spinChunkScan3dCoordinateReferenceSelectorEnums(enum.IntEnum):
    ChunkScan3dCoordinateReferenceSelector_RotationX   =_int32(0)
    ChunkScan3dCoordinateReferenceSelector_RotationY   =_int32(1)
    ChunkScan3dCoordinateReferenceSelector_RotationZ   =_int32(2)
    ChunkScan3dCoordinateReferenceSelector_TranslationX=_int32(3)
    ChunkScan3dCoordinateReferenceSelector_TranslationY=_int32(4)
    ChunkScan3dCoordinateReferenceSelector_TranslationZ=_int32(5)
    NUM_CHUNKSCAN3DCOORDINATEREFERENCESELECTOR         =_int32(6)
dspinChunkScan3dCoordinateReferenceSelectorEnums={a.name:a.value for a in spinChunkScan3dCoordinateReferenceSelectorEnums}
drspinChunkScan3dCoordinateReferenceSelectorEnums={a.value:a.name for a in spinChunkScan3dCoordinateReferenceSelectorEnums}


class spinDeviceTapGeometryEnums(enum.IntEnum):
    DeviceTapGeometry_Geometry_1X_1Y                  =_int32(0)
    DeviceTapGeometry_Geometry_1X2_1Y                 =_int32(1)
    DeviceTapGeometry_Geometry_1X2_1Y2                =_int32(2)
    DeviceTapGeometry_Geometry_2X_1Y                  =_int32(3)
    DeviceTapGeometry_Geometry_2X_1Y2Geometry_2XE_1Y  =_int32(4)
    DeviceTapGeometry_Geometry_2XE_1Y2                =_int32(5)
    DeviceTapGeometry_Geometry_2XM_1Y                 =_int32(6)
    DeviceTapGeometry_Geometry_2XM_1Y2                =_int32(7)
    DeviceTapGeometry_Geometry_1X_1Y2                 =_int32(8)
    DeviceTapGeometry_Geometry_1X_2YE                 =_int32(9)
    DeviceTapGeometry_Geometry_1X3_1Y                 =_int32(10)
    DeviceTapGeometry_Geometry_3X_1Y                  =_int32(11)
    DeviceTapGeometry_Geometry_1X                     =_int32(12)
    DeviceTapGeometry_Geometry_1X2                    =_int32(13)
    DeviceTapGeometry_Geometry_2X                     =_int32(14)
    DeviceTapGeometry_Geometry_2XE                    =_int32(15)
    DeviceTapGeometry_Geometry_2XM                    =_int32(16)
    DeviceTapGeometry_Geometry_1X3                    =_int32(17)
    DeviceTapGeometry_Geometry_3X                     =_int32(18)
    DeviceTapGeometry_Geometry_1X4_1Y                 =_int32(19)
    DeviceTapGeometry_Geometry_4X_1Y                  =_int32(20)
    DeviceTapGeometry_Geometry_2X2_1Y                 =_int32(21)
    DeviceTapGeometry_Geometry_2X2E_1YGeometry_2X2M_1Y=_int32(22)
    DeviceTapGeometry_Geometry_1X2_2YE                =_int32(23)
    DeviceTapGeometry_Geometry_2X_2YE                 =_int32(24)
    DeviceTapGeometry_Geometry_2XE_2YE                =_int32(25)
    DeviceTapGeometry_Geometry_2XM_2YE                =_int32(26)
    DeviceTapGeometry_Geometry_1X4                    =_int32(27)
    DeviceTapGeometry_Geometry_4X                     =_int32(28)
    DeviceTapGeometry_Geometry_2X2                    =_int32(29)
    DeviceTapGeometry_Geometry_2X2E                   =_int32(30)
    DeviceTapGeometry_Geometry_2X2M                   =_int32(31)
    DeviceTapGeometry_Geometry_1X8_1Y                 =_int32(32)
    DeviceTapGeometry_Geometry_8X_1Y                  =_int32(33)
    DeviceTapGeometry_Geometry_4X2_1Y                 =_int32(34)
    DeviceTapGeometry_Geometry_2X2E_2YE               =_int32(35)
    DeviceTapGeometry_Geometry_1X8                    =_int32(36)
    DeviceTapGeometry_Geometry_8X                     =_int32(37)
    DeviceTapGeometry_Geometry_4X2                    =_int32(38)
    DeviceTapGeometry_Geometry_4X2E                   =_int32(39)
    DeviceTapGeometry_Geometry_4X2E_1Y                =_int32(40)
    DeviceTapGeometry_Geometry_1X10_1Y                =_int32(41)
    DeviceTapGeometry_Geometry_10X_1Y                 =_int32(42)
    DeviceTapGeometry_Geometry_1X10                   =_int32(43)
    DeviceTapGeometry_Geometry_10X                    =_int32(44)
    NUM_DEVICETAPGEOMETRY                             =_int32(45)
dspinDeviceTapGeometryEnums={a.name:a.value for a in spinDeviceTapGeometryEnums}
drspinDeviceTapGeometryEnums={a.value:a.name for a in spinDeviceTapGeometryEnums}


class spinGevPhysicalLinkConfigurationEnums(enum.IntEnum):
    GevPhysicalLinkConfiguration_SingleLink=_int32(0)
    GevPhysicalLinkConfiguration_MultiLink =_int32(1)
    GevPhysicalLinkConfiguration_StaticLAG =_int32(2)
    GevPhysicalLinkConfiguration_DynamicLAG=_int32(3)
    NUM_GEVPHYSICALLINKCONFIGURATION       =_int32(4)
dspinGevPhysicalLinkConfigurationEnums={a.name:a.value for a in spinGevPhysicalLinkConfigurationEnums}
drspinGevPhysicalLinkConfigurationEnums={a.value:a.name for a in spinGevPhysicalLinkConfigurationEnums}


class spinGevCurrentPhysicalLinkConfigurationEnums(enum.IntEnum):
    GevCurrentPhysicalLinkConfiguration_SingleLink=_int32(0)
    GevCurrentPhysicalLinkConfiguration_MultiLink =_int32(1)
    GevCurrentPhysicalLinkConfiguration_StaticLAG =_int32(2)
    GevCurrentPhysicalLinkConfiguration_DynamicLAG=_int32(3)
    NUM_GEVCURRENTPHYSICALLINKCONFIGURATION       =_int32(4)
dspinGevCurrentPhysicalLinkConfigurationEnums={a.name:a.value for a in spinGevCurrentPhysicalLinkConfigurationEnums}
drspinGevCurrentPhysicalLinkConfigurationEnums={a.value:a.name for a in spinGevCurrentPhysicalLinkConfigurationEnums}


class spinGevIPConfigurationStatusEnums(enum.IntEnum):
    GevIPConfigurationStatus_None        =_int32(0)
    GevIPConfigurationStatus_PersistentIP=_int32(1)
    GevIPConfigurationStatus_DHCP        =_int32(2)
    GevIPConfigurationStatus_LLA         =_int32(3)
    GevIPConfigurationStatus_ForceIP     =_int32(4)
    NUM_GEVIPCONFIGURATIONSTATUS         =_int32(5)
dspinGevIPConfigurationStatusEnums={a.name:a.value for a in spinGevIPConfigurationStatusEnums}
drspinGevIPConfigurationStatusEnums={a.value:a.name for a in spinGevIPConfigurationStatusEnums}


class spinGevGVCPExtendedStatusCodesSelectorEnums(enum.IntEnum):
    GevGVCPExtendedStatusCodesSelector_Version1_1=_int32(0)
    GevGVCPExtendedStatusCodesSelector_Version2_0=_int32(1)
    NUM_GEVGVCPEXTENDEDSTATUSCODESSELECTOR       =_int32(2)
dspinGevGVCPExtendedStatusCodesSelectorEnums={a.name:a.value for a in spinGevGVCPExtendedStatusCodesSelectorEnums}
drspinGevGVCPExtendedStatusCodesSelectorEnums={a.value:a.name for a in spinGevGVCPExtendedStatusCodesSelectorEnums}


class spinGevGVSPExtendedIDModeEnums(enum.IntEnum):
    GevGVSPExtendedIDMode_Off=_int32(0)
    GevGVSPExtendedIDMode_On =_int32(1)
    NUM_GEVGVSPEXTENDEDIDMODE=_int32(2)
dspinGevGVSPExtendedIDModeEnums={a.name:a.value for a in spinGevGVSPExtendedIDModeEnums}
drspinGevGVSPExtendedIDModeEnums={a.value:a.name for a in spinGevGVSPExtendedIDModeEnums}


class spinClConfigurationEnums(enum.IntEnum):
    ClConfiguration_Base     =_int32(0)
    ClConfiguration_Medium   =_int32(1)
    ClConfiguration_Full     =_int32(2)
    ClConfiguration_DualBase =_int32(3)
    ClConfiguration_EightyBit=_int32(4)
    NUM_CLCONFIGURATION      =_int32(5)
dspinClConfigurationEnums={a.name:a.value for a in spinClConfigurationEnums}
drspinClConfigurationEnums={a.value:a.name for a in spinClConfigurationEnums}


class spinClTimeSlotsCountEnums(enum.IntEnum):
    ClTimeSlotsCount_One  =_int32(0)
    ClTimeSlotsCount_Two  =_int32(1)
    ClTimeSlotsCount_Three=_int32(2)
    NUM_CLTIMESLOTSCOUNT  =_int32(3)
dspinClTimeSlotsCountEnums={a.name:a.value for a in spinClTimeSlotsCountEnums}
drspinClTimeSlotsCountEnums={a.value:a.name for a in spinClTimeSlotsCountEnums}


class spinCxpLinkConfigurationStatusEnums(enum.IntEnum):
    CxpLinkConfigurationStatus_None   =_int32(0)
    CxpLinkConfigurationStatus_Pending=_int32(1)
    CxpLinkConfigurationStatus_CXP1_X1=_int32(2)
    CxpLinkConfigurationStatus_CXP2_X1=_int32(3)
    CxpLinkConfigurationStatus_CXP3_X1=_int32(4)
    CxpLinkConfigurationStatus_CXP5_X1=_int32(5)
    CxpLinkConfigurationStatus_CXP6_X1=_int32(6)
    CxpLinkConfigurationStatus_CXP1_X2=_int32(7)
    CxpLinkConfigurationStatus_CXP2_X2=_int32(8)
    CxpLinkConfigurationStatus_CXP3_X2=_int32(9)
    CxpLinkConfigurationStatus_CXP5_X2=_int32(10)
    CxpLinkConfigurationStatus_CXP6_X2=_int32(11)
    CxpLinkConfigurationStatus_CXP1_X3=_int32(12)
    CxpLinkConfigurationStatus_CXP2_X3=_int32(13)
    CxpLinkConfigurationStatus_CXP3_X3=_int32(14)
    CxpLinkConfigurationStatus_CXP5_X3=_int32(15)
    CxpLinkConfigurationStatus_CXP6_X3=_int32(16)
    CxpLinkConfigurationStatus_CXP1_X4=_int32(17)
    CxpLinkConfigurationStatus_CXP2_X4=_int32(18)
    CxpLinkConfigurationStatus_CXP3_X4=_int32(19)
    CxpLinkConfigurationStatus_CXP5_X4=_int32(20)
    CxpLinkConfigurationStatus_CXP6_X4=_int32(21)
    CxpLinkConfigurationStatus_CXP1_X5=_int32(22)
    CxpLinkConfigurationStatus_CXP2_X5=_int32(23)
    CxpLinkConfigurationStatus_CXP3_X5=_int32(24)
    CxpLinkConfigurationStatus_CXP5_X5=_int32(25)
    CxpLinkConfigurationStatus_CXP6_X5=_int32(26)
    CxpLinkConfigurationStatus_CXP1_X6=_int32(27)
    CxpLinkConfigurationStatus_CXP2_X6=_int32(28)
    CxpLinkConfigurationStatus_CXP3_X6=_int32(29)
    CxpLinkConfigurationStatus_CXP5_X6=_int32(30)
    CxpLinkConfigurationStatus_CXP6_X6=_int32(31)
    NUM_CXPLINKCONFIGURATIONSTATUS    =_int32(32)
dspinCxpLinkConfigurationStatusEnums={a.name:a.value for a in spinCxpLinkConfigurationStatusEnums}
drspinCxpLinkConfigurationStatusEnums={a.value:a.name for a in spinCxpLinkConfigurationStatusEnums}


class spinCxpLinkConfigurationPreferredEnums(enum.IntEnum):
    CxpLinkConfigurationPreferred_CXP1_X1=_int32(0)
    CxpLinkConfigurationPreferred_CXP2_X1=_int32(1)
    CxpLinkConfigurationPreferred_CXP3_X1=_int32(2)
    CxpLinkConfigurationPreferred_CXP5_X1=_int32(3)
    CxpLinkConfigurationPreferred_CXP6_X1=_int32(4)
    CxpLinkConfigurationPreferred_CXP1_X2=_int32(5)
    CxpLinkConfigurationPreferred_CXP2_X2=_int32(6)
    CxpLinkConfigurationPreferred_CXP3_X2=_int32(7)
    CxpLinkConfigurationPreferred_CXP5_X2=_int32(8)
    CxpLinkConfigurationPreferred_CXP6_X2=_int32(9)
    CxpLinkConfigurationPreferred_CXP1_X3=_int32(10)
    CxpLinkConfigurationPreferred_CXP2_X3=_int32(11)
    CxpLinkConfigurationPreferred_CXP3_X3=_int32(12)
    CxpLinkConfigurationPreferred_CXP5_X3=_int32(13)
    CxpLinkConfigurationPreferred_CXP6_X3=_int32(14)
    CxpLinkConfigurationPreferred_CXP1_X4=_int32(15)
    CxpLinkConfigurationPreferred_CXP2_X4=_int32(16)
    CxpLinkConfigurationPreferred_CXP3_X4=_int32(17)
    CxpLinkConfigurationPreferred_CXP5_X4=_int32(18)
    CxpLinkConfigurationPreferred_CXP6_X4=_int32(19)
    CxpLinkConfigurationPreferred_CXP1_X5=_int32(20)
    CxpLinkConfigurationPreferred_CXP2_X5=_int32(21)
    CxpLinkConfigurationPreferred_CXP3_X5=_int32(22)
    CxpLinkConfigurationPreferred_CXP5_X5=_int32(23)
    CxpLinkConfigurationPreferred_CXP6_X5=_int32(24)
    CxpLinkConfigurationPreferred_CXP1_X6=_int32(25)
    CxpLinkConfigurationPreferred_CXP2_X6=_int32(26)
    CxpLinkConfigurationPreferred_CXP3_X6=_int32(27)
    CxpLinkConfigurationPreferred_CXP5_X6=_int32(28)
    CxpLinkConfigurationPreferred_CXP6_X6=_int32(29)
    NUM_CXPLINKCONFIGURATIONPREFERRED    =_int32(30)
dspinCxpLinkConfigurationPreferredEnums={a.name:a.value for a in spinCxpLinkConfigurationPreferredEnums}
drspinCxpLinkConfigurationPreferredEnums={a.value:a.name for a in spinCxpLinkConfigurationPreferredEnums}


class spinCxpLinkConfigurationEnums(enum.IntEnum):
    CxpLinkConfiguration_Auto   =_int32(0)
    CxpLinkConfiguration_CXP1_X1=_int32(1)
    CxpLinkConfiguration_CXP2_X1=_int32(2)
    CxpLinkConfiguration_CXP3_X1=_int32(3)
    CxpLinkConfiguration_CXP5_X1=_int32(4)
    CxpLinkConfiguration_CXP6_X1=_int32(5)
    CxpLinkConfiguration_CXP1_X2=_int32(6)
    CxpLinkConfiguration_CXP2_X2=_int32(7)
    CxpLinkConfiguration_CXP3_X2=_int32(8)
    CxpLinkConfiguration_CXP5_X2=_int32(9)
    CxpLinkConfiguration_CXP6_X2=_int32(10)
    CxpLinkConfiguration_CXP1_X3=_int32(11)
    CxpLinkConfiguration_CXP2_X3=_int32(12)
    CxpLinkConfiguration_CXP3_X3=_int32(13)
    CxpLinkConfiguration_CXP5_X3=_int32(14)
    CxpLinkConfiguration_CXP6_X3=_int32(15)
    CxpLinkConfiguration_CXP1_X4=_int32(16)
    CxpLinkConfiguration_CXP2_X4=_int32(17)
    CxpLinkConfiguration_CXP3_X4=_int32(18)
    CxpLinkConfiguration_CXP5_X4=_int32(19)
    CxpLinkConfiguration_CXP6_X4=_int32(20)
    CxpLinkConfiguration_CXP1_X5=_int32(21)
    CxpLinkConfiguration_CXP2_X5=_int32(22)
    CxpLinkConfiguration_CXP3_X5=_int32(23)
    CxpLinkConfiguration_CXP5_X5=_int32(24)
    CxpLinkConfiguration_CXP6_X5=_int32(25)
    CxpLinkConfiguration_CXP1_X6=_int32(26)
    CxpLinkConfiguration_CXP2_X6=_int32(27)
    CxpLinkConfiguration_CXP3_X6=_int32(28)
    CxpLinkConfiguration_CXP5_X6=_int32(29)
    CxpLinkConfiguration_CXP6_X6=_int32(30)
    NUM_CXPLINKCONFIGURATION    =_int32(31)
dspinCxpLinkConfigurationEnums={a.name:a.value for a in spinCxpLinkConfigurationEnums}
drspinCxpLinkConfigurationEnums={a.value:a.name for a in spinCxpLinkConfigurationEnums}


class spinCxpConnectionTestModeEnums(enum.IntEnum):
    CxpConnectionTestMode_Off  =_int32(0)
    CxpConnectionTestMode_Mode1=_int32(1)
    NUM_CXPCONNECTIONTESTMODE  =_int32(2)
dspinCxpConnectionTestModeEnums={a.name:a.value for a in spinCxpConnectionTestModeEnums}
drspinCxpConnectionTestModeEnums={a.value:a.name for a in spinCxpConnectionTestModeEnums}


class spinCxpPoCxpStatusEnums(enum.IntEnum):
    CxpPoCxpStatus_Auto   =_int32(0)
    CxpPoCxpStatus_Off    =_int32(1)
    CxpPoCxpStatus_Tripped=_int32(2)
    NUM_CXPPOCXPSTATUS    =_int32(3)
dspinCxpPoCxpStatusEnums={a.name:a.value for a in spinCxpPoCxpStatusEnums}
drspinCxpPoCxpStatusEnums={a.value:a.name for a in spinCxpPoCxpStatusEnums}


class spinChunkData(ctypes.Structure):
    _fields_=[  ("m_blackLevel",ctypes.c_double),
                ("m_frameID",ctypes.c_int64),
                ("m_exposureTime",ctypes.c_double),
                ("m_compressionMode",ctypes.c_int64),
                ("m_compressionRatio",ctypes.c_double),
                ("m_timestamp",ctypes.c_int64),
                ("m_exposureEndLineStatusAll",ctypes.c_int64),
                ("m_width",ctypes.c_int64),
                ("m_image",ctypes.c_int64),
                ("m_height",ctypes.c_int64),
                ("m_gain",ctypes.c_double),
                ("m_sequencerSetActive",ctypes.c_int64),
                ("m_cRC",ctypes.c_int64),
                ("m_offsetX",ctypes.c_int64),
                ("m_offsetY",ctypes.c_int64),
                ("m_serialDataLength",ctypes.c_int64),
                ("m_partSelector",ctypes.c_int64),
                ("m_pixelDynamicRangeMin",ctypes.c_int64),
                ("m_pixelDynamicRangeMax",ctypes.c_int64),
                ("m_timestampLatchValue",ctypes.c_int64),
                ("m_lineStatusAll",ctypes.c_int64),
                ("m_counterValue",ctypes.c_int64),
                ("m_timerValue",ctypes.c_double),
                ("m_scanLineSelector",ctypes.c_int64),
                ("m_encoderValue",ctypes.c_int64),
                ("m_linePitch",ctypes.c_int64),
                ("m_transferBlockID",ctypes.c_int64),
                ("m_transferQueueCurrentBlockCount",ctypes.c_int64),
                ("m_streamChannelID",ctypes.c_int64),
                ("m_scan3dCoordinateScale",ctypes.c_double),
                ("m_scan3dCoordinateOffset",ctypes.c_double),
                ("m_scan3dInvalidDataValue",ctypes.c_double),
                ("m_scan3dAxisMin",ctypes.c_double),
                ("m_scan3dAxisMax",ctypes.c_double),
                ("m_scan3dTransformValue",ctypes.c_double),
                ("m_scan3dCoordinateReferenceValue",ctypes.c_double),
                ("m_inferenceFrameId",ctypes.c_int64),
                ("m_inferenceResult",ctypes.c_int64),
                ("m_inferenceConfidence",ctypes.c_double) ]
PspinChunkData=ctypes.POINTER(spinChunkData)
class CspinChunkData(ctypes_wrap.CStructWrapper):
    _struct=spinChunkData


spinNodeMapHandle=ctypes.c_void_p
spinNodeHandle=ctypes.c_void_p
spinNodeCallbackHandle=ctypes.c_void_p
spinNodeCallbackFunction=ctypes.c_void_p
class spinNodeType(enum.IntEnum):
    ValueNode      =_int32(0)
    BaseNode       =_int32(1)
    IntegerNode    =_int32(2)
    BooleanNode    =_int32(3)
    FloatNode      =_int32(4)
    CommandNode    =_int32(5)
    StringNode     =_int32(6)
    RegisterNode   =_int32(7)
    EnumerationNode=_int32(8)
    EnumEntryNode  =_int32(9)
    CategoryNode   =_int32(10)
    PortNode       =_int32(11)
    UnknownNode    =_int32((-1))
dspinNodeType={a.name:a.value for a in spinNodeType}
drspinNodeType={a.value:a.name for a in spinNodeType}


class spinSign(enum.IntEnum):
    Signed        =_int32(0)
    Unsigned      =_int32(1)
    _UndefinedSign=_int32(2)
dspinSign={a.name:a.value for a in spinSign}
drspinSign={a.value:a.name for a in spinSign}


class spinAccessMode(enum.IntEnum):
    NI                   =_int32(0)
    NA                   =_int32(1)
    WO                   =_int32(2)
    RO                   =_int32(3)
    RW                   =_int32(4)
    _UndefinedAccesMode  =_int32(5)
    _CycleDetectAccesMode=_int32(6)
dspinAccessMode={a.name:a.value for a in spinAccessMode}
drspinAccessMode={a.value:a.name for a in spinAccessMode}


class spinVisibility(enum.IntEnum):
    Beginner            =_int32(0)
    Expert              =_int32(1)
    Guru                =_int32(2)
    Invisible           =_int32(3)
    _UndefinedVisibility=_int32(99)
dspinVisibility={a.name:a.value for a in spinVisibility}
drspinVisibility={a.value:a.name for a in spinVisibility}


class spinCachingMode(enum.IntEnum):
    NoCache              =_int32(0)
    WriteThrough         =_int32(1)
    WriteAround          =_int32(2)
    _UndefinedCachingMode=_int32(3)
dspinCachingMode={a.name:a.value for a in spinCachingMode}
drspinCachingMode={a.value:a.name for a in spinCachingMode}


class spinRepresentation(enum.IntEnum):
    Linear                  =_int32(0)
    Logarithmic             =_int32(1)
    Boolean                 =_int32(2)
    PureNumber              =_int32(3)
    HexNumber               =_int32(4)
    IPV4Address             =_int32(5)
    MACAddress              =_int32(6)
    _UndefinedRepresentation=_int32(7)
dspinRepresentation={a.name:a.value for a in spinRepresentation}
drspinRepresentation={a.value:a.name for a in spinRepresentation}


class spinEndianess(enum.IntEnum):
    BigEndian       =_int32(0)
    LittleEndian    =_int32(1)
    _UndefinedEndian=_int32(2)
dspinEndianess={a.name:a.value for a in spinEndianess}
drspinEndianess={a.value:a.name for a in spinEndianess}


class spinNameSpace(enum.IntEnum):
    Custom             =_int32(0)
    Standard           =_int32(1)
    _UndefinedNameSpace=_int32(2)
dspinNameSpace={a.name:a.value for a in spinNameSpace}
drspinNameSpace={a.value:a.name for a in spinNameSpace}


class spinStandardNameSpace(enum.IntEnum):
    NONE                       =_int32(0)
    GEV                        =_int32(1)
    IIDC                       =_int32(2)
    CL                         =_int32(3)
    USB                        =_int32(4)
    _UndefinedStandardNameSpace=_int32(5)
dspinStandardNameSpace={a.name:a.value for a in spinStandardNameSpace}
drspinStandardNameSpace={a.value:a.name for a in spinStandardNameSpace}


class spinYesNo(enum.IntEnum):
    Yes            =_int32(1)
    No             =_int32(0)
    _UndefinedYesNo=_int32(2)
dspinYesNo={a.name:a.value for a in spinYesNo}
drspinYesNo={a.value:a.name for a in spinYesNo}


class spinSlope(enum.IntEnum):
    Increasing      =_int32(0)
    Decreasing      =_int32(1)
    Varying         =_int32(2)
    Automatic       =_int32(3)
    _UndefinedESlope=_int32(4)
dspinSlope={a.name:a.value for a in spinSlope}
drspinSlope={a.value:a.name for a in spinSlope}


class spinXMLValidation(enum.IntEnum):
    xvLoad                  =_int32(0x00000001)
    xvCycles                =_int32(0x00000002)
    xvSFNC                  =_int32(0x00000004)
    xvDefault               =_int32(0x00000000)
    xvAll                   =_int32(0xffffffff)
    _UndefinedEXMLValidation=_int32(0x8000000)
dspinXMLValidation={a.name:a.value for a in spinXMLValidation}
drspinXMLValidation={a.value:a.name for a in spinXMLValidation}


class spinDisplayNotation(enum.IntEnum):
    fnAutomatic               =_int32(0)
    fnFixed                   =_int32(1)
    fnScientific              =_int32(2)
    _UndefinedEDisplayNotation=_int32(3)
dspinDisplayNotation={a.name:a.value for a in spinDisplayNotation}
drspinDisplayNotation={a.value:a.name for a in spinDisplayNotation}


class spinInterfaceType(enum.IntEnum):
    intfIValue      =_int32(0)
    intfIBase       =_int32(1)
    intfIInteger    =_int32(2)
    intfIBoolean    =_int32(3)
    intfICommand    =_int32(4)
    intfIFloat      =_int32(5)
    intfIString     =_int32(6)
    intfIRegister   =_int32(7)
    intfICategory   =_int32(8)
    intfIEnumeration=_int32(9)
    intfIEnumEntry  =_int32(10)
    intfIPort       =_int32(11)
dspinInterfaceType={a.name:a.value for a in spinInterfaceType}
drspinInterfaceType={a.value:a.name for a in spinInterfaceType}


class spinLinkType(enum.IntEnum):
    ctAllDependingNodes=_int32(0)
    ctAllTerminalNodes =_int32(1)
    ctInvalidators     =_int32(2)
    ctReadingChildren  =_int32(3)
    ctWritingChildren  =_int32(4)
    ctDependingChildren=_int32(5)
dspinLinkType={a.name:a.value for a in spinLinkType}
drspinLinkType={a.value:a.name for a in spinLinkType}


class spinIncMode(enum.IntEnum):
    noIncrement   =_int32(0)
    fixedIncrement=_int32(1)
    listIncrement =_int32(2)
dspinIncMode={a.name:a.value for a in spinIncMode}
drspinIncMode={a.value:a.name for a in spinIncMode}


class spinInputDirection(enum.IntEnum):
    idFrom=_int32(0)
    idTo  =_int32(1)
    idNone=_int32(2)
dspinInputDirection={a.name:a.value for a in spinInputDirection}
drspinInputDirection={a.value:a.name for a in spinInputDirection}


quickSpinStringNode=spinNodeHandle
quickSpinIntegerNode=spinNodeHandle
quickSpinFloatNode=spinNodeHandle
quickSpinBooleanNode=spinNodeHandle
quickSpinEnumerationNode=spinNodeHandle
quickSpinCommandNode=spinNodeHandle
quickSpinRegisterNode=spinNodeHandle
class quickSpin(ctypes.Structure):
    _fields_=[  ("LUTIndex",quickSpinIntegerNode),
                ("LUTEnable",quickSpinBooleanNode),
                ("LUTValue",quickSpinIntegerNode),
                ("LUTSelector",quickSpinEnumerationNode),
                ("ExposureTime",quickSpinFloatNode),
                ("AcquisitionStop",quickSpinCommandNode),
                ("AcquisitionResultingFrameRate",quickSpinFloatNode),
                ("AcquisitionLineRate",quickSpinFloatNode),
                ("AcquisitionStart",quickSpinCommandNode),
                ("TriggerSoftware",quickSpinCommandNode),
                ("ExposureMode",quickSpinEnumerationNode),
                ("AcquisitionMode",quickSpinEnumerationNode),
                ("AcquisitionFrameCount",quickSpinIntegerNode),
                ("TriggerSource",quickSpinEnumerationNode),
                ("TriggerActivation",quickSpinEnumerationNode),
                ("SensorShutterMode",quickSpinEnumerationNode),
                ("TriggerDelay",quickSpinFloatNode),
                ("TriggerMode",quickSpinEnumerationNode),
                ("AcquisitionFrameRate",quickSpinFloatNode),
                ("TriggerOverlap",quickSpinEnumerationNode),
                ("TriggerSelector",quickSpinEnumerationNode),
                ("AcquisitionFrameRateEnable",quickSpinBooleanNode),
                ("ExposureAuto",quickSpinEnumerationNode),
                ("AcquisitionBurstFrameCount",quickSpinIntegerNode),
                ("EventTest",quickSpinIntegerNode),
                ("EventTestTimestamp",quickSpinIntegerNode),
                ("EventExposureEndFrameID",quickSpinIntegerNode),
                ("EventExposureEnd",quickSpinIntegerNode),
                ("EventExposureEndTimestamp",quickSpinIntegerNode),
                ("EventError",quickSpinIntegerNode),
                ("EventErrorTimestamp",quickSpinIntegerNode),
                ("EventErrorCode",quickSpinIntegerNode),
                ("EventErrorFrameID",quickSpinIntegerNode),
                ("EventSelector",quickSpinEnumerationNode),
                ("EventSerialReceiveOverflow",quickSpinBooleanNode),
                ("EventSerialPortReceive",quickSpinIntegerNode),
                ("EventSerialPortReceiveTimestamp",quickSpinIntegerNode),
                ("EventSerialData",quickSpinStringNode),
                ("EventSerialDataLength",quickSpinIntegerNode),
                ("EventNotification",quickSpinEnumerationNode),
                ("LogicBlockLUTRowIndex",quickSpinIntegerNode),
                ("LogicBlockSelector",quickSpinEnumerationNode),
                ("LogicBlockLUTInputActivation",quickSpinEnumerationNode),
                ("LogicBlockLUTInputSelector",quickSpinEnumerationNode),
                ("LogicBlockLUTInputSource",quickSpinEnumerationNode),
                ("LogicBlockLUTOutputValue",quickSpinBooleanNode),
                ("LogicBlockLUTOutputValueAll",quickSpinIntegerNode),
                ("LogicBlockLUTSelector",quickSpinEnumerationNode),
                ("ColorTransformationValue",quickSpinFloatNode),
                ("ColorTransformationEnable",quickSpinBooleanNode),
                ("ColorTransformationSelector",quickSpinEnumerationNode),
                ("RgbTransformLightSource",quickSpinEnumerationNode),
                ("Saturation",quickSpinFloatNode),
                ("SaturationEnable",quickSpinBooleanNode),
                ("ColorTransformationValueSelector",quickSpinEnumerationNode),
                ("TimestampLatchValue",quickSpinIntegerNode),
                ("TimestampReset",quickSpinCommandNode),
                ("DeviceUserID",quickSpinStringNode),
                ("DeviceTemperature",quickSpinFloatNode),
                ("MaxDeviceResetTime",quickSpinIntegerNode),
                ("DeviceTLVersionMinor",quickSpinIntegerNode),
                ("DeviceSerialNumber",quickSpinStringNode),
                ("DeviceVendorName",quickSpinStringNode),
                ("DeviceRegistersEndianness",quickSpinEnumerationNode),
                ("DeviceManufacturerInfo",quickSpinStringNode),
                ("DeviceLinkSpeed",quickSpinIntegerNode),
                ("LinkUptime",quickSpinIntegerNode),
                ("DeviceEventChannelCount",quickSpinIntegerNode),
                ("TimestampLatch",quickSpinCommandNode),
                ("DeviceScanType",quickSpinEnumerationNode),
                ("DeviceReset",quickSpinCommandNode),
                ("DeviceCharacterSet",quickSpinEnumerationNode),
                ("DeviceLinkThroughputLimit",quickSpinIntegerNode),
                ("DeviceFirmwareVersion",quickSpinStringNode),
                ("DeviceStreamChannelCount",quickSpinIntegerNode),
                ("DeviceTLType",quickSpinEnumerationNode),
                ("DeviceVersion",quickSpinStringNode),
                ("DevicePowerSupplySelector",quickSpinEnumerationNode),
                ("SensorDescription",quickSpinStringNode),
                ("DeviceModelName",quickSpinStringNode),
                ("DeviceTLVersionMajor",quickSpinIntegerNode),
                ("DeviceTemperatureSelector",quickSpinEnumerationNode),
                ("EnumerationCount",quickSpinIntegerNode),
                ("PowerSupplyCurrent",quickSpinFloatNode),
                ("DeviceID",quickSpinStringNode),
                ("DeviceUptime",quickSpinIntegerNode),
                ("DeviceLinkCurrentThroughput",quickSpinIntegerNode),
                ("DeviceMaxThroughput",quickSpinIntegerNode),
                ("FactoryReset",quickSpinCommandNode),
                ("PowerSupplyVoltage",quickSpinFloatNode),
                ("DeviceIndicatorMode",quickSpinEnumerationNode),
                ("DeviceLinkBandwidthReserve",quickSpinFloatNode),
                ("AasRoiOffsetY",quickSpinIntegerNode),
                ("AasRoiOffsetX",quickSpinIntegerNode),
                ("AutoExposureControlPriority",quickSpinEnumerationNode),
                ("BalanceWhiteAutoLowerLimit",quickSpinFloatNode),
                ("BalanceWhiteAutoDamping",quickSpinFloatNode),
                ("AasRoiHeight",quickSpinIntegerNode),
                ("AutoExposureGreyValueUpperLimit",quickSpinFloatNode),
                ("AutoExposureTargetGreyValue",quickSpinFloatNode),
                ("AutoExposureGainLowerLimit",quickSpinFloatNode),
                ("AutoExposureGreyValueLowerLimit",quickSpinFloatNode),
                ("AutoExposureMeteringMode",quickSpinEnumerationNode),
                ("AutoExposureExposureTimeUpperLimit",quickSpinFloatNode),
                ("AutoExposureGainUpperLimit",quickSpinFloatNode),
                ("AutoExposureControlLoopDamping",quickSpinFloatNode),
                ("AutoExposureEVCompensation",quickSpinFloatNode),
                ("AutoExposureExposureTimeLowerLimit",quickSpinFloatNode),
                ("BalanceWhiteAutoProfile",quickSpinEnumerationNode),
                ("AutoAlgorithmSelector",quickSpinEnumerationNode),
                ("AutoExposureTargetGreyValueAuto",quickSpinEnumerationNode),
                ("AasRoiEnable",quickSpinBooleanNode),
                ("AutoExposureLightingMode",quickSpinEnumerationNode),
                ("AasRoiWidth",quickSpinIntegerNode),
                ("BalanceWhiteAutoUpperLimit",quickSpinFloatNode),
                ("LinkErrorCount",quickSpinIntegerNode),
                ("GevCurrentIPConfigurationDHCP",quickSpinBooleanNode),
                ("GevInterfaceSelector",quickSpinIntegerNode),
                ("GevSCPD",quickSpinIntegerNode),
                ("GevTimestampTickFrequency",quickSpinIntegerNode),
                ("GevSCPSPacketSize",quickSpinIntegerNode),
                ("GevCurrentDefaultGateway",quickSpinIntegerNode),
                ("GevSCCFGUnconditionalStreaming",quickSpinBooleanNode),
                ("GevMCTT",quickSpinIntegerNode),
                ("GevSCPSDoNotFragment",quickSpinBooleanNode),
                ("GevCurrentSubnetMask",quickSpinIntegerNode),
                ("GevStreamChannelSelector",quickSpinIntegerNode),
                ("GevCurrentIPAddress",quickSpinIntegerNode),
                ("GevMCSP",quickSpinIntegerNode),
                ("GevGVCPPendingTimeout",quickSpinIntegerNode),
                ("GevIEEE1588Status",quickSpinEnumerationNode),
                ("GevFirstURL",quickSpinStringNode),
                ("GevMACAddress",quickSpinIntegerNode),
                ("GevPersistentSubnetMask",quickSpinIntegerNode),
                ("GevMCPHostPort",quickSpinIntegerNode),
                ("GevSCPHostPort",quickSpinIntegerNode),
                ("GevGVCPPendingAck",quickSpinBooleanNode),
                ("GevSCPInterfaceIndex",quickSpinIntegerNode),
                ("GevSupportedOption",quickSpinBooleanNode),
                ("GevIEEE1588Mode",quickSpinEnumerationNode),
                ("GevCurrentIPConfigurationLLA",quickSpinBooleanNode),
                ("GevSCSP",quickSpinIntegerNode),
                ("GevIEEE1588",quickSpinBooleanNode),
                ("GevSCCFGExtendedChunkData",quickSpinBooleanNode),
                ("GevPersistentIPAddress",quickSpinIntegerNode),
                ("GevCurrentIPConfigurationPersistentIP",quickSpinBooleanNode),
                ("GevIEEE1588ClockAccuracy",quickSpinEnumerationNode),
                ("GevHeartbeatTimeout",quickSpinIntegerNode),
                ("GevPersistentDefaultGateway",quickSpinIntegerNode),
                ("GevCCP",quickSpinEnumerationNode),
                ("GevMCDA",quickSpinIntegerNode),
                ("GevSCDA",quickSpinIntegerNode),
                ("GevSCPDirection",quickSpinIntegerNode),
                ("GevSCPSFireTestPacket",quickSpinBooleanNode),
                ("GevSecondURL",quickSpinStringNode),
                ("GevSupportedOptionSelector",quickSpinEnumerationNode),
                ("GevGVCPHeartbeatDisable",quickSpinBooleanNode),
                ("GevMCRC",quickSpinIntegerNode),
                ("GevSCPSBigEndian",quickSpinBooleanNode),
                ("GevNumberOfInterfaces",quickSpinIntegerNode),
                ("TLParamsLocked",quickSpinIntegerNode),
                ("PayloadSize",quickSpinIntegerNode),
                ("PacketResendRequestCount",quickSpinIntegerNode),
                ("SharpeningEnable",quickSpinBooleanNode),
                ("BlackLevelSelector",quickSpinEnumerationNode),
                ("GammaEnable",quickSpinBooleanNode),
                ("SharpeningAuto",quickSpinBooleanNode),
                ("BlackLevelClampingEnable",quickSpinBooleanNode),
                ("BalanceRatio",quickSpinFloatNode),
                ("BalanceWhiteAuto",quickSpinEnumerationNode),
                ("SharpeningThreshold",quickSpinFloatNode),
                ("GainAuto",quickSpinEnumerationNode),
                ("Sharpening",quickSpinFloatNode),
                ("Gain",quickSpinFloatNode),
                ("BalanceRatioSelector",quickSpinEnumerationNode),
                ("GainSelector",quickSpinEnumerationNode),
                ("BlackLevel",quickSpinFloatNode),
                ("BlackLevelRaw",quickSpinIntegerNode),
                ("Gamma",quickSpinFloatNode),
                ("DefectTableIndex",quickSpinIntegerNode),
                ("DefectTableFactoryRestore",quickSpinCommandNode),
                ("DefectTableCoordinateY",quickSpinIntegerNode),
                ("DefectTableSave",quickSpinCommandNode),
                ("DefectCorrectionMode",quickSpinEnumerationNode),
                ("DefectTableCoordinateX",quickSpinIntegerNode),
                ("DefectTablePixelCount",quickSpinIntegerNode),
                ("DefectCorrectStaticEnable",quickSpinBooleanNode),
                ("DefectTableApply",quickSpinCommandNode),
                ("UserSetFeatureEnable",quickSpinBooleanNode),
                ("UserSetSave",quickSpinCommandNode),
                ("UserSetSelector",quickSpinEnumerationNode),
                ("UserSetLoad",quickSpinCommandNode),
                ("UserSetDefault",quickSpinEnumerationNode),
                ("SerialPortBaudRate",quickSpinEnumerationNode),
                ("SerialPortDataBits",quickSpinIntegerNode),
                ("SerialPortParity",quickSpinEnumerationNode),
                ("SerialTransmitQueueMaxCharacterCount",quickSpinIntegerNode),
                ("SerialReceiveQueueCurrentCharacterCount",quickSpinIntegerNode),
                ("SerialPortSelector",quickSpinEnumerationNode),
                ("SerialPortStopBits",quickSpinEnumerationNode),
                ("SerialReceiveQueueClear",quickSpinCommandNode),
                ("SerialReceiveFramingErrorCount",quickSpinIntegerNode),
                ("SerialTransmitQueueCurrentCharacterCount",quickSpinIntegerNode),
                ("SerialReceiveParityErrorCount",quickSpinIntegerNode),
                ("SerialPortSource",quickSpinEnumerationNode),
                ("SerialReceiveQueueMaxCharacterCount",quickSpinIntegerNode),
                ("SequencerSetStart",quickSpinIntegerNode),
                ("SequencerMode",quickSpinEnumerationNode),
                ("SequencerConfigurationValid",quickSpinEnumerationNode),
                ("SequencerSetValid",quickSpinEnumerationNode),
                ("SequencerSetSelector",quickSpinIntegerNode),
                ("SequencerTriggerActivation",quickSpinEnumerationNode),
                ("SequencerConfigurationMode",quickSpinEnumerationNode),
                ("SequencerSetSave",quickSpinCommandNode),
                ("SequencerTriggerSource",quickSpinEnumerationNode),
                ("SequencerSetActive",quickSpinIntegerNode),
                ("SequencerSetNext",quickSpinIntegerNode),
                ("SequencerSetLoad",quickSpinCommandNode),
                ("SequencerPathSelector",quickSpinIntegerNode),
                ("SequencerFeatureEnable",quickSpinBooleanNode),
                ("TransferBlockCount",quickSpinIntegerNode),
                ("TransferStart",quickSpinCommandNode),
                ("TransferQueueMaxBlockCount",quickSpinIntegerNode),
                ("TransferQueueCurrentBlockCount",quickSpinIntegerNode),
                ("TransferQueueMode",quickSpinEnumerationNode),
                ("TransferOperationMode",quickSpinEnumerationNode),
                ("TransferStop",quickSpinCommandNode),
                ("TransferQueueOverflowCount",quickSpinIntegerNode),
                ("TransferControlMode",quickSpinEnumerationNode),
                ("ChunkBlackLevel",quickSpinFloatNode),
                ("ChunkFrameID",quickSpinIntegerNode),
                ("ChunkSerialData",quickSpinStringNode),
                ("ChunkExposureTime",quickSpinFloatNode),
                ("ChunkCompressionMode",quickSpinIntegerNode),
                ("ChunkCompressionRatio",quickSpinFloatNode),
                ("ChunkSerialReceiveOverflow",quickSpinBooleanNode),
                ("ChunkTimestamp",quickSpinIntegerNode),
                ("ChunkModeActive",quickSpinBooleanNode),
                ("ChunkExposureEndLineStatusAll",quickSpinIntegerNode),
                ("ChunkGainSelector",quickSpinEnumerationNode),
                ("ChunkSelector",quickSpinEnumerationNode),
                ("ChunkBlackLevelSelector",quickSpinEnumerationNode),
                ("ChunkWidth",quickSpinIntegerNode),
                ("ChunkImage",quickSpinIntegerNode),
                ("ChunkHeight",quickSpinIntegerNode),
                ("ChunkPixelFormat",quickSpinEnumerationNode),
                ("ChunkGain",quickSpinFloatNode),
                ("ChunkSequencerSetActive",quickSpinIntegerNode),
                ("ChunkCRC",quickSpinIntegerNode),
                ("ChunkOffsetX",quickSpinIntegerNode),
                ("ChunkOffsetY",quickSpinIntegerNode),
                ("ChunkEnable",quickSpinBooleanNode),
                ("ChunkSerialDataLength",quickSpinIntegerNode),
                ("FileAccessOffset",quickSpinIntegerNode),
                ("FileAccessLength",quickSpinIntegerNode),
                ("FileOperationStatus",quickSpinEnumerationNode),
                ("FileOperationExecute",quickSpinCommandNode),
                ("FileOpenMode",quickSpinEnumerationNode),
                ("FileOperationResult",quickSpinIntegerNode),
                ("FileOperationSelector",quickSpinEnumerationNode),
                ("FileSelector",quickSpinEnumerationNode),
                ("FileSize",quickSpinIntegerNode),
                ("BinningSelector",quickSpinEnumerationNode),
                ("PixelDynamicRangeMin",quickSpinIntegerNode),
                ("PixelDynamicRangeMax",quickSpinIntegerNode),
                ("OffsetY",quickSpinIntegerNode),
                ("BinningHorizontal",quickSpinIntegerNode),
                ("Width",quickSpinIntegerNode),
                ("TestPatternGeneratorSelector",quickSpinEnumerationNode),
                ("CompressionRatio",quickSpinFloatNode),
                ("CompressionSaturationPriority",quickSpinEnumerationNode),
                ("ReverseX",quickSpinBooleanNode),
                ("ReverseY",quickSpinBooleanNode),
                ("TestPattern",quickSpinEnumerationNode),
                ("PixelColorFilter",quickSpinEnumerationNode),
                ("WidthMax",quickSpinIntegerNode),
                ("AdcBitDepth",quickSpinEnumerationNode),
                ("BinningVertical",quickSpinIntegerNode),
                ("DecimationHorizontalMode",quickSpinEnumerationNode),
                ("BinningVerticalMode",quickSpinEnumerationNode),
                ("OffsetX",quickSpinIntegerNode),
                ("HeightMax",quickSpinIntegerNode),
                ("DecimationHorizontal",quickSpinIntegerNode),
                ("PixelSize",quickSpinEnumerationNode),
                ("SensorHeight",quickSpinIntegerNode),
                ("DecimationSelector",quickSpinEnumerationNode),
                ("IspEnable",quickSpinBooleanNode),
                ("AdaptiveCompressionEnable",quickSpinBooleanNode),
                ("ImageCompressionMode",quickSpinEnumerationNode),
                ("DecimationVertical",quickSpinIntegerNode),
                ("Height",quickSpinIntegerNode),
                ("BinningHorizontalMode",quickSpinEnumerationNode),
                ("PixelFormat",quickSpinEnumerationNode),
                ("SensorWidth",quickSpinIntegerNode),
                ("DecimationVerticalMode",quickSpinEnumerationNode),
                ("TestEventGenerate",quickSpinCommandNode),
                ("TriggerEventTest",quickSpinCommandNode),
                ("GuiXmlManifestAddress",quickSpinIntegerNode),
                ("Test0001",quickSpinIntegerNode),
                ("V3_3Enable",quickSpinBooleanNode),
                ("LineMode",quickSpinEnumerationNode),
                ("LineSource",quickSpinEnumerationNode),
                ("LineInputFilterSelector",quickSpinEnumerationNode),
                ("UserOutputValue",quickSpinBooleanNode),
                ("UserOutputValueAll",quickSpinIntegerNode),
                ("UserOutputSelector",quickSpinEnumerationNode),
                ("LineStatus",quickSpinBooleanNode),
                ("LineFormat",quickSpinEnumerationNode),
                ("LineStatusAll",quickSpinIntegerNode),
                ("LineSelector",quickSpinEnumerationNode),
                ("ExposureActiveMode",quickSpinEnumerationNode),
                ("LineInverter",quickSpinBooleanNode),
                ("LineFilterWidth",quickSpinFloatNode),
                ("CounterTriggerActivation",quickSpinEnumerationNode),
                ("CounterValue",quickSpinIntegerNode),
                ("CounterSelector",quickSpinEnumerationNode),
                ("CounterValueAtReset",quickSpinIntegerNode),
                ("CounterStatus",quickSpinEnumerationNode),
                ("CounterTriggerSource",quickSpinEnumerationNode),
                ("CounterDelay",quickSpinIntegerNode),
                ("CounterResetSource",quickSpinEnumerationNode),
                ("CounterEventSource",quickSpinEnumerationNode),
                ("CounterEventActivation",quickSpinEnumerationNode),
                ("CounterDuration",quickSpinIntegerNode),
                ("CounterResetActivation",quickSpinEnumerationNode),
                ("DeviceType",quickSpinEnumerationNode),
                ("DeviceFamilyName",quickSpinStringNode),
                ("DeviceSFNCVersionMajor",quickSpinIntegerNode),
                ("DeviceSFNCVersionMinor",quickSpinIntegerNode),
                ("DeviceSFNCVersionSubMinor",quickSpinIntegerNode),
                ("DeviceManifestEntrySelector",quickSpinIntegerNode),
                ("DeviceManifestXMLMajorVersion",quickSpinIntegerNode),
                ("DeviceManifestXMLMinorVersion",quickSpinIntegerNode),
                ("DeviceManifestXMLSubMinorVersion",quickSpinIntegerNode),
                ("DeviceManifestSchemaMajorVersion",quickSpinIntegerNode),
                ("DeviceManifestSchemaMinorVersion",quickSpinIntegerNode),
                ("DeviceManifestPrimaryURL",quickSpinStringNode),
                ("DeviceManifestSecondaryURL",quickSpinStringNode),
                ("DeviceTLVersionSubMinor",quickSpinIntegerNode),
                ("DeviceGenCPVersionMajor",quickSpinIntegerNode),
                ("DeviceGenCPVersionMinor",quickSpinIntegerNode),
                ("DeviceConnectionSelector",quickSpinIntegerNode),
                ("DeviceConnectionSpeed",quickSpinIntegerNode),
                ("DeviceConnectionStatus",quickSpinEnumerationNode),
                ("DeviceLinkSelector",quickSpinIntegerNode),
                ("DeviceLinkThroughputLimitMode",quickSpinEnumerationNode),
                ("DeviceLinkConnectionCount",quickSpinIntegerNode),
                ("DeviceLinkHeartbeatMode",quickSpinEnumerationNode),
                ("DeviceLinkHeartbeatTimeout",quickSpinFloatNode),
                ("DeviceLinkCommandTimeout",quickSpinFloatNode),
                ("DeviceStreamChannelSelector",quickSpinIntegerNode),
                ("DeviceStreamChannelType",quickSpinEnumerationNode),
                ("DeviceStreamChannelLink",quickSpinIntegerNode),
                ("DeviceStreamChannelEndianness",quickSpinEnumerationNode),
                ("DeviceStreamChannelPacketSize",quickSpinIntegerNode),
                ("DeviceFeaturePersistenceStart",quickSpinCommandNode),
                ("DeviceFeaturePersistenceEnd",quickSpinCommandNode),
                ("DeviceRegistersStreamingStart",quickSpinCommandNode),
                ("DeviceRegistersStreamingEnd",quickSpinCommandNode),
                ("DeviceRegistersCheck",quickSpinCommandNode),
                ("DeviceRegistersValid",quickSpinBooleanNode),
                ("DeviceClockSelector",quickSpinEnumerationNode),
                ("DeviceClockFrequency",quickSpinFloatNode),
                ("DeviceSerialPortSelector",quickSpinEnumerationNode),
                ("DeviceSerialPortBaudRate",quickSpinEnumerationNode),
                ("Timestamp",quickSpinIntegerNode),
                ("SensorTaps",quickSpinEnumerationNode),
                ("SensorDigitizationTaps",quickSpinEnumerationNode),
                ("RegionSelector",quickSpinEnumerationNode),
                ("RegionMode",quickSpinEnumerationNode),
                ("RegionDestination",quickSpinEnumerationNode),
                ("ImageComponentSelector",quickSpinEnumerationNode),
                ("ImageComponentEnable",quickSpinBooleanNode),
                ("LinePitch",quickSpinIntegerNode),
                ("PixelFormatInfoSelector",quickSpinEnumerationNode),
                ("PixelFormatInfoID",quickSpinIntegerNode),
                ("Deinterlacing",quickSpinEnumerationNode),
                ("ImageCompressionRateOption",quickSpinEnumerationNode),
                ("ImageCompressionQuality",quickSpinIntegerNode),
                ("ImageCompressionBitrate",quickSpinFloatNode),
                ("ImageCompressionJPEGFormatOption",quickSpinEnumerationNode),
                ("AcquisitionAbort",quickSpinCommandNode),
                ("AcquisitionArm",quickSpinCommandNode),
                ("AcquisitionStatusSelector",quickSpinEnumerationNode),
                ("AcquisitionStatus",quickSpinBooleanNode),
                ("TriggerDivider",quickSpinIntegerNode),
                ("TriggerMultiplier",quickSpinIntegerNode),
                ("ExposureTimeMode",quickSpinEnumerationNode),
                ("ExposureTimeSelector",quickSpinEnumerationNode),
                ("GainAutoBalance",quickSpinEnumerationNode),
                ("BlackLevelAuto",quickSpinEnumerationNode),
                ("BlackLevelAutoBalance",quickSpinEnumerationNode),
                ("WhiteClipSelector",quickSpinEnumerationNode),
                ("WhiteClip",quickSpinFloatNode),
                ("LUTValueAll",quickSpinRegisterNode),
                ("UserOutputValueAllMask",quickSpinIntegerNode),
                ("CounterReset",quickSpinCommandNode),
                ("TimerSelector",quickSpinEnumerationNode),
                ("TimerDuration",quickSpinFloatNode),
                ("TimerDelay",quickSpinFloatNode),
                ("TimerReset",quickSpinCommandNode),
                ("TimerValue",quickSpinFloatNode),
                ("TimerStatus",quickSpinEnumerationNode),
                ("TimerTriggerSource",quickSpinEnumerationNode),
                ("TimerTriggerActivation",quickSpinEnumerationNode),
                ("EncoderSelector",quickSpinEnumerationNode),
                ("EncoderSourceA",quickSpinEnumerationNode),
                ("EncoderSourceB",quickSpinEnumerationNode),
                ("EncoderMode",quickSpinEnumerationNode),
                ("EncoderDivider",quickSpinIntegerNode),
                ("EncoderOutputMode",quickSpinEnumerationNode),
                ("EncoderStatus",quickSpinEnumerationNode),
                ("EncoderTimeout",quickSpinFloatNode),
                ("EncoderResetSource",quickSpinEnumerationNode),
                ("EncoderResetActivation",quickSpinEnumerationNode),
                ("EncoderReset",quickSpinCommandNode),
                ("EncoderValue",quickSpinIntegerNode),
                ("EncoderValueAtReset",quickSpinIntegerNode),
                ("SoftwareSignalSelector",quickSpinEnumerationNode),
                ("SoftwareSignalPulse",quickSpinCommandNode),
                ("ActionUnconditionalMode",quickSpinEnumerationNode),
                ("ActionDeviceKey",quickSpinIntegerNode),
                ("ActionQueueSize",quickSpinIntegerNode),
                ("ActionSelector",quickSpinIntegerNode),
                ("ActionGroupMask",quickSpinIntegerNode),
                ("ActionGroupKey",quickSpinIntegerNode),
                ("EventAcquisitionTrigger",quickSpinIntegerNode),
                ("EventAcquisitionTriggerTimestamp",quickSpinIntegerNode),
                ("EventAcquisitionTriggerFrameID",quickSpinIntegerNode),
                ("EventAcquisitionStart",quickSpinIntegerNode),
                ("EventAcquisitionStartTimestamp",quickSpinIntegerNode),
                ("EventAcquisitionStartFrameID",quickSpinIntegerNode),
                ("EventAcquisitionEnd",quickSpinIntegerNode),
                ("EventAcquisitionEndTimestamp",quickSpinIntegerNode),
                ("EventAcquisitionEndFrameID",quickSpinIntegerNode),
                ("EventAcquisitionTransferStart",quickSpinIntegerNode),
                ("EventAcquisitionTransferStartTimestamp",quickSpinIntegerNode),
                ("EventAcquisitionTransferStartFrameID",quickSpinIntegerNode),
                ("EventAcquisitionTransferEnd",quickSpinIntegerNode),
                ("EventAcquisitionTransferEndTimestamp",quickSpinIntegerNode),
                ("EventAcquisitionTransferEndFrameID",quickSpinIntegerNode),
                ("EventAcquisitionError",quickSpinIntegerNode),
                ("EventAcquisitionErrorTimestamp",quickSpinIntegerNode),
                ("EventAcquisitionErrorFrameID",quickSpinIntegerNode),
                ("EventFrameTrigger",quickSpinIntegerNode),
                ("EventFrameTriggerTimestamp",quickSpinIntegerNode),
                ("EventFrameTriggerFrameID",quickSpinIntegerNode),
                ("EventFrameStart",quickSpinIntegerNode),
                ("EventFrameStartTimestamp",quickSpinIntegerNode),
                ("EventFrameStartFrameID",quickSpinIntegerNode),
                ("EventFrameEnd",quickSpinIntegerNode),
                ("EventFrameEndTimestamp",quickSpinIntegerNode),
                ("EventFrameEndFrameID",quickSpinIntegerNode),
                ("EventFrameBurstStart",quickSpinIntegerNode),
                ("EventFrameBurstStartTimestamp",quickSpinIntegerNode),
                ("EventFrameBurstStartFrameID",quickSpinIntegerNode),
                ("EventFrameBurstEnd",quickSpinIntegerNode),
                ("EventFrameBurstEndTimestamp",quickSpinIntegerNode),
                ("EventFrameBurstEndFrameID",quickSpinIntegerNode),
                ("EventFrameTransferStart",quickSpinIntegerNode),
                ("EventFrameTransferStartTimestamp",quickSpinIntegerNode),
                ("EventFrameTransferStartFrameID",quickSpinIntegerNode),
                ("EventFrameTransferEnd",quickSpinIntegerNode),
                ("EventFrameTransferEndTimestamp",quickSpinIntegerNode),
                ("EventFrameTransferEndFrameID",quickSpinIntegerNode),
                ("EventExposureStart",quickSpinIntegerNode),
                ("EventExposureStartTimestamp",quickSpinIntegerNode),
                ("EventExposureStartFrameID",quickSpinIntegerNode),
                ("EventStream0TransferStart",quickSpinIntegerNode),
                ("EventStream0TransferStartTimestamp",quickSpinIntegerNode),
                ("EventStream0TransferStartFrameID",quickSpinIntegerNode),
                ("EventStream0TransferEnd",quickSpinIntegerNode),
                ("EventStream0TransferEndTimestamp",quickSpinIntegerNode),
                ("EventStream0TransferEndFrameID",quickSpinIntegerNode),
                ("EventStream0TransferPause",quickSpinIntegerNode),
                ("EventStream0TransferPauseTimestamp",quickSpinIntegerNode),
                ("EventStream0TransferPauseFrameID",quickSpinIntegerNode),
                ("EventStream0TransferResume",quickSpinIntegerNode),
                ("EventStream0TransferResumeTimestamp",quickSpinIntegerNode),
                ("EventStream0TransferResumeFrameID",quickSpinIntegerNode),
                ("EventStream0TransferBlockStart",quickSpinIntegerNode),
                ("EventStream0TransferBlockStartTimestamp",quickSpinIntegerNode),
                ("EventStream0TransferBlockStartFrameID",quickSpinIntegerNode),
                ("EventStream0TransferBlockEnd",quickSpinIntegerNode),
                ("EventStream0TransferBlockEndTimestamp",quickSpinIntegerNode),
                ("EventStream0TransferBlockEndFrameID",quickSpinIntegerNode),
                ("EventStream0TransferBlockTrigger",quickSpinIntegerNode),
                ("EventStream0TransferBlockTriggerTimestamp",quickSpinIntegerNode),
                ("EventStream0TransferBlockTriggerFrameID",quickSpinIntegerNode),
                ("EventStream0TransferBurstStart",quickSpinIntegerNode),
                ("EventStream0TransferBurstStartTimestamp",quickSpinIntegerNode),
                ("EventStream0TransferBurstStartFrameID",quickSpinIntegerNode),
                ("EventStream0TransferBurstEnd",quickSpinIntegerNode),
                ("EventStream0TransferBurstEndTimestamp",quickSpinIntegerNode),
                ("EventStream0TransferBurstEndFrameID",quickSpinIntegerNode),
                ("EventStream0TransferOverflow",quickSpinIntegerNode),
                ("EventStream0TransferOverflowTimestamp",quickSpinIntegerNode),
                ("EventStream0TransferOverflowFrameID",quickSpinIntegerNode),
                ("EventSequencerSetChange",quickSpinIntegerNode),
                ("EventSequencerSetChangeTimestamp",quickSpinIntegerNode),
                ("EventSequencerSetChangeFrameID",quickSpinIntegerNode),
                ("EventCounter0Start",quickSpinIntegerNode),
                ("EventCounter0StartTimestamp",quickSpinIntegerNode),
                ("EventCounter0StartFrameID",quickSpinIntegerNode),
                ("EventCounter1Start",quickSpinIntegerNode),
                ("EventCounter1StartTimestamp",quickSpinIntegerNode),
                ("EventCounter1StartFrameID",quickSpinIntegerNode),
                ("EventCounter0End",quickSpinIntegerNode),
                ("EventCounter0EndTimestamp",quickSpinIntegerNode),
                ("EventCounter0EndFrameID",quickSpinIntegerNode),
                ("EventCounter1End",quickSpinIntegerNode),
                ("EventCounter1EndTimestamp",quickSpinIntegerNode),
                ("EventCounter1EndFrameID",quickSpinIntegerNode),
                ("EventTimer0Start",quickSpinIntegerNode),
                ("EventTimer0StartTimestamp",quickSpinIntegerNode),
                ("EventTimer0StartFrameID",quickSpinIntegerNode),
                ("EventTimer1Start",quickSpinIntegerNode),
                ("EventTimer1StartTimestamp",quickSpinIntegerNode),
                ("EventTimer1StartFrameID",quickSpinIntegerNode),
                ("EventTimer0End",quickSpinIntegerNode),
                ("EventTimer0EndTimestamp",quickSpinIntegerNode),
                ("EventTimer0EndFrameID",quickSpinIntegerNode),
                ("EventTimer1End",quickSpinIntegerNode),
                ("EventTimer1EndTimestamp",quickSpinIntegerNode),
                ("EventTimer1EndFrameID",quickSpinIntegerNode),
                ("EventEncoder0Stopped",quickSpinIntegerNode),
                ("EventEncoder0StoppedTimestamp",quickSpinIntegerNode),
                ("EventEncoder0StoppedFrameID",quickSpinIntegerNode),
                ("EventEncoder1Stopped",quickSpinIntegerNode),
                ("EventEncoder1StoppedTimestamp",quickSpinIntegerNode),
                ("EventEncoder1StoppedFrameID",quickSpinIntegerNode),
                ("EventEncoder0Restarted",quickSpinIntegerNode),
                ("EventEncoder0RestartedTimestamp",quickSpinIntegerNode),
                ("EventEncoder0RestartedFrameID",quickSpinIntegerNode),
                ("EventEncoder1Restarted",quickSpinIntegerNode),
                ("EventEncoder1RestartedTimestamp",quickSpinIntegerNode),
                ("EventEncoder1RestartedFrameID",quickSpinIntegerNode),
                ("EventLine0RisingEdge",quickSpinIntegerNode),
                ("EventLine0RisingEdgeTimestamp",quickSpinIntegerNode),
                ("EventLine0RisingEdgeFrameID",quickSpinIntegerNode),
                ("EventLine1RisingEdge",quickSpinIntegerNode),
                ("EventLine1RisingEdgeTimestamp",quickSpinIntegerNode),
                ("EventLine1RisingEdgeFrameID",quickSpinIntegerNode),
                ("EventLine0FallingEdge",quickSpinIntegerNode),
                ("EventLine0FallingEdgeTimestamp",quickSpinIntegerNode),
                ("EventLine0FallingEdgeFrameID",quickSpinIntegerNode),
                ("EventLine1FallingEdge",quickSpinIntegerNode),
                ("EventLine1FallingEdgeTimestamp",quickSpinIntegerNode),
                ("EventLine1FallingEdgeFrameID",quickSpinIntegerNode),
                ("EventLine0AnyEdge",quickSpinIntegerNode),
                ("EventLine0AnyEdgeTimestamp",quickSpinIntegerNode),
                ("EventLine0AnyEdgeFrameID",quickSpinIntegerNode),
                ("EventLine1AnyEdge",quickSpinIntegerNode),
                ("EventLine1AnyEdgeTimestamp",quickSpinIntegerNode),
                ("EventLine1AnyEdgeFrameID",quickSpinIntegerNode),
                ("EventLinkTrigger0",quickSpinIntegerNode),
                ("EventLinkTrigger0Timestamp",quickSpinIntegerNode),
                ("EventLinkTrigger0FrameID",quickSpinIntegerNode),
                ("EventLinkTrigger1",quickSpinIntegerNode),
                ("EventLinkTrigger1Timestamp",quickSpinIntegerNode),
                ("EventLinkTrigger1FrameID",quickSpinIntegerNode),
                ("EventActionLate",quickSpinIntegerNode),
                ("EventActionLateTimestamp",quickSpinIntegerNode),
                ("EventActionLateFrameID",quickSpinIntegerNode),
                ("EventLinkSpeedChange",quickSpinIntegerNode),
                ("EventLinkSpeedChangeTimestamp",quickSpinIntegerNode),
                ("EventLinkSpeedChangeFrameID",quickSpinIntegerNode),
                ("FileAccessBuffer",quickSpinRegisterNode),
                ("SourceCount",quickSpinIntegerNode),
                ("SourceSelector",quickSpinEnumerationNode),
                ("TransferSelector",quickSpinEnumerationNode),
                ("TransferBurstCount",quickSpinIntegerNode),
                ("TransferAbort",quickSpinCommandNode),
                ("TransferPause",quickSpinCommandNode),
                ("TransferResume",quickSpinCommandNode),
                ("TransferTriggerSelector",quickSpinEnumerationNode),
                ("TransferTriggerMode",quickSpinEnumerationNode),
                ("TransferTriggerSource",quickSpinEnumerationNode),
                ("TransferTriggerActivation",quickSpinEnumerationNode),
                ("TransferStatusSelector",quickSpinEnumerationNode),
                ("TransferStatus",quickSpinBooleanNode),
                ("TransferComponentSelector",quickSpinEnumerationNode),
                ("TransferStreamChannel",quickSpinIntegerNode),
                ("Scan3dDistanceUnit",quickSpinEnumerationNode),
                ("Scan3dCoordinateSystem",quickSpinEnumerationNode),
                ("Scan3dOutputMode",quickSpinEnumerationNode),
                ("Scan3dCoordinateSystemReference",quickSpinEnumerationNode),
                ("Scan3dCoordinateSelector",quickSpinEnumerationNode),
                ("Scan3dCoordinateScale",quickSpinFloatNode),
                ("Scan3dCoordinateOffset",quickSpinFloatNode),
                ("Scan3dInvalidDataFlag",quickSpinBooleanNode),
                ("Scan3dInvalidDataValue",quickSpinFloatNode),
                ("Scan3dAxisMin",quickSpinFloatNode),
                ("Scan3dAxisMax",quickSpinFloatNode),
                ("Scan3dCoordinateTransformSelector",quickSpinEnumerationNode),
                ("Scan3dTransformValue",quickSpinFloatNode),
                ("Scan3dCoordinateReferenceSelector",quickSpinEnumerationNode),
                ("Scan3dCoordinateReferenceValue",quickSpinFloatNode),
                ("ChunkPartSelector",quickSpinIntegerNode),
                ("ChunkImageComponent",quickSpinEnumerationNode),
                ("ChunkPixelDynamicRangeMin",quickSpinIntegerNode),
                ("ChunkPixelDynamicRangeMax",quickSpinIntegerNode),
                ("ChunkTimestampLatchValue",quickSpinIntegerNode),
                ("ChunkLineStatusAll",quickSpinIntegerNode),
                ("ChunkCounterSelector",quickSpinEnumerationNode),
                ("ChunkCounterValue",quickSpinIntegerNode),
                ("ChunkTimerSelector",quickSpinEnumerationNode),
                ("ChunkTimerValue",quickSpinFloatNode),
                ("ChunkEncoderSelector",quickSpinEnumerationNode),
                ("ChunkScanLineSelector",quickSpinIntegerNode),
                ("ChunkEncoderValue",quickSpinIntegerNode),
                ("ChunkEncoderStatus",quickSpinEnumerationNode),
                ("ChunkExposureTimeSelector",quickSpinEnumerationNode),
                ("ChunkLinePitch",quickSpinIntegerNode),
                ("ChunkSourceID",quickSpinEnumerationNode),
                ("ChunkRegionID",quickSpinEnumerationNode),
                ("ChunkTransferBlockID",quickSpinIntegerNode),
                ("ChunkTransferStreamID",quickSpinEnumerationNode),
                ("ChunkTransferQueueCurrentBlockCount",quickSpinIntegerNode),
                ("ChunkStreamChannelID",quickSpinIntegerNode),
                ("ChunkScan3dDistanceUnit",quickSpinEnumerationNode),
                ("ChunkScan3dOutputMode",quickSpinEnumerationNode),
                ("ChunkScan3dCoordinateSystem",quickSpinEnumerationNode),
                ("ChunkScan3dCoordinateSystemReference",quickSpinEnumerationNode),
                ("ChunkScan3dCoordinateSelector",quickSpinEnumerationNode),
                ("ChunkScan3dCoordinateScale",quickSpinFloatNode),
                ("ChunkScan3dCoordinateOffset",quickSpinFloatNode),
                ("ChunkScan3dInvalidDataFlag",quickSpinBooleanNode),
                ("ChunkScan3dInvalidDataValue",quickSpinFloatNode),
                ("ChunkScan3dAxisMin",quickSpinFloatNode),
                ("ChunkScan3dAxisMax",quickSpinFloatNode),
                ("ChunkScan3dCoordinateTransformSelector",quickSpinEnumerationNode),
                ("ChunkScan3dTransformValue",quickSpinFloatNode),
                ("ChunkScan3dCoordinateReferenceSelector",quickSpinEnumerationNode),
                ("ChunkScan3dCoordinateReferenceValue",quickSpinFloatNode),
                ("TestPendingAck",quickSpinIntegerNode),
                ("DeviceTapGeometry",quickSpinEnumerationNode),
                ("GevPhysicalLinkConfiguration",quickSpinEnumerationNode),
                ("GevCurrentPhysicalLinkConfiguration",quickSpinEnumerationNode),
                ("GevActiveLinkCount",quickSpinIntegerNode),
                ("GevPAUSEFrameReception",quickSpinBooleanNode),
                ("GevPAUSEFrameTransmission",quickSpinBooleanNode),
                ("GevIPConfigurationStatus",quickSpinEnumerationNode),
                ("GevDiscoveryAckDelay",quickSpinIntegerNode),
                ("GevGVCPExtendedStatusCodesSelector",quickSpinEnumerationNode),
                ("GevGVCPExtendedStatusCodes",quickSpinBooleanNode),
                ("GevPrimaryApplicationSwitchoverKey",quickSpinIntegerNode),
                ("GevGVSPExtendedIDMode",quickSpinEnumerationNode),
                ("GevPrimaryApplicationSocket",quickSpinIntegerNode),
                ("GevPrimaryApplicationIPAddress",quickSpinIntegerNode),
                ("GevSCCFGPacketResendDestination",quickSpinBooleanNode),
                ("GevSCCFGAllInTransmission",quickSpinBooleanNode),
                ("GevSCZoneCount",quickSpinIntegerNode),
                ("GevSCZoneDirectionAll",quickSpinIntegerNode),
                ("GevSCZoneConfigurationLock",quickSpinBooleanNode),
                ("aPAUSEMACCtrlFramesTransmitted",quickSpinIntegerNode),
                ("aPAUSEMACCtrlFramesReceived",quickSpinIntegerNode),
                ("ClConfiguration",quickSpinEnumerationNode),
                ("ClTimeSlotsCount",quickSpinEnumerationNode),
                ("CxpLinkConfigurationStatus",quickSpinEnumerationNode),
                ("CxpLinkConfigurationPreferred",quickSpinEnumerationNode),
                ("CxpLinkConfiguration",quickSpinEnumerationNode),
                ("CxpConnectionSelector",quickSpinIntegerNode),
                ("CxpConnectionTestMode",quickSpinEnumerationNode),
                ("CxpConnectionTestErrorCount",quickSpinIntegerNode),
                ("CxpConnectionTestPacketCount",quickSpinIntegerNode),
                ("CxpPoCxpAuto",quickSpinCommandNode),
                ("CxpPoCxpTurnOff",quickSpinCommandNode),
                ("CxpPoCxpTripReset",quickSpinCommandNode),
                ("CxpPoCxpStatus",quickSpinEnumerationNode),
                ("ChunkInferenceFrameId",quickSpinIntegerNode),
                ("ChunkInferenceResult",quickSpinIntegerNode),
                ("ChunkInferenceConfidence",quickSpinFloatNode),
                ("ChunkInferenceBoundingBoxResult",quickSpinRegisterNode) ]
PquickSpin=ctypes.POINTER(quickSpin)
class CquickSpin(ctypes_wrap.CStructWrapper):
    _struct=quickSpin


class quickSpinTLSystem(ctypes.Structure):
    _fields_=[  ("TLID",quickSpinStringNode),
                ("TLVendorName",quickSpinStringNode),
                ("TLModelName",quickSpinStringNode),
                ("TLVersion",quickSpinStringNode),
                ("TLFileName",quickSpinStringNode),
                ("TLDisplayName",quickSpinStringNode),
                ("TLPath",quickSpinStringNode),
                ("TLType",quickSpinEnumerationNode),
                ("GenTLVersionMajor",quickSpinIntegerNode),
                ("GenTLVersionMinor",quickSpinIntegerNode),
                ("GenTLSFNCVersionMajor",quickSpinIntegerNode),
                ("GenTLSFNCVersionMinor",quickSpinIntegerNode),
                ("GenTLSFNCVersionSubMinor",quickSpinIntegerNode),
                ("GevVersionMajor",quickSpinIntegerNode),
                ("GevVersionMinor",quickSpinIntegerNode),
                ("InterfaceUpdateList",quickSpinCommandNode),
                ("InterfaceSelector",quickSpinIntegerNode),
                ("InterfaceID",quickSpinStringNode),
                ("InterfaceDisplayName",quickSpinStringNode),
                ("GevInterfaceMACAddress",quickSpinIntegerNode),
                ("GevInterfaceDefaultIPAddress",quickSpinIntegerNode),
                ("GevInterfaceDefaultSubnetMask",quickSpinIntegerNode),
                ("GevInterfaceDefaultGateway",quickSpinIntegerNode),
                ("EnumerateGEVInterfaces",quickSpinBooleanNode),
                ("EnumerateUSBInterfaces",quickSpinBooleanNode),
                ("EnumerateGen2Cameras",quickSpinBooleanNode),
                ("GevAutoAssignIPEnable",quickSpinBooleanNode) ]
PquickSpinTLSystem=ctypes.POINTER(quickSpinTLSystem)
class CquickSpinTLSystem(ctypes_wrap.CStructWrapper):
    _struct=quickSpinTLSystem


class quickSpinTLDevice(ctypes.Structure):
    _fields_=[  ("DeviceID",quickSpinStringNode),
                ("DeviceSerialNumber",quickSpinStringNode),
                ("DeviceUserID",quickSpinStringNode),
                ("DeviceVendorName",quickSpinStringNode),
                ("DeviceModelName",quickSpinStringNode),
                ("DeviceVersion",quickSpinStringNode),
                ("DeviceBootloaderVersion",quickSpinIntegerNode),
                ("DeviceType",quickSpinEnumerationNode),
                ("DeviceDisplayName",quickSpinStringNode),
                ("DeviceAccessStatus",quickSpinEnumerationNode),
                ("DeviceLinkSpeed",quickSpinIntegerNode),
                ("DeviceDriverVersion",quickSpinStringNode),
                ("DeviceIsUpdater",quickSpinBooleanNode),
                ("GenICamXMLLocation",quickSpinEnumerationNode),
                ("GenICamXMLPath",quickSpinStringNode),
                ("GUIXMLLocation",quickSpinEnumerationNode),
                ("GUIXMLPath",quickSpinStringNode),
                ("GevCCP",quickSpinEnumerationNode),
                ("GevDeviceMACAddress",quickSpinIntegerNode),
                ("GevDeviceIPAddress",quickSpinIntegerNode),
                ("GevDeviceSubnetMask",quickSpinIntegerNode),
                ("GevDeviceGateway",quickSpinIntegerNode),
                ("GevVersionMajor",quickSpinIntegerNode),
                ("GevVersionMinor",quickSpinIntegerNode),
                ("GevDeviceModeIsBigEndian",quickSpinBooleanNode),
                ("GevDeviceReadAndWriteTimeout",quickSpinIntegerNode),
                ("GevDeviceMaximumRetryCount",quickSpinIntegerNode),
                ("GevDevicePort",quickSpinIntegerNode),
                ("GevDeviceDiscoverMaximumPacketSize",quickSpinCommandNode),
                ("GevDeviceMaximumPacketSize",quickSpinIntegerNode),
                ("GevDeviceIsWrongSubnet",quickSpinBooleanNode),
                ("GevDeviceAutoForceIP",quickSpinCommandNode),
                ("GevDeviceForceIP",quickSpinCommandNode),
                ("GevDeviceForceIPAddress",quickSpinIntegerNode),
                ("GevDeviceForceSubnetMask",quickSpinIntegerNode),
                ("GevDeviceForceGateway",quickSpinIntegerNode),
                ("DeviceMulticastMonitorMode",quickSpinBooleanNode),
                ("DeviceEndianessMechanism",quickSpinEnumerationNode),
                ("DeviceReset",quickSpinCommandNode),
                ("DeviceInstanceId",quickSpinStringNode),
                ("DeviceLocation",quickSpinStringNode),
                ("DeviceCurrentSpeed",quickSpinEnumerationNode),
                ("DeviceU3VProtocol",quickSpinBooleanNode),
                ("DevicePortId",quickSpinStringNode) ]
PquickSpinTLDevice=ctypes.POINTER(quickSpinTLDevice)
class CquickSpinTLDevice(ctypes_wrap.CStructWrapper):
    _struct=quickSpinTLDevice


class quickSpinTLInterface(ctypes.Structure):
    _fields_=[  ("InterfaceID",quickSpinStringNode),
                ("InterfaceDisplayName",quickSpinStringNode),
                ("InterfaceType",quickSpinEnumerationNode),
                ("GevInterfaceGatewaySelector",quickSpinIntegerNode),
                ("GevInterfaceGateway",quickSpinIntegerNode),
                ("GevInterfaceMACAddress",quickSpinIntegerNode),
                ("GevInterfaceSubnetSelector",quickSpinIntegerNode),
                ("GevInterfaceSubnetIPAddress",quickSpinIntegerNode),
                ("GevInterfaceSubnetMask",quickSpinIntegerNode),
                ("GevInterfaceTransmitLinkSpeed",quickSpinIntegerNode),
                ("GevInterfaceReceiveLinkSpeed",quickSpinIntegerNode),
                ("GevInterfaceMTU",quickSpinIntegerNode),
                ("GevInterfaceIsIPConflict",quickSpinBooleanNode),
                ("POEStatus",quickSpinEnumerationNode),
                ("FLIRFilterDriverStatus",quickSpinEnumerationNode),
                ("TeledyneGigeVisionFilterDriverStatus",quickSpinEnumerationNode),
                ("GevActionDeviceKey",quickSpinIntegerNode),
                ("GevActionGroupKey",quickSpinIntegerNode),
                ("GevActionGroupMask",quickSpinIntegerNode),
                ("GevActionTime",quickSpinIntegerNode),
                ("GevActionAckRequired",quickSpinBooleanNode),
                ("ActionCommand",quickSpinCommandNode),
                ("DeviceUnlock",quickSpinStringNode),
                ("DeviceUpdateList",quickSpinCommandNode),
                ("DeviceCount",quickSpinIntegerNode),
                ("DeviceSelector",quickSpinIntegerNode),
                ("DeviceID",quickSpinStringNode),
                ("DeviceVendorName",quickSpinStringNode),
                ("DeviceModelName",quickSpinStringNode),
                ("DeviceSerialNumber",quickSpinStringNode),
                ("DeviceAccessStatus",quickSpinEnumerationNode),
                ("GevDeviceIPAddress",quickSpinIntegerNode),
                ("GevDeviceSubnetMask",quickSpinIntegerNode),
                ("GevDeviceGateway",quickSpinIntegerNode),
                ("GevDeviceMACAddress",quickSpinIntegerNode),
                ("IncompatibleDeviceCount",quickSpinIntegerNode),
                ("IncompatibleDeviceSelector",quickSpinIntegerNode),
                ("IncompatibleDeviceID",quickSpinStringNode),
                ("IncompatibleDeviceVendorName",quickSpinStringNode),
                ("IncompatibleDeviceModelName",quickSpinStringNode),
                ("IncompatibleGevDeviceIPAddress",quickSpinIntegerNode),
                ("IncompatibleGevDeviceSubnetMask",quickSpinIntegerNode),
                ("IncompatibleGevDeviceMACAddress",quickSpinIntegerNode),
                ("GevDeviceForceIP",quickSpinCommandNode),
                ("GevDeviceForceIPAddress",quickSpinIntegerNode),
                ("GevDeviceForceSubnetMask",quickSpinIntegerNode),
                ("GevDeviceForceGateway",quickSpinIntegerNode),
                ("GevDeviceAutoForceIP",quickSpinCommandNode),
                ("GevDeviceDiscoveryEnabled",quickSpinBooleanNode),
                ("GevDeviceEnableDiscovery",quickSpinCommandNode),
                ("GevDeviceDisableDiscovery",quickSpinCommandNode),
                ("HostAdapterName",quickSpinStringNode),
                ("HostAdapterVendor",quickSpinStringNode),
                ("HostAdapterDriverVersion",quickSpinStringNode) ]
PquickSpinTLInterface=ctypes.POINTER(quickSpinTLInterface)
class CquickSpinTLInterface(ctypes_wrap.CStructWrapper):
    _struct=quickSpinTLInterface


class quickSpinTLStream(ctypes.Structure):
    _fields_=[  ("StreamID",quickSpinStringNode),
                ("StreamType",quickSpinEnumerationNode),
                ("StreamMode",quickSpinEnumerationNode),
                ("StreamBufferCountManual",quickSpinIntegerNode),
                ("StreamBufferCountResult",quickSpinIntegerNode),
                ("StreamBufferCountMax",quickSpinIntegerNode),
                ("StreamBufferCountMode",quickSpinEnumerationNode),
                ("StreamBufferHandlingMode",quickSpinEnumerationNode),
                ("StreamAnnounceBufferMinimum",quickSpinIntegerNode),
                ("StreamAnnouncedBufferCount",quickSpinIntegerNode),
                ("StreamStartedFrameCount",quickSpinIntegerNode),
                ("StreamDeliveredFrameCount",quickSpinIntegerNode),
                ("StreamReceivedFrameCount",quickSpinIntegerNode),
                ("StreamIncompleteFrameCount",quickSpinIntegerNode),
                ("StreamLostFrameCount",quickSpinIntegerNode),
                ("StreamDroppedFrameCount",quickSpinIntegerNode),
                ("StreamInputBufferCount",quickSpinIntegerNode),
                ("StreamOutputBufferCount",quickSpinIntegerNode),
                ("StreamIsGrabbing",quickSpinBooleanNode),
                ("StreamChunkCountMaximum",quickSpinIntegerNode),
                ("StreamBufferAlignment",quickSpinIntegerNode),
                ("StreamCRCCheckEnable",quickSpinBooleanNode),
                ("StreamReceivedPacketCount",quickSpinIntegerNode),
                ("StreamMissedPacketCount",quickSpinIntegerNode),
                ("StreamPacketResendEnable",quickSpinBooleanNode),
                ("StreamPacketResendTimeout",quickSpinIntegerNode),
                ("StreamPacketResendMaxRequests",quickSpinIntegerNode),
                ("StreamPacketResendRequestCount",quickSpinIntegerNode),
                ("StreamPacketResendRequestTimeoutCount",quickSpinIntegerNode),
                ("StreamPacketResendRequestedPacketCount",quickSpinIntegerNode),
                ("StreamPacketResendReceivedPacketCount",quickSpinIntegerNode),
                ("StreamPacketsDuplicatedCount",quickSpinIntegerNode),
                ("StreamPacketsTimeoutCount",quickSpinIntegerNode),
                ("StreamPacketsNotYetAvailableCount",quickSpinIntegerNode),
                ("StreamPacketsTemporarilyUnavailableCount",quickSpinIntegerNode),
                ("StreamPacketsPerFrameCount",quickSpinIntegerNode),
                ("StreamPacketsUnavailableCount",quickSpinIntegerNode),
                ("StreamBlocksReceptionTimeLast",quickSpinIntegerNode),
                ("StreamBlocksReceptionTimeMin",quickSpinIntegerNode),
                ("StreamBlocksReceptionTimeMax",quickSpinIntegerNode),
                ("StreamBlocksProcessingTimeLast",quickSpinIntegerNode),
                ("StreamBlocksProcessingTimeMin",quickSpinIntegerNode),
                ("StreamBlocksProcessingTimeMax",quickSpinIntegerNode),
                ("StreamBlockTransferSize",quickSpinIntegerNode) ]
PquickSpinTLStream=ctypes.POINTER(quickSpinTLStream)
class CquickSpinTLStream(ctypes_wrap.CStructWrapper):
    _struct=quickSpinTLStream


class spinTLStreamTypeEnums(enum.IntEnum):
    StreamType_GigEVision  =_int32(0)
    StreamType_CameraLink  =_int32(1)
    StreamType_CameraLinkHS=_int32(2)
    StreamType_CoaXPress   =_int32(3)
    StreamType_USB3Vision  =_int32(4)
    StreamType_Custom      =_int32(5)
    NUMSTREAMTYPE          =_int32(6)
dspinTLStreamTypeEnums={a.name:a.value for a in spinTLStreamTypeEnums}
drspinTLStreamTypeEnums={a.value:a.name for a in spinTLStreamTypeEnums}


class spinTLStreamModeEnums(enum.IntEnum):
    StreamMode_Socket            =_int32(0)
    StreamMode_LWF               =_int32(1)
    StreamMode_TeledyneGigeVision=_int32(2)
    NUMSTREAMMODE                =_int32(3)
dspinTLStreamModeEnums={a.name:a.value for a in spinTLStreamModeEnums}
drspinTLStreamModeEnums={a.value:a.name for a in spinTLStreamModeEnums}


class spinTLStreamBufferCountModeEnums(enum.IntEnum):
    StreamBufferCountMode_Manual=_int32(0)
    NUMSTREAMBUFFERCOUNTMODE    =_int32(1)
dspinTLStreamBufferCountModeEnums={a.name:a.value for a in spinTLStreamBufferCountModeEnums}
drspinTLStreamBufferCountModeEnums={a.value:a.name for a in spinTLStreamBufferCountModeEnums}


class spinTLStreamBufferHandlingModeEnums(enum.IntEnum):
    StreamBufferHandlingMode_OldestFirst         =_int32(0)
    StreamBufferHandlingMode_OldestFirstOverwrite=_int32(1)
    StreamBufferHandlingMode_NewestOnly          =_int32(2)
    StreamBufferHandlingMode_NewestFirst         =_int32(3)
    NUMSTREAMBUFFERHANDLINGMODE                  =_int32(4)
dspinTLStreamBufferHandlingModeEnums={a.name:a.value for a in spinTLStreamBufferHandlingModeEnums}
drspinTLStreamBufferHandlingModeEnums={a.value:a.name for a in spinTLStreamBufferHandlingModeEnums}


class spinTLDeviceTypeEnums(enum.IntEnum):
    DeviceType_GigEVision  =_int32(0)
    DeviceType_CameraLink  =_int32(1)
    DeviceType_CameraLinkHS=_int32(2)
    DeviceType_CoaXPress   =_int32(3)
    DeviceType_USB3Vision  =_int32(4)
    DeviceType_Custom      =_int32(5)
    NUMDEVICETYPE          =_int32(6)
dspinTLDeviceTypeEnums={a.name:a.value for a in spinTLDeviceTypeEnums}
drspinTLDeviceTypeEnums={a.value:a.name for a in spinTLDeviceTypeEnums}


class spinTLDeviceAccessStatusEnums(enum.IntEnum):
    DeviceAccessStatus_Unknown      =_int32(0)
    DeviceAccessStatus_ReadWrite    =_int32(1)
    DeviceAccessStatus_ReadOnly     =_int32(2)
    DeviceAccessStatus_NoAccess     =_int32(3)
    DeviceAccessStatus_Busy         =_int32(4)
    DeviceAccessStatus_OpenReadWrite=_int32(5)
    DeviceAccessStatus_OpenReadOnly =_int32(6)
    NUMDEVICEACCESSSTATUS           =_int32(7)
dspinTLDeviceAccessStatusEnums={a.name:a.value for a in spinTLDeviceAccessStatusEnums}
drspinTLDeviceAccessStatusEnums={a.value:a.name for a in spinTLDeviceAccessStatusEnums}


class spinTLGenICamXMLLocationEnums(enum.IntEnum):
    GenICamXMLLocation_Device=_int32(0)
    GenICamXMLLocation_Host  =_int32(1)
    NUMGENICAMXMLLOCATION    =_int32(2)
dspinTLGenICamXMLLocationEnums={a.name:a.value for a in spinTLGenICamXMLLocationEnums}
drspinTLGenICamXMLLocationEnums={a.value:a.name for a in spinTLGenICamXMLLocationEnums}


class spinTLGUIXMLLocationEnums(enum.IntEnum):
    GUIXMLLocation_Device=_int32(0)
    GUIXMLLocation_Host  =_int32(1)
    NUMGUIXMLLOCATION    =_int32(2)
dspinTLGUIXMLLocationEnums={a.name:a.value for a in spinTLGUIXMLLocationEnums}
drspinTLGUIXMLLocationEnums={a.value:a.name for a in spinTLGUIXMLLocationEnums}


class spinTLGevCCPEnums(enum.IntEnum):
    GevCCP_EnumEntry_GevCCP_OpenAccess     =_int32(0)
    GevCCP_EnumEntry_GevCCP_ExclusiveAccess=_int32(1)
    GevCCP_EnumEntry_GevCCP_ControlAccess  =_int32(2)
    NUMGEVCCP                              =_int32(3)
dspinTLGevCCPEnums={a.name:a.value for a in spinTLGevCCPEnums}
drspinTLGevCCPEnums={a.value:a.name for a in spinTLGevCCPEnums}


class spinTLDeviceEndianessMechanismEnums(enum.IntEnum):
    DeviceEndianessMechanism_Legacy  =_int32(0)
    DeviceEndianessMechanism_Standard=_int32(1)
    NUMDEVICEENDIANESSMECHANISM      =_int32(2)
dspinTLDeviceEndianessMechanismEnums={a.name:a.value for a in spinTLDeviceEndianessMechanismEnums}
drspinTLDeviceEndianessMechanismEnums={a.value:a.name for a in spinTLDeviceEndianessMechanismEnums}


class spinTLDeviceCurrentSpeedEnums(enum.IntEnum):
    DeviceCurrentSpeed_UnknownSpeed=_int32(0)
    DeviceCurrentSpeed_LowSpeed    =_int32(1)
    DeviceCurrentSpeed_FullSpeed   =_int32(2)
    DeviceCurrentSpeed_HighSpeed   =_int32(3)
    DeviceCurrentSpeed_SuperSpeed  =_int32(4)
    NUMDEVICECURRENTSPEED          =_int32(5)
dspinTLDeviceCurrentSpeedEnums={a.name:a.value for a in spinTLDeviceCurrentSpeedEnums}
drspinTLDeviceCurrentSpeedEnums={a.value:a.name for a in spinTLDeviceCurrentSpeedEnums}


class spinTLInterfaceTypeEnums(enum.IntEnum):
    InterfaceType_GigEVision  =_int32(0)
    InterfaceType_CameraLink  =_int32(1)
    InterfaceType_CameraLinkHS=_int32(2)
    InterfaceType_CoaXPress   =_int32(3)
    InterfaceType_USB3Vision  =_int32(4)
    InterfaceType_Custom      =_int32(5)
    NUMINTERFACETYPE          =_int32(6)
dspinTLInterfaceTypeEnums={a.name:a.value for a in spinTLInterfaceTypeEnums}
drspinTLInterfaceTypeEnums={a.value:a.name for a in spinTLInterfaceTypeEnums}


class spinTLPOEStatusEnums(enum.IntEnum):
    POEStatus_NotSupported=_int32(0)
    POEStatus_PowerOff    =_int32(1)
    POEStatus_PowerOn     =_int32(2)
    NUMPOESTATUS          =_int32(3)
dspinTLPOEStatusEnums={a.name:a.value for a in spinTLPOEStatusEnums}
drspinTLPOEStatusEnums={a.value:a.name for a in spinTLPOEStatusEnums}


class spinTLFLIRFilterDriverStatusEnums(enum.IntEnum):
    FLIRFilterDriverStatus_NotSupported=_int32(0)
    FLIRFilterDriverStatus_Disabled    =_int32(1)
    FLIRFilterDriverStatus_Enabled     =_int32(2)
    NUMFLIRFILTERDRIVERSTATUS          =_int32(3)
dspinTLFLIRFilterDriverStatusEnums={a.name:a.value for a in spinTLFLIRFilterDriverStatusEnums}
drspinTLFLIRFilterDriverStatusEnums={a.value:a.name for a in spinTLFLIRFilterDriverStatusEnums}


class spinTLTeledyneGigeVisionFilterDriverStatusEnums(enum.IntEnum):
    TeledyneGigeVisionFilterDriverStatus_NotSupported=_int32(0)
    TeledyneGigeVisionFilterDriverStatus_Disabled    =_int32(1)
    TeledyneGigeVisionFilterDriverStatus_Enabled     =_int32(2)
    NUMTELEDYNEGIGEVISIONFILTERDRIVERSTATUS          =_int32(3)
dspinTLTeledyneGigeVisionFilterDriverStatusEnums={a.name:a.value for a in spinTLTeledyneGigeVisionFilterDriverStatusEnums}
drspinTLTeledyneGigeVisionFilterDriverStatusEnums={a.value:a.name for a in spinTLTeledyneGigeVisionFilterDriverStatusEnums}


class spinTLTLTypeEnums(enum.IntEnum):
    TLType_GigEVision  =_int32(0)
    TLType_CameraLink  =_int32(1)
    TLType_CameraLinkHS=_int32(2)
    TLType_CoaXPress   =_int32(3)
    TLType_USB3Vision  =_int32(4)
    TLType_Mixed       =_int32(5)
    TLType_Custom      =_int32(6)
    NUMTLTYPE          =_int32(7)
dspinTLTLTypeEnums={a.name:a.value for a in spinTLTLTypeEnums}
drspinTLTLTypeEnums={a.value:a.name for a in spinTLTLTypeEnums}





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
    #  ctypes.c_int spinNodeMapGetNode(spinNodeMapHandle hNodeMap, ctypes.c_char_p pName, ctypes.POINTER(spinNodeHandle) phNode)
    addfunc(lib, "spinNodeMapGetNode", restype = ctypes.c_int,
            argtypes = [spinNodeMapHandle, ctypes.c_char_p, ctypes.POINTER(spinNodeHandle)],
            argnames = ["hNodeMap", "pName", "phNode"] )
    #  ctypes.c_int spinNodeMapGetNumNodes(spinNodeMapHandle hNodeMap, ctypes.POINTER(ctypes.c_size_t) pValue)
    addfunc(lib, "spinNodeMapGetNumNodes", restype = ctypes.c_int,
            argtypes = [spinNodeMapHandle, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hNodeMap", "pValue"] )
    #  ctypes.c_int spinNodeMapGetNodeByIndex(spinNodeMapHandle hNodeMap, ctypes.c_size_t index, ctypes.POINTER(spinNodeHandle) phNode)
    addfunc(lib, "spinNodeMapGetNodeByIndex", restype = ctypes.c_int,
            argtypes = [spinNodeMapHandle, ctypes.c_size_t, ctypes.POINTER(spinNodeHandle)],
            argnames = ["hNodeMap", "index", "phNode"] )
    #  ctypes.c_int spinNodeMapReleaseNode(spinNodeMapHandle hNodeMap, spinNodeHandle hNode)
    addfunc(lib, "spinNodeMapReleaseNode", restype = ctypes.c_int,
            argtypes = [spinNodeMapHandle, spinNodeHandle],
            argnames = ["hNodeMap", "hNode"] )
    #  ctypes.c_int spinNodeMapPoll(spinNodeMapHandle hNodeMap, ctypes.c_int64 timestamp)
    addfunc(lib, "spinNodeMapPoll", restype = ctypes.c_int,
            argtypes = [spinNodeMapHandle, ctypes.c_int64],
            argnames = ["hNodeMap", "timestamp"] )
    #  ctypes.c_int spinNodeIsImplemented(spinNodeHandle hNode, ctypes.POINTER(bool8_t) pbResult)
    addfunc(lib, "spinNodeIsImplemented", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(bool8_t)],
            argnames = ["hNode", "pbResult"] )
    #  ctypes.c_int spinNodeIsReadable(spinNodeHandle hNode, ctypes.POINTER(bool8_t) pbResult)
    addfunc(lib, "spinNodeIsReadable", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(bool8_t)],
            argnames = ["hNode", "pbResult"] )
    #  ctypes.c_int spinNodeIsWritable(spinNodeHandle hNode, ctypes.POINTER(bool8_t) pbResult)
    addfunc(lib, "spinNodeIsWritable", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(bool8_t)],
            argnames = ["hNode", "pbResult"] )
    #  ctypes.c_int spinNodeIsAvailable(spinNodeHandle hNode, ctypes.POINTER(bool8_t) pbResult)
    addfunc(lib, "spinNodeIsAvailable", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(bool8_t)],
            argnames = ["hNode", "pbResult"] )
    #  ctypes.c_int spinNodeIsEqual(spinNodeHandle hNodeFirst, spinNodeHandle hNodeSecond, ctypes.POINTER(bool8_t) pbResult)
    addfunc(lib, "spinNodeIsEqual", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, spinNodeHandle, ctypes.POINTER(bool8_t)],
            argnames = ["hNodeFirst", "hNodeSecond", "pbResult"] )
    #  ctypes.c_int spinNodeGetAccessMode(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int) pAccessMode)
    addfunc(lib, "spinNodeGetAccessMode", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hNode", "pAccessMode"] )
    #  ctypes.c_int spinNodeGetName(spinNodeHandle hNode, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinNodeGetName", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hNode", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinNodeGetNameSpace(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int) pNamespace)
    addfunc(lib, "spinNodeGetNameSpace", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hNode", "pNamespace"] )
    #  ctypes.c_int spinNodeGetVisibility(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int) pVisibility)
    addfunc(lib, "spinNodeGetVisibility", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hNode", "pVisibility"] )
    #  ctypes.c_int spinNodeInvalidateNode(spinNodeHandle hNode)
    addfunc(lib, "spinNodeInvalidateNode", restype = ctypes.c_int,
            argtypes = [spinNodeHandle],
            argnames = ["hNode"] )
    #  ctypes.c_int spinNodeGetCachingMode(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int) pCachingMode)
    addfunc(lib, "spinNodeGetCachingMode", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hNode", "pCachingMode"] )
    #  ctypes.c_int spinNodeGetToolTip(spinNodeHandle hNode, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinNodeGetToolTip", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hNode", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinNodeGetDescription(spinNodeHandle hNode, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinNodeGetDescription", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hNode", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinNodeGetDisplayName(spinNodeHandle hNode, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinNodeGetDisplayName", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hNode", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinNodeGetType(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int) pType)
    addfunc(lib, "spinNodeGetType", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hNode", "pType"] )
    #  ctypes.c_int spinNodeGetPollingTime(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int64) pPollingTime)
    addfunc(lib, "spinNodeGetPollingTime", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["hNode", "pPollingTime"] )
    #  ctypes.c_int spinNodeRegisterCallback(spinNodeHandle hNode, spinNodeCallbackFunction pCbFunction, ctypes.POINTER(spinNodeCallbackHandle) phCb)
    addfunc(lib, "spinNodeRegisterCallback", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, spinNodeCallbackFunction, ctypes.POINTER(spinNodeCallbackHandle)],
            argnames = ["hNode", "pCbFunction", "phCb"] )
    #  ctypes.c_int spinNodeDeregisterCallback(spinNodeHandle hNode, spinNodeCallbackHandle hCb)
    addfunc(lib, "spinNodeDeregisterCallback", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, spinNodeCallbackHandle],
            argnames = ["hNode", "hCb"] )
    #  ctypes.c_int spinNodeGetImposedAccessMode(spinNodeHandle hNode, ctypes.c_int imposedAccessMode)
    addfunc(lib, "spinNodeGetImposedAccessMode", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_int],
            argnames = ["hNode", "imposedAccessMode"] )
    #  ctypes.c_int spinNodeGetImposedVisibility(spinNodeHandle hNode, ctypes.c_int imposedVisibility)
    addfunc(lib, "spinNodeGetImposedVisibility", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_int],
            argnames = ["hNode", "imposedVisibility"] )
    #  ctypes.c_int spinNodeToString(spinNodeHandle hNode, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinNodeToString", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hNode", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinNodeToStringEx(spinNodeHandle hNode, bool8_t bVerify, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinNodeToStringEx", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, bool8_t, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hNode", "bVerify", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinNodeFromString(spinNodeHandle hNode, ctypes.c_char_p pBuf)
    addfunc(lib, "spinNodeFromString", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_char_p],
            argnames = ["hNode", "pBuf"] )
    #  ctypes.c_int spinNodeFromStringEx(spinNodeHandle hNode, bool8_t bVerify, ctypes.c_char_p pBuf)
    addfunc(lib, "spinNodeFromStringEx", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, bool8_t, ctypes.c_char_p],
            argnames = ["hNode", "bVerify", "pBuf"] )
    #  ctypes.c_int spinStringSetValue(spinNodeHandle hNode, ctypes.c_char_p pBuf)
    addfunc(lib, "spinStringSetValue", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_char_p],
            argnames = ["hNode", "pBuf"] )
    #  ctypes.c_int spinStringSetValueEx(spinNodeHandle hNode, bool8_t bVerify, ctypes.c_char_p pBuf)
    addfunc(lib, "spinStringSetValueEx", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, bool8_t, ctypes.c_char_p],
            argnames = ["hNode", "bVerify", "pBuf"] )
    #  ctypes.c_int spinStringGetValue(spinNodeHandle hNode, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinStringGetValue", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hNode", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinStringGetValueEx(spinNodeHandle hNode, bool8_t bVerify, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinStringGetValueEx", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, bool8_t, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hNode", "bVerify", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinStringGetMaxLength(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int64) pValue)
    addfunc(lib, "spinStringGetMaxLength", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["hNode", "pValue"] )
    #  ctypes.c_int spinIntegerSetValue(spinNodeHandle hNode, ctypes.c_int64 value)
    addfunc(lib, "spinIntegerSetValue", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_int64],
            argnames = ["hNode", "value"] )
    #  ctypes.c_int spinIntegerSetValueEx(spinNodeHandle hNode, bool8_t bVerify, ctypes.c_int64 value)
    addfunc(lib, "spinIntegerSetValueEx", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, bool8_t, ctypes.c_int64],
            argnames = ["hNode", "bVerify", "value"] )
    #  ctypes.c_int spinIntegerGetValue(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int64) pValue)
    addfunc(lib, "spinIntegerGetValue", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["hNode", "pValue"] )
    #  ctypes.c_int spinIntegerGetValueEx(spinNodeHandle hNode, bool8_t bVerify, ctypes.POINTER(ctypes.c_int64) pValue)
    addfunc(lib, "spinIntegerGetValueEx", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, bool8_t, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["hNode", "bVerify", "pValue"] )
    #  ctypes.c_int spinIntegerGetMin(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int64) pValue)
    addfunc(lib, "spinIntegerGetMin", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["hNode", "pValue"] )
    #  ctypes.c_int spinIntegerGetMax(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int64) pValue)
    addfunc(lib, "spinIntegerGetMax", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["hNode", "pValue"] )
    #  ctypes.c_int spinIntegerGetInc(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int64) pValue)
    addfunc(lib, "spinIntegerGetInc", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["hNode", "pValue"] )
    #  ctypes.c_int spinIntegerGetRepresentation(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int) pValue)
    addfunc(lib, "spinIntegerGetRepresentation", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hNode", "pValue"] )
    #  ctypes.c_int spinFloatSetValue(spinNodeHandle hNode, ctypes.c_double value)
    addfunc(lib, "spinFloatSetValue", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_double],
            argnames = ["hNode", "value"] )
    #  ctypes.c_int spinFloatSetValueEx(spinNodeHandle hNode, bool8_t bVerify, ctypes.c_double value)
    addfunc(lib, "spinFloatSetValueEx", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, bool8_t, ctypes.c_double],
            argnames = ["hNode", "bVerify", "value"] )
    #  ctypes.c_int spinFloatGetValue(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_double) pValue)
    addfunc(lib, "spinFloatGetValue", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_double)],
            argnames = ["hNode", "pValue"] )
    #  ctypes.c_int spinFloatGetValueEx(spinNodeHandle hNode, bool8_t bVerify, ctypes.POINTER(ctypes.c_double) pValue)
    addfunc(lib, "spinFloatGetValueEx", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, bool8_t, ctypes.POINTER(ctypes.c_double)],
            argnames = ["hNode", "bVerify", "pValue"] )
    #  ctypes.c_int spinFloatGetMin(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_double) pValue)
    addfunc(lib, "spinFloatGetMin", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_double)],
            argnames = ["hNode", "pValue"] )
    #  ctypes.c_int spinFloatGetMax(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_double) pValue)
    addfunc(lib, "spinFloatGetMax", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_double)],
            argnames = ["hNode", "pValue"] )
    #  ctypes.c_int spinFloatGetRepresentation(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int) pValue)
    addfunc(lib, "spinFloatGetRepresentation", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hNode", "pValue"] )
    #  ctypes.c_int spinFloatGetUnit(spinNodeHandle hNode, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinFloatGetUnit", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hNode", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinEnumerationGetNumEntries(spinNodeHandle hEnumNode, ctypes.POINTER(ctypes.c_size_t) pValue)
    addfunc(lib, "spinEnumerationGetNumEntries", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hEnumNode", "pValue"] )
    #  ctypes.c_int spinEnumerationGetEntryByIndex(spinNodeHandle hEnumNode, ctypes.c_size_t index, ctypes.POINTER(spinNodeHandle) phEntry)
    addfunc(lib, "spinEnumerationGetEntryByIndex", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_size_t, ctypes.POINTER(spinNodeHandle)],
            argnames = ["hEnumNode", "index", "phEntry"] )
    #  ctypes.c_int spinEnumerationGetEntryByName(spinNodeHandle hEnumNode, ctypes.c_char_p pName, ctypes.POINTER(spinNodeHandle) phEntry)
    addfunc(lib, "spinEnumerationGetEntryByName", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_char_p, ctypes.POINTER(spinNodeHandle)],
            argnames = ["hEnumNode", "pName", "phEntry"] )
    #  ctypes.c_int spinEnumerationGetCurrentEntry(spinNodeHandle hEnumNode, ctypes.POINTER(spinNodeHandle) phEntry)
    addfunc(lib, "spinEnumerationGetCurrentEntry", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(spinNodeHandle)],
            argnames = ["hEnumNode", "phEntry"] )
    #  ctypes.c_int spinEnumerationReleaseNode(spinNodeHandle hEnumNode, spinNodeHandle hEntry)
    addfunc(lib, "spinEnumerationReleaseNode", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, spinNodeHandle],
            argnames = ["hEnumNode", "hEntry"] )
    #  ctypes.c_int spinEnumerationSetIntValue(spinNodeHandle hEnumNode, ctypes.c_int64 value)
    addfunc(lib, "spinEnumerationSetIntValue", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_int64],
            argnames = ["hEnumNode", "value"] )
    #  ctypes.c_int spinEnumerationSetEnumValue(spinNodeHandle hEnumNode, ctypes.c_size_t value)
    addfunc(lib, "spinEnumerationSetEnumValue", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_size_t],
            argnames = ["hEnumNode", "value"] )
    #  ctypes.c_int spinEnumerationEntryGetIntValue(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int64) pValue)
    addfunc(lib, "spinEnumerationEntryGetIntValue", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["hNode", "pValue"] )
    #  ctypes.c_int spinEnumerationEntryGetEnumValue(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_size_t) pValue)
    addfunc(lib, "spinEnumerationEntryGetEnumValue", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hNode", "pValue"] )
    #  ctypes.c_int spinEnumerationEntryGetSymbolic(spinNodeHandle hNode, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinEnumerationEntryGetSymbolic", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hNode", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinBooleanSetValue(spinNodeHandle hNode, bool8_t value)
    addfunc(lib, "spinBooleanSetValue", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, bool8_t],
            argnames = ["hNode", "value"] )
    #  ctypes.c_int spinBooleanGetValue(spinNodeHandle hNode, ctypes.POINTER(bool8_t) pbValue)
    addfunc(lib, "spinBooleanGetValue", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(bool8_t)],
            argnames = ["hNode", "pbValue"] )
    #  ctypes.c_int spinCommandExecute(spinNodeHandle hNode)
    addfunc(lib, "spinCommandExecute", restype = ctypes.c_int,
            argtypes = [spinNodeHandle],
            argnames = ["hNode"] )
    #  ctypes.c_int spinCommandIsDone(spinNodeHandle hNode, ctypes.POINTER(bool8_t) pbValue)
    addfunc(lib, "spinCommandIsDone", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(bool8_t)],
            argnames = ["hNode", "pbValue"] )
    #  ctypes.c_int spinCategoryGetNumFeatures(spinNodeHandle hCategoryNode, ctypes.POINTER(ctypes.c_size_t) pValue)
    addfunc(lib, "spinCategoryGetNumFeatures", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hCategoryNode", "pValue"] )
    #  ctypes.c_int spinCategoryGetFeatureByIndex(spinNodeHandle hCategoryNode, ctypes.c_size_t index, ctypes.POINTER(spinNodeHandle) phFeature)
    addfunc(lib, "spinCategoryGetFeatureByIndex", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.c_size_t, ctypes.POINTER(spinNodeHandle)],
            argnames = ["hCategoryNode", "index", "phFeature"] )
    #  ctypes.c_int spinCategoryReleaseNode(spinNodeHandle hCategoryNode, spinNodeHandle hFeature)
    addfunc(lib, "spinCategoryReleaseNode", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, spinNodeHandle],
            argnames = ["hCategoryNode", "hFeature"] )
    #  ctypes.c_int spinRegisterGet(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_uint8) pBuf, ctypes.c_int64 length)
    addfunc(lib, "spinRegisterGet", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_uint8), ctypes.c_int64],
            argnames = ["hNode", "pBuf", "length"] )
    #  ctypes.c_int spinRegisterGetEx(spinNodeHandle hNode, bool8_t bVerify, bool8_t bIgnoreCache, ctypes.POINTER(ctypes.c_uint8) pBuf, ctypes.c_int64 length)
    addfunc(lib, "spinRegisterGetEx", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, bool8_t, bool8_t, ctypes.POINTER(ctypes.c_uint8), ctypes.c_int64],
            argnames = ["hNode", "bVerify", "bIgnoreCache", "pBuf", "length"] )
    #  ctypes.c_int spinRegisterGetAddress(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int64) pAddress)
    addfunc(lib, "spinRegisterGetAddress", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["hNode", "pAddress"] )
    #  ctypes.c_int spinRegisterGetLength(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_int64) pLength)
    addfunc(lib, "spinRegisterGetLength", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["hNode", "pLength"] )
    #  ctypes.c_int spinRegisterSet(spinNodeHandle hNode, ctypes.POINTER(ctypes.c_uint8) pBuf, ctypes.c_int64 length)
    addfunc(lib, "spinRegisterSet", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, ctypes.POINTER(ctypes.c_uint8), ctypes.c_int64],
            argnames = ["hNode", "pBuf", "length"] )
    #  ctypes.c_int spinRegisterSetEx(spinNodeHandle hNode, bool8_t bVerify, ctypes.POINTER(ctypes.c_uint8) pBuf, ctypes.c_int64 length)
    addfunc(lib, "spinRegisterSetEx", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, bool8_t, ctypes.POINTER(ctypes.c_uint8), ctypes.c_int64],
            argnames = ["hNode", "bVerify", "pBuf", "length"] )
    #  ctypes.c_int spinRegisterSetReference(spinNodeHandle hNode, spinNodeHandle hRef)
    addfunc(lib, "spinRegisterSetReference", restype = ctypes.c_int,
            argtypes = [spinNodeHandle, spinNodeHandle],
            argnames = ["hNode", "hRef"] )
    #  ctypes.c_int quickSpinInit(spinCamera hCamera, ctypes.POINTER(quickSpin) pQuickSpin)
    addfunc(lib, "quickSpinInit", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.POINTER(quickSpin)],
            argnames = ["hCamera", "pQuickSpin"] )
    #  ctypes.c_int quickSpinInitEx(spinCamera hCamera, ctypes.POINTER(quickSpin) pQuickSpin, ctypes.POINTER(quickSpinTLDevice) pQuickSpinTLDevice, ctypes.POINTER(quickSpinTLStream) pQuickSpinTLStream)
    addfunc(lib, "quickSpinInitEx", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.POINTER(quickSpin), ctypes.POINTER(quickSpinTLDevice), ctypes.POINTER(quickSpinTLStream)],
            argnames = ["hCamera", "pQuickSpin", "pQuickSpinTLDevice", "pQuickSpinTLStream"] )
    #  ctypes.c_int quickSpinTLDeviceInit(spinCamera hCamera, ctypes.POINTER(quickSpinTLDevice) pQuickSpinTLDevice)
    addfunc(lib, "quickSpinTLDeviceInit", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.POINTER(quickSpinTLDevice)],
            argnames = ["hCamera", "pQuickSpinTLDevice"] )
    #  ctypes.c_int quickSpinTLStreamInit(spinCamera hCamera, ctypes.POINTER(quickSpinTLStream) pQuickSpinTLStream)
    addfunc(lib, "quickSpinTLStreamInit", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.POINTER(quickSpinTLStream)],
            argnames = ["hCamera", "pQuickSpinTLStream"] )
    #  ctypes.c_int quickSpinTLInterfaceInit(spinInterface hInterface, ctypes.POINTER(quickSpinTLInterface) pQuickSpinTLInterface)
    addfunc(lib, "quickSpinTLInterfaceInit", restype = ctypes.c_int,
            argtypes = [spinInterface, ctypes.POINTER(quickSpinTLInterface)],
            argnames = ["hInterface", "pQuickSpinTLInterface"] )
    #  ctypes.c_int quickSpinTLSystemInit(spinSystem hSystem, ctypes.POINTER(quickSpinTLSystem) pQuickSpinTLSystem)
    addfunc(lib, "quickSpinTLSystemInit", restype = ctypes.c_int,
            argtypes = [spinSystem, ctypes.POINTER(quickSpinTLSystem)],
            argnames = ["hSystem", "pQuickSpinTLSystem"] )
    #  ctypes.c_int spinErrorGetLast(ctypes.POINTER(ctypes.c_int) pError)
    addfunc(lib, "spinErrorGetLast", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(ctypes.c_int)],
            argnames = ["pError"] )
    #  ctypes.c_int spinErrorGetLastMessage(ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinErrorGetLastMessage", restype = ctypes.c_int,
            argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["pBuf", "pBufLen"] )
    #  ctypes.c_int spinErrorGetLastBuildDate(ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinErrorGetLastBuildDate", restype = ctypes.c_int,
            argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["pBuf", "pBufLen"] )
    #  ctypes.c_int spinErrorGetLastBuildTime(ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinErrorGetLastBuildTime", restype = ctypes.c_int,
            argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["pBuf", "pBufLen"] )
    #  ctypes.c_int spinErrorGetLastFileName(ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinErrorGetLastFileName", restype = ctypes.c_int,
            argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["pBuf", "pBufLen"] )
    #  ctypes.c_int spinErrorGetLastFullMessage(ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinErrorGetLastFullMessage", restype = ctypes.c_int,
            argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["pBuf", "pBufLen"] )
    #  ctypes.c_int spinErrorGetLastFunctionName(ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinErrorGetLastFunctionName", restype = ctypes.c_int,
            argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["pBuf", "pBufLen"] )
    #  ctypes.c_int spinErrorGetLastLineNumber(ctypes.POINTER(ctypes.c_int64) pLineNum)
    addfunc(lib, "spinErrorGetLastLineNumber", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(ctypes.c_int64)],
            argnames = ["pLineNum"] )
    #  ctypes.c_int spinSystemGetInstance(ctypes.POINTER(spinSystem) phSystem)
    addfunc(lib, "spinSystemGetInstance", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinSystem)],
            argnames = ["phSystem"] )
    #  ctypes.c_int spinSystemReleaseInstance(spinSystem hSystem)
    addfunc(lib, "spinSystemReleaseInstance", restype = ctypes.c_int,
            argtypes = [spinSystem],
            argnames = ["hSystem"] )
    #  ctypes.c_int spinSystemGetInterfaces(spinSystem hSystem, spinInterfaceList hInterfaceList)
    addfunc(lib, "spinSystemGetInterfaces", restype = ctypes.c_int,
            argtypes = [spinSystem, spinInterfaceList],
            argnames = ["hSystem", "hInterfaceList"] )
    #  ctypes.c_int spinSystemGetCameras(spinSystem hSystem, spinCameraList hCameraList)
    addfunc(lib, "spinSystemGetCameras", restype = ctypes.c_int,
            argtypes = [spinSystem, spinCameraList],
            argnames = ["hSystem", "hCameraList"] )
    #  ctypes.c_int spinSystemGetCamerasEx(spinSystem hSystem, bool8_t bUpdateInterfaces, bool8_t bUpdateCameras, spinCameraList hCameraList)
    addfunc(lib, "spinSystemGetCamerasEx", restype = ctypes.c_int,
            argtypes = [spinSystem, bool8_t, bool8_t, spinCameraList],
            argnames = ["hSystem", "bUpdateInterfaces", "bUpdateCameras", "hCameraList"] )
    #  ctypes.c_int spinSystemSetLoggingLevel(spinSystem hSystem, ctypes.c_int logLevel)
    addfunc(lib, "spinSystemSetLoggingLevel", restype = ctypes.c_int,
            argtypes = [spinSystem, ctypes.c_int],
            argnames = ["hSystem", "logLevel"] )
    #  ctypes.c_int spinSystemGetLoggingLevel(spinSystem hSystem, ctypes.POINTER(ctypes.c_int) pLogLevel)
    addfunc(lib, "spinSystemGetLoggingLevel", restype = ctypes.c_int,
            argtypes = [spinSystem, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hSystem", "pLogLevel"] )
    #  ctypes.c_int spinSystemRegisterLogEventHandler(spinSystem hSystem, spinLogEventHandler hLogEventHandler)
    addfunc(lib, "spinSystemRegisterLogEventHandler", restype = ctypes.c_int,
            argtypes = [spinSystem, spinLogEventHandler],
            argnames = ["hSystem", "hLogEventHandler"] )
    #  ctypes.c_int spinSystemUnregisterLogEventHandler(spinSystem hSystem, spinLogEventHandler hLogEventHandler)
    addfunc(lib, "spinSystemUnregisterLogEventHandler", restype = ctypes.c_int,
            argtypes = [spinSystem, spinLogEventHandler],
            argnames = ["hSystem", "hLogEventHandler"] )
    #  ctypes.c_int spinSystemUnregisterAllLogEventHandlers(spinSystem hSystem)
    addfunc(lib, "spinSystemUnregisterAllLogEventHandlers", restype = ctypes.c_int,
            argtypes = [spinSystem],
            argnames = ["hSystem"] )
    #  ctypes.c_int spinSystemIsInUse(spinSystem hSystem, ctypes.POINTER(bool8_t) pbIsInUse)
    addfunc(lib, "spinSystemIsInUse", restype = ctypes.c_int,
            argtypes = [spinSystem, ctypes.POINTER(bool8_t)],
            argnames = ["hSystem", "pbIsInUse"] )
    #  ctypes.c_int spinSystemRegisterDeviceArrivalEventHandler(spinSystem hSystem, spinDeviceArrivalEventHandler hDeviceArrivalEventHandler)
    addfunc(lib, "spinSystemRegisterDeviceArrivalEventHandler", restype = ctypes.c_int,
            argtypes = [spinSystem, spinDeviceArrivalEventHandler],
            argnames = ["hSystem", "hDeviceArrivalEventHandler"] )
    #  ctypes.c_int spinSystemRegisterDeviceRemovalEventHandler(spinSystem hSystem, spinDeviceRemovalEventHandler hDeviceRemovalEventHandler)
    addfunc(lib, "spinSystemRegisterDeviceRemovalEventHandler", restype = ctypes.c_int,
            argtypes = [spinSystem, spinDeviceRemovalEventHandler],
            argnames = ["hSystem", "hDeviceRemovalEventHandler"] )
    #  ctypes.c_int spinSystemUnregisterDeviceArrivalEventHandler(spinSystem hSystem, spinDeviceArrivalEventHandler hDeviceArrivalEventHandler)
    addfunc(lib, "spinSystemUnregisterDeviceArrivalEventHandler", restype = ctypes.c_int,
            argtypes = [spinSystem, spinDeviceArrivalEventHandler],
            argnames = ["hSystem", "hDeviceArrivalEventHandler"] )
    #  ctypes.c_int spinSystemUnregisterDeviceRemovalEventHandler(spinSystem hSystem, spinDeviceRemovalEventHandler hDeviceRemovalEventHandler)
    addfunc(lib, "spinSystemUnregisterDeviceRemovalEventHandler", restype = ctypes.c_int,
            argtypes = [spinSystem, spinDeviceRemovalEventHandler],
            argnames = ["hSystem", "hDeviceRemovalEventHandler"] )
    #  ctypes.c_int spinSystemRegisterInterfaceEventHandler(spinSystem hSystem, spinInterfaceEventHandler hInterfaceEventHandler)
    addfunc(lib, "spinSystemRegisterInterfaceEventHandler", restype = ctypes.c_int,
            argtypes = [spinSystem, spinInterfaceEventHandler],
            argnames = ["hSystem", "hInterfaceEventHandler"] )
    #  ctypes.c_int spinSystemUnregisterInterfaceEventHandler(spinSystem hSystem, spinInterfaceEventHandler hInterfaceEventHandler)
    addfunc(lib, "spinSystemUnregisterInterfaceEventHandler", restype = ctypes.c_int,
            argtypes = [spinSystem, spinInterfaceEventHandler],
            argnames = ["hSystem", "hInterfaceEventHandler"] )
    #  ctypes.c_int spinSystemUpdateCameras(spinSystem hSystem, ctypes.POINTER(bool8_t) pbChanged)
    addfunc(lib, "spinSystemUpdateCameras", restype = ctypes.c_int,
            argtypes = [spinSystem, ctypes.POINTER(bool8_t)],
            argnames = ["hSystem", "pbChanged"] )
    #  ctypes.c_int spinSystemUpdateCamerasEx(spinSystem hSystem, bool8_t bUpdateInterfaces, ctypes.POINTER(bool8_t) pbChanged)
    addfunc(lib, "spinSystemUpdateCamerasEx", restype = ctypes.c_int,
            argtypes = [spinSystem, bool8_t, ctypes.POINTER(bool8_t)],
            argnames = ["hSystem", "bUpdateInterfaces", "pbChanged"] )
    #  ctypes.c_int spinSystemSendActionCommand(spinSystem hSystem, ctypes.c_size_t iDeviceKey, ctypes.c_size_t iGroupKey, ctypes.c_size_t iGroupMask, ctypes.c_size_t iActionTime, bool8_t requestAck, ctypes.POINTER(ctypes.c_size_t) piResultSize, ctypes.POINTER(actionCommandResult) results)
    addfunc(lib, "spinSystemSendActionCommand", restype = ctypes.c_int,
            argtypes = [spinSystem, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, bool8_t, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(actionCommandResult)],
            argnames = ["hSystem", "iDeviceKey", "iGroupKey", "iGroupMask", "iActionTime", "requestAck", "piResultSize", "results"] )
    #  ctypes.c_int spinSystemGetLibraryVersion(spinSystem hSystem, ctypes.POINTER(spinLibraryVersion) hLibraryVersion)
    addfunc(lib, "spinSystemGetLibraryVersion", restype = ctypes.c_int,
            argtypes = [spinSystem, ctypes.POINTER(spinLibraryVersion)],
            argnames = ["hSystem", "hLibraryVersion"] )
    #  ctypes.c_int spinSystemGetTLNodeMap(spinSystem hSystem, ctypes.POINTER(spinNodeMapHandle) phNodeMap)
    addfunc(lib, "spinSystemGetTLNodeMap", restype = ctypes.c_int,
            argtypes = [spinSystem, ctypes.POINTER(spinNodeMapHandle)],
            argnames = ["hSystem", "phNodeMap"] )
    #  ctypes.c_int spinInterfaceListCreateEmpty(ctypes.POINTER(spinInterfaceList) phInterfaceList)
    addfunc(lib, "spinInterfaceListCreateEmpty", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinInterfaceList)],
            argnames = ["phInterfaceList"] )
    #  ctypes.c_int spinInterfaceListDestroy(spinInterfaceList hInterfaceList)
    addfunc(lib, "spinInterfaceListDestroy", restype = ctypes.c_int,
            argtypes = [spinInterfaceList],
            argnames = ["hInterfaceList"] )
    #  ctypes.c_int spinInterfaceListGetSize(spinInterfaceList hInterfaceList, ctypes.POINTER(ctypes.c_size_t) pSize)
    addfunc(lib, "spinInterfaceListGetSize", restype = ctypes.c_int,
            argtypes = [spinInterfaceList, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hInterfaceList", "pSize"] )
    #  ctypes.c_int spinInterfaceListGet(spinInterfaceList hInterfaceList, ctypes.c_size_t index, ctypes.POINTER(spinInterface) phInterface)
    addfunc(lib, "spinInterfaceListGet", restype = ctypes.c_int,
            argtypes = [spinInterfaceList, ctypes.c_size_t, ctypes.POINTER(spinInterface)],
            argnames = ["hInterfaceList", "index", "phInterface"] )
    #  ctypes.c_int spinInterfaceListClear(spinInterfaceList hInterfaceList)
    addfunc(lib, "spinInterfaceListClear", restype = ctypes.c_int,
            argtypes = [spinInterfaceList],
            argnames = ["hInterfaceList"] )
    #  ctypes.c_int spinCameraListCreateEmpty(ctypes.POINTER(spinCameraList) phCameraList)
    addfunc(lib, "spinCameraListCreateEmpty", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinCameraList)],
            argnames = ["phCameraList"] )
    #  ctypes.c_int spinCameraListDestroy(spinCameraList hCameraList)
    addfunc(lib, "spinCameraListDestroy", restype = ctypes.c_int,
            argtypes = [spinCameraList],
            argnames = ["hCameraList"] )
    #  ctypes.c_int spinCameraListGetSize(spinCameraList hCameraList, ctypes.POINTER(ctypes.c_size_t) pSize)
    addfunc(lib, "spinCameraListGetSize", restype = ctypes.c_int,
            argtypes = [spinCameraList, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hCameraList", "pSize"] )
    #  ctypes.c_int spinCameraListGet(spinCameraList hCameraList, ctypes.c_size_t index, ctypes.POINTER(spinCamera) phCamera)
    addfunc(lib, "spinCameraListGet", restype = ctypes.c_int,
            argtypes = [spinCameraList, ctypes.c_size_t, ctypes.POINTER(spinCamera)],
            argnames = ["hCameraList", "index", "phCamera"] )
    #  ctypes.c_int spinCameraListClear(spinCameraList hCameraList)
    addfunc(lib, "spinCameraListClear", restype = ctypes.c_int,
            argtypes = [spinCameraList],
            argnames = ["hCameraList"] )
    #  ctypes.c_int spinCameraListRemove(spinCameraList hCameraList, ctypes.c_size_t index)
    addfunc(lib, "spinCameraListRemove", restype = ctypes.c_int,
            argtypes = [spinCameraList, ctypes.c_size_t],
            argnames = ["hCameraList", "index"] )
    #  ctypes.c_int spinCameraListAppend(spinCameraList hCameraListBase, spinCameraList hCameraListToAppend)
    addfunc(lib, "spinCameraListAppend", restype = ctypes.c_int,
            argtypes = [spinCameraList, spinCameraList],
            argnames = ["hCameraListBase", "hCameraListToAppend"] )
    #  ctypes.c_int spinCameraListGetBySerial(spinCameraList hCameraList, ctypes.c_char_p pSerial, ctypes.POINTER(spinCamera) phCamera)
    addfunc(lib, "spinCameraListGetBySerial", restype = ctypes.c_int,
            argtypes = [spinCameraList, ctypes.c_char_p, ctypes.POINTER(spinCamera)],
            argnames = ["hCameraList", "pSerial", "phCamera"] )
    #  ctypes.c_int spinCameraListRemoveBySerial(spinCameraList hCameraList, ctypes.c_char_p pSerial)
    addfunc(lib, "spinCameraListRemoveBySerial", restype = ctypes.c_int,
            argtypes = [spinCameraList, ctypes.c_char_p],
            argnames = ["hCameraList", "pSerial"] )
    #  ctypes.c_int spinImageListCreateEmpty(ctypes.POINTER(spinImageList) phImageList)
    addfunc(lib, "spinImageListCreateEmpty", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinImageList)],
            argnames = ["phImageList"] )
    #  ctypes.c_int spinImageListDestroy(spinImageList hImageList)
    addfunc(lib, "spinImageListDestroy", restype = ctypes.c_int,
            argtypes = [spinImageList],
            argnames = ["hImageList"] )
    #  ctypes.c_int spinImageListGetSize(spinImageList hImageList, ctypes.POINTER(ctypes.c_size_t) pSize)
    addfunc(lib, "spinImageListGetSize", restype = ctypes.c_int,
            argtypes = [spinImageList, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hImageList", "pSize"] )
    #  ctypes.c_int spinImageListGet(spinImageList hImageList, ctypes.c_size_t index, ctypes.POINTER(spinImage) phImage)
    addfunc(lib, "spinImageListGet", restype = ctypes.c_int,
            argtypes = [spinImageList, ctypes.c_size_t, ctypes.POINTER(spinImage)],
            argnames = ["hImageList", "index", "phImage"] )
    #  ctypes.c_int spinImageListClear(spinImageList hImageList)
    addfunc(lib, "spinImageListClear", restype = ctypes.c_int,
            argtypes = [spinImageList],
            argnames = ["hImageList"] )
    #  ctypes.c_int spinImageListRemove(spinImageList hImageList, ctypes.c_size_t index)
    addfunc(lib, "spinImageListRemove", restype = ctypes.c_int,
            argtypes = [spinImageList, ctypes.c_size_t],
            argnames = ["hImageList", "index"] )
    #  ctypes.c_int spinImageListAppend(spinImageList hImageListBase, spinImageList hImageListToAppend)
    addfunc(lib, "spinImageListAppend", restype = ctypes.c_int,
            argtypes = [spinImageList, spinImageList],
            argnames = ["hImageListBase", "hImageListToAppend"] )
    #  ctypes.c_int spinImageListGetByPixelFormat(spinImageList hImageList, ctypes.c_int pixelFormat, ctypes.POINTER(spinImage) phImage)
    addfunc(lib, "spinImageListGetByPixelFormat", restype = ctypes.c_int,
            argtypes = [spinImageList, ctypes.c_int, ctypes.POINTER(spinImage)],
            argnames = ["hImageList", "pixelFormat", "phImage"] )
    #  ctypes.c_int spinImageListRemoveByPixelFormat(spinImageList hImageList, ctypes.c_int pixelFormat)
    addfunc(lib, "spinImageListRemoveByPixelFormat", restype = ctypes.c_int,
            argtypes = [spinImageList, ctypes.c_int],
            argnames = ["hImageList", "pixelFormat"] )
    #  ctypes.c_int spinImageListRelease(spinImageList hImageList)
    addfunc(lib, "spinImageListRelease", restype = ctypes.c_int,
            argtypes = [spinImageList],
            argnames = ["hImageList"] )
    #  ctypes.c_int spinImageListSave(spinImageList hImageList, ctypes.c_char_p fileName)
    addfunc(lib, "spinImageListSave", restype = ctypes.c_int,
            argtypes = [spinImageList, ctypes.c_char_p],
            argnames = ["hImageList", "fileName"] )
    #  ctypes.c_int spinImageListLoad(ctypes.POINTER(spinImageList) phImageList, ctypes.c_char_p fileName)
    addfunc(lib, "spinImageListLoad", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinImageList), ctypes.c_char_p],
            argnames = ["phImageList", "fileName"] )
    #  ctypes.c_int spinInterfaceUpdateCameras(spinInterface hInterface, ctypes.POINTER(bool8_t) pbChanged)
    addfunc(lib, "spinInterfaceUpdateCameras", restype = ctypes.c_int,
            argtypes = [spinInterface, ctypes.POINTER(bool8_t)],
            argnames = ["hInterface", "pbChanged"] )
    #  ctypes.c_int spinInterfaceGetCameras(spinInterface hInterface, spinCameraList hCameraList)
    addfunc(lib, "spinInterfaceGetCameras", restype = ctypes.c_int,
            argtypes = [spinInterface, spinCameraList],
            argnames = ["hInterface", "hCameraList"] )
    #  ctypes.c_int spinInterfaceGetCamerasEx(spinInterface hInterface, bool8_t bUpdateCameras, spinCameraList hCameraList)
    addfunc(lib, "spinInterfaceGetCamerasEx", restype = ctypes.c_int,
            argtypes = [spinInterface, bool8_t, spinCameraList],
            argnames = ["hInterface", "bUpdateCameras", "hCameraList"] )
    #  ctypes.c_int spinInterfaceGetTLNodeMap(spinInterface hInterface, ctypes.POINTER(spinNodeMapHandle) phNodeMap)
    addfunc(lib, "spinInterfaceGetTLNodeMap", restype = ctypes.c_int,
            argtypes = [spinInterface, ctypes.POINTER(spinNodeMapHandle)],
            argnames = ["hInterface", "phNodeMap"] )
    #  ctypes.c_int spinInterfaceRegisterDeviceArrivalEventHandler(spinInterface hInterface, spinDeviceArrivalEventHandler hDeviceArrivalEventHandler)
    addfunc(lib, "spinInterfaceRegisterDeviceArrivalEventHandler", restype = ctypes.c_int,
            argtypes = [spinInterface, spinDeviceArrivalEventHandler],
            argnames = ["hInterface", "hDeviceArrivalEventHandler"] )
    #  ctypes.c_int spinInterfaceRegisterDeviceRemovalEventHandler(spinInterface hInterface, spinDeviceRemovalEventHandler hDeviceRemovalEventHandler)
    addfunc(lib, "spinInterfaceRegisterDeviceRemovalEventHandler", restype = ctypes.c_int,
            argtypes = [spinInterface, spinDeviceRemovalEventHandler],
            argnames = ["hInterface", "hDeviceRemovalEventHandler"] )
    #  ctypes.c_int spinInterfaceUnregisterDeviceArrivalEventHandler(spinInterface hInterface, spinDeviceArrivalEventHandler hDeviceArrivalEventHandler)
    addfunc(lib, "spinInterfaceUnregisterDeviceArrivalEventHandler", restype = ctypes.c_int,
            argtypes = [spinInterface, spinDeviceArrivalEventHandler],
            argnames = ["hInterface", "hDeviceArrivalEventHandler"] )
    #  ctypes.c_int spinInterfaceUnregisterDeviceRemovalEventHandler(spinInterface hInterface, spinDeviceRemovalEventHandler hDeviceRemovalEventHandler)
    addfunc(lib, "spinInterfaceUnregisterDeviceRemovalEventHandler", restype = ctypes.c_int,
            argtypes = [spinInterface, spinDeviceRemovalEventHandler],
            argnames = ["hInterface", "hDeviceRemovalEventHandler"] )
    #  ctypes.c_int spinInterfaceRegisterInterfaceEventHandler(spinInterface hInterface, spinInterfaceEventHandler hInterfaceEventHandler)
    addfunc(lib, "spinInterfaceRegisterInterfaceEventHandler", restype = ctypes.c_int,
            argtypes = [spinInterface, spinInterfaceEventHandler],
            argnames = ["hInterface", "hInterfaceEventHandler"] )
    #  ctypes.c_int spinInterfaceUnregisterInterfaceEventHandler(spinInterface hInterface, spinInterfaceEventHandler hInterfaceEventHandler)
    addfunc(lib, "spinInterfaceUnregisterInterfaceEventHandler", restype = ctypes.c_int,
            argtypes = [spinInterface, spinInterfaceEventHandler],
            argnames = ["hInterface", "hInterfaceEventHandler"] )
    #  ctypes.c_int spinInterfaceRelease(spinInterface hInterface)
    addfunc(lib, "spinInterfaceRelease", restype = ctypes.c_int,
            argtypes = [spinInterface],
            argnames = ["hInterface"] )
    #  ctypes.c_int spinInterfaceIsInUse(spinInterface hInterface, ctypes.POINTER(bool8_t) pbIsInUse)
    addfunc(lib, "spinInterfaceIsInUse", restype = ctypes.c_int,
            argtypes = [spinInterface, ctypes.POINTER(bool8_t)],
            argnames = ["hInterface", "pbIsInUse"] )
    #  ctypes.c_int spinInterfaceSendActionCommand(spinInterface hInterface, ctypes.c_size_t iDeviceKey, ctypes.c_size_t iGroupKey, ctypes.c_size_t iGroupMask, ctypes.c_size_t iActionTime, bool8_t requestAck, ctypes.POINTER(ctypes.c_size_t) piResultSize, ctypes.POINTER(actionCommandResult) results)
    addfunc(lib, "spinInterfaceSendActionCommand", restype = ctypes.c_int,
            argtypes = [spinInterface, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, bool8_t, ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(actionCommandResult)],
            argnames = ["hInterface", "iDeviceKey", "iGroupKey", "iGroupMask", "iActionTime", "requestAck", "piResultSize", "results"] )
    #  ctypes.c_int spinCameraInit(spinCamera hCamera)
    addfunc(lib, "spinCameraInit", restype = ctypes.c_int,
            argtypes = [spinCamera],
            argnames = ["hCamera"] )
    #  ctypes.c_int spinCameraDeInit(spinCamera hCamera)
    addfunc(lib, "spinCameraDeInit", restype = ctypes.c_int,
            argtypes = [spinCamera],
            argnames = ["hCamera"] )
    #  ctypes.c_int spinCameraGetNodeMap(spinCamera hCamera, ctypes.POINTER(spinNodeMapHandle) phNodeMap)
    addfunc(lib, "spinCameraGetNodeMap", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.POINTER(spinNodeMapHandle)],
            argnames = ["hCamera", "phNodeMap"] )
    #  ctypes.c_int spinCameraGetTLDeviceNodeMap(spinCamera hCamera, ctypes.POINTER(spinNodeMapHandle) phNodeMap)
    addfunc(lib, "spinCameraGetTLDeviceNodeMap", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.POINTER(spinNodeMapHandle)],
            argnames = ["hCamera", "phNodeMap"] )
    #  ctypes.c_int spinCameraGetTLStreamNodeMap(spinCamera hCamera, ctypes.POINTER(spinNodeMapHandle) phNodeMap)
    addfunc(lib, "spinCameraGetTLStreamNodeMap", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.POINTER(spinNodeMapHandle)],
            argnames = ["hCamera", "phNodeMap"] )
    #  ctypes.c_int spinCameraGetAccessMode(spinCamera hCamera, ctypes.POINTER(ctypes.c_int) pAccessMode)
    addfunc(lib, "spinCameraGetAccessMode", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hCamera", "pAccessMode"] )
    #  ctypes.c_int spinCameraReadPort(spinCamera hCamera, ctypes.c_uint64 iAddress, ctypes.c_void_p pBuffer, ctypes.c_size_t iSize)
    addfunc(lib, "spinCameraReadPort", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_size_t],
            argnames = ["hCamera", "iAddress", "pBuffer", "iSize"] )
    #  ctypes.c_int spinCameraWritePort(spinCamera hCamera, ctypes.c_uint64 iAddress, ctypes.c_void_p pBuffer, ctypes.c_size_t iSize)
    addfunc(lib, "spinCameraWritePort", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_size_t],
            argnames = ["hCamera", "iAddress", "pBuffer", "iSize"] )
    #  ctypes.c_int spinCameraBeginAcquisition(spinCamera hCamera)
    addfunc(lib, "spinCameraBeginAcquisition", restype = ctypes.c_int,
            argtypes = [spinCamera],
            argnames = ["hCamera"] )
    #  ctypes.c_int spinCameraEndAcquisition(spinCamera hCamera)
    addfunc(lib, "spinCameraEndAcquisition", restype = ctypes.c_int,
            argtypes = [spinCamera],
            argnames = ["hCamera"] )
    #  ctypes.c_int spinCameraGetNextImage(spinCamera hCamera, ctypes.POINTER(spinImage) phImage)
    addfunc(lib, "spinCameraGetNextImage", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.POINTER(spinImage)],
            argnames = ["hCamera", "phImage"] )
    #  ctypes.c_int spinCameraGetNextImageEx(spinCamera hCamera, ctypes.c_uint64 grabTimeout, ctypes.POINTER(spinImage) phImage)
    addfunc(lib, "spinCameraGetNextImageEx", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.c_uint64, ctypes.POINTER(spinImage)],
            argnames = ["hCamera", "grabTimeout", "phImage"] )
    #  ctypes.c_int spinCameraGetNextImageSync(spinCamera hCamera, ctypes.c_uint64 grabTimeout, ctypes.POINTER(spinImageList) phImageList)
    addfunc(lib, "spinCameraGetNextImageSync", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.c_uint64, ctypes.POINTER(spinImageList)],
            argnames = ["hCamera", "grabTimeout", "phImageList"] )
    #  ctypes.c_int spinCameraGetDeviceID(spinCamera hCamera, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinCameraGetDeviceID", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hCamera", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinCameraGetUniqueID(spinCamera hCamera, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinCameraGetUniqueID", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hCamera", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinCameraIsStreaming(spinCamera hCamera, ctypes.POINTER(bool8_t) pbIsStreaming)
    addfunc(lib, "spinCameraIsStreaming", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.POINTER(bool8_t)],
            argnames = ["hCamera", "pbIsStreaming"] )
    #  ctypes.c_int spinCameraGetGuiXml(spinCamera hCamera, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinCameraGetGuiXml", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hCamera", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinCameraRegisterDeviceEventHandler(spinCamera hCamera, spinDeviceEventHandler hDeviceEventHandler)
    addfunc(lib, "spinCameraRegisterDeviceEventHandler", restype = ctypes.c_int,
            argtypes = [spinCamera, spinDeviceEventHandler],
            argnames = ["hCamera", "hDeviceEventHandler"] )
    #  ctypes.c_int spinCameraRegisterDeviceEventHandlerEx(spinCamera hCamera, spinDeviceEventHandler hDeviceEventHandler, ctypes.c_char_p pName)
    addfunc(lib, "spinCameraRegisterDeviceEventHandlerEx", restype = ctypes.c_int,
            argtypes = [spinCamera, spinDeviceEventHandler, ctypes.c_char_p],
            argnames = ["hCamera", "hDeviceEventHandler", "pName"] )
    #  ctypes.c_int spinCameraUnregisterDeviceEventHandler(spinCamera hCamera, spinDeviceEventHandler hDeviceEventHandler)
    addfunc(lib, "spinCameraUnregisterDeviceEventHandler", restype = ctypes.c_int,
            argtypes = [spinCamera, spinDeviceEventHandler],
            argnames = ["hCamera", "hDeviceEventHandler"] )
    #  ctypes.c_int spinCameraRegisterImageEventHandler(spinCamera hCamera, spinImageEventHandler hImageEventHandler)
    addfunc(lib, "spinCameraRegisterImageEventHandler", restype = ctypes.c_int,
            argtypes = [spinCamera, spinImageEventHandler],
            argnames = ["hCamera", "hImageEventHandler"] )
    #  ctypes.c_int spinCameraRegisterImageEventHandlerEx(spinCamera hCamera, spinImageEventHandler hImageEventHandler, ctypes.c_uint64 streamIndex)
    addfunc(lib, "spinCameraRegisterImageEventHandlerEx", restype = ctypes.c_int,
            argtypes = [spinCamera, spinImageEventHandler, ctypes.c_uint64],
            argnames = ["hCamera", "hImageEventHandler", "streamIndex"] )
    #  ctypes.c_int spinCameraUnregisterImageEventHandler(spinCamera hCamera, spinImageEventHandler hImageEventHandler)
    addfunc(lib, "spinCameraUnregisterImageEventHandler", restype = ctypes.c_int,
            argtypes = [spinCamera, spinImageEventHandler],
            argnames = ["hCamera", "hImageEventHandler"] )
    #  ctypes.c_int spinCameraRegisterImageListEventHandler(spinCamera hCamera, spinImageListEventHandler hImageListEventHandler)
    addfunc(lib, "spinCameraRegisterImageListEventHandler", restype = ctypes.c_int,
            argtypes = [spinCamera, spinImageListEventHandler],
            argnames = ["hCamera", "hImageListEventHandler"] )
    #  ctypes.c_int spinCameraUnregisterImageListEventHandler(spinCamera hCamera, spinImageListEventHandler hImageListEventHandler)
    addfunc(lib, "spinCameraUnregisterImageListEventHandler", restype = ctypes.c_int,
            argtypes = [spinCamera, spinImageListEventHandler],
            argnames = ["hCamera", "hImageListEventHandler"] )
    #  ctypes.c_int spinCameraRelease(spinCamera hCamera)
    addfunc(lib, "spinCameraRelease", restype = ctypes.c_int,
            argtypes = [spinCamera],
            argnames = ["hCamera"] )
    #  ctypes.c_int spinCameraIsValid(spinCamera hCamera, ctypes.POINTER(bool8_t) pbValid)
    addfunc(lib, "spinCameraIsValid", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.POINTER(bool8_t)],
            argnames = ["hCamera", "pbValid"] )
    #  ctypes.c_int spinCameraIsInitialized(spinCamera hCamera, ctypes.POINTER(bool8_t) pbInit)
    addfunc(lib, "spinCameraIsInitialized", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.POINTER(bool8_t)],
            argnames = ["hCamera", "pbInit"] )
    #  ctypes.c_int spinCameraDiscoverMaxPacketSize(spinCamera hCamera, ctypes.POINTER(ctypes.c_uint) pMaxPacketSize)
    addfunc(lib, "spinCameraDiscoverMaxPacketSize", restype = ctypes.c_int,
            argtypes = [spinCamera, ctypes.POINTER(ctypes.c_uint)],
            argnames = ["hCamera", "pMaxPacketSize"] )
    #  ctypes.c_int spinCameraForceIP()
    addfunc(lib, "spinCameraForceIP", restype = ctypes.c_int,
            argtypes = [],
            argnames = [] )
    #  ctypes.c_int spinImageCreateEmpty(ctypes.POINTER(spinImage) phImage)
    addfunc(lib, "spinImageCreateEmpty", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinImage)],
            argnames = ["phImage"] )
    #  ctypes.c_int spinImageCreate(spinImage hSrcImage, ctypes.POINTER(spinImage) phDestImage)
    addfunc(lib, "spinImageCreate", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(spinImage)],
            argnames = ["hSrcImage", "phDestImage"] )
    #  ctypes.c_int spinImageCreateEx(ctypes.POINTER(spinImage) phImage, ctypes.c_size_t width, ctypes.c_size_t height, ctypes.c_size_t offsetX, ctypes.c_size_t offsetY, ctypes.c_int pixelFormat, ctypes.c_void_p pData)
    addfunc(lib, "spinImageCreateEx", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinImage), ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_int, ctypes.c_void_p],
            argnames = ["phImage", "width", "height", "offsetX", "offsetY", "pixelFormat", "pData"] )
    #  ctypes.c_int spinImageCreateEx2(ctypes.POINTER(spinImage) phImage, ctypes.c_size_t width, ctypes.c_size_t height, ctypes.c_size_t offsetX, ctypes.c_size_t offsetY, ctypes.c_int pixelFormat, ctypes.c_void_p pData, ctypes.c_int dataPayloadType, ctypes.c_size_t dataSize)
    addfunc(lib, "spinImageCreateEx2", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinImage), ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_size_t],
            argnames = ["phImage", "width", "height", "offsetX", "offsetY", "pixelFormat", "pData", "dataPayloadType", "dataSize"] )
    #  ctypes.c_int spinImageDestroy(spinImage hImage)
    addfunc(lib, "spinImageDestroy", restype = ctypes.c_int,
            argtypes = [spinImage],
            argnames = ["hImage"] )
    #  ctypes.c_int spinImageGetColorProcessing(spinImage hImage, ctypes.POINTER(ctypes.c_int) pAlgorithm)
    addfunc(lib, "spinImageGetColorProcessing", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hImage", "pAlgorithm"] )
    #  ctypes.c_int spinImageReset(spinImage hImage, ctypes.c_size_t width, ctypes.c_size_t height, ctypes.c_size_t offsetX, ctypes.c_size_t offsetY, ctypes.c_int pixelFormat)
    addfunc(lib, "spinImageReset", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_int],
            argnames = ["hImage", "width", "height", "offsetX", "offsetY", "pixelFormat"] )
    #  ctypes.c_int spinImageResetEx(spinImage hImage, ctypes.c_size_t width, ctypes.c_size_t height, ctypes.c_size_t offsetX, ctypes.c_size_t offsetY, ctypes.c_int pixelFormat, ctypes.c_void_p pData)
    addfunc(lib, "spinImageResetEx", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_int, ctypes.c_void_p],
            argnames = ["hImage", "width", "height", "offsetX", "offsetY", "pixelFormat", "pData"] )
    #  ctypes.c_int spinImageGetID(spinImage hImage, ctypes.POINTER(ctypes.c_uint64) pId)
    addfunc(lib, "spinImageGetID", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["hImage", "pId"] )
    #  ctypes.c_int spinImageGetData(spinImage hImage, ctypes.POINTER(ctypes.c_void_p) ppData)
    addfunc(lib, "spinImageGetData", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_void_p)],
            argnames = ["hImage", "ppData"] )
    #  ctypes.c_int spinImageGetPrivateData(spinImage hImage, ctypes.POINTER(ctypes.c_void_p) ppData)
    addfunc(lib, "spinImageGetPrivateData", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_void_p)],
            argnames = ["hImage", "ppData"] )
    #  ctypes.c_int spinImageGetBufferSize(spinImage hImage, ctypes.POINTER(ctypes.c_size_t) pSize)
    addfunc(lib, "spinImageGetBufferSize", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hImage", "pSize"] )
    #  ctypes.c_int spinImageDeepCopy(spinImage hSrcImage, spinImage hDestImage)
    addfunc(lib, "spinImageDeepCopy", restype = ctypes.c_int,
            argtypes = [spinImage, spinImage],
            argnames = ["hSrcImage", "hDestImage"] )
    #  ctypes.c_int spinImageGetWidth(spinImage hImage, ctypes.POINTER(ctypes.c_size_t) pWidth)
    addfunc(lib, "spinImageGetWidth", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hImage", "pWidth"] )
    #  ctypes.c_int spinImageGetHeight(spinImage hImage, ctypes.POINTER(ctypes.c_size_t) pHeight)
    addfunc(lib, "spinImageGetHeight", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hImage", "pHeight"] )
    #  ctypes.c_int spinImageGetOffsetX(spinImage hImage, ctypes.POINTER(ctypes.c_size_t) pOffsetX)
    addfunc(lib, "spinImageGetOffsetX", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hImage", "pOffsetX"] )
    #  ctypes.c_int spinImageGetOffsetY(spinImage hImage, ctypes.POINTER(ctypes.c_size_t) pOffsetY)
    addfunc(lib, "spinImageGetOffsetY", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hImage", "pOffsetY"] )
    #  ctypes.c_int spinImageGetPaddingX(spinImage hImage, ctypes.POINTER(ctypes.c_size_t) pPaddingX)
    addfunc(lib, "spinImageGetPaddingX", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hImage", "pPaddingX"] )
    #  ctypes.c_int spinImageGetPaddingY(spinImage hImage, ctypes.POINTER(ctypes.c_size_t) pPaddingY)
    addfunc(lib, "spinImageGetPaddingY", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hImage", "pPaddingY"] )
    #  ctypes.c_int spinImageGetFrameID(spinImage hImage, ctypes.POINTER(ctypes.c_uint64) pFrameID)
    addfunc(lib, "spinImageGetFrameID", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["hImage", "pFrameID"] )
    #  ctypes.c_int spinImageGetTimeStamp(spinImage hImage, ctypes.POINTER(ctypes.c_uint64) pTimeStamp)
    addfunc(lib, "spinImageGetTimeStamp", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["hImage", "pTimeStamp"] )
    #  ctypes.c_int spinImageGetPayloadType(spinImage hImage, ctypes.POINTER(ctypes.c_size_t) pPayloadType)
    addfunc(lib, "spinImageGetPayloadType", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hImage", "pPayloadType"] )
    #  ctypes.c_int spinImageGetTLPayloadType(spinImage hImage, ctypes.POINTER(ctypes.c_int) pPayloadType)
    addfunc(lib, "spinImageGetTLPayloadType", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hImage", "pPayloadType"] )
    #  ctypes.c_int spinImageGetPixelFormat(spinImage hImage, ctypes.POINTER(ctypes.c_int) pPixelFormat)
    addfunc(lib, "spinImageGetPixelFormat", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hImage", "pPixelFormat"] )
    #  ctypes.c_int spinImageGetTLPixelFormat(spinImage hImage, ctypes.POINTER(ctypes.c_uint64) pPixelFormat)
    addfunc(lib, "spinImageGetTLPixelFormat", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["hImage", "pPixelFormat"] )
    #  ctypes.c_int spinImageGetTLPixelFormatNamespace(spinImage hImage, ctypes.POINTER(ctypes.c_int) pPixelFormatNamespace)
    addfunc(lib, "spinImageGetTLPixelFormatNamespace", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hImage", "pPixelFormatNamespace"] )
    #  ctypes.c_int spinImageGetPixelFormatName(spinImage hImage, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinImageGetPixelFormatName", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hImage", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinImageIsIncomplete(spinImage hImage, ctypes.POINTER(bool8_t) pbIsIncomplete)
    addfunc(lib, "spinImageIsIncomplete", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(bool8_t)],
            argnames = ["hImage", "pbIsIncomplete"] )
    #  ctypes.c_int spinImageGetValidPayloadSize(spinImage hImage, ctypes.POINTER(ctypes.c_size_t) pSize)
    addfunc(lib, "spinImageGetValidPayloadSize", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hImage", "pSize"] )
    #  ctypes.c_int spinImageSave(spinImage hImage, ctypes.c_char_p pFilename, ctypes.c_int format)
    addfunc(lib, "spinImageSave", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.c_char_p, ctypes.c_int],
            argnames = ["hImage", "pFilename", "format"] )
    #  ctypes.c_int spinImageSaveFromExt(spinImage hImage, ctypes.c_char_p pFilename)
    addfunc(lib, "spinImageSaveFromExt", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.c_char_p],
            argnames = ["hImage", "pFilename"] )
    #  ctypes.c_int spinImageSavePng(spinImage hImage, ctypes.c_char_p pFilename, ctypes.POINTER(spinPNGOption) pOption)
    addfunc(lib, "spinImageSavePng", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.c_char_p, ctypes.POINTER(spinPNGOption)],
            argnames = ["hImage", "pFilename", "pOption"] )
    #  ctypes.c_int spinImageSavePpm(spinImage hImage, ctypes.c_char_p pFilename, ctypes.POINTER(spinPPMOption) pOption)
    addfunc(lib, "spinImageSavePpm", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.c_char_p, ctypes.POINTER(spinPPMOption)],
            argnames = ["hImage", "pFilename", "pOption"] )
    #  ctypes.c_int spinImageSavePgm(spinImage hImage, ctypes.c_char_p pFilename, ctypes.POINTER(spinPGMOption) pOption)
    addfunc(lib, "spinImageSavePgm", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.c_char_p, ctypes.POINTER(spinPGMOption)],
            argnames = ["hImage", "pFilename", "pOption"] )
    #  ctypes.c_int spinImageSaveTiff(spinImage hImage, ctypes.c_char_p pFilename, ctypes.POINTER(spinTIFFOption) pOption)
    addfunc(lib, "spinImageSaveTiff", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.c_char_p, ctypes.POINTER(spinTIFFOption)],
            argnames = ["hImage", "pFilename", "pOption"] )
    #  ctypes.c_int spinImageSaveJpeg(spinImage hImage, ctypes.c_char_p pFilename, ctypes.POINTER(spinJPEGOption) pOption)
    addfunc(lib, "spinImageSaveJpeg", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.c_char_p, ctypes.POINTER(spinJPEGOption)],
            argnames = ["hImage", "pFilename", "pOption"] )
    #  ctypes.c_int spinImageSaveJpg2(spinImage hImage, ctypes.c_char_p pFilename, ctypes.POINTER(spinJPG2Option) pOption)
    addfunc(lib, "spinImageSaveJpg2", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.c_char_p, ctypes.POINTER(spinJPG2Option)],
            argnames = ["hImage", "pFilename", "pOption"] )
    #  ctypes.c_int spinImageSaveBmp(spinImage hImage, ctypes.c_char_p pFilename, ctypes.POINTER(spinBMPOption) pOption)
    addfunc(lib, "spinImageSaveBmp", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.c_char_p, ctypes.POINTER(spinBMPOption)],
            argnames = ["hImage", "pFilename", "pOption"] )
    #  ctypes.c_int spinImageGetChunkLayoutID(spinImage hImage, ctypes.POINTER(ctypes.c_uint64) pId)
    addfunc(lib, "spinImageGetChunkLayoutID", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["hImage", "pId"] )
    #  ctypes.c_int spinImageCalculateStatistics(spinImage hImage, spinImageStatistics hStatistics)
    addfunc(lib, "spinImageCalculateStatistics", restype = ctypes.c_int,
            argtypes = [spinImage, spinImageStatistics],
            argnames = ["hImage", "hStatistics"] )
    #  ctypes.c_int spinImageGetStatus(spinImage hImage, ctypes.POINTER(ctypes.c_int) pStatus)
    addfunc(lib, "spinImageGetStatus", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hImage", "pStatus"] )
    #  ctypes.c_int spinImageGetStatusDescription(ctypes.c_int status, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinImageGetStatusDescription", restype = ctypes.c_int,
            argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["status", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinImageRelease(spinImage hImage)
    addfunc(lib, "spinImageRelease", restype = ctypes.c_int,
            argtypes = [spinImage],
            argnames = ["hImage"] )
    #  ctypes.c_int spinImageHasCRC(spinImage hImage, ctypes.POINTER(bool8_t) pbHasCRC)
    addfunc(lib, "spinImageHasCRC", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(bool8_t)],
            argnames = ["hImage", "pbHasCRC"] )
    #  ctypes.c_int spinImageCheckCRC(spinImage hImage, ctypes.POINTER(bool8_t) pbCheckCRC)
    addfunc(lib, "spinImageCheckCRC", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(bool8_t)],
            argnames = ["hImage", "pbCheckCRC"] )
    #  ctypes.c_int spinImageGetBitsPerPixel(spinImage hImage, ctypes.POINTER(ctypes.c_size_t) pBitsPerPixel)
    addfunc(lib, "spinImageGetBitsPerPixel", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hImage", "pBitsPerPixel"] )
    #  ctypes.c_int spinImageGetSize(spinImage hImage, ctypes.POINTER(ctypes.c_size_t) pImageSize)
    addfunc(lib, "spinImageGetSize", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hImage", "pImageSize"] )
    #  ctypes.c_int spinImageGetStride(spinImage hImage, ctypes.POINTER(ctypes.c_size_t) pStride)
    addfunc(lib, "spinImageGetStride", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hImage", "pStride"] )
    #  ctypes.c_int spinImageProcessorCreate(ctypes.POINTER(spinImageProcessor) phImageProcessor)
    addfunc(lib, "spinImageProcessorCreate", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinImageProcessor)],
            argnames = ["phImageProcessor"] )
    #  ctypes.c_int spinImageProcessorDestroy(spinImageProcessor hImageProcessor)
    addfunc(lib, "spinImageProcessorDestroy", restype = ctypes.c_int,
            argtypes = [spinImageProcessor],
            argnames = ["hImageProcessor"] )
    #  ctypes.c_int spinImageProcessorSetColorProcessing(spinImageProcessor hImageProcessor, ctypes.c_int colorAlgorithm)
    addfunc(lib, "spinImageProcessorSetColorProcessing", restype = ctypes.c_int,
            argtypes = [spinImageProcessor, ctypes.c_int],
            argnames = ["hImageProcessor", "colorAlgorithm"] )
    #  ctypes.c_int spinImageProcessorGetColorProcessing(spinImageProcessor hImageProcessor, ctypes.POINTER(ctypes.c_int) pColorAlgorithm)
    addfunc(lib, "spinImageProcessorGetColorProcessing", restype = ctypes.c_int,
            argtypes = [spinImageProcessor, ctypes.POINTER(ctypes.c_int)],
            argnames = ["hImageProcessor", "pColorAlgorithm"] )
    #  ctypes.c_int spinImageProcessorSetNumDecompressionThreads(spinImageProcessor hImageProcessor, ctypes.c_uint numThreads)
    addfunc(lib, "spinImageProcessorSetNumDecompressionThreads", restype = ctypes.c_int,
            argtypes = [spinImageProcessor, ctypes.c_uint],
            argnames = ["hImageProcessor", "numThreads"] )
    #  ctypes.c_int spinImageProcessorGetNumDecompressionThreads(spinImageProcessor hImageProcessor, ctypes.POINTER(ctypes.c_uint) pNumThreads)
    addfunc(lib, "spinImageProcessorGetNumDecompressionThreads", restype = ctypes.c_int,
            argtypes = [spinImageProcessor, ctypes.POINTER(ctypes.c_uint)],
            argnames = ["hImageProcessor", "pNumThreads"] )
    #  ctypes.c_int spinImageProcessorConvert(spinImageProcessor hImageProcessor, spinImage hSrcImage, spinImage hDestImage, ctypes.c_int destFormat)
    addfunc(lib, "spinImageProcessorConvert", restype = ctypes.c_int,
            argtypes = [spinImageProcessor, spinImage, spinImage, ctypes.c_int],
            argnames = ["hImageProcessor", "hSrcImage", "hDestImage", "destFormat"] )
    #  ctypes.c_int spinImageProcessorConvertImageList(spinImageProcessor hImageProcessor, spinImageList hSrcImageList, spinImage hDestImage, ctypes.c_int destFormat)
    addfunc(lib, "spinImageProcessorConvertImageList", restype = ctypes.c_int,
            argtypes = [spinImageProcessor, spinImageList, spinImage, ctypes.c_int],
            argnames = ["hImageProcessor", "hSrcImageList", "hDestImage", "destFormat"] )
    #  ctypes.c_int spinImageProcessorApplyGamma(spinImageProcessor hImageProcessor, spinImage hSrcImage, spinImage hDestImage, ctypes.c_float gamma, bool8_t applyGammaInverse)
    addfunc(lib, "spinImageProcessorApplyGamma", restype = ctypes.c_int,
            argtypes = [spinImageProcessor, spinImage, spinImage, ctypes.c_float, bool8_t],
            argnames = ["hImageProcessor", "hSrcImage", "hDestImage", "gamma", "applyGammaInverse"] )
    #  ctypes.c_int spinDeviceEventHandlerCreate(ctypes.POINTER(spinDeviceEventHandler) phDeviceEventHandler, spinDeviceEventFunction pFunction, ctypes.c_void_p pUserData)
    addfunc(lib, "spinDeviceEventHandlerCreate", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinDeviceEventHandler), spinDeviceEventFunction, ctypes.c_void_p],
            argnames = ["phDeviceEventHandler", "pFunction", "pUserData"] )
    #  ctypes.c_int spinDeviceEventHandlerDestroy(spinDeviceEventHandler hDeviceEventHandler)
    addfunc(lib, "spinDeviceEventHandlerDestroy", restype = ctypes.c_int,
            argtypes = [spinDeviceEventHandler],
            argnames = ["hDeviceEventHandler"] )
    #  ctypes.c_int spinImageEventHandlerCreate(ctypes.POINTER(spinImageEventHandler) phImageEventHandler, spinImageEventFunction pFunction, ctypes.c_void_p pUserData)
    addfunc(lib, "spinImageEventHandlerCreate", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinImageEventHandler), spinImageEventFunction, ctypes.c_void_p],
            argnames = ["phImageEventHandler", "pFunction", "pUserData"] )
    #  ctypes.c_int spinImageEventHandlerDestroy(spinImageEventHandler hImageEventHandler)
    addfunc(lib, "spinImageEventHandlerDestroy", restype = ctypes.c_int,
            argtypes = [spinImageEventHandler],
            argnames = ["hImageEventHandler"] )
    #  ctypes.c_int spinImageListEventHandlerCreate(ctypes.POINTER(spinImageListEventHandler) phImageEventHandler, spinImageListEventFunction pFunction, ctypes.c_void_p pUserData)
    addfunc(lib, "spinImageListEventHandlerCreate", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinImageListEventHandler), spinImageListEventFunction, ctypes.c_void_p],
            argnames = ["phImageEventHandler", "pFunction", "pUserData"] )
    #  ctypes.c_int spinImageListEventHandlerDestroy(spinImageListEventHandler hImageListEventHandler)
    addfunc(lib, "spinImageListEventHandlerDestroy", restype = ctypes.c_int,
            argtypes = [spinImageListEventHandler],
            argnames = ["hImageListEventHandler"] )
    #  ctypes.c_int spinDeviceArrivalEventHandlerCreate(ctypes.POINTER(spinDeviceArrivalEventHandler) phDeviceArrivalEventHandler, spinArrivalEventFunction pFunction, ctypes.c_void_p pUserData)
    addfunc(lib, "spinDeviceArrivalEventHandlerCreate", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinDeviceArrivalEventHandler), spinArrivalEventFunction, ctypes.c_void_p],
            argnames = ["phDeviceArrivalEventHandler", "pFunction", "pUserData"] )
    #  ctypes.c_int spinDeviceArrivalEventHandlerDestroy(spinDeviceArrivalEventHandler hDeviceArrivalEventHandler)
    addfunc(lib, "spinDeviceArrivalEventHandlerDestroy", restype = ctypes.c_int,
            argtypes = [spinDeviceArrivalEventHandler],
            argnames = ["hDeviceArrivalEventHandler"] )
    #  ctypes.c_int spinDeviceRemovalEventHandlerCreate(ctypes.POINTER(spinDeviceRemovalEventHandler) phDeviceRemovalEventHandler, spinRemovalEventFunction pFunction, ctypes.c_void_p pUserData)
    addfunc(lib, "spinDeviceRemovalEventHandlerCreate", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinDeviceRemovalEventHandler), spinRemovalEventFunction, ctypes.c_void_p],
            argnames = ["phDeviceRemovalEventHandler", "pFunction", "pUserData"] )
    #  ctypes.c_int spinDeviceRemovalEventHandlerDestroy(spinDeviceRemovalEventHandler hDeviceRemovalEventHandler)
    addfunc(lib, "spinDeviceRemovalEventHandlerDestroy", restype = ctypes.c_int,
            argtypes = [spinDeviceRemovalEventHandler],
            argnames = ["hDeviceRemovalEventHandler"] )
    #  ctypes.c_int spinInterfaceEventHandlerCreate(ctypes.POINTER(spinInterfaceEventHandler) phInterfaceEventHandler, spinArrivalEventFunction pArrivalFunction, spinRemovalEventFunction pRemovalFunction, ctypes.c_void_p pUserData)
    addfunc(lib, "spinInterfaceEventHandlerCreate", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinInterfaceEventHandler), spinArrivalEventFunction, spinRemovalEventFunction, ctypes.c_void_p],
            argnames = ["phInterfaceEventHandler", "pArrivalFunction", "pRemovalFunction", "pUserData"] )
    #  ctypes.c_int spinInterfaceEventHandlerDestroy(spinInterfaceEventHandler hInterfaceEventHandler)
    addfunc(lib, "spinInterfaceEventHandlerDestroy", restype = ctypes.c_int,
            argtypes = [spinInterfaceEventHandler],
            argnames = ["hInterfaceEventHandler"] )
    #  ctypes.c_int spinLogEventHandlerCreate(ctypes.POINTER(spinLogEventHandler) phLogEventHandler, spinLogEventFunction pFunction, ctypes.c_void_p pUserData)
    addfunc(lib, "spinLogEventHandlerCreate", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinLogEventHandler), spinLogEventFunction, ctypes.c_void_p],
            argnames = ["phLogEventHandler", "pFunction", "pUserData"] )
    #  ctypes.c_int spinLogEventHandlerDestroy(spinLogEventHandler hLogEventHandler)
    addfunc(lib, "spinLogEventHandlerDestroy", restype = ctypes.c_int,
            argtypes = [spinLogEventHandler],
            argnames = ["hLogEventHandler"] )
    #  ctypes.c_int spinImageStatisticsCreate(ctypes.POINTER(spinImageStatistics) phStatistics)
    addfunc(lib, "spinImageStatisticsCreate", restype = ctypes.c_int,
            argtypes = [ctypes.POINTER(spinImageStatistics)],
            argnames = ["phStatistics"] )
    #  ctypes.c_int spinImageStatisticsDestroy(spinImageStatistics hStatistics)
    addfunc(lib, "spinImageStatisticsDestroy", restype = ctypes.c_int,
            argtypes = [spinImageStatistics],
            argnames = ["hStatistics"] )
    #  ctypes.c_int spinImageStatisticsEnableAll(spinImageStatistics hStatistics)
    addfunc(lib, "spinImageStatisticsEnableAll", restype = ctypes.c_int,
            argtypes = [spinImageStatistics],
            argnames = ["hStatistics"] )
    #  ctypes.c_int spinImageStatisticsDisableAll(spinImageStatistics hStatistics)
    addfunc(lib, "spinImageStatisticsDisableAll", restype = ctypes.c_int,
            argtypes = [spinImageStatistics],
            argnames = ["hStatistics"] )
    #  ctypes.c_int spinImageStatisticsEnableGreyOnly(spinImageStatistics hStatistics)
    addfunc(lib, "spinImageStatisticsEnableGreyOnly", restype = ctypes.c_int,
            argtypes = [spinImageStatistics],
            argnames = ["hStatistics"] )
    #  ctypes.c_int spinImageStatisticsEnableRgbOnly(spinImageStatistics hStatistics)
    addfunc(lib, "spinImageStatisticsEnableRgbOnly", restype = ctypes.c_int,
            argtypes = [spinImageStatistics],
            argnames = ["hStatistics"] )
    #  ctypes.c_int spinImageStatisticsEnableHslOnly(spinImageStatistics hStatistics)
    addfunc(lib, "spinImageStatisticsEnableHslOnly", restype = ctypes.c_int,
            argtypes = [spinImageStatistics],
            argnames = ["hStatistics"] )
    #  ctypes.c_int spinImageStatisticsGetChannelStatus(spinImageStatistics hStatistics, ctypes.c_int channel, ctypes.POINTER(bool8_t) pbEnabled)
    addfunc(lib, "spinImageStatisticsGetChannelStatus", restype = ctypes.c_int,
            argtypes = [spinImageStatistics, ctypes.c_int, ctypes.POINTER(bool8_t)],
            argnames = ["hStatistics", "channel", "pbEnabled"] )
    #  ctypes.c_int spinImageStatisticsSetChannelStatus(spinImageStatistics hStatistics, ctypes.c_int channel, bool8_t bEnable)
    addfunc(lib, "spinImageStatisticsSetChannelStatus", restype = ctypes.c_int,
            argtypes = [spinImageStatistics, ctypes.c_int, bool8_t],
            argnames = ["hStatistics", "channel", "bEnable"] )
    #  ctypes.c_int spinImageStatisticsGetRange(spinImageStatistics hStatistics, ctypes.c_int channel, ctypes.POINTER(ctypes.c_uint) pMin, ctypes.POINTER(ctypes.c_uint) pMax)
    addfunc(lib, "spinImageStatisticsGetRange", restype = ctypes.c_int,
            argtypes = [spinImageStatistics, ctypes.c_int, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint)],
            argnames = ["hStatistics", "channel", "pMin", "pMax"] )
    #  ctypes.c_int spinImageStatisticsGetPixelValueRange(spinImageStatistics hStatistics, ctypes.c_int channel, ctypes.POINTER(ctypes.c_uint) pMin, ctypes.POINTER(ctypes.c_uint) pMax)
    addfunc(lib, "spinImageStatisticsGetPixelValueRange", restype = ctypes.c_int,
            argtypes = [spinImageStatistics, ctypes.c_int, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint)],
            argnames = ["hStatistics", "channel", "pMin", "pMax"] )
    #  ctypes.c_int spinImageStatisticsGetNumPixelValues(spinImageStatistics hStatistics, ctypes.c_int channel, ctypes.POINTER(ctypes.c_uint) pNumValues)
    addfunc(lib, "spinImageStatisticsGetNumPixelValues", restype = ctypes.c_int,
            argtypes = [spinImageStatistics, ctypes.c_int, ctypes.POINTER(ctypes.c_uint)],
            argnames = ["hStatistics", "channel", "pNumValues"] )
    #  ctypes.c_int spinImageStatisticsGetMean(spinImageStatistics hStatistics, ctypes.c_int channel, ctypes.POINTER(ctypes.c_float) pMean)
    addfunc(lib, "spinImageStatisticsGetMean", restype = ctypes.c_int,
            argtypes = [spinImageStatistics, ctypes.c_int, ctypes.POINTER(ctypes.c_float)],
            argnames = ["hStatistics", "channel", "pMean"] )
    #  ctypes.c_int spinImageStatisticsGetHistogram(spinImageStatistics hStatistics, ctypes.c_int channel, ctypes.POINTER(ctypes.POINTER(ctypes.c_int)) ppHistogram)
    addfunc(lib, "spinImageStatisticsGetHistogram", restype = ctypes.c_int,
            argtypes = [spinImageStatistics, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_int))],
            argnames = ["hStatistics", "channel", "ppHistogram"] )
    #  ctypes.c_int spinImageStatisticsGetAll(spinImageStatistics hStatistics, ctypes.c_int channel, ctypes.POINTER(ctypes.c_uint) pRangeMin, ctypes.POINTER(ctypes.c_uint) pRangeMax, ctypes.POINTER(ctypes.c_uint) pPixelValueMin, ctypes.POINTER(ctypes.c_uint) pPixelValueMax, ctypes.POINTER(ctypes.c_uint) pNumPixelValues, ctypes.POINTER(ctypes.c_float) pPixelValueMean, ctypes.POINTER(ctypes.POINTER(ctypes.c_int)) ppHistogram)
    addfunc(lib, "spinImageStatisticsGetAll", restype = ctypes.c_int,
            argtypes = [spinImageStatistics, ctypes.c_int, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.POINTER(ctypes.c_int))],
            argnames = ["hStatistics", "channel", "pRangeMin", "pRangeMax", "pPixelValueMin", "pPixelValueMax", "pNumPixelValues", "pPixelValueMean", "ppHistogram"] )
    #  ctypes.c_int spinLogDataGetCategoryName(spinLogEventData hLogEventData, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinLogDataGetCategoryName", restype = ctypes.c_int,
            argtypes = [spinLogEventData, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hLogEventData", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinLogDataGetPriority(spinLogEventData hLogEventData, ctypes.POINTER(ctypes.c_int64) pValue)
    addfunc(lib, "spinLogDataGetPriority", restype = ctypes.c_int,
            argtypes = [spinLogEventData, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["hLogEventData", "pValue"] )
    #  ctypes.c_int spinLogDataGetPriorityName(spinLogEventData hLogEventData, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinLogDataGetPriorityName", restype = ctypes.c_int,
            argtypes = [spinLogEventData, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hLogEventData", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinLogDataGetTimestamp(spinLogEventData hLogEventData, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinLogDataGetTimestamp", restype = ctypes.c_int,
            argtypes = [spinLogEventData, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hLogEventData", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinLogDataGetNDC(spinLogEventData hLogEventData, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinLogDataGetNDC", restype = ctypes.c_int,
            argtypes = [spinLogEventData, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hLogEventData", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinLogDataGetThreadName(spinLogEventData hLogEventData, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinLogDataGetThreadName", restype = ctypes.c_int,
            argtypes = [spinLogEventData, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hLogEventData", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinLogDataGetLogMessage(spinLogEventData hLogEventData, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinLogDataGetLogMessage", restype = ctypes.c_int,
            argtypes = [spinLogEventData, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hLogEventData", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinDeviceEventGetId(spinDeviceEventData hDeviceEventData, ctypes.POINTER(ctypes.c_uint64) pEventId)
    addfunc(lib, "spinDeviceEventGetId", restype = ctypes.c_int,
            argtypes = [spinDeviceEventData, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["hDeviceEventData", "pEventId"] )
    #  ctypes.c_int spinDeviceEventGetPayloadData(spinDeviceEventData hDeviceEventData, ctypes.POINTER(ctypes.c_uint8) pBuf, ctypes.POINTER(ctypes.c_size_t) pBufSize)
    addfunc(lib, "spinDeviceEventGetPayloadData", restype = ctypes.c_int,
            argtypes = [spinDeviceEventData, ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hDeviceEventData", "pBuf", "pBufSize"] )
    #  ctypes.c_int spinDeviceEventGetPayloadDataSize(spinDeviceEventData hDeviceEventData, ctypes.POINTER(ctypes.c_size_t) pBufSize)
    addfunc(lib, "spinDeviceEventGetPayloadDataSize", restype = ctypes.c_int,
            argtypes = [spinDeviceEventData, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hDeviceEventData", "pBufSize"] )
    #  ctypes.c_int spinDeviceEventGetName(spinDeviceEventData hDeviceEventData, ctypes.c_char_p pBuf, ctypes.POINTER(ctypes.c_size_t) pBufLen)
    addfunc(lib, "spinDeviceEventGetName", restype = ctypes.c_int,
            argtypes = [spinDeviceEventData, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["hDeviceEventData", "pBuf", "pBufLen"] )
    #  ctypes.c_int spinImageChunkDataGetIntValue(spinImage hImage, ctypes.c_char_p pName, ctypes.POINTER(ctypes.c_int64) pValue)
    addfunc(lib, "spinImageChunkDataGetIntValue", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["hImage", "pName", "pValue"] )
    #  ctypes.c_int spinImageChunkDataGetFloatValue(spinImage hImage, ctypes.c_char_p pName, ctypes.POINTER(ctypes.c_double) pValue)
    addfunc(lib, "spinImageChunkDataGetFloatValue", restype = ctypes.c_int,
            argtypes = [spinImage, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double)],
            argnames = ["hImage", "pName", "pValue"] )


