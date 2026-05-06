##########   This file is generated automatically based on peak_backend.h   ##########

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
PEAK_BOOL8=ctypes.c_int8
class PEAK_ACQUISITION_START_MODE_t(enum.IntEnum):
    PEAK_ACQUISITION_START_MODE_DEFAULT=_int32(0)
    PEAK_ACQUISITION_START_MODE_CUSTOM =_int32(1000)
dPEAK_ACQUISITION_START_MODE_t={a.name:a.value for a in PEAK_ACQUISITION_START_MODE_t}
drPEAK_ACQUISITION_START_MODE_t={a.value:a.name for a in PEAK_ACQUISITION_START_MODE_t}


PEAK_ACQUISITION_START_MODE=ctypes.c_int32
class PEAK_ACQUISITION_STOP_MODE_t(enum.IntEnum):
    PEAK_ACQUISITION_STOP_MODE_DEFAULT=_int32(0)
    PEAK_ACQUISITION_STOP_MODE_KILL   =enum.auto()
    PEAK_ACQUISITION_STOP_MODE_CUSTOM =_int32(1000)
dPEAK_ACQUISITION_STOP_MODE_t={a.name:a.value for a in PEAK_ACQUISITION_STOP_MODE_t}
drPEAK_ACQUISITION_STOP_MODE_t={a.value:a.name for a in PEAK_ACQUISITION_STOP_MODE_t}


PEAK_ACQUISITION_STOP_MODE=ctypes.c_int32
class PEAK_BUFFER_PART_TYPE_t(enum.IntEnum):
    PEAK_BUFFER_PART_TYPE_UNKNOWN             =_int32(0)
    PEAK_BUFFER_PART_TYPE_IMAGE_2D            =enum.auto()
    PEAK_BUFFER_PART_TYPE_PLANE_BI_PLANAR_2D  =enum.auto()
    PEAK_BUFFER_PART_TYPE_PLANE_TRI_PLANAR_2D =enum.auto()
    PEAK_BUFFER_PART_TYPE_PLANE_QUAD_PLANAR_2D=enum.auto()
    PEAK_BUFFER_PART_TYPE_IMAGE_3D            =enum.auto()
    PEAK_BUFFER_PART_TYPE_PLANE_BI_PLANAR_3D  =enum.auto()
    PEAK_BUFFER_PART_TYPE_PLANE_TRI_PLANAR_3D =enum.auto()
    PEAK_BUFFER_PART_TYPE_PLANE_QUAD_PLANAR_3D=enum.auto()
    PEAK_BUFFER_PART_TYPE_CONFIDENCE_MAP      =enum.auto()
    PEAK_BUFFER_PART_TYPE_CUSTOM              =_int32(1000)
dPEAK_BUFFER_PART_TYPE_t={a.name:a.value for a in PEAK_BUFFER_PART_TYPE_t}
drPEAK_BUFFER_PART_TYPE_t={a.value:a.name for a in PEAK_BUFFER_PART_TYPE_t}


PEAK_BUFFER_PART_TYPE=ctypes.c_int32
class PEAK_BUFFER_PAYLOAD_TYPE_t(enum.IntEnum):
    PEAK_BUFFER_PAYLOAD_TYPE_UNKNOWN        =_int32(0)
    PEAK_BUFFER_PAYLOAD_TYPE_IMAGE          =enum.auto()
    PEAK_BUFFER_PAYLOAD_TYPE_RAW_DATA       =enum.auto()
    PEAK_BUFFER_PAYLOAD_TYPE_FILE           =enum.auto()
    PEAK_BUFFER_PAYLOAD_TYPE_CHUNK          =enum.auto()
    PEAK_BUFFER_PAYLOAD_TYPE_JPEG           =enum.auto()
    PEAK_BUFFER_PAYLOAD_TYPE_JPEG_2000      =enum.auto()
    PEAK_BUFFER_PAYLOAD_TYPE_H264           =enum.auto()
    PEAK_BUFFER_PAYLOAD_TYPE_CHUNK_ONLY     =enum.auto()
    PEAK_BUFFER_PAYLOAD_TYPE_DEVICE_SPECIFIC=enum.auto()
    PEAK_BUFFER_PAYLOAD_TYPE_MULTI_PART     =enum.auto()
    PEAK_BUFFER_PAYLOAD_TYPE_CUSTOM         =_int32(1000)
dPEAK_BUFFER_PAYLOAD_TYPE_t={a.name:a.value for a in PEAK_BUFFER_PAYLOAD_TYPE_t}
drPEAK_BUFFER_PAYLOAD_TYPE_t={a.value:a.name for a in PEAK_BUFFER_PAYLOAD_TYPE_t}


PEAK_BUFFER_PAYLOAD_TYPE=ctypes.c_int32
class PEAK_CHARACTER_ENCODING_t(enum.IntEnum):
    PEAK_CHARACTER_ENCODING_ASCII=_int32(0)
    PEAK_CHARACTER_ENCODING_UTF8 =enum.auto()
dPEAK_CHARACTER_ENCODING_t={a.name:a.value for a in PEAK_CHARACTER_ENCODING_t}
drPEAK_CHARACTER_ENCODING_t={a.value:a.name for a in PEAK_CHARACTER_ENCODING_t}


PEAK_CHARACTER_ENCODING=ctypes.c_int32
class PEAK_DATA_STREAM_FLUSH_MODE_t(enum.IntEnum):
    PEAK_DATA_STREAM_FLUSH_MODE_INPUT_POOL_TO_OUTPUT_QUEUE=_int32(0)
    PEAK_DATA_STREAM_FLUSH_MODE_DISCARD_OUTPUT_QUEUE      =enum.auto()
    PEAK_DATA_STREAM_FLUSH_MODE_ALL_TO_INPUT_POOL         =enum.auto()
    PEAK_DATA_STREAM_FLUSH_MODE_UNQUEUED_TO_INPUT_POOL    =enum.auto()
    PEAK_DATA_STREAM_FLUSH_MODE_DISCARD_ALL               =enum.auto()
    PEAK_DATA_STREAM_FLUSH_MODE_CUSTOM                    =_int32(1000)
dPEAK_DATA_STREAM_FLUSH_MODE_t={a.name:a.value for a in PEAK_DATA_STREAM_FLUSH_MODE_t}
drPEAK_DATA_STREAM_FLUSH_MODE_t={a.value:a.name for a in PEAK_DATA_STREAM_FLUSH_MODE_t}


PEAK_DATA_STREAM_FLUSH_MODE=ctypes.c_int32
class PEAK_DEVICE_ACCESS_STATUS_t(enum.IntEnum):
    PEAK_DEVICE_ACCESS_STATUS_READ_WRITE     =_int32(1)
    PEAK_DEVICE_ACCESS_STATUS_READ_ONLY      =enum.auto()
    PEAK_DEVICE_ACCESS_STATUS_NO_ACCESS      =enum.auto()
    PEAK_DEVICE_ACCESS_STATUS_BUSY           =enum.auto()
    PEAK_DEVICE_ACCESS_STATUS_OPEN_READ_WRITE=enum.auto()
    PEAK_DEVICE_ACCESS_STATUS_OPEN_READ_ONLY =enum.auto()
    PEAK_DEVICE_ACCESS_STATUS_CUSTOM         =_int32(1000)
dPEAK_DEVICE_ACCESS_STATUS_t={a.name:a.value for a in PEAK_DEVICE_ACCESS_STATUS_t}
drPEAK_DEVICE_ACCESS_STATUS_t={a.value:a.name for a in PEAK_DEVICE_ACCESS_STATUS_t}


PEAK_DEVICE_ACCESS_STATUS=ctypes.c_int32
class PEAK_DEVICE_ACCESS_TYPE_t(enum.IntEnum):
    PEAK_DEVICE_ACCESS_TYPE_READ_ONLY=_int32(2)
    PEAK_DEVICE_ACCESS_TYPE_CONTROL  =enum.auto()
    PEAK_DEVICE_ACCESS_TYPE_EXCLUSIVE=enum.auto()
    PEAK_DEVICE_ACCESS_TYPE_CUSTOM   =_int32(1000)
dPEAK_DEVICE_ACCESS_TYPE_t={a.name:a.value for a in PEAK_DEVICE_ACCESS_TYPE_t}
drPEAK_DEVICE_ACCESS_TYPE_t={a.value:a.name for a in PEAK_DEVICE_ACCESS_TYPE_t}


PEAK_DEVICE_ACCESS_TYPE=ctypes.c_int32
class PEAK_DEVICE_INFORMATION_ROLE_t(enum.IntEnum):
    PEAK_DEVICE_INFORMATION_ROLE_ID                      =_int32(0)
    PEAK_DEVICE_INFORMATION_ROLE_VENDOR_NAME             =enum.auto()
    PEAK_DEVICE_INFORMATION_ROLE_MODEL_NAME              =enum.auto()
    PEAK_DEVICE_INFORMATION_ROLE_TL_TYPE                 =enum.auto()
    PEAK_DEVICE_INFORMATION_ROLE_DISPLAY_NAME            =enum.auto()
    PEAK_DEVICE_INFORMATION_ROLE_ACCESS_STATUS           =enum.auto()
    PEAK_DEVICE_INFORMATION_ROLE_USER_DEFINED_NAME       =enum.auto()
    PEAK_DEVICE_INFORMATION_ROLE_SERIAL_NUMBER           =enum.auto()
    PEAK_DEVICE_INFORMATION_ROLE_VERSION                 =enum.auto()
    PEAK_DEVICE_INFORMATION_ROLE_TIMESTAMP_TICK_FREQUENCY=enum.auto()
    PEAK_DEVICE_INFORMATION_ROLE_CUSTOM                  =_int32(1000)
dPEAK_DEVICE_INFORMATION_ROLE_t={a.name:a.value for a in PEAK_DEVICE_INFORMATION_ROLE_t}
drPEAK_DEVICE_INFORMATION_ROLE_t={a.value:a.name for a in PEAK_DEVICE_INFORMATION_ROLE_t}


PEAK_DEVICE_INFORMATION_ROLE=ctypes.c_int32
class PEAK_ENDIANNESS_t(enum.IntEnum):
    PEAK_ENDIANNESS_UNKNOWN=_int32(0)
    PEAK_ENDIANNESS_LITTLE =enum.auto()
    PEAK_ENDIANNESS_BIG    =enum.auto()
dPEAK_ENDIANNESS_t={a.name:a.value for a in PEAK_ENDIANNESS_t}
drPEAK_ENDIANNESS_t={a.value:a.name for a in PEAK_ENDIANNESS_t}


PEAK_ENDIANNESS=ctypes.c_int32
class PEAK_EVENT_TYPE_t(enum.IntEnum):
    PEAK_EVENT_TYPE_ERROR             =_int32(0)
    PEAK_EVENT_TYPE_FEATURE_INVALIDATE=_int32(2)
    PEAK_EVENT_TYPE_FEATURE_CHANGE    =enum.auto()
    PEAK_EVENT_TYPE_REMOTE_DEVICE     =enum.auto()
    PEAK_EVENT_TYPE_MODULE            =enum.auto()
    PEAK_EVENT_TYPE_FEATURE_CUSTOM    =_int32(1000)
dPEAK_EVENT_TYPE_t={a.name:a.value for a in PEAK_EVENT_TYPE_t}
drPEAK_EVENT_TYPE_t={a.value:a.name for a in PEAK_EVENT_TYPE_t}


PEAK_EVENT_TYPE=ctypes.c_int32
class PEAK_FIRMWARE_UPDATE_PERSISTENCE_t(enum.IntEnum):
    PEAK_FIRMWARE_UPDATE_PERSISTENCE_NONE=_int32(0)
    PEAK_FIRMWARE_UPDATE_PERSISTENCE_FULL=enum.auto()
dPEAK_FIRMWARE_UPDATE_PERSISTENCE_t={a.name:a.value for a in PEAK_FIRMWARE_UPDATE_PERSISTENCE_t}
drPEAK_FIRMWARE_UPDATE_PERSISTENCE_t={a.value:a.name for a in PEAK_FIRMWARE_UPDATE_PERSISTENCE_t}


PEAK_FIRMWARE_UPDATE_PERSISTENCE=ctypes.c_int32
class PEAK_FIRMWARE_UPDATE_STEP_t(enum.IntEnum):
    PEAK_FIRMWARE_UPDATE_STEP_CHECK_PRECONDITIONS=_int32(0)
    PEAK_FIRMWARE_UPDATE_STEP_ACQUIRE_UPDATE_DATA=enum.auto()
    PEAK_FIRMWARE_UPDATE_STEP_WRITE_FEATURE      =enum.auto()
    PEAK_FIRMWARE_UPDATE_STEP_EXECUTE_FEATURE    =enum.auto()
    PEAK_FIRMWARE_UPDATE_STEP_ASSERT_FEATURE     =enum.auto()
    PEAK_FIRMWARE_UPDATE_STEP_UPLOAD_FILE        =enum.auto()
    PEAK_FIRMWARE_UPDATE_STEP_RESET_DEVICE       =enum.auto()
dPEAK_FIRMWARE_UPDATE_STEP_t={a.name:a.value for a in PEAK_FIRMWARE_UPDATE_STEP_t}
drPEAK_FIRMWARE_UPDATE_STEP_t={a.value:a.name for a in PEAK_FIRMWARE_UPDATE_STEP_t}


PEAK_FIRMWARE_UPDATE_STEP=ctypes.c_int32
class PEAK_FIRMWARE_UPDATE_VERSION_STYLE_t(enum.IntEnum):
    PEAK_FIRMWARE_UPDATE_VERSION_STYLE_DOTTED  =_int32(0)
    PEAK_FIRMWARE_UPDATE_VERSION_STYLE_SEMANTIC=enum.auto()
dPEAK_FIRMWARE_UPDATE_VERSION_STYLE_t={a.name:a.value for a in PEAK_FIRMWARE_UPDATE_VERSION_STYLE_t}
drPEAK_FIRMWARE_UPDATE_VERSION_STYLE_t={a.value:a.name for a in PEAK_FIRMWARE_UPDATE_VERSION_STYLE_t}


PEAK_FIRMWARE_UPDATE_VERSION_STYLE=ctypes.c_int32
class PEAK_NODE_ACCESS_STATUS_t(enum.IntEnum):
    PEAK_NODE_ACCESS_STATUS_NOT_IMPLEMENTED=_int32(0)
    PEAK_NODE_ACCESS_STATUS_NOT_AVAILABLE  =enum.auto()
    PEAK_NODE_ACCESS_STATUS_WRITE_ONLY     =enum.auto()
    PEAK_NODE_ACCESS_STATUS_READ_ONLY      =enum.auto()
    PEAK_NODE_ACCESS_STATUS_READ_WRITE     =enum.auto()
dPEAK_NODE_ACCESS_STATUS_t={a.name:a.value for a in PEAK_NODE_ACCESS_STATUS_t}
drPEAK_NODE_ACCESS_STATUS_t={a.value:a.name for a in PEAK_NODE_ACCESS_STATUS_t}


PEAK_NODE_ACCESS_STATUS=ctypes.c_int32
class PEAK_NODE_CACHING_MODE_t(enum.IntEnum):
    PEAK_NODE_CACHING_MODE_NO_CACHE     =_int32(0)
    PEAK_NODE_CACHING_MODE_WRITE_THROUGH=enum.auto()
    PEAK_NODE_CACHING_MODE_WRITE_AROUND =enum.auto()
dPEAK_NODE_CACHING_MODE_t={a.name:a.value for a in PEAK_NODE_CACHING_MODE_t}
drPEAK_NODE_CACHING_MODE_t={a.value:a.name for a in PEAK_NODE_CACHING_MODE_t}


PEAK_NODE_CACHING_MODE=ctypes.c_int32
class PEAK_NODE_CACHE_USE_POLICY_t(enum.IntEnum):
    PEAK_NODE_CACHE_USE_POLICY_USE_CACHE   =_int32(0)
    PEAK_NODE_CACHE_USE_POLICY_IGNORE_CACHE=enum.auto()
dPEAK_NODE_CACHE_USE_POLICY_t={a.name:a.value for a in PEAK_NODE_CACHE_USE_POLICY_t}
drPEAK_NODE_CACHE_USE_POLICY_t={a.value:a.name for a in PEAK_NODE_CACHE_USE_POLICY_t}


PEAK_NODE_CACHE_USE_POLICY=ctypes.c_int32
class PEAK_NODE_DISPLAY_NOTATION_t(enum.IntEnum):
    PEAK_NODE_DISPLAY_NOTATION_AUTOMATIC =_int32(0)
    PEAK_NODE_DISPLAY_NOTATION_FIXED     =enum.auto()
    PEAK_NODE_DISPLAY_NOTATION_SCIENTIFIC=enum.auto()
dPEAK_NODE_DISPLAY_NOTATION_t={a.name:a.value for a in PEAK_NODE_DISPLAY_NOTATION_t}
drPEAK_NODE_DISPLAY_NOTATION_t={a.value:a.name for a in PEAK_NODE_DISPLAY_NOTATION_t}


PEAK_NODE_DISPLAY_NOTATION=ctypes.c_int32
class PEAK_NODE_INCREMENT_TYPE_t(enum.IntEnum):
    PEAK_NODE_INCREMENT_TYPE_NO_INCREMENT   =_int32(0)
    PEAK_NODE_INCREMENT_TYPE_FIXED_INCREMENT=enum.auto()
    PEAK_NODE_INCREMENT_TYPE_LIST_INCREMENT =enum.auto()
dPEAK_NODE_INCREMENT_TYPE_t={a.name:a.value for a in PEAK_NODE_INCREMENT_TYPE_t}
drPEAK_NODE_INCREMENT_TYPE_t={a.value:a.name for a in PEAK_NODE_INCREMENT_TYPE_t}


PEAK_NODE_INCREMENT_TYPE=ctypes.c_int32
class PEAK_NODE_NAMESPACE_t(enum.IntEnum):
    PEAK_NODE_NAMESPACE_CUSTOM  =_int32(0)
    PEAK_NODE_NAMESPACE_STANDARD=enum.auto()
dPEAK_NODE_NAMESPACE_t={a.name:a.value for a in PEAK_NODE_NAMESPACE_t}
drPEAK_NODE_NAMESPACE_t={a.value:a.name for a in PEAK_NODE_NAMESPACE_t}


PEAK_NODE_NAMESPACE=ctypes.c_int32
class PEAK_NODE_REPRESENTATION_t(enum.IntEnum):
    PEAK_NODE_REPRESENTATION_LINEAR     =_int32(0)
    PEAK_NODE_REPRESENTATION_LOGARITHMIC=enum.auto()
    PEAK_NODE_REPRESENTATION_BOOLEAN    =enum.auto()
    PEAK_NODE_REPRESENTATION_PURE_NUMBER=enum.auto()
    PEAK_NODE_REPRESENTATION_HEX_NUMBER =enum.auto()
    PEAK_NODE_REPRESENTATION_IP4_ADDRESS=enum.auto()
    PEAK_NODE_REPRESENTATION_MAC_ADDRESS=enum.auto()
dPEAK_NODE_REPRESENTATION_t={a.name:a.value for a in PEAK_NODE_REPRESENTATION_t}
drPEAK_NODE_REPRESENTATION_t={a.value:a.name for a in PEAK_NODE_REPRESENTATION_t}


PEAK_NODE_REPRESENTATION=ctypes.c_int32
class PEAK_NODE_TYPE_t(enum.IntEnum):
    PEAK_NODE_TYPE_INTEGER          =_int32(0)
    PEAK_NODE_TYPE_BOOLEAN          =enum.auto()
    PEAK_NODE_TYPE_COMMAND          =enum.auto()
    PEAK_NODE_TYPE_FLOAT            =enum.auto()
    PEAK_NODE_TYPE_STRING           =enum.auto()
    PEAK_NODE_TYPE_REGISTER         =enum.auto()
    PEAK_NODE_TYPE_CATEGORY         =enum.auto()
    PEAK_NODE_TYPE_ENUMERATION      =enum.auto()
    PEAK_NODE_TYPE_ENUMERATION_ENTRY=enum.auto()
dPEAK_NODE_TYPE_t={a.name:a.value for a in PEAK_NODE_TYPE_t}
drPEAK_NODE_TYPE_t={a.value:a.name for a in PEAK_NODE_TYPE_t}


PEAK_NODE_TYPE=ctypes.c_int32
class PEAK_NODE_VISIBILITY_t(enum.IntEnum):
    PEAK_NODE_VISIBILITY_BEGINNER =_int32(0)
    PEAK_NODE_VISIBILITY_EXPERT   =enum.auto()
    PEAK_NODE_VISIBILITY_GURU     =enum.auto()
    PEAK_NODE_VISIBILITY_INVISIBLE=enum.auto()
dPEAK_NODE_VISIBILITY_t={a.name:a.value for a in PEAK_NODE_VISIBILITY_t}
drPEAK_NODE_VISIBILITY_t={a.value:a.name for a in PEAK_NODE_VISIBILITY_t}


PEAK_NODE_VISIBILITY=ctypes.c_int32
class PEAK_PIXEL_FORMAT_NAMESPACE_t(enum.IntEnum):
    PEAK_PIXEL_FORMAT_NAMESPACE_GEV        =_int32(1)
    PEAK_PIXEL_FORMAT_NAMESPACE_IIDC       =enum.auto()
    PEAK_PIXEL_FORMAT_NAMESPACE_PFNC_16_BIT=enum.auto()
    PEAK_PIXEL_FORMAT_NAMESPACE_PFNC_32_BIT=enum.auto()
    PEAK_PIXEL_FORMAT_NAMESPACE_CUSTOM     =_int32(1000)
dPEAK_PIXEL_FORMAT_NAMESPACE_t={a.name:a.value for a in PEAK_PIXEL_FORMAT_NAMESPACE_t}
drPEAK_PIXEL_FORMAT_NAMESPACE_t={a.value:a.name for a in PEAK_PIXEL_FORMAT_NAMESPACE_t}


PEAK_PIXEL_FORMAT_NAMESPACE=ctypes.c_int32
class PEAK_PORT_URL_SCHEME_t(enum.IntEnum):
    PEAK_PORT_URL_SCHEME_LOCAL =_int32(0)
    PEAK_PORT_URL_SCHEME_HTTP  =enum.auto()
    PEAK_PORT_URL_SCHEME_FILE  =enum.auto()
    PEAK_PORT_URL_SCHEME_CUSTOM=_int32(1000)
dPEAK_PORT_URL_SCHEME_t={a.name:a.value for a in PEAK_PORT_URL_SCHEME_t}
drPEAK_PORT_URL_SCHEME_t={a.value:a.name for a in PEAK_PORT_URL_SCHEME_t}


PEAK_PORT_URL_SCHEME=ctypes.c_int32
class PEAK_RETURN_CODE_t(enum.IntEnum):
    PEAK_RETURN_CODE_SUCCESS          =_int32(0)
    PEAK_RETURN_CODE_ERROR            =enum.auto()
    PEAK_RETURN_CODE_NOT_INITIALIZED  =enum.auto()
    PEAK_RETURN_CODE_ABORTED          =enum.auto()
    PEAK_RETURN_CODE_BAD_ACCESS       =enum.auto()
    PEAK_RETURN_CODE_BAD_ALLOC        =enum.auto()
    PEAK_RETURN_CODE_BUFFER_TOO_SMALL =enum.auto()
    PEAK_RETURN_CODE_INVALID_ADDRESS  =enum.auto()
    PEAK_RETURN_CODE_INVALID_ARGUMENT =enum.auto()
    PEAK_RETURN_CODE_INVALID_CAST     =enum.auto()
    PEAK_RETURN_CODE_INVALID_HANDLE   =enum.auto()
    PEAK_RETURN_CODE_NOT_FOUND        =enum.auto()
    PEAK_RETURN_CODE_OUT_OF_RANGE     =enum.auto()
    PEAK_RETURN_CODE_TIMEOUT          =enum.auto()
    PEAK_RETURN_CODE_NOT_AVAILABLE    =enum.auto()
    PEAK_RETURN_CODE_NOT_IMPLEMENTED  =enum.auto()
    PEAK_RETURN_CODE_CTI_LOADING_ERROR=enum.auto()
dPEAK_RETURN_CODE_t={a.name:a.value for a in PEAK_RETURN_CODE_t}
drPEAK_RETURN_CODE_t={a.value:a.name for a in PEAK_RETURN_CODE_t}


PEAK_RETURN_CODE=ctypes.c_int32
PEAK_PRODUCER_LIBRARY_HANDLE=ctypes.c_void_p
PEAK_SYSTEM_DESCRIPTOR_HANDLE=ctypes.c_void_p
PEAK_SYSTEM_HANDLE=ctypes.c_void_p
PEAK_INTERFACE_DESCRIPTOR_HANDLE=ctypes.c_void_p
PEAK_INTERFACE_HANDLE=ctypes.c_void_p
PEAK_DEVICE_DESCRIPTOR_HANDLE=ctypes.c_void_p
PEAK_DEVICE_HANDLE=ctypes.c_void_p
PEAK_REMOTE_DEVICE_HANDLE=ctypes.c_void_p
PEAK_DATA_STREAM_DESCRIPTOR_HANDLE=ctypes.c_void_p
PEAK_DATA_STREAM_HANDLE=ctypes.c_void_p
PEAK_BUFFER_HANDLE=ctypes.c_void_p
PEAK_BUFFER_CHUNK_HANDLE=ctypes.c_void_p
PEAK_BUFFER_PART_HANDLE=ctypes.c_void_p
PEAK_MODULE_DESCRIPTOR_HANDLE=ctypes.c_void_p
PEAK_MODULE_HANDLE=ctypes.c_void_p
PEAK_NODE_MAP_HANDLE=ctypes.c_void_p
PEAK_NODE_HANDLE=ctypes.c_void_p
PEAK_INTEGER_NODE_HANDLE=ctypes.c_void_p
PEAK_BOOLEAN_NODE_HANDLE=ctypes.c_void_p
PEAK_COMMAND_NODE_HANDLE=ctypes.c_void_p
PEAK_FLOAT_NODE_HANDLE=ctypes.c_void_p
PEAK_STRING_NODE_HANDLE=ctypes.c_void_p
PEAK_REGISTER_NODE_HANDLE=ctypes.c_void_p
PEAK_CATEGORY_NODE_HANDLE=ctypes.c_void_p
PEAK_ENUMERATION_NODE_HANDLE=ctypes.c_void_p
PEAK_ENUMERATION_ENTRY_NODE_HANDLE=ctypes.c_void_p
PEAK_PORT_HANDLE=ctypes.c_void_p
PEAK_PORT_URL_HANDLE=ctypes.c_void_p
PEAK_EVENT_SUPPORTING_MODULE_HANDLE=ctypes.c_void_p
PEAK_EVENT_CONTROLLER_HANDLE=ctypes.c_void_p
PEAK_EVENT_HANDLE=ctypes.c_void_p
PEAK_FIRMWARE_UPDATER_HANDLE=ctypes.c_void_p
PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE=ctypes.c_void_p
PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE=ctypes.c_void_p
PEAK_INTERFACE_FOUND_CALLBACK=ctypes.c_void_p
PEAK_INTERFACE_LOST_CALLBACK=ctypes.c_void_p
PEAK_INTERFACE_FOUND_CALLBACK_HANDLE=ctypes.POINTER(PEAK_INTERFACE_FOUND_CALLBACK)
PEAK_INTERFACE_LOST_CALLBACK_HANDLE=ctypes.POINTER(PEAK_INTERFACE_LOST_CALLBACK)
PEAK_DEVICE_FOUND_CALLBACK=ctypes.c_void_p
PEAK_DEVICE_LOST_CALLBACK=ctypes.c_void_p
PEAK_DEVICE_FOUND_CALLBACK_HANDLE=ctypes.POINTER(PEAK_DEVICE_FOUND_CALLBACK)
PEAK_DEVICE_LOST_CALLBACK_HANDLE=ctypes.POINTER(PEAK_DEVICE_LOST_CALLBACK)
PEAK_BUFFER_REVOCATION_CALLBACK=ctypes.c_void_p
PEAK_NODE_CHANGED_CALLBACK=ctypes.c_void_p
PEAK_NODE_CHANGED_CALLBACK_HANDLE=ctypes.POINTER(PEAK_NODE_CHANGED_CALLBACK)
PEAK_DEVICE_DESCRIPTOR_INFORMATION_CHANGED_CALLBACK=ctypes.c_void_p
PEAK_DEVICE_DESCRIPTOR_INFORMATION_CHANGED_CALLBACK_HANDLE=ctypes.POINTER(PEAK_DEVICE_DESCRIPTOR_INFORMATION_CHANGED_CALLBACK)
PEAK_FIRMWARE_UPDATE_STARTED_CALLBACK=ctypes.c_void_p
PEAK_FIRMWARE_UPDATE_STARTED_CALLBACK_HANDLE=ctypes.POINTER(PEAK_FIRMWARE_UPDATE_STARTED_CALLBACK)
PEAK_FIRMWARE_UPDATE_STEP_STARTED_CALLBACK=ctypes.c_void_p
PEAK_FIRMWARE_UPDATE_STEP_STARTED_CALLBACK_HANDLE=ctypes.POINTER(PEAK_FIRMWARE_UPDATE_STEP_STARTED_CALLBACK)
PEAK_FIRMWARE_UPDATE_STEP_PROGRESS_CHANGED_CALLBACK=ctypes.c_void_p
PEAK_FIRMWARE_UPDATE_STEP_PROGRESS_CHANGED_CALLBACK_HANDLE=ctypes.POINTER(PEAK_FIRMWARE_UPDATE_STEP_PROGRESS_CHANGED_CALLBACK)
PEAK_FIRMWARE_UPDATE_STEP_FINISHED_CALLBACK=ctypes.c_void_p
PEAK_FIRMWARE_UPDATE_STEP_FINISHED_CALLBACK_HANDLE=ctypes.POINTER(PEAK_FIRMWARE_UPDATE_STEP_FINISHED_CALLBACK)
PEAK_FIRMWARE_UPDATE_FINISHED_CALLBACK=ctypes.c_void_p
PEAK_FIRMWARE_UPDATE_FINISHED_CALLBACK_HANDLE=ctypes.POINTER(PEAK_FIRMWARE_UPDATE_FINISHED_CALLBACK)
PEAK_FIRMWARE_UPDATE_FAILED_CALLBACK=ctypes.c_void_p
PEAK_FIRMWARE_UPDATE_FAILED_CALLBACK_HANDLE=ctypes.POINTER(PEAK_FIRMWARE_UPDATE_FAILED_CALLBACK)



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
    #  PEAK_RETURN_CODE PEAK_Library_Initialize()
    addfunc(lib, "PEAK_Library_Initialize", restype = PEAK_RETURN_CODE,
            argtypes = [],
            argnames = [] )
    #  PEAK_RETURN_CODE PEAK_Library_Close()
    addfunc(lib, "PEAK_Library_Close", restype = PEAK_RETURN_CODE,
            argtypes = [],
            argnames = [] )
    #  PEAK_RETURN_CODE PEAK_Library_IsInitialized(ctypes.POINTER(PEAK_BOOL8) isInitialized)
    addfunc(lib, "PEAK_Library_IsInitialized", restype = PEAK_RETURN_CODE,
            argtypes = [ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["isInitialized"] )
    #  PEAK_RETURN_CODE PEAK_Library_GetVersionMajor(ctypes.POINTER(ctypes.c_uint32) libraryVersionMajor)
    addfunc(lib, "PEAK_Library_GetVersionMajor", restype = PEAK_RETURN_CODE,
            argtypes = [ctypes.POINTER(ctypes.c_uint32)],
            argnames = ["libraryVersionMajor"] )
    #  PEAK_RETURN_CODE PEAK_Library_GetVersionMinor(ctypes.POINTER(ctypes.c_uint32) libraryVersionMinor)
    addfunc(lib, "PEAK_Library_GetVersionMinor", restype = PEAK_RETURN_CODE,
            argtypes = [ctypes.POINTER(ctypes.c_uint32)],
            argnames = ["libraryVersionMinor"] )
    #  PEAK_RETURN_CODE PEAK_Library_GetVersionSubminor(ctypes.POINTER(ctypes.c_uint32) libraryVersionSubminor)
    addfunc(lib, "PEAK_Library_GetVersionSubminor", restype = PEAK_RETURN_CODE,
            argtypes = [ctypes.POINTER(ctypes.c_uint32)],
            argnames = ["libraryVersionSubminor"] )
    #  PEAK_RETURN_CODE PEAK_Library_GetLastError(ctypes.POINTER(PEAK_RETURN_CODE) lastErrorCode, ctypes.c_char_p lastErrorDescription, ctypes.POINTER(ctypes.c_size_t) lastErrorDescriptionSize)
    addfunc(lib, "PEAK_Library_GetLastError", restype = PEAK_RETURN_CODE,
            argtypes = [ctypes.POINTER(PEAK_RETURN_CODE), ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["lastErrorCode", "lastErrorDescription", "lastErrorDescriptionSize"] )
    #  PEAK_RETURN_CODE PEAK_EnvironmentInspector_UpdateCTIPaths()
    addfunc(lib, "PEAK_EnvironmentInspector_UpdateCTIPaths", restype = PEAK_RETURN_CODE,
            argtypes = [],
            argnames = [] )
    #  PEAK_RETURN_CODE PEAK_EnvironmentInspector_GetNumCTIPaths(ctypes.POINTER(ctypes.c_size_t) numCtiPaths)
    addfunc(lib, "PEAK_EnvironmentInspector_GetNumCTIPaths", restype = PEAK_RETURN_CODE,
            argtypes = [ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["numCtiPaths"] )
    #  PEAK_RETURN_CODE PEAK_EnvironmentInspector_GetCTIPath(ctypes.c_size_t index, ctypes.c_char_p ctiPath, ctypes.POINTER(ctypes.c_size_t) ctiPathSize)
    addfunc(lib, "PEAK_EnvironmentInspector_GetCTIPath", restype = PEAK_RETURN_CODE,
            argtypes = [ctypes.c_size_t, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["index", "ctiPath", "ctiPathSize"] )
    #  PEAK_RETURN_CODE PEAK_ProducerLibrary_Construct(ctypes.c_char_p ctiPath, ctypes.c_size_t ctiPathSize, ctypes.POINTER(PEAK_PRODUCER_LIBRARY_HANDLE) producerLibraryHandle)
    addfunc(lib, "PEAK_ProducerLibrary_Construct", restype = PEAK_RETURN_CODE,
            argtypes = [ctypes.c_char_p, ctypes.c_size_t, ctypes.POINTER(PEAK_PRODUCER_LIBRARY_HANDLE)],
            argnames = ["ctiPath", "ctiPathSize", "producerLibraryHandle"] )
    #  PEAK_RETURN_CODE PEAK_ProducerLibrary_GetKey(PEAK_PRODUCER_LIBRARY_HANDLE producerLibraryHandle, ctypes.c_char_p key, ctypes.POINTER(ctypes.c_size_t) keySize)
    addfunc(lib, "PEAK_ProducerLibrary_GetKey", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PRODUCER_LIBRARY_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["producerLibraryHandle", "key", "keySize"] )
    #  PEAK_RETURN_CODE PEAK_ProducerLibrary_GetSystem(PEAK_PRODUCER_LIBRARY_HANDLE producerLibraryHandle, ctypes.POINTER(PEAK_SYSTEM_DESCRIPTOR_HANDLE) systemDescriptorHandle)
    addfunc(lib, "PEAK_ProducerLibrary_GetSystem", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PRODUCER_LIBRARY_HANDLE, ctypes.POINTER(PEAK_SYSTEM_DESCRIPTOR_HANDLE)],
            argnames = ["producerLibraryHandle", "systemDescriptorHandle"] )
    #  PEAK_RETURN_CODE PEAK_ProducerLibrary_Destruct(PEAK_PRODUCER_LIBRARY_HANDLE producerLibraryHandle)
    addfunc(lib, "PEAK_ProducerLibrary_Destruct", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PRODUCER_LIBRARY_HANDLE],
            argnames = ["producerLibraryHandle"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_ToModuleDescriptor(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.POINTER(PEAK_MODULE_DESCRIPTOR_HANDLE) moduleDescriptorHandle)
    addfunc(lib, "PEAK_SystemDescriptor_ToModuleDescriptor", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.POINTER(PEAK_MODULE_DESCRIPTOR_HANDLE)],
            argnames = ["systemDescriptorHandle", "moduleDescriptorHandle"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_GetKey(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.c_char_p key, ctypes.POINTER(ctypes.c_size_t) keySize)
    addfunc(lib, "PEAK_SystemDescriptor_GetKey", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemDescriptorHandle", "key", "keySize"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_GetInfo(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.c_int32 infoCommand, ctypes.POINTER(ctypes.c_int32) infoDataType, ctypes.POINTER(ctypes.c_uint8) info, ctypes.POINTER(ctypes.c_size_t) infoSize)
    addfunc(lib, "PEAK_SystemDescriptor_GetInfo", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemDescriptorHandle", "infoCommand", "infoDataType", "info", "infoSize"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_GetDisplayName(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.c_char_p displayName, ctypes.POINTER(ctypes.c_size_t) displayNameSize)
    addfunc(lib, "PEAK_SystemDescriptor_GetDisplayName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemDescriptorHandle", "displayName", "displayNameSize"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_GetVendorName(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.c_char_p vendorName, ctypes.POINTER(ctypes.c_size_t) vendorNameSize)
    addfunc(lib, "PEAK_SystemDescriptor_GetVendorName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemDescriptorHandle", "vendorName", "vendorNameSize"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_GetModelName(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.c_char_p modelName, ctypes.POINTER(ctypes.c_size_t) modelNameSize)
    addfunc(lib, "PEAK_SystemDescriptor_GetModelName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemDescriptorHandle", "modelName", "modelNameSize"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_GetVersion(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.c_char_p version, ctypes.POINTER(ctypes.c_size_t) versionSize)
    addfunc(lib, "PEAK_SystemDescriptor_GetVersion", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemDescriptorHandle", "version", "versionSize"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_GetTLType(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.c_char_p tlType, ctypes.POINTER(ctypes.c_size_t) tlTypeSize)
    addfunc(lib, "PEAK_SystemDescriptor_GetTLType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemDescriptorHandle", "tlType", "tlTypeSize"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_GetCTIFileName(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.c_char_p ctiFileName, ctypes.POINTER(ctypes.c_size_t) ctiFileNameSize)
    addfunc(lib, "PEAK_SystemDescriptor_GetCTIFileName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemDescriptorHandle", "ctiFileName", "ctiFileNameSize"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_GetCTIFullPath(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.c_char_p ctiFullPath, ctypes.POINTER(ctypes.c_size_t) ctiFullPathSize)
    addfunc(lib, "PEAK_SystemDescriptor_GetCTIFullPath", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemDescriptorHandle", "ctiFullPath", "ctiFullPathSize"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_GetGenTLVersionMajor(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.POINTER(ctypes.c_uint32) gentlVersionMajor)
    addfunc(lib, "PEAK_SystemDescriptor_GetGenTLVersionMajor", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.POINTER(ctypes.c_uint32)],
            argnames = ["systemDescriptorHandle", "gentlVersionMajor"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_GetGenTLVersionMinor(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.POINTER(ctypes.c_uint32) gentlVersionMinor)
    addfunc(lib, "PEAK_SystemDescriptor_GetGenTLVersionMinor", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.POINTER(ctypes.c_uint32)],
            argnames = ["systemDescriptorHandle", "gentlVersionMinor"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_GetCharacterEncoding(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.POINTER(PEAK_CHARACTER_ENCODING) characterEncoding)
    addfunc(lib, "PEAK_SystemDescriptor_GetCharacterEncoding", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.POINTER(PEAK_CHARACTER_ENCODING)],
            argnames = ["systemDescriptorHandle", "characterEncoding"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_GetParentLibrary(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.POINTER(PEAK_PRODUCER_LIBRARY_HANDLE) producerLibraryHandle)
    addfunc(lib, "PEAK_SystemDescriptor_GetParentLibrary", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.POINTER(PEAK_PRODUCER_LIBRARY_HANDLE)],
            argnames = ["systemDescriptorHandle", "producerLibraryHandle"] )
    #  PEAK_RETURN_CODE PEAK_SystemDescriptor_OpenSystem(PEAK_SYSTEM_DESCRIPTOR_HANDLE systemDescriptorHandle, ctypes.POINTER(PEAK_SYSTEM_HANDLE) systemHandle)
    addfunc(lib, "PEAK_SystemDescriptor_OpenSystem", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_DESCRIPTOR_HANDLE, ctypes.POINTER(PEAK_SYSTEM_HANDLE)],
            argnames = ["systemDescriptorHandle", "systemHandle"] )
    #  PEAK_RETURN_CODE PEAK_System_ToModule(PEAK_SYSTEM_HANDLE systemHandle, ctypes.POINTER(PEAK_MODULE_HANDLE) moduleHandle)
    addfunc(lib, "PEAK_System_ToModule", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.POINTER(PEAK_MODULE_HANDLE)],
            argnames = ["systemHandle", "moduleHandle"] )
    #  PEAK_RETURN_CODE PEAK_System_ToEventSupportingModule(PEAK_SYSTEM_HANDLE systemHandle, ctypes.POINTER(PEAK_EVENT_SUPPORTING_MODULE_HANDLE) eventSupportingModuleHandle)
    addfunc(lib, "PEAK_System_ToEventSupportingModule", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.POINTER(PEAK_EVENT_SUPPORTING_MODULE_HANDLE)],
            argnames = ["systemHandle", "eventSupportingModuleHandle"] )
    #  PEAK_RETURN_CODE PEAK_System_GetKey(PEAK_SYSTEM_HANDLE systemHandle, ctypes.c_char_p key, ctypes.POINTER(ctypes.c_size_t) keySize)
    addfunc(lib, "PEAK_System_GetKey", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemHandle", "key", "keySize"] )
    #  PEAK_RETURN_CODE PEAK_System_GetInfo(PEAK_SYSTEM_HANDLE systemHandle, ctypes.c_int32 infoCommand, ctypes.POINTER(ctypes.c_int32) infoDataType, ctypes.POINTER(ctypes.c_uint8) info, ctypes.POINTER(ctypes.c_size_t) infoSize)
    addfunc(lib, "PEAK_System_GetInfo", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemHandle", "infoCommand", "infoDataType", "info", "infoSize"] )
    #  PEAK_RETURN_CODE PEAK_System_GetID(PEAK_SYSTEM_HANDLE systemHandle, ctypes.c_char_p id, ctypes.POINTER(ctypes.c_size_t) idSize)
    addfunc(lib, "PEAK_System_GetID", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemHandle", "id", "idSize"] )
    #  PEAK_RETURN_CODE PEAK_System_GetDisplayName(PEAK_SYSTEM_HANDLE systemHandle, ctypes.c_char_p displayName, ctypes.POINTER(ctypes.c_size_t) displayNameSize)
    addfunc(lib, "PEAK_System_GetDisplayName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemHandle", "displayName", "displayNameSize"] )
    #  PEAK_RETURN_CODE PEAK_System_GetVendorName(PEAK_SYSTEM_HANDLE systemHandle, ctypes.c_char_p vendorName, ctypes.POINTER(ctypes.c_size_t) vendorNameSize)
    addfunc(lib, "PEAK_System_GetVendorName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemHandle", "vendorName", "vendorNameSize"] )
    #  PEAK_RETURN_CODE PEAK_System_GetModelName(PEAK_SYSTEM_HANDLE systemHandle, ctypes.c_char_p modelName, ctypes.POINTER(ctypes.c_size_t) modelNameSize)
    addfunc(lib, "PEAK_System_GetModelName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemHandle", "modelName", "modelNameSize"] )
    #  PEAK_RETURN_CODE PEAK_System_GetVersion(PEAK_SYSTEM_HANDLE systemHandle, ctypes.c_char_p version, ctypes.POINTER(ctypes.c_size_t) versionSize)
    addfunc(lib, "PEAK_System_GetVersion", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemHandle", "version", "versionSize"] )
    #  PEAK_RETURN_CODE PEAK_System_GetTLType(PEAK_SYSTEM_HANDLE systemHandle, ctypes.c_char_p tlType, ctypes.POINTER(ctypes.c_size_t) tlTypeSize)
    addfunc(lib, "PEAK_System_GetTLType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemHandle", "tlType", "tlTypeSize"] )
    #  PEAK_RETURN_CODE PEAK_System_GetCTIFileName(PEAK_SYSTEM_HANDLE systemHandle, ctypes.c_char_p ctiFileName, ctypes.POINTER(ctypes.c_size_t) ctiFileNameSize)
    addfunc(lib, "PEAK_System_GetCTIFileName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemHandle", "ctiFileName", "ctiFileNameSize"] )
    #  PEAK_RETURN_CODE PEAK_System_GetCTIFullPath(PEAK_SYSTEM_HANDLE systemHandle, ctypes.c_char_p ctiFullPath, ctypes.POINTER(ctypes.c_size_t) ctiFullPathSize)
    addfunc(lib, "PEAK_System_GetCTIFullPath", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemHandle", "ctiFullPath", "ctiFullPathSize"] )
    #  PEAK_RETURN_CODE PEAK_System_GetGenTLVersionMajor(PEAK_SYSTEM_HANDLE systemHandle, ctypes.POINTER(ctypes.c_uint32) gentlVersionMajor)
    addfunc(lib, "PEAK_System_GetGenTLVersionMajor", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.POINTER(ctypes.c_uint32)],
            argnames = ["systemHandle", "gentlVersionMajor"] )
    #  PEAK_RETURN_CODE PEAK_System_GetGenTLVersionMinor(PEAK_SYSTEM_HANDLE systemHandle, ctypes.POINTER(ctypes.c_uint32) gentlVersionMinor)
    addfunc(lib, "PEAK_System_GetGenTLVersionMinor", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.POINTER(ctypes.c_uint32)],
            argnames = ["systemHandle", "gentlVersionMinor"] )
    #  PEAK_RETURN_CODE PEAK_System_GetCharacterEncoding(PEAK_SYSTEM_HANDLE systemHandle, ctypes.POINTER(PEAK_CHARACTER_ENCODING) characterEncoding)
    addfunc(lib, "PEAK_System_GetCharacterEncoding", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.POINTER(PEAK_CHARACTER_ENCODING)],
            argnames = ["systemHandle", "characterEncoding"] )
    #  PEAK_RETURN_CODE PEAK_System_GetParentLibrary(PEAK_SYSTEM_HANDLE systemHandle, ctypes.POINTER(PEAK_PRODUCER_LIBRARY_HANDLE) producerLibraryHandle)
    addfunc(lib, "PEAK_System_GetParentLibrary", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.POINTER(PEAK_PRODUCER_LIBRARY_HANDLE)],
            argnames = ["systemHandle", "producerLibraryHandle"] )
    #  PEAK_RETURN_CODE PEAK_System_UpdateInterfaces(PEAK_SYSTEM_HANDLE systemHandle, ctypes.c_uint64 timeout_ms)
    addfunc(lib, "PEAK_System_UpdateInterfaces", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.c_uint64],
            argnames = ["systemHandle", "timeout_ms"] )
    #  PEAK_RETURN_CODE PEAK_System_GetNumInterfaces(PEAK_SYSTEM_HANDLE systemHandle, ctypes.POINTER(ctypes.c_size_t) numInterfaces)
    addfunc(lib, "PEAK_System_GetNumInterfaces", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["systemHandle", "numInterfaces"] )
    #  PEAK_RETURN_CODE PEAK_System_GetInterface(PEAK_SYSTEM_HANDLE systemHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_INTERFACE_DESCRIPTOR_HANDLE) interfaceDescriptorHandle)
    addfunc(lib, "PEAK_System_GetInterface", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_INTERFACE_DESCRIPTOR_HANDLE)],
            argnames = ["systemHandle", "index", "interfaceDescriptorHandle"] )
    #  PEAK_RETURN_CODE PEAK_System_RegisterInterfaceFoundCallback(PEAK_SYSTEM_HANDLE systemHandle, PEAK_INTERFACE_FOUND_CALLBACK callback, ctypes.c_void_p callbackContext, ctypes.POINTER(PEAK_INTERFACE_FOUND_CALLBACK_HANDLE) callbackHandle)
    addfunc(lib, "PEAK_System_RegisterInterfaceFoundCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, PEAK_INTERFACE_FOUND_CALLBACK, ctypes.c_void_p, ctypes.POINTER(PEAK_INTERFACE_FOUND_CALLBACK_HANDLE)],
            argnames = ["systemHandle", "callback", "callbackContext", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_System_UnregisterInterfaceFoundCallback(PEAK_SYSTEM_HANDLE systemHandle, PEAK_INTERFACE_FOUND_CALLBACK_HANDLE callbackHandle)
    addfunc(lib, "PEAK_System_UnregisterInterfaceFoundCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, PEAK_INTERFACE_FOUND_CALLBACK_HANDLE],
            argnames = ["systemHandle", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_System_RegisterInterfaceLostCallback(PEAK_SYSTEM_HANDLE systemHandle, PEAK_INTERFACE_LOST_CALLBACK callback, ctypes.c_void_p callbackContext, ctypes.POINTER(PEAK_INTERFACE_LOST_CALLBACK_HANDLE) callbackHandle)
    addfunc(lib, "PEAK_System_RegisterInterfaceLostCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, PEAK_INTERFACE_LOST_CALLBACK, ctypes.c_void_p, ctypes.POINTER(PEAK_INTERFACE_LOST_CALLBACK_HANDLE)],
            argnames = ["systemHandle", "callback", "callbackContext", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_System_UnregisterInterfaceLostCallback(PEAK_SYSTEM_HANDLE systemHandle, PEAK_INTERFACE_LOST_CALLBACK_HANDLE callbackHandle)
    addfunc(lib, "PEAK_System_UnregisterInterfaceLostCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE, PEAK_INTERFACE_LOST_CALLBACK_HANDLE],
            argnames = ["systemHandle", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_System_Destruct(PEAK_SYSTEM_HANDLE systemHandle)
    addfunc(lib, "PEAK_System_Destruct", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_SYSTEM_HANDLE],
            argnames = ["systemHandle"] )
    #  PEAK_RETURN_CODE PEAK_InterfaceDescriptor_ToModuleDescriptor(PEAK_INTERFACE_DESCRIPTOR_HANDLE interfaceDescriptorHandle, ctypes.POINTER(PEAK_MODULE_DESCRIPTOR_HANDLE) moduleDescriptorHandle)
    addfunc(lib, "PEAK_InterfaceDescriptor_ToModuleDescriptor", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_DESCRIPTOR_HANDLE, ctypes.POINTER(PEAK_MODULE_DESCRIPTOR_HANDLE)],
            argnames = ["interfaceDescriptorHandle", "moduleDescriptorHandle"] )
    #  PEAK_RETURN_CODE PEAK_InterfaceDescriptor_GetKey(PEAK_INTERFACE_DESCRIPTOR_HANDLE interfaceDescriptorHandle, ctypes.c_char_p key, ctypes.POINTER(ctypes.c_size_t) keySize)
    addfunc(lib, "PEAK_InterfaceDescriptor_GetKey", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["interfaceDescriptorHandle", "key", "keySize"] )
    #  PEAK_RETURN_CODE PEAK_InterfaceDescriptor_GetInfo(PEAK_INTERFACE_DESCRIPTOR_HANDLE interfaceDescriptorHandle, ctypes.c_int32 infoCommand, ctypes.POINTER(ctypes.c_int32) infoDataType, ctypes.POINTER(ctypes.c_uint8) info, ctypes.POINTER(ctypes.c_size_t) infoSize)
    addfunc(lib, "PEAK_InterfaceDescriptor_GetInfo", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_DESCRIPTOR_HANDLE, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["interfaceDescriptorHandle", "infoCommand", "infoDataType", "info", "infoSize"] )
    #  PEAK_RETURN_CODE PEAK_InterfaceDescriptor_GetDisplayName(PEAK_INTERFACE_DESCRIPTOR_HANDLE interfaceDescriptorHandle, ctypes.c_char_p displayName, ctypes.POINTER(ctypes.c_size_t) displayNameSize)
    addfunc(lib, "PEAK_InterfaceDescriptor_GetDisplayName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["interfaceDescriptorHandle", "displayName", "displayNameSize"] )
    #  PEAK_RETURN_CODE PEAK_InterfaceDescriptor_GetTLType(PEAK_INTERFACE_DESCRIPTOR_HANDLE interfaceDescriptorHandle, ctypes.c_char_p tlType, ctypes.POINTER(ctypes.c_size_t) tlTypeSize)
    addfunc(lib, "PEAK_InterfaceDescriptor_GetTLType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["interfaceDescriptorHandle", "tlType", "tlTypeSize"] )
    #  PEAK_RETURN_CODE PEAK_InterfaceDescriptor_GetParentSystem(PEAK_INTERFACE_DESCRIPTOR_HANDLE interfaceDescriptorHandle, ctypes.POINTER(PEAK_SYSTEM_HANDLE) systemHandle)
    addfunc(lib, "PEAK_InterfaceDescriptor_GetParentSystem", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_DESCRIPTOR_HANDLE, ctypes.POINTER(PEAK_SYSTEM_HANDLE)],
            argnames = ["interfaceDescriptorHandle", "systemHandle"] )
    #  PEAK_RETURN_CODE PEAK_InterfaceDescriptor_OpenInterface(PEAK_INTERFACE_DESCRIPTOR_HANDLE interfaceDescriptorHandle, ctypes.POINTER(PEAK_INTERFACE_HANDLE) interfaceHandle)
    addfunc(lib, "PEAK_InterfaceDescriptor_OpenInterface", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_DESCRIPTOR_HANDLE, ctypes.POINTER(PEAK_INTERFACE_HANDLE)],
            argnames = ["interfaceDescriptorHandle", "interfaceHandle"] )
    #  PEAK_RETURN_CODE PEAK_Interface_ToModule(PEAK_INTERFACE_HANDLE interfaceHandle, ctypes.POINTER(PEAK_MODULE_HANDLE) moduleHandle)
    addfunc(lib, "PEAK_Interface_ToModule", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, ctypes.POINTER(PEAK_MODULE_HANDLE)],
            argnames = ["interfaceHandle", "moduleHandle"] )
    #  PEAK_RETURN_CODE PEAK_Interface_ToEventSupportingModule(PEAK_INTERFACE_HANDLE interfaceHandle, ctypes.POINTER(PEAK_EVENT_SUPPORTING_MODULE_HANDLE) eventSupportingModuleHandle)
    addfunc(lib, "PEAK_Interface_ToEventSupportingModule", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, ctypes.POINTER(PEAK_EVENT_SUPPORTING_MODULE_HANDLE)],
            argnames = ["interfaceHandle", "eventSupportingModuleHandle"] )
    #  PEAK_RETURN_CODE PEAK_Interface_GetKey(PEAK_INTERFACE_HANDLE interfaceHandle, ctypes.c_char_p key, ctypes.POINTER(ctypes.c_size_t) keySize)
    addfunc(lib, "PEAK_Interface_GetKey", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["interfaceHandle", "key", "keySize"] )
    #  PEAK_RETURN_CODE PEAK_Interface_GetInfo(PEAK_INTERFACE_HANDLE interfaceHandle, ctypes.c_int32 infoCommand, ctypes.POINTER(ctypes.c_int32) infoDataType, ctypes.POINTER(ctypes.c_uint8) info, ctypes.POINTER(ctypes.c_size_t) infoSize)
    addfunc(lib, "PEAK_Interface_GetInfo", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["interfaceHandle", "infoCommand", "infoDataType", "info", "infoSize"] )
    #  PEAK_RETURN_CODE PEAK_Interface_GetID(PEAK_INTERFACE_HANDLE interfaceHandle, ctypes.c_char_p id, ctypes.POINTER(ctypes.c_size_t) idSize)
    addfunc(lib, "PEAK_Interface_GetID", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["interfaceHandle", "id", "idSize"] )
    #  PEAK_RETURN_CODE PEAK_Interface_GetDisplayName(PEAK_INTERFACE_HANDLE interfaceHandle, ctypes.c_char_p displayName, ctypes.POINTER(ctypes.c_size_t) displayNameSize)
    addfunc(lib, "PEAK_Interface_GetDisplayName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["interfaceHandle", "displayName", "displayNameSize"] )
    #  PEAK_RETURN_CODE PEAK_Interface_GetTLType(PEAK_INTERFACE_HANDLE interfaceHandle, ctypes.c_char_p tlType, ctypes.POINTER(ctypes.c_size_t) tlTypeSize)
    addfunc(lib, "PEAK_Interface_GetTLType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["interfaceHandle", "tlType", "tlTypeSize"] )
    #  PEAK_RETURN_CODE PEAK_Interface_GetParentSystem(PEAK_INTERFACE_HANDLE interfaceHandle, ctypes.POINTER(PEAK_SYSTEM_HANDLE) systemHandle)
    addfunc(lib, "PEAK_Interface_GetParentSystem", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, ctypes.POINTER(PEAK_SYSTEM_HANDLE)],
            argnames = ["interfaceHandle", "systemHandle"] )
    #  PEAK_RETURN_CODE PEAK_Interface_UpdateDevices(PEAK_INTERFACE_HANDLE interfaceHandle, ctypes.c_uint64 timeout_ms)
    addfunc(lib, "PEAK_Interface_UpdateDevices", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, ctypes.c_uint64],
            argnames = ["interfaceHandle", "timeout_ms"] )
    #  PEAK_RETURN_CODE PEAK_Interface_GetNumDevices(PEAK_INTERFACE_HANDLE interfaceHandle, ctypes.POINTER(ctypes.c_size_t) numDevices)
    addfunc(lib, "PEAK_Interface_GetNumDevices", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["interfaceHandle", "numDevices"] )
    #  PEAK_RETURN_CODE PEAK_Interface_GetDevice(PEAK_INTERFACE_HANDLE interfaceHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_DEVICE_DESCRIPTOR_HANDLE) deviceDescriptorHandle)
    addfunc(lib, "PEAK_Interface_GetDevice", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_DEVICE_DESCRIPTOR_HANDLE)],
            argnames = ["interfaceHandle", "index", "deviceDescriptorHandle"] )
    #  PEAK_RETURN_CODE PEAK_Interface_RegisterDeviceFoundCallback(PEAK_INTERFACE_HANDLE interfaceHandle, PEAK_DEVICE_FOUND_CALLBACK callback, ctypes.c_void_p callbackContext, ctypes.POINTER(PEAK_DEVICE_FOUND_CALLBACK_HANDLE) callbackHandle)
    addfunc(lib, "PEAK_Interface_RegisterDeviceFoundCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, PEAK_DEVICE_FOUND_CALLBACK, ctypes.c_void_p, ctypes.POINTER(PEAK_DEVICE_FOUND_CALLBACK_HANDLE)],
            argnames = ["interfaceHandle", "callback", "callbackContext", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_Interface_UnregisterDeviceFoundCallback(PEAK_INTERFACE_HANDLE interfaceHandle, PEAK_DEVICE_FOUND_CALLBACK_HANDLE callbackHandle)
    addfunc(lib, "PEAK_Interface_UnregisterDeviceFoundCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, PEAK_DEVICE_FOUND_CALLBACK_HANDLE],
            argnames = ["interfaceHandle", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_Interface_RegisterDeviceLostCallback(PEAK_INTERFACE_HANDLE interfaceHandle, PEAK_DEVICE_LOST_CALLBACK callback, ctypes.c_void_p callbackContext, ctypes.POINTER(PEAK_DEVICE_LOST_CALLBACK_HANDLE) callbackHandle)
    addfunc(lib, "PEAK_Interface_RegisterDeviceLostCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, PEAK_DEVICE_LOST_CALLBACK, ctypes.c_void_p, ctypes.POINTER(PEAK_DEVICE_LOST_CALLBACK_HANDLE)],
            argnames = ["interfaceHandle", "callback", "callbackContext", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_Interface_UnregisterDeviceLostCallback(PEAK_INTERFACE_HANDLE interfaceHandle, PEAK_DEVICE_LOST_CALLBACK_HANDLE callbackHandle)
    addfunc(lib, "PEAK_Interface_UnregisterDeviceLostCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE, PEAK_DEVICE_LOST_CALLBACK_HANDLE],
            argnames = ["interfaceHandle", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_Interface_Destruct(PEAK_INTERFACE_HANDLE interfaceHandle)
    addfunc(lib, "PEAK_Interface_Destruct", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTERFACE_HANDLE],
            argnames = ["interfaceHandle"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_ToModuleDescriptor(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.POINTER(PEAK_MODULE_DESCRIPTOR_HANDLE) moduleDescriptorHandle)
    addfunc(lib, "PEAK_DeviceDescriptor_ToModuleDescriptor", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.POINTER(PEAK_MODULE_DESCRIPTOR_HANDLE)],
            argnames = ["deviceDescriptorHandle", "moduleDescriptorHandle"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetKey(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.c_char_p key, ctypes.POINTER(ctypes.c_size_t) keySize)
    addfunc(lib, "PEAK_DeviceDescriptor_GetKey", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceDescriptorHandle", "key", "keySize"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetInfo(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.c_int32 infoCommand, ctypes.POINTER(ctypes.c_int32) infoDataType, ctypes.POINTER(ctypes.c_uint8) info, ctypes.POINTER(ctypes.c_size_t) infoSize)
    addfunc(lib, "PEAK_DeviceDescriptor_GetInfo", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceDescriptorHandle", "infoCommand", "infoDataType", "info", "infoSize"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetDisplayName(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.c_char_p displayName, ctypes.POINTER(ctypes.c_size_t) displayNameSize)
    addfunc(lib, "PEAK_DeviceDescriptor_GetDisplayName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceDescriptorHandle", "displayName", "displayNameSize"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetVendorName(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.c_char_p vendorName, ctypes.POINTER(ctypes.c_size_t) vendorNameSize)
    addfunc(lib, "PEAK_DeviceDescriptor_GetVendorName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceDescriptorHandle", "vendorName", "vendorNameSize"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetModelName(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.c_char_p modelName, ctypes.POINTER(ctypes.c_size_t) modelNameSize)
    addfunc(lib, "PEAK_DeviceDescriptor_GetModelName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceDescriptorHandle", "modelName", "modelNameSize"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetVersion(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.c_char_p version, ctypes.POINTER(ctypes.c_size_t) versionSize)
    addfunc(lib, "PEAK_DeviceDescriptor_GetVersion", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceDescriptorHandle", "version", "versionSize"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetTLType(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.c_char_p tlType, ctypes.POINTER(ctypes.c_size_t) tlTypeSize)
    addfunc(lib, "PEAK_DeviceDescriptor_GetTLType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceDescriptorHandle", "tlType", "tlTypeSize"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetUserDefinedName(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.c_char_p userDefinedName, ctypes.POINTER(ctypes.c_size_t) userDefinedNameSize)
    addfunc(lib, "PEAK_DeviceDescriptor_GetUserDefinedName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceDescriptorHandle", "userDefinedName", "userDefinedNameSize"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetSerialNumber(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.c_char_p serialNumber, ctypes.POINTER(ctypes.c_size_t) serialNumberSize)
    addfunc(lib, "PEAK_DeviceDescriptor_GetSerialNumber", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceDescriptorHandle", "serialNumber", "serialNumberSize"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetAccessStatus(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.POINTER(PEAK_DEVICE_ACCESS_STATUS) accessStatus)
    addfunc(lib, "PEAK_DeviceDescriptor_GetAccessStatus", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.POINTER(PEAK_DEVICE_ACCESS_STATUS)],
            argnames = ["deviceDescriptorHandle", "accessStatus"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetTimestampTickFrequency(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.POINTER(ctypes.c_uint64) timestampTickFrequency)
    addfunc(lib, "PEAK_DeviceDescriptor_GetTimestampTickFrequency", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["deviceDescriptorHandle", "timestampTickFrequency"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetIsOpenableExclusive(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.POINTER(PEAK_BOOL8) isOpenable)
    addfunc(lib, "PEAK_DeviceDescriptor_GetIsOpenableExclusive", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["deviceDescriptorHandle", "isOpenable"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetIsOpenable(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, PEAK_DEVICE_ACCESS_TYPE accessType, ctypes.POINTER(PEAK_BOOL8) isOpenable)
    addfunc(lib, "PEAK_DeviceDescriptor_GetIsOpenable", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, PEAK_DEVICE_ACCESS_TYPE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["deviceDescriptorHandle", "accessType", "isOpenable"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_OpenDevice(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, PEAK_DEVICE_ACCESS_TYPE accessType, ctypes.POINTER(PEAK_DEVICE_HANDLE) deviceHandle)
    addfunc(lib, "PEAK_DeviceDescriptor_OpenDevice", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, PEAK_DEVICE_ACCESS_TYPE, ctypes.POINTER(PEAK_DEVICE_HANDLE)],
            argnames = ["deviceDescriptorHandle", "accessType", "deviceHandle"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetParentInterface(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.POINTER(PEAK_INTERFACE_HANDLE) interfaceHandle)
    addfunc(lib, "PEAK_DeviceDescriptor_GetParentInterface", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.POINTER(PEAK_INTERFACE_HANDLE)],
            argnames = ["deviceDescriptorHandle", "interfaceHandle"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_GetMonitoringUpdateInterval(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.POINTER(ctypes.c_uint64) monitoringUpdateInterval_ms)
    addfunc(lib, "PEAK_DeviceDescriptor_GetMonitoringUpdateInterval", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["deviceDescriptorHandle", "monitoringUpdateInterval_ms"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_SetMonitoringUpdateInterval(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, ctypes.c_uint64 monitoringUpdateInterval_ms)
    addfunc(lib, "PEAK_DeviceDescriptor_SetMonitoringUpdateInterval", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, ctypes.c_uint64],
            argnames = ["deviceDescriptorHandle", "monitoringUpdateInterval_ms"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_IsInformationRoleMonitored(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, PEAK_DEVICE_INFORMATION_ROLE informationRole, ctypes.POINTER(PEAK_BOOL8) isInformationRoleMonitored)
    addfunc(lib, "PEAK_DeviceDescriptor_IsInformationRoleMonitored", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, PEAK_DEVICE_INFORMATION_ROLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["deviceDescriptorHandle", "informationRole", "isInformationRoleMonitored"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_AddInformationRoleToMonitoring(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, PEAK_DEVICE_INFORMATION_ROLE informationRole)
    addfunc(lib, "PEAK_DeviceDescriptor_AddInformationRoleToMonitoring", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, PEAK_DEVICE_INFORMATION_ROLE],
            argnames = ["deviceDescriptorHandle", "informationRole"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_RemoveInformationRoleFromMonitoring(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, PEAK_DEVICE_INFORMATION_ROLE informationRole)
    addfunc(lib, "PEAK_DeviceDescriptor_RemoveInformationRoleFromMonitoring", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, PEAK_DEVICE_INFORMATION_ROLE],
            argnames = ["deviceDescriptorHandle", "informationRole"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_RegisterInformationChangedCallback(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, PEAK_DEVICE_DESCRIPTOR_INFORMATION_CHANGED_CALLBACK callback, ctypes.c_void_p callbackContext, ctypes.POINTER(PEAK_DEVICE_DESCRIPTOR_INFORMATION_CHANGED_CALLBACK_HANDLE) callbackHandle)
    addfunc(lib, "PEAK_DeviceDescriptor_RegisterInformationChangedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, PEAK_DEVICE_DESCRIPTOR_INFORMATION_CHANGED_CALLBACK, ctypes.c_void_p, ctypes.POINTER(PEAK_DEVICE_DESCRIPTOR_INFORMATION_CHANGED_CALLBACK_HANDLE)],
            argnames = ["deviceDescriptorHandle", "callback", "callbackContext", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_DeviceDescriptor_UnregisterInformationChangedCallback(PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, PEAK_DEVICE_DESCRIPTOR_INFORMATION_CHANGED_CALLBACK_HANDLE callbackHandle)
    addfunc(lib, "PEAK_DeviceDescriptor_UnregisterInformationChangedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_DESCRIPTOR_HANDLE, PEAK_DEVICE_DESCRIPTOR_INFORMATION_CHANGED_CALLBACK_HANDLE],
            argnames = ["deviceDescriptorHandle", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_Device_ToModule(PEAK_DEVICE_HANDLE deviceHandle, ctypes.POINTER(PEAK_MODULE_HANDLE) moduleHandle)
    addfunc(lib, "PEAK_Device_ToModule", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.POINTER(PEAK_MODULE_HANDLE)],
            argnames = ["deviceHandle", "moduleHandle"] )
    #  PEAK_RETURN_CODE PEAK_Device_ToEventSupportingModule(PEAK_DEVICE_HANDLE deviceHandle, ctypes.POINTER(PEAK_EVENT_SUPPORTING_MODULE_HANDLE) eventSupportingModuleHandle)
    addfunc(lib, "PEAK_Device_ToEventSupportingModule", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.POINTER(PEAK_EVENT_SUPPORTING_MODULE_HANDLE)],
            argnames = ["deviceHandle", "eventSupportingModuleHandle"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetKey(PEAK_DEVICE_HANDLE deviceHandle, ctypes.c_char_p key, ctypes.POINTER(ctypes.c_size_t) keySize)
    addfunc(lib, "PEAK_Device_GetKey", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceHandle", "key", "keySize"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetInfo(PEAK_DEVICE_HANDLE deviceHandle, ctypes.c_int32 infoCommand, ctypes.POINTER(ctypes.c_int32) infoDataType, ctypes.POINTER(ctypes.c_uint8) info, ctypes.POINTER(ctypes.c_size_t) infoSize)
    addfunc(lib, "PEAK_Device_GetInfo", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceHandle", "infoCommand", "infoDataType", "info", "infoSize"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetID(PEAK_DEVICE_HANDLE deviceHandle, ctypes.c_char_p id, ctypes.POINTER(ctypes.c_size_t) idSize)
    addfunc(lib, "PEAK_Device_GetID", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceHandle", "id", "idSize"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetDisplayName(PEAK_DEVICE_HANDLE deviceHandle, ctypes.c_char_p displayName, ctypes.POINTER(ctypes.c_size_t) displayNameSize)
    addfunc(lib, "PEAK_Device_GetDisplayName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceHandle", "displayName", "displayNameSize"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetVendorName(PEAK_DEVICE_HANDLE deviceHandle, ctypes.c_char_p vendorName, ctypes.POINTER(ctypes.c_size_t) vendorNameSize)
    addfunc(lib, "PEAK_Device_GetVendorName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceHandle", "vendorName", "vendorNameSize"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetModelName(PEAK_DEVICE_HANDLE deviceHandle, ctypes.c_char_p modelName, ctypes.POINTER(ctypes.c_size_t) modelNameSize)
    addfunc(lib, "PEAK_Device_GetModelName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceHandle", "modelName", "modelNameSize"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetVersion(PEAK_DEVICE_HANDLE deviceHandle, ctypes.c_char_p version, ctypes.POINTER(ctypes.c_size_t) versionSize)
    addfunc(lib, "PEAK_Device_GetVersion", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceHandle", "version", "versionSize"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetTLType(PEAK_DEVICE_HANDLE deviceHandle, ctypes.c_char_p tlType, ctypes.POINTER(ctypes.c_size_t) tlTypeSize)
    addfunc(lib, "PEAK_Device_GetTLType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceHandle", "tlType", "tlTypeSize"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetUserDefinedName(PEAK_DEVICE_HANDLE deviceHandle, ctypes.c_char_p userDefinedName, ctypes.POINTER(ctypes.c_size_t) userDefinedNameSize)
    addfunc(lib, "PEAK_Device_GetUserDefinedName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceHandle", "userDefinedName", "userDefinedNameSize"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetSerialNumber(PEAK_DEVICE_HANDLE deviceHandle, ctypes.c_char_p serialNumber, ctypes.POINTER(ctypes.c_size_t) serialNumberSize)
    addfunc(lib, "PEAK_Device_GetSerialNumber", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceHandle", "serialNumber", "serialNumberSize"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetAccessStatus(PEAK_DEVICE_HANDLE deviceHandle, ctypes.POINTER(PEAK_DEVICE_ACCESS_STATUS) accessStatus)
    addfunc(lib, "PEAK_Device_GetAccessStatus", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.POINTER(PEAK_DEVICE_ACCESS_STATUS)],
            argnames = ["deviceHandle", "accessStatus"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetTimestampTickFrequency(PEAK_DEVICE_HANDLE deviceHandle, ctypes.POINTER(ctypes.c_uint64) timestampTickFrequency)
    addfunc(lib, "PEAK_Device_GetTimestampTickFrequency", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["deviceHandle", "timestampTickFrequency"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetParentInterface(PEAK_DEVICE_HANDLE deviceHandle, ctypes.POINTER(PEAK_INTERFACE_HANDLE) interfaceHandle)
    addfunc(lib, "PEAK_Device_GetParentInterface", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.POINTER(PEAK_INTERFACE_HANDLE)],
            argnames = ["deviceHandle", "interfaceHandle"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetRemoteDevice(PEAK_DEVICE_HANDLE deviceHandle, ctypes.POINTER(PEAK_REMOTE_DEVICE_HANDLE) remoteDeviceHandle)
    addfunc(lib, "PEAK_Device_GetRemoteDevice", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.POINTER(PEAK_REMOTE_DEVICE_HANDLE)],
            argnames = ["deviceHandle", "remoteDeviceHandle"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetNumDataStreams(PEAK_DEVICE_HANDLE deviceHandle, ctypes.POINTER(ctypes.c_size_t) numDataStreams)
    addfunc(lib, "PEAK_Device_GetNumDataStreams", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["deviceHandle", "numDataStreams"] )
    #  PEAK_RETURN_CODE PEAK_Device_GetDataStream(PEAK_DEVICE_HANDLE deviceHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_DATA_STREAM_DESCRIPTOR_HANDLE) dataStreamDescriptorHandle)
    addfunc(lib, "PEAK_Device_GetDataStream", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_DATA_STREAM_DESCRIPTOR_HANDLE)],
            argnames = ["deviceHandle", "index", "dataStreamDescriptorHandle"] )
    #  PEAK_RETURN_CODE PEAK_Device_Destruct(PEAK_DEVICE_HANDLE deviceHandle)
    addfunc(lib, "PEAK_Device_Destruct", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DEVICE_HANDLE],
            argnames = ["deviceHandle"] )
    #  PEAK_RETURN_CODE PEAK_RemoteDevice_ToModule(PEAK_REMOTE_DEVICE_HANDLE remoteDeviceHandle, ctypes.POINTER(PEAK_MODULE_HANDLE) moduleHandle)
    addfunc(lib, "PEAK_RemoteDevice_ToModule", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_REMOTE_DEVICE_HANDLE, ctypes.POINTER(PEAK_MODULE_HANDLE)],
            argnames = ["remoteDeviceHandle", "moduleHandle"] )
    #  PEAK_RETURN_CODE PEAK_RemoteDevice_GetLocalDevice(PEAK_REMOTE_DEVICE_HANDLE remoteDeviceHandle, ctypes.POINTER(PEAK_DEVICE_HANDLE) deviceHandle)
    addfunc(lib, "PEAK_RemoteDevice_GetLocalDevice", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_REMOTE_DEVICE_HANDLE, ctypes.POINTER(PEAK_DEVICE_HANDLE)],
            argnames = ["remoteDeviceHandle", "deviceHandle"] )
    #  PEAK_RETURN_CODE PEAK_DataStreamDescriptor_ToModuleDescriptor(PEAK_DATA_STREAM_DESCRIPTOR_HANDLE dataStreamDescriptorHandle, ctypes.POINTER(PEAK_MODULE_DESCRIPTOR_HANDLE) moduleDescriptorHandle)
    addfunc(lib, "PEAK_DataStreamDescriptor_ToModuleDescriptor", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_DESCRIPTOR_HANDLE, ctypes.POINTER(PEAK_MODULE_DESCRIPTOR_HANDLE)],
            argnames = ["dataStreamDescriptorHandle", "moduleDescriptorHandle"] )
    #  PEAK_RETURN_CODE PEAK_DataStreamDescriptor_GetKey(PEAK_DATA_STREAM_DESCRIPTOR_HANDLE dataStreamDescriptorHandle, ctypes.c_char_p key, ctypes.POINTER(ctypes.c_size_t) keySize)
    addfunc(lib, "PEAK_DataStreamDescriptor_GetKey", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["dataStreamDescriptorHandle", "key", "keySize"] )
    #  PEAK_RETURN_CODE PEAK_DataStreamDescriptor_GetParentDevice(PEAK_DATA_STREAM_DESCRIPTOR_HANDLE dataStreamDescriptorHandle, ctypes.POINTER(PEAK_DEVICE_HANDLE) deviceHandle)
    addfunc(lib, "PEAK_DataStreamDescriptor_GetParentDevice", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_DESCRIPTOR_HANDLE, ctypes.POINTER(PEAK_DEVICE_HANDLE)],
            argnames = ["dataStreamDescriptorHandle", "deviceHandle"] )
    #  PEAK_RETURN_CODE PEAK_DataStreamDescriptor_OpenDataStream(PEAK_DATA_STREAM_DESCRIPTOR_HANDLE dataStreamDescriptorHandle, ctypes.POINTER(PEAK_DATA_STREAM_HANDLE) dataStreamHandle)
    addfunc(lib, "PEAK_DataStreamDescriptor_OpenDataStream", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_DESCRIPTOR_HANDLE, ctypes.POINTER(PEAK_DATA_STREAM_HANDLE)],
            argnames = ["dataStreamDescriptorHandle", "dataStreamHandle"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_ToModule(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(PEAK_MODULE_HANDLE) moduleHandle)
    addfunc(lib, "PEAK_DataStream_ToModule", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(PEAK_MODULE_HANDLE)],
            argnames = ["dataStreamHandle", "moduleHandle"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_ToEventSupportingModule(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(PEAK_EVENT_SUPPORTING_MODULE_HANDLE) eventSupportingModuleHandle)
    addfunc(lib, "PEAK_DataStream_ToEventSupportingModule", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(PEAK_EVENT_SUPPORTING_MODULE_HANDLE)],
            argnames = ["dataStreamHandle", "eventSupportingModuleHandle"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetKey(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.c_char_p key, ctypes.POINTER(ctypes.c_size_t) keySize)
    addfunc(lib, "PEAK_DataStream_GetKey", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["dataStreamHandle", "key", "keySize"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetInfo(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.c_int32 infoCommand, ctypes.POINTER(ctypes.c_int32) infoDataType, ctypes.POINTER(ctypes.c_uint8) info, ctypes.POINTER(ctypes.c_size_t) infoSize)
    addfunc(lib, "PEAK_DataStream_GetInfo", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["dataStreamHandle", "infoCommand", "infoDataType", "info", "infoSize"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetID(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.c_char_p id, ctypes.POINTER(ctypes.c_size_t) idSize)
    addfunc(lib, "PEAK_DataStream_GetID", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["dataStreamHandle", "id", "idSize"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetTLType(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.c_char_p tlType, ctypes.POINTER(ctypes.c_size_t) tlTypeSize)
    addfunc(lib, "PEAK_DataStream_GetTLType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["dataStreamHandle", "tlType", "tlTypeSize"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetNumBuffersAnnouncedMinRequired(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(ctypes.c_size_t) numBuffersAnnouncedMinRequired)
    addfunc(lib, "PEAK_DataStream_GetNumBuffersAnnouncedMinRequired", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["dataStreamHandle", "numBuffersAnnouncedMinRequired"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetNumBuffersAnnounced(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(ctypes.c_size_t) numBuffersAnnounced)
    addfunc(lib, "PEAK_DataStream_GetNumBuffersAnnounced", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["dataStreamHandle", "numBuffersAnnounced"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetNumBuffersQueued(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(ctypes.c_size_t) numBuffersQueued)
    addfunc(lib, "PEAK_DataStream_GetNumBuffersQueued", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["dataStreamHandle", "numBuffersQueued"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetNumBuffersAwaitDelivery(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(ctypes.c_size_t) numBuffersAwaitDelivery)
    addfunc(lib, "PEAK_DataStream_GetNumBuffersAwaitDelivery", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["dataStreamHandle", "numBuffersAwaitDelivery"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetNumBuffersDelivered(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(ctypes.c_uint64) numBuffersDelivered)
    addfunc(lib, "PEAK_DataStream_GetNumBuffersDelivered", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["dataStreamHandle", "numBuffersDelivered"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetNumBuffersStarted(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(ctypes.c_uint64) numBuffersStarted)
    addfunc(lib, "PEAK_DataStream_GetNumBuffersStarted", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["dataStreamHandle", "numBuffersStarted"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetNumUnderruns(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(ctypes.c_uint64) numUnderruns)
    addfunc(lib, "PEAK_DataStream_GetNumUnderruns", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["dataStreamHandle", "numUnderruns"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetNumChunksPerBufferMax(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(ctypes.c_size_t) numChunksPerBufferMax)
    addfunc(lib, "PEAK_DataStream_GetNumChunksPerBufferMax", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["dataStreamHandle", "numChunksPerBufferMax"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetBufferAlignment(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(ctypes.c_size_t) bufferAlignment)
    addfunc(lib, "PEAK_DataStream_GetBufferAlignment", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["dataStreamHandle", "bufferAlignment"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetPayloadSize(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(ctypes.c_size_t) payloadSize)
    addfunc(lib, "PEAK_DataStream_GetPayloadSize", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["dataStreamHandle", "payloadSize"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetDefinesPayloadSize(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(PEAK_BOOL8) definesPayloadSize)
    addfunc(lib, "PEAK_DataStream_GetDefinesPayloadSize", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["dataStreamHandle", "definesPayloadSize"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetIsGrabbing(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(PEAK_BOOL8) isGrabbing)
    addfunc(lib, "PEAK_DataStream_GetIsGrabbing", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["dataStreamHandle", "isGrabbing"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_GetParentDevice(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.POINTER(PEAK_DEVICE_HANDLE) deviceHandle)
    addfunc(lib, "PEAK_DataStream_GetParentDevice", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.POINTER(PEAK_DEVICE_HANDLE)],
            argnames = ["dataStreamHandle", "deviceHandle"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_AnnounceBuffer(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.c_void_p buffer, ctypes.c_size_t bufferSize, ctypes.c_void_p userPtr, PEAK_BUFFER_REVOCATION_CALLBACK revocationCallback, ctypes.c_void_p callbackContext, ctypes.POINTER(PEAK_BUFFER_HANDLE) bufferHandle)
    addfunc(lib, "PEAK_DataStream_AnnounceBuffer", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p, PEAK_BUFFER_REVOCATION_CALLBACK, ctypes.c_void_p, ctypes.POINTER(PEAK_BUFFER_HANDLE)],
            argnames = ["dataStreamHandle", "buffer", "bufferSize", "userPtr", "revocationCallback", "callbackContext", "bufferHandle"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_AllocAndAnnounceBuffer(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.c_size_t bufferSize, ctypes.c_void_p userPtr, ctypes.POINTER(PEAK_BUFFER_HANDLE) bufferHandle)
    addfunc(lib, "PEAK_DataStream_AllocAndAnnounceBuffer", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.c_size_t, ctypes.c_void_p, ctypes.POINTER(PEAK_BUFFER_HANDLE)],
            argnames = ["dataStreamHandle", "bufferSize", "userPtr", "bufferHandle"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_QueueBuffer(PEAK_DATA_STREAM_HANDLE dataStreamHandle, PEAK_BUFFER_HANDLE bufferHandle)
    addfunc(lib, "PEAK_DataStream_QueueBuffer", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, PEAK_BUFFER_HANDLE],
            argnames = ["dataStreamHandle", "bufferHandle"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_RevokeBuffer(PEAK_DATA_STREAM_HANDLE dataStreamHandle, PEAK_BUFFER_HANDLE bufferHandle)
    addfunc(lib, "PEAK_DataStream_RevokeBuffer", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, PEAK_BUFFER_HANDLE],
            argnames = ["dataStreamHandle", "bufferHandle"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_WaitForFinishedBuffer(PEAK_DATA_STREAM_HANDLE dataStreamHandle, ctypes.c_uint64 timeout_ms, ctypes.POINTER(PEAK_BUFFER_HANDLE) bufferHandle)
    addfunc(lib, "PEAK_DataStream_WaitForFinishedBuffer", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, ctypes.c_uint64, ctypes.POINTER(PEAK_BUFFER_HANDLE)],
            argnames = ["dataStreamHandle", "timeout_ms", "bufferHandle"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_KillWait(PEAK_DATA_STREAM_HANDLE dataStreamHandle)
    addfunc(lib, "PEAK_DataStream_KillWait", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE],
            argnames = ["dataStreamHandle"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_Flush(PEAK_DATA_STREAM_HANDLE dataStreamHandle, PEAK_DATA_STREAM_FLUSH_MODE flushMode)
    addfunc(lib, "PEAK_DataStream_Flush", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, PEAK_DATA_STREAM_FLUSH_MODE],
            argnames = ["dataStreamHandle", "flushMode"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_StartAcquisitionInfinite(PEAK_DATA_STREAM_HANDLE dataStreamHandle, PEAK_ACQUISITION_START_MODE startMode)
    addfunc(lib, "PEAK_DataStream_StartAcquisitionInfinite", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, PEAK_ACQUISITION_START_MODE],
            argnames = ["dataStreamHandle", "startMode"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_StartAcquisition(PEAK_DATA_STREAM_HANDLE dataStreamHandle, PEAK_ACQUISITION_START_MODE startMode, ctypes.c_uint64 numToAcquire)
    addfunc(lib, "PEAK_DataStream_StartAcquisition", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, PEAK_ACQUISITION_START_MODE, ctypes.c_uint64],
            argnames = ["dataStreamHandle", "startMode", "numToAcquire"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_StopAcquisition(PEAK_DATA_STREAM_HANDLE dataStreamHandle, PEAK_ACQUISITION_STOP_MODE stopMode)
    addfunc(lib, "PEAK_DataStream_StopAcquisition", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE, PEAK_ACQUISITION_STOP_MODE],
            argnames = ["dataStreamHandle", "stopMode"] )
    #  PEAK_RETURN_CODE PEAK_DataStream_Destruct(PEAK_DATA_STREAM_HANDLE dataStreamHandle)
    addfunc(lib, "PEAK_DataStream_Destruct", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_DATA_STREAM_HANDLE],
            argnames = ["dataStreamHandle"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_ToModule(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(PEAK_MODULE_HANDLE) moduleHandle)
    addfunc(lib, "PEAK_Buffer_ToModule", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(PEAK_MODULE_HANDLE)],
            argnames = ["bufferHandle", "moduleHandle"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_ToEventSupportingModule(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(PEAK_EVENT_SUPPORTING_MODULE_HANDLE) eventSupportingModuleHandle)
    addfunc(lib, "PEAK_Buffer_ToEventSupportingModule", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(PEAK_EVENT_SUPPORTING_MODULE_HANDLE)],
            argnames = ["bufferHandle", "eventSupportingModuleHandle"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetInfo(PEAK_BUFFER_HANDLE bufferHandle, ctypes.c_int32 infoCommand, ctypes.POINTER(ctypes.c_int32) infoDataType, ctypes.POINTER(ctypes.c_uint8) info, ctypes.POINTER(ctypes.c_size_t) infoSize)
    addfunc(lib, "PEAK_Buffer_GetInfo", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "infoCommand", "infoDataType", "info", "infoSize"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetTLType(PEAK_BUFFER_HANDLE bufferHandle, ctypes.c_char_p tlType, ctypes.POINTER(ctypes.c_size_t) tlTypeSize)
    addfunc(lib, "PEAK_Buffer_GetTLType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "tlType", "tlTypeSize"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetBasePtr(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_void_p) basePtr)
    addfunc(lib, "PEAK_Buffer_GetBasePtr", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_void_p)],
            argnames = ["bufferHandle", "basePtr"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetSize(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_size_t) size)
    addfunc(lib, "PEAK_Buffer_GetSize", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "size"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetUserPtr(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_void_p) userPtr)
    addfunc(lib, "PEAK_Buffer_GetUserPtr", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_void_p)],
            argnames = ["bufferHandle", "userPtr"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetPayloadType(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(PEAK_BUFFER_PAYLOAD_TYPE) payloadType)
    addfunc(lib, "PEAK_Buffer_GetPayloadType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(PEAK_BUFFER_PAYLOAD_TYPE)],
            argnames = ["bufferHandle", "payloadType"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetPixelFormat(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_uint64) pixelFormat)
    addfunc(lib, "PEAK_Buffer_GetPixelFormat", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["bufferHandle", "pixelFormat"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetPixelFormatNamespace(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(PEAK_PIXEL_FORMAT_NAMESPACE) pixelFormatNamespace)
    addfunc(lib, "PEAK_Buffer_GetPixelFormatNamespace", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(PEAK_PIXEL_FORMAT_NAMESPACE)],
            argnames = ["bufferHandle", "pixelFormatNamespace"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetPixelEndianness(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(PEAK_ENDIANNESS) pixelEndianness)
    addfunc(lib, "PEAK_Buffer_GetPixelEndianness", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(PEAK_ENDIANNESS)],
            argnames = ["bufferHandle", "pixelEndianness"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetExpectedDataSize(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_size_t) expectedDataSize)
    addfunc(lib, "PEAK_Buffer_GetExpectedDataSize", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "expectedDataSize"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetDeliveredDataSize(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_size_t) deliveredDataSize)
    addfunc(lib, "PEAK_Buffer_GetDeliveredDataSize", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "deliveredDataSize"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetFrameID(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_uint64) frameId)
    addfunc(lib, "PEAK_Buffer_GetFrameID", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["bufferHandle", "frameId"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetImageOffset(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_size_t) imageOffset)
    addfunc(lib, "PEAK_Buffer_GetImageOffset", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "imageOffset"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetDeliveredImageHeight(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_size_t) deliveredImageHeight)
    addfunc(lib, "PEAK_Buffer_GetDeliveredImageHeight", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "deliveredImageHeight"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetDeliveredChunkPayloadSize(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_size_t) deliveredChunkPayloadSize)
    addfunc(lib, "PEAK_Buffer_GetDeliveredChunkPayloadSize", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "deliveredChunkPayloadSize"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetChunkLayoutID(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_uint64) chunkLayoutId)
    addfunc(lib, "PEAK_Buffer_GetChunkLayoutID", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["bufferHandle", "chunkLayoutId"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetFileName(PEAK_BUFFER_HANDLE bufferHandle, ctypes.c_char_p fileName, ctypes.POINTER(ctypes.c_size_t) fileNameSize)
    addfunc(lib, "PEAK_Buffer_GetFileName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "fileName", "fileNameSize"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetWidth(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_size_t) width)
    addfunc(lib, "PEAK_Buffer_GetWidth", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "width"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetHeight(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_size_t) height)
    addfunc(lib, "PEAK_Buffer_GetHeight", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "height"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetXOffset(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_size_t) xOffset)
    addfunc(lib, "PEAK_Buffer_GetXOffset", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "xOffset"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetYOffset(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_size_t) yOffset)
    addfunc(lib, "PEAK_Buffer_GetYOffset", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "yOffset"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetXPadding(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_size_t) xPadding)
    addfunc(lib, "PEAK_Buffer_GetXPadding", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "xPadding"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetYPadding(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_size_t) yPadding)
    addfunc(lib, "PEAK_Buffer_GetYPadding", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "yPadding"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetTimestamp_ticks(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_uint64) timestamp_ticks)
    addfunc(lib, "PEAK_Buffer_GetTimestamp_ticks", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["bufferHandle", "timestamp_ticks"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetTimestamp_ns(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_uint64) timestamp_ns)
    addfunc(lib, "PEAK_Buffer_GetTimestamp_ns", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["bufferHandle", "timestamp_ns"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetIsQueued(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(PEAK_BOOL8) isQueued)
    addfunc(lib, "PEAK_Buffer_GetIsQueued", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["bufferHandle", "isQueued"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetIsAcquiring(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(PEAK_BOOL8) isAcquiring)
    addfunc(lib, "PEAK_Buffer_GetIsAcquiring", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["bufferHandle", "isAcquiring"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetIsIncomplete(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(PEAK_BOOL8) isIncomplete)
    addfunc(lib, "PEAK_Buffer_GetIsIncomplete", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["bufferHandle", "isIncomplete"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetHasNewData(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(PEAK_BOOL8) hasNewData)
    addfunc(lib, "PEAK_Buffer_GetHasNewData", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["bufferHandle", "hasNewData"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetHasImage(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(PEAK_BOOL8) hasImage)
    addfunc(lib, "PEAK_Buffer_GetHasImage", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["bufferHandle", "hasImage"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetHasChunks(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(PEAK_BOOL8) hasChunks)
    addfunc(lib, "PEAK_Buffer_GetHasChunks", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["bufferHandle", "hasChunks"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_UpdateChunks(PEAK_BUFFER_HANDLE bufferHandle)
    addfunc(lib, "PEAK_Buffer_UpdateChunks", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE],
            argnames = ["bufferHandle"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetNumChunks(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_size_t) numChunks)
    addfunc(lib, "PEAK_Buffer_GetNumChunks", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "numChunks"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetChunk(PEAK_BUFFER_HANDLE bufferHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_BUFFER_CHUNK_HANDLE) bufferChunkHandle)
    addfunc(lib, "PEAK_Buffer_GetChunk", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_BUFFER_CHUNK_HANDLE)],
            argnames = ["bufferHandle", "index", "bufferChunkHandle"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_UpdateParts(PEAK_BUFFER_HANDLE bufferHandle)
    addfunc(lib, "PEAK_Buffer_UpdateParts", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE],
            argnames = ["bufferHandle"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetNumParts(PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(ctypes.c_size_t) numParts)
    addfunc(lib, "PEAK_Buffer_GetNumParts", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferHandle", "numParts"] )
    #  PEAK_RETURN_CODE PEAK_Buffer_GetPart(PEAK_BUFFER_HANDLE bufferHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_BUFFER_PART_HANDLE) bufferPartHandle)
    addfunc(lib, "PEAK_Buffer_GetPart", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_BUFFER_PART_HANDLE)],
            argnames = ["bufferHandle", "index", "bufferPartHandle"] )
    #  PEAK_RETURN_CODE PEAK_BufferChunk_GetID(PEAK_BUFFER_CHUNK_HANDLE bufferChunkHandle, ctypes.POINTER(ctypes.c_uint64) id)
    addfunc(lib, "PEAK_BufferChunk_GetID", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_CHUNK_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["bufferChunkHandle", "id"] )
    #  PEAK_RETURN_CODE PEAK_BufferChunk_GetBasePtr(PEAK_BUFFER_CHUNK_HANDLE bufferChunkHandle, ctypes.POINTER(ctypes.c_void_p) basePtr)
    addfunc(lib, "PEAK_BufferChunk_GetBasePtr", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_CHUNK_HANDLE, ctypes.POINTER(ctypes.c_void_p)],
            argnames = ["bufferChunkHandle", "basePtr"] )
    #  PEAK_RETURN_CODE PEAK_BufferChunk_GetSize(PEAK_BUFFER_CHUNK_HANDLE bufferChunkHandle, ctypes.POINTER(ctypes.c_size_t) size)
    addfunc(lib, "PEAK_BufferChunk_GetSize", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_CHUNK_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferChunkHandle", "size"] )
    #  PEAK_RETURN_CODE PEAK_BufferChunk_GetParentBuffer(PEAK_BUFFER_CHUNK_HANDLE bufferChunkHandle, ctypes.POINTER(PEAK_BUFFER_HANDLE) bufferHandle)
    addfunc(lib, "PEAK_BufferChunk_GetParentBuffer", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_CHUNK_HANDLE, ctypes.POINTER(PEAK_BUFFER_HANDLE)],
            argnames = ["bufferChunkHandle", "bufferHandle"] )
    #  PEAK_RETURN_CODE PEAK_BufferChunk_Destruct(PEAK_BUFFER_CHUNK_HANDLE bufferChunkHandle)
    addfunc(lib, "PEAK_BufferChunk_Destruct", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_CHUNK_HANDLE],
            argnames = ["bufferChunkHandle"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_GetInfo(PEAK_BUFFER_PART_HANDLE bufferPartHandle, ctypes.c_int32 infoCommand, ctypes.POINTER(ctypes.c_int32) infoDataType, ctypes.POINTER(ctypes.c_uint8) info, ctypes.POINTER(ctypes.c_size_t) infoSize)
    addfunc(lib, "PEAK_BufferPart_GetInfo", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferPartHandle", "infoCommand", "infoDataType", "info", "infoSize"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_GetSourceID(PEAK_BUFFER_PART_HANDLE bufferPartHandle, ctypes.POINTER(ctypes.c_uint64) sourceId)
    addfunc(lib, "PEAK_BufferPart_GetSourceID", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["bufferPartHandle", "sourceId"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_GetBasePtr(PEAK_BUFFER_PART_HANDLE bufferPartHandle, ctypes.POINTER(ctypes.c_void_p) basePtr)
    addfunc(lib, "PEAK_BufferPart_GetBasePtr", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE, ctypes.POINTER(ctypes.c_void_p)],
            argnames = ["bufferPartHandle", "basePtr"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_GetSize(PEAK_BUFFER_PART_HANDLE bufferPartHandle, ctypes.POINTER(ctypes.c_size_t) size)
    addfunc(lib, "PEAK_BufferPart_GetSize", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferPartHandle", "size"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_GetType(PEAK_BUFFER_PART_HANDLE bufferPartHandle, ctypes.POINTER(PEAK_BUFFER_PART_TYPE) type)
    addfunc(lib, "PEAK_BufferPart_GetType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE, ctypes.POINTER(PEAK_BUFFER_PART_TYPE)],
            argnames = ["bufferPartHandle", "type"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_GetFormat(PEAK_BUFFER_PART_HANDLE bufferPartHandle, ctypes.POINTER(ctypes.c_uint64) format)
    addfunc(lib, "PEAK_BufferPart_GetFormat", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["bufferPartHandle", "format"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_GetFormatNamespace(PEAK_BUFFER_PART_HANDLE bufferPartHandle, ctypes.POINTER(ctypes.c_uint64) formatNamespace)
    addfunc(lib, "PEAK_BufferPart_GetFormatNamespace", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["bufferPartHandle", "formatNamespace"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_GetWidth(PEAK_BUFFER_PART_HANDLE bufferPartHandle, ctypes.POINTER(ctypes.c_size_t) width)
    addfunc(lib, "PEAK_BufferPart_GetWidth", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferPartHandle", "width"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_GetHeight(PEAK_BUFFER_PART_HANDLE bufferPartHandle, ctypes.POINTER(ctypes.c_size_t) height)
    addfunc(lib, "PEAK_BufferPart_GetHeight", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferPartHandle", "height"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_GetXOffset(PEAK_BUFFER_PART_HANDLE bufferPartHandle, ctypes.POINTER(ctypes.c_size_t) xOffset)
    addfunc(lib, "PEAK_BufferPart_GetXOffset", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferPartHandle", "xOffset"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_GetYOffset(PEAK_BUFFER_PART_HANDLE bufferPartHandle, ctypes.POINTER(ctypes.c_size_t) yOffset)
    addfunc(lib, "PEAK_BufferPart_GetYOffset", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferPartHandle", "yOffset"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_GetXPadding(PEAK_BUFFER_PART_HANDLE bufferPartHandle, ctypes.POINTER(ctypes.c_size_t) xPadding)
    addfunc(lib, "PEAK_BufferPart_GetXPadding", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferPartHandle", "xPadding"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_GetDeliveredImageHeight(PEAK_BUFFER_PART_HANDLE bufferPartHandle, ctypes.POINTER(ctypes.c_size_t) deliveredImageHeight)
    addfunc(lib, "PEAK_BufferPart_GetDeliveredImageHeight", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["bufferPartHandle", "deliveredImageHeight"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_GetParentBuffer(PEAK_BUFFER_PART_HANDLE bufferPartHandle, ctypes.POINTER(PEAK_BUFFER_HANDLE) bufferHandle)
    addfunc(lib, "PEAK_BufferPart_GetParentBuffer", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE, ctypes.POINTER(PEAK_BUFFER_HANDLE)],
            argnames = ["bufferPartHandle", "bufferHandle"] )
    #  PEAK_RETURN_CODE PEAK_BufferPart_Destruct(PEAK_BUFFER_PART_HANDLE bufferPartHandle)
    addfunc(lib, "PEAK_BufferPart_Destruct", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BUFFER_PART_HANDLE],
            argnames = ["bufferPartHandle"] )
    #  PEAK_RETURN_CODE PEAK_ModuleDescriptor_GetID(PEAK_MODULE_DESCRIPTOR_HANDLE moduleDescriptorHandle, ctypes.c_char_p id, ctypes.POINTER(ctypes.c_size_t) idSize)
    addfunc(lib, "PEAK_ModuleDescriptor_GetID", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_MODULE_DESCRIPTOR_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["moduleDescriptorHandle", "id", "idSize"] )
    #  PEAK_RETURN_CODE PEAK_Module_GetNumNodeMaps(PEAK_MODULE_HANDLE moduleHandle, ctypes.POINTER(ctypes.c_size_t) numNodeMaps)
    addfunc(lib, "PEAK_Module_GetNumNodeMaps", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_MODULE_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["moduleHandle", "numNodeMaps"] )
    #  PEAK_RETURN_CODE PEAK_Module_GetNodeMap(PEAK_MODULE_HANDLE moduleHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_NODE_MAP_HANDLE) nodeMapHandle)
    addfunc(lib, "PEAK_Module_GetNodeMap", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_MODULE_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_NODE_MAP_HANDLE)],
            argnames = ["moduleHandle", "index", "nodeMapHandle"] )
    #  PEAK_RETURN_CODE PEAK_Module_GetPort(PEAK_MODULE_HANDLE moduleHandle, ctypes.POINTER(PEAK_PORT_HANDLE) portHandle)
    addfunc(lib, "PEAK_Module_GetPort", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_MODULE_HANDLE, ctypes.POINTER(PEAK_PORT_HANDLE)],
            argnames = ["moduleHandle", "portHandle"] )
    #  PEAK_RETURN_CODE PEAK_NodeMap_GetHasNode(PEAK_NODE_MAP_HANDLE nodeMapHandle, ctypes.c_char_p nodeName, ctypes.c_size_t nodeNameSize, ctypes.POINTER(PEAK_BOOL8) hasNode)
    addfunc(lib, "PEAK_NodeMap_GetHasNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_MAP_HANDLE, ctypes.c_char_p, ctypes.c_size_t, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["nodeMapHandle", "nodeName", "nodeNameSize", "hasNode"] )
    #  PEAK_RETURN_CODE PEAK_NodeMap_FindNode(PEAK_NODE_MAP_HANDLE nodeMapHandle, ctypes.c_char_p nodeName, ctypes.c_size_t nodeNameSize, ctypes.POINTER(PEAK_NODE_HANDLE) nodeHandle)
    addfunc(lib, "PEAK_NodeMap_FindNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_MAP_HANDLE, ctypes.c_char_p, ctypes.c_size_t, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["nodeMapHandle", "nodeName", "nodeNameSize", "nodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_NodeMap_InvalidateNodes(PEAK_NODE_MAP_HANDLE nodeMapHandle)
    addfunc(lib, "PEAK_NodeMap_InvalidateNodes", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_MAP_HANDLE],
            argnames = ["nodeMapHandle"] )
    #  PEAK_RETURN_CODE PEAK_NodeMap_PollNodes(PEAK_NODE_MAP_HANDLE nodeMapHandle, ctypes.c_int64 elapsedTime_ms)
    addfunc(lib, "PEAK_NodeMap_PollNodes", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_MAP_HANDLE, ctypes.c_int64],
            argnames = ["nodeMapHandle", "elapsedTime_ms"] )
    #  PEAK_RETURN_CODE PEAK_NodeMap_GetNumNodes(PEAK_NODE_MAP_HANDLE nodeMapHandle, ctypes.POINTER(ctypes.c_size_t) numNodes)
    addfunc(lib, "PEAK_NodeMap_GetNumNodes", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_MAP_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["nodeMapHandle", "numNodes"] )
    #  PEAK_RETURN_CODE PEAK_NodeMap_GetNode(PEAK_NODE_MAP_HANDLE nodeMapHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_NODE_HANDLE) nodeHandle)
    addfunc(lib, "PEAK_NodeMap_GetNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_MAP_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["nodeMapHandle", "index", "nodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_NodeMap_GetHasBufferSupportedChunks(PEAK_NODE_MAP_HANDLE nodeMapHandle, PEAK_BUFFER_HANDLE bufferHandle, ctypes.POINTER(PEAK_BOOL8) hasSupportedChunks)
    addfunc(lib, "PEAK_NodeMap_GetHasBufferSupportedChunks", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_MAP_HANDLE, PEAK_BUFFER_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["nodeMapHandle", "bufferHandle", "hasSupportedChunks"] )
    #  PEAK_RETURN_CODE PEAK_NodeMap_UpdateChunkNodes(PEAK_NODE_MAP_HANDLE nodeMapHandle, PEAK_BUFFER_HANDLE bufferHandle)
    addfunc(lib, "PEAK_NodeMap_UpdateChunkNodes", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_MAP_HANDLE, PEAK_BUFFER_HANDLE],
            argnames = ["nodeMapHandle", "bufferHandle"] )
    #  PEAK_RETURN_CODE PEAK_NodeMap_GetHasEventSupportedData(PEAK_NODE_MAP_HANDLE nodeMapHandle, PEAK_EVENT_HANDLE eventHandle, ctypes.POINTER(PEAK_BOOL8) hasSupportedData)
    addfunc(lib, "PEAK_NodeMap_GetHasEventSupportedData", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_MAP_HANDLE, PEAK_EVENT_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["nodeMapHandle", "eventHandle", "hasSupportedData"] )
    #  PEAK_RETURN_CODE PEAK_NodeMap_UpdateEventNodes(PEAK_NODE_MAP_HANDLE nodeMapHandle, PEAK_EVENT_HANDLE eventHandle)
    addfunc(lib, "PEAK_NodeMap_UpdateEventNodes", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_MAP_HANDLE, PEAK_EVENT_HANDLE],
            argnames = ["nodeMapHandle", "eventHandle"] )
    #  PEAK_RETURN_CODE PEAK_NodeMap_StoreToFile(PEAK_NODE_MAP_HANDLE nodeMapHandle, ctypes.c_char_p filePath, ctypes.c_size_t filePathSize)
    addfunc(lib, "PEAK_NodeMap_StoreToFile", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_MAP_HANDLE, ctypes.c_char_p, ctypes.c_size_t],
            argnames = ["nodeMapHandle", "filePath", "filePathSize"] )
    #  PEAK_RETURN_CODE PEAK_NodeMap_LoadFromFile(PEAK_NODE_MAP_HANDLE nodeMapHandle, ctypes.c_char_p filePath, ctypes.c_size_t filePathSize)
    addfunc(lib, "PEAK_NodeMap_LoadFromFile", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_MAP_HANDLE, ctypes.c_char_p, ctypes.c_size_t],
            argnames = ["nodeMapHandle", "filePath", "filePathSize"] )
    #  PEAK_RETURN_CODE PEAK_NodeMap_Lock(PEAK_NODE_MAP_HANDLE nodeMapHandle)
    addfunc(lib, "PEAK_NodeMap_Lock", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_MAP_HANDLE],
            argnames = ["nodeMapHandle"] )
    #  PEAK_RETURN_CODE PEAK_NodeMap_Unlock(PEAK_NODE_MAP_HANDLE nodeMapHandle)
    addfunc(lib, "PEAK_NodeMap_Unlock", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_MAP_HANDLE],
            argnames = ["nodeMapHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_ToIntegerNode(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_INTEGER_NODE_HANDLE) integerNodeHandle)
    addfunc(lib, "PEAK_Node_ToIntegerNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_INTEGER_NODE_HANDLE)],
            argnames = ["nodeHandle", "integerNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_ToBooleanNode(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_BOOLEAN_NODE_HANDLE) booleanNodeHandle)
    addfunc(lib, "PEAK_Node_ToBooleanNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_BOOLEAN_NODE_HANDLE)],
            argnames = ["nodeHandle", "booleanNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_ToCommandNode(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_COMMAND_NODE_HANDLE) commandNodeHandle)
    addfunc(lib, "PEAK_Node_ToCommandNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_COMMAND_NODE_HANDLE)],
            argnames = ["nodeHandle", "commandNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_ToFloatNode(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_FLOAT_NODE_HANDLE) floatNodeHandle)
    addfunc(lib, "PEAK_Node_ToFloatNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_FLOAT_NODE_HANDLE)],
            argnames = ["nodeHandle", "floatNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_ToStringNode(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_STRING_NODE_HANDLE) stringNodeHandle)
    addfunc(lib, "PEAK_Node_ToStringNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_STRING_NODE_HANDLE)],
            argnames = ["nodeHandle", "stringNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_ToRegisterNode(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_REGISTER_NODE_HANDLE) registerNodeHandle)
    addfunc(lib, "PEAK_Node_ToRegisterNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_REGISTER_NODE_HANDLE)],
            argnames = ["nodeHandle", "registerNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_ToCategoryNode(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_CATEGORY_NODE_HANDLE) categoryNodeHandle)
    addfunc(lib, "PEAK_Node_ToCategoryNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_CATEGORY_NODE_HANDLE)],
            argnames = ["nodeHandle", "categoryNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_ToEnumerationNode(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_ENUMERATION_NODE_HANDLE) enumerationNodeHandle)
    addfunc(lib, "PEAK_Node_ToEnumerationNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_ENUMERATION_NODE_HANDLE)],
            argnames = ["nodeHandle", "enumerationNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_ToEnumerationEntryNode(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_ENUMERATION_ENTRY_NODE_HANDLE) enumerationEntryNodeHandle)
    addfunc(lib, "PEAK_Node_ToEnumerationEntryNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_ENUMERATION_ENTRY_NODE_HANDLE)],
            argnames = ["nodeHandle", "enumerationEntryNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetName(PEAK_NODE_HANDLE nodeHandle, ctypes.c_char_p name, ctypes.POINTER(ctypes.c_size_t) nameSize)
    addfunc(lib, "PEAK_Node_GetName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["nodeHandle", "name", "nameSize"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetDisplayName(PEAK_NODE_HANDLE nodeHandle, ctypes.c_char_p displayName, ctypes.POINTER(ctypes.c_size_t) displayNameSize)
    addfunc(lib, "PEAK_Node_GetDisplayName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["nodeHandle", "displayName", "displayNameSize"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetNamespace(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_NODE_NAMESPACE) _namespace)
    addfunc(lib, "PEAK_Node_GetNamespace", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_NAMESPACE)],
            argnames = ["nodeHandle", "_namespace"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetVisibility(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_NODE_VISIBILITY) visibility)
    addfunc(lib, "PEAK_Node_GetVisibility", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_VISIBILITY)],
            argnames = ["nodeHandle", "visibility"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetAccessStatus(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_NODE_ACCESS_STATUS) accessStatus)
    addfunc(lib, "PEAK_Node_GetAccessStatus", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_ACCESS_STATUS)],
            argnames = ["nodeHandle", "accessStatus"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetIsCacheable(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_BOOL8) isCacheable)
    addfunc(lib, "PEAK_Node_GetIsCacheable", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["nodeHandle", "isCacheable"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetIsAccessStatusCacheable(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_BOOL8) isAccessStatusCacheable)
    addfunc(lib, "PEAK_Node_GetIsAccessStatusCacheable", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["nodeHandle", "isAccessStatusCacheable"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetIsStreamable(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_BOOL8) isStreamable)
    addfunc(lib, "PEAK_Node_GetIsStreamable", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["nodeHandle", "isStreamable"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetIsDeprecated(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_BOOL8) isDeprecated)
    addfunc(lib, "PEAK_Node_GetIsDeprecated", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["nodeHandle", "isDeprecated"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetIsFeature(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_BOOL8) isFeature)
    addfunc(lib, "PEAK_Node_GetIsFeature", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["nodeHandle", "isFeature"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetCachingMode(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_NODE_CACHING_MODE) cachingMode)
    addfunc(lib, "PEAK_Node_GetCachingMode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_CACHING_MODE)],
            argnames = ["nodeHandle", "cachingMode"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetPollingTime(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(ctypes.c_int64) pollingTime_ms)
    addfunc(lib, "PEAK_Node_GetPollingTime", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["nodeHandle", "pollingTime_ms"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetToolTip(PEAK_NODE_HANDLE nodeHandle, ctypes.c_char_p toolTip, ctypes.POINTER(ctypes.c_size_t) toolTipSize)
    addfunc(lib, "PEAK_Node_GetToolTip", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["nodeHandle", "toolTip", "toolTipSize"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetDescription(PEAK_NODE_HANDLE nodeHandle, ctypes.c_char_p description, ctypes.POINTER(ctypes.c_size_t) descriptionSize)
    addfunc(lib, "PEAK_Node_GetDescription", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["nodeHandle", "description", "descriptionSize"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetType(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_NODE_TYPE) type)
    addfunc(lib, "PEAK_Node_GetType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_TYPE)],
            argnames = ["nodeHandle", "type"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetParentNodeMap(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(PEAK_NODE_MAP_HANDLE) nodeMapHandle)
    addfunc(lib, "PEAK_Node_GetParentNodeMap", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_MAP_HANDLE)],
            argnames = ["nodeHandle", "nodeMapHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_FindInvalidatedNode(PEAK_NODE_HANDLE nodeHandle, ctypes.c_char_p name, ctypes.c_size_t nameSize, ctypes.POINTER(PEAK_NODE_HANDLE) invalidatedNodeHandle)
    addfunc(lib, "PEAK_Node_FindInvalidatedNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.c_char_p, ctypes.c_size_t, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["nodeHandle", "name", "nameSize", "invalidatedNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetNumInvalidatedNodes(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(ctypes.c_size_t) numInvalidatedNodes)
    addfunc(lib, "PEAK_Node_GetNumInvalidatedNodes", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["nodeHandle", "numInvalidatedNodes"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetInvalidatedNode(PEAK_NODE_HANDLE nodeHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_NODE_HANDLE) invalidatedNodeHandle)
    addfunc(lib, "PEAK_Node_GetInvalidatedNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["nodeHandle", "index", "invalidatedNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_FindInvalidatingNode(PEAK_NODE_HANDLE nodeHandle, ctypes.c_char_p name, ctypes.c_size_t nameSize, ctypes.POINTER(PEAK_NODE_HANDLE) invalidatingNodeHandle)
    addfunc(lib, "PEAK_Node_FindInvalidatingNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.c_char_p, ctypes.c_size_t, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["nodeHandle", "name", "nameSize", "invalidatingNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetNumInvalidatingNodes(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(ctypes.c_size_t) numInvalidatingNodes)
    addfunc(lib, "PEAK_Node_GetNumInvalidatingNodes", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["nodeHandle", "numInvalidatingNodes"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetInvalidatingNode(PEAK_NODE_HANDLE nodeHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_NODE_HANDLE) invalidatingNodeHandle)
    addfunc(lib, "PEAK_Node_GetInvalidatingNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["nodeHandle", "index", "invalidatingNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_FindSelectedNode(PEAK_NODE_HANDLE nodeHandle, ctypes.c_char_p name, ctypes.c_size_t nameSize, ctypes.POINTER(PEAK_NODE_HANDLE) selectedNodeHandle)
    addfunc(lib, "PEAK_Node_FindSelectedNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.c_char_p, ctypes.c_size_t, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["nodeHandle", "name", "nameSize", "selectedNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetNumSelectedNodes(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(ctypes.c_size_t) numSelectedNodes)
    addfunc(lib, "PEAK_Node_GetNumSelectedNodes", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["nodeHandle", "numSelectedNodes"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetSelectedNode(PEAK_NODE_HANDLE nodeHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_NODE_HANDLE) selectedNodeHandle)
    addfunc(lib, "PEAK_Node_GetSelectedNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["nodeHandle", "index", "selectedNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_FindSelectingNode(PEAK_NODE_HANDLE nodeHandle, ctypes.c_char_p name, ctypes.c_size_t nameSize, ctypes.POINTER(PEAK_NODE_HANDLE) selectingNodeHandle)
    addfunc(lib, "PEAK_Node_FindSelectingNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.c_char_p, ctypes.c_size_t, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["nodeHandle", "name", "nameSize", "selectingNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetNumSelectingNodes(PEAK_NODE_HANDLE nodeHandle, ctypes.POINTER(ctypes.c_size_t) numSelectingNodes)
    addfunc(lib, "PEAK_Node_GetNumSelectingNodes", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["nodeHandle", "numSelectingNodes"] )
    #  PEAK_RETURN_CODE PEAK_Node_GetSelectingNode(PEAK_NODE_HANDLE nodeHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_NODE_HANDLE) selectingNodeHandle)
    addfunc(lib, "PEAK_Node_GetSelectingNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["nodeHandle", "index", "selectingNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_RegisterChangedCallback(PEAK_NODE_HANDLE nodeHandle, PEAK_NODE_CHANGED_CALLBACK callback, ctypes.c_void_p callbackContext, ctypes.POINTER(PEAK_NODE_CHANGED_CALLBACK_HANDLE) callbackHandle)
    addfunc(lib, "PEAK_Node_RegisterChangedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, PEAK_NODE_CHANGED_CALLBACK, ctypes.c_void_p, ctypes.POINTER(PEAK_NODE_CHANGED_CALLBACK_HANDLE)],
            argnames = ["nodeHandle", "callback", "callbackContext", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_Node_UnregisterChangedCallback(PEAK_NODE_HANDLE nodeHandle, PEAK_NODE_CHANGED_CALLBACK_HANDLE callbackHandle)
    addfunc(lib, "PEAK_Node_UnregisterChangedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_NODE_HANDLE, PEAK_NODE_CHANGED_CALLBACK_HANDLE],
            argnames = ["nodeHandle", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_IntegerNode_ToNode(PEAK_INTEGER_NODE_HANDLE integerNodeHandle, ctypes.POINTER(PEAK_NODE_HANDLE) nodeHandle)
    addfunc(lib, "PEAK_IntegerNode_ToNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTEGER_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["integerNodeHandle", "nodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_IntegerNode_GetMinimum(PEAK_INTEGER_NODE_HANDLE integerNodeHandle, ctypes.POINTER(ctypes.c_int64) minimum)
    addfunc(lib, "PEAK_IntegerNode_GetMinimum", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTEGER_NODE_HANDLE, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["integerNodeHandle", "minimum"] )
    #  PEAK_RETURN_CODE PEAK_IntegerNode_GetMaximum(PEAK_INTEGER_NODE_HANDLE integerNodeHandle, ctypes.POINTER(ctypes.c_int64) maximum)
    addfunc(lib, "PEAK_IntegerNode_GetMaximum", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTEGER_NODE_HANDLE, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["integerNodeHandle", "maximum"] )
    #  PEAK_RETURN_CODE PEAK_IntegerNode_GetIncrement(PEAK_INTEGER_NODE_HANDLE integerNodeHandle, ctypes.POINTER(ctypes.c_int64) increment)
    addfunc(lib, "PEAK_IntegerNode_GetIncrement", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTEGER_NODE_HANDLE, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["integerNodeHandle", "increment"] )
    #  PEAK_RETURN_CODE PEAK_IntegerNode_GetIncrementType(PEAK_INTEGER_NODE_HANDLE integerNodeHandle, ctypes.POINTER(PEAK_NODE_INCREMENT_TYPE) incrementType)
    addfunc(lib, "PEAK_IntegerNode_GetIncrementType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTEGER_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_INCREMENT_TYPE)],
            argnames = ["integerNodeHandle", "incrementType"] )
    #  PEAK_RETURN_CODE PEAK_IntegerNode_GetValidValues(PEAK_INTEGER_NODE_HANDLE integerNodeHandle, ctypes.POINTER(ctypes.c_int64) validValues, ctypes.POINTER(ctypes.c_size_t) validValuesSize)
    addfunc(lib, "PEAK_IntegerNode_GetValidValues", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTEGER_NODE_HANDLE, ctypes.POINTER(ctypes.c_int64), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["integerNodeHandle", "validValues", "validValuesSize"] )
    #  PEAK_RETURN_CODE PEAK_IntegerNode_GetRepresentation(PEAK_INTEGER_NODE_HANDLE integerNodeHandle, ctypes.POINTER(PEAK_NODE_REPRESENTATION) representation)
    addfunc(lib, "PEAK_IntegerNode_GetRepresentation", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTEGER_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_REPRESENTATION)],
            argnames = ["integerNodeHandle", "representation"] )
    #  PEAK_RETURN_CODE PEAK_IntegerNode_GetUnit(PEAK_INTEGER_NODE_HANDLE integerNodeHandle, ctypes.c_char_p unit, ctypes.POINTER(ctypes.c_size_t) unitSize)
    addfunc(lib, "PEAK_IntegerNode_GetUnit", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTEGER_NODE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["integerNodeHandle", "unit", "unitSize"] )
    #  PEAK_RETURN_CODE PEAK_IntegerNode_GetValue(PEAK_INTEGER_NODE_HANDLE integerNodeHandle, PEAK_NODE_CACHE_USE_POLICY cacheUsePolicy, ctypes.POINTER(ctypes.c_int64) value)
    addfunc(lib, "PEAK_IntegerNode_GetValue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTEGER_NODE_HANDLE, PEAK_NODE_CACHE_USE_POLICY, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["integerNodeHandle", "cacheUsePolicy", "value"] )
    #  PEAK_RETURN_CODE PEAK_IntegerNode_SetValue(PEAK_INTEGER_NODE_HANDLE integerNodeHandle, ctypes.c_int64 value)
    addfunc(lib, "PEAK_IntegerNode_SetValue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_INTEGER_NODE_HANDLE, ctypes.c_int64],
            argnames = ["integerNodeHandle", "value"] )
    #  PEAK_RETURN_CODE PEAK_BooleanNode_ToNode(PEAK_BOOLEAN_NODE_HANDLE booleanNodeHandle, ctypes.POINTER(PEAK_NODE_HANDLE) nodeHandle)
    addfunc(lib, "PEAK_BooleanNode_ToNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BOOLEAN_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["booleanNodeHandle", "nodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_BooleanNode_GetValue(PEAK_BOOLEAN_NODE_HANDLE booleanNodeHandle, PEAK_NODE_CACHE_USE_POLICY cacheUsePolicy, ctypes.POINTER(PEAK_BOOL8) value)
    addfunc(lib, "PEAK_BooleanNode_GetValue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BOOLEAN_NODE_HANDLE, PEAK_NODE_CACHE_USE_POLICY, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["booleanNodeHandle", "cacheUsePolicy", "value"] )
    #  PEAK_RETURN_CODE PEAK_BooleanNode_SetValue(PEAK_BOOLEAN_NODE_HANDLE booleanNodeHandle, PEAK_BOOL8 value)
    addfunc(lib, "PEAK_BooleanNode_SetValue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_BOOLEAN_NODE_HANDLE, PEAK_BOOL8],
            argnames = ["booleanNodeHandle", "value"] )
    #  PEAK_RETURN_CODE PEAK_CommandNode_ToNode(PEAK_COMMAND_NODE_HANDLE commandNodeHandle, ctypes.POINTER(PEAK_NODE_HANDLE) nodeHandle)
    addfunc(lib, "PEAK_CommandNode_ToNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_COMMAND_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["commandNodeHandle", "nodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_CommandNode_GetIsDone(PEAK_COMMAND_NODE_HANDLE commandNodeHandle, ctypes.POINTER(PEAK_BOOL8) isDone)
    addfunc(lib, "PEAK_CommandNode_GetIsDone", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_COMMAND_NODE_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["commandNodeHandle", "isDone"] )
    #  PEAK_RETURN_CODE PEAK_CommandNode_Execute(PEAK_COMMAND_NODE_HANDLE commandNodeHandle)
    addfunc(lib, "PEAK_CommandNode_Execute", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_COMMAND_NODE_HANDLE],
            argnames = ["commandNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_CommandNode_WaitUntilDoneInfinite(PEAK_COMMAND_NODE_HANDLE commandNodeHandle)
    addfunc(lib, "PEAK_CommandNode_WaitUntilDoneInfinite", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_COMMAND_NODE_HANDLE],
            argnames = ["commandNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_CommandNode_WaitUntilDone(PEAK_COMMAND_NODE_HANDLE commandNodeHandle, ctypes.c_uint64 waitTimeout_ms)
    addfunc(lib, "PEAK_CommandNode_WaitUntilDone", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_COMMAND_NODE_HANDLE, ctypes.c_uint64],
            argnames = ["commandNodeHandle", "waitTimeout_ms"] )
    #  PEAK_RETURN_CODE PEAK_FloatNode_ToNode(PEAK_FLOAT_NODE_HANDLE floatNodeHandle, ctypes.POINTER(PEAK_NODE_HANDLE) nodeHandle)
    addfunc(lib, "PEAK_FloatNode_ToNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FLOAT_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["floatNodeHandle", "nodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_FloatNode_GetMinimum(PEAK_FLOAT_NODE_HANDLE floatNodeHandle, ctypes.POINTER(ctypes.c_double) minimum)
    addfunc(lib, "PEAK_FloatNode_GetMinimum", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FLOAT_NODE_HANDLE, ctypes.POINTER(ctypes.c_double)],
            argnames = ["floatNodeHandle", "minimum"] )
    #  PEAK_RETURN_CODE PEAK_FloatNode_GetMaximum(PEAK_FLOAT_NODE_HANDLE floatNodeHandle, ctypes.POINTER(ctypes.c_double) maximum)
    addfunc(lib, "PEAK_FloatNode_GetMaximum", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FLOAT_NODE_HANDLE, ctypes.POINTER(ctypes.c_double)],
            argnames = ["floatNodeHandle", "maximum"] )
    #  PEAK_RETURN_CODE PEAK_FloatNode_GetIncrement(PEAK_FLOAT_NODE_HANDLE floatNodeHandle, ctypes.POINTER(ctypes.c_double) increment)
    addfunc(lib, "PEAK_FloatNode_GetIncrement", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FLOAT_NODE_HANDLE, ctypes.POINTER(ctypes.c_double)],
            argnames = ["floatNodeHandle", "increment"] )
    #  PEAK_RETURN_CODE PEAK_FloatNode_GetIncrementType(PEAK_FLOAT_NODE_HANDLE floatNodeHandle, ctypes.POINTER(PEAK_NODE_INCREMENT_TYPE) incrementType)
    addfunc(lib, "PEAK_FloatNode_GetIncrementType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FLOAT_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_INCREMENT_TYPE)],
            argnames = ["floatNodeHandle", "incrementType"] )
    #  PEAK_RETURN_CODE PEAK_FloatNode_GetValidValues(PEAK_FLOAT_NODE_HANDLE floatNodeHandle, ctypes.POINTER(ctypes.c_double) validValues, ctypes.POINTER(ctypes.c_size_t) validValuesSize)
    addfunc(lib, "PEAK_FloatNode_GetValidValues", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FLOAT_NODE_HANDLE, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["floatNodeHandle", "validValues", "validValuesSize"] )
    #  PEAK_RETURN_CODE PEAK_FloatNode_GetRepresentation(PEAK_FLOAT_NODE_HANDLE floatNodeHandle, ctypes.POINTER(PEAK_NODE_REPRESENTATION) representation)
    addfunc(lib, "PEAK_FloatNode_GetRepresentation", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FLOAT_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_REPRESENTATION)],
            argnames = ["floatNodeHandle", "representation"] )
    #  PEAK_RETURN_CODE PEAK_FloatNode_GetUnit(PEAK_FLOAT_NODE_HANDLE floatNodeHandle, ctypes.c_char_p unit, ctypes.POINTER(ctypes.c_size_t) unitSize)
    addfunc(lib, "PEAK_FloatNode_GetUnit", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FLOAT_NODE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["floatNodeHandle", "unit", "unitSize"] )
    #  PEAK_RETURN_CODE PEAK_FloatNode_GetDisplayNotation(PEAK_FLOAT_NODE_HANDLE floatNodeHandle, ctypes.POINTER(PEAK_NODE_DISPLAY_NOTATION) displayNotation)
    addfunc(lib, "PEAK_FloatNode_GetDisplayNotation", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FLOAT_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_DISPLAY_NOTATION)],
            argnames = ["floatNodeHandle", "displayNotation"] )
    #  PEAK_RETURN_CODE PEAK_FloatNode_GetDisplayPrecision(PEAK_FLOAT_NODE_HANDLE floatNodeHandle, ctypes.POINTER(ctypes.c_int64) displayPrecision)
    addfunc(lib, "PEAK_FloatNode_GetDisplayPrecision", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FLOAT_NODE_HANDLE, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["floatNodeHandle", "displayPrecision"] )
    #  PEAK_RETURN_CODE PEAK_FloatNode_GetHasConstantIncrement(PEAK_FLOAT_NODE_HANDLE floatNodeHandle, ctypes.POINTER(PEAK_BOOL8) hasConstantIncrement)
    addfunc(lib, "PEAK_FloatNode_GetHasConstantIncrement", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FLOAT_NODE_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["floatNodeHandle", "hasConstantIncrement"] )
    #  PEAK_RETURN_CODE PEAK_FloatNode_GetValue(PEAK_FLOAT_NODE_HANDLE floatNodeHandle, PEAK_NODE_CACHE_USE_POLICY cacheUsePolicy, ctypes.POINTER(ctypes.c_double) value)
    addfunc(lib, "PEAK_FloatNode_GetValue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FLOAT_NODE_HANDLE, PEAK_NODE_CACHE_USE_POLICY, ctypes.POINTER(ctypes.c_double)],
            argnames = ["floatNodeHandle", "cacheUsePolicy", "value"] )
    #  PEAK_RETURN_CODE PEAK_FloatNode_SetValue(PEAK_FLOAT_NODE_HANDLE floatNodeHandle, ctypes.c_double value)
    addfunc(lib, "PEAK_FloatNode_SetValue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FLOAT_NODE_HANDLE, ctypes.c_double],
            argnames = ["floatNodeHandle", "value"] )
    #  PEAK_RETURN_CODE PEAK_StringNode_ToNode(PEAK_STRING_NODE_HANDLE stringNodeHandle, ctypes.POINTER(PEAK_NODE_HANDLE) nodeHandle)
    addfunc(lib, "PEAK_StringNode_ToNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_STRING_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["stringNodeHandle", "nodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_StringNode_GetMaximumLength(PEAK_STRING_NODE_HANDLE stringNodeHandle, ctypes.POINTER(ctypes.c_int64) maximumLength)
    addfunc(lib, "PEAK_StringNode_GetMaximumLength", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_STRING_NODE_HANDLE, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["stringNodeHandle", "maximumLength"] )
    #  PEAK_RETURN_CODE PEAK_StringNode_GetValue(PEAK_STRING_NODE_HANDLE stringNodeHandle, PEAK_NODE_CACHE_USE_POLICY cacheUsePolicy, ctypes.c_char_p value, ctypes.POINTER(ctypes.c_size_t) valueSize)
    addfunc(lib, "PEAK_StringNode_GetValue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_STRING_NODE_HANDLE, PEAK_NODE_CACHE_USE_POLICY, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["stringNodeHandle", "cacheUsePolicy", "value", "valueSize"] )
    #  PEAK_RETURN_CODE PEAK_StringNode_SetValue(PEAK_STRING_NODE_HANDLE stringNodeHandle, ctypes.c_char_p value, ctypes.c_size_t valueSize)
    addfunc(lib, "PEAK_StringNode_SetValue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_STRING_NODE_HANDLE, ctypes.c_char_p, ctypes.c_size_t],
            argnames = ["stringNodeHandle", "value", "valueSize"] )
    #  PEAK_RETURN_CODE PEAK_RegisterNode_ToNode(PEAK_REGISTER_NODE_HANDLE registerNodeHandle, ctypes.POINTER(PEAK_NODE_HANDLE) nodeHandle)
    addfunc(lib, "PEAK_RegisterNode_ToNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_REGISTER_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["registerNodeHandle", "nodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_RegisterNode_GetAddress(PEAK_REGISTER_NODE_HANDLE registerNodeHandle, ctypes.POINTER(ctypes.c_uint64) address)
    addfunc(lib, "PEAK_RegisterNode_GetAddress", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_REGISTER_NODE_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["registerNodeHandle", "address"] )
    #  PEAK_RETURN_CODE PEAK_RegisterNode_GetLength(PEAK_REGISTER_NODE_HANDLE registerNodeHandle, ctypes.POINTER(ctypes.c_size_t) length)
    addfunc(lib, "PEAK_RegisterNode_GetLength", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_REGISTER_NODE_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["registerNodeHandle", "length"] )
    #  PEAK_RETURN_CODE PEAK_RegisterNode_Read(PEAK_REGISTER_NODE_HANDLE registerNodeHandle, PEAK_NODE_CACHE_USE_POLICY cacheUsePolicy, ctypes.POINTER(ctypes.c_uint8) bytesToRead, ctypes.c_size_t bytesToReadSize)
    addfunc(lib, "PEAK_RegisterNode_Read", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_REGISTER_NODE_HANDLE, PEAK_NODE_CACHE_USE_POLICY, ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t],
            argnames = ["registerNodeHandle", "cacheUsePolicy", "bytesToRead", "bytesToReadSize"] )
    #  PEAK_RETURN_CODE PEAK_RegisterNode_Write(PEAK_REGISTER_NODE_HANDLE registerNodeHandle, ctypes.POINTER(ctypes.c_uint8) bytesToWrite, ctypes.c_size_t bytesToWriteSize)
    addfunc(lib, "PEAK_RegisterNode_Write", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_REGISTER_NODE_HANDLE, ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t],
            argnames = ["registerNodeHandle", "bytesToWrite", "bytesToWriteSize"] )
    #  PEAK_RETURN_CODE PEAK_CategoryNode_ToNode(PEAK_CATEGORY_NODE_HANDLE categoryNodeHandle, ctypes.POINTER(PEAK_NODE_HANDLE) nodeHandle)
    addfunc(lib, "PEAK_CategoryNode_ToNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_CATEGORY_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["categoryNodeHandle", "nodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_CategoryNode_GetNumSubNodes(PEAK_CATEGORY_NODE_HANDLE categoryNodeHandle, ctypes.POINTER(ctypes.c_size_t) numSubNodes)
    addfunc(lib, "PEAK_CategoryNode_GetNumSubNodes", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_CATEGORY_NODE_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["categoryNodeHandle", "numSubNodes"] )
    #  PEAK_RETURN_CODE PEAK_CategoryNode_GetSubNode(PEAK_CATEGORY_NODE_HANDLE categoryNodeHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_NODE_HANDLE) nodeHandle)
    addfunc(lib, "PEAK_CategoryNode_GetSubNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_CATEGORY_NODE_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["categoryNodeHandle", "index", "nodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_EnumerationNode_ToNode(PEAK_ENUMERATION_NODE_HANDLE enumerationNodeHandle, ctypes.POINTER(PEAK_NODE_HANDLE) nodeHandle)
    addfunc(lib, "PEAK_EnumerationNode_ToNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_ENUMERATION_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["enumerationNodeHandle", "nodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_EnumerationNode_GetCurrentEntry(PEAK_ENUMERATION_NODE_HANDLE enumerationNodeHandle, PEAK_NODE_CACHE_USE_POLICY cacheUsePolicy, ctypes.POINTER(PEAK_ENUMERATION_ENTRY_NODE_HANDLE) enumerationEntryNodeHandle)
    addfunc(lib, "PEAK_EnumerationNode_GetCurrentEntry", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_ENUMERATION_NODE_HANDLE, PEAK_NODE_CACHE_USE_POLICY, ctypes.POINTER(PEAK_ENUMERATION_ENTRY_NODE_HANDLE)],
            argnames = ["enumerationNodeHandle", "cacheUsePolicy", "enumerationEntryNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_EnumerationNode_SetCurrentEntry(PEAK_ENUMERATION_NODE_HANDLE enumerationNodeHandle, PEAK_ENUMERATION_ENTRY_NODE_HANDLE enumerationEntryNodeHandle)
    addfunc(lib, "PEAK_EnumerationNode_SetCurrentEntry", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_ENUMERATION_NODE_HANDLE, PEAK_ENUMERATION_ENTRY_NODE_HANDLE],
            argnames = ["enumerationNodeHandle", "enumerationEntryNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_EnumerationNode_SetCurrentEntryBySymbolicValue(PEAK_ENUMERATION_NODE_HANDLE enumerationNodeHandle, ctypes.c_char_p symbolicValue, ctypes.c_size_t symbolicValueSize)
    addfunc(lib, "PEAK_EnumerationNode_SetCurrentEntryBySymbolicValue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_ENUMERATION_NODE_HANDLE, ctypes.c_char_p, ctypes.c_size_t],
            argnames = ["enumerationNodeHandle", "symbolicValue", "symbolicValueSize"] )
    #  PEAK_RETURN_CODE PEAK_EnumerationNode_SetCurrentEntryByValue(PEAK_ENUMERATION_NODE_HANDLE enumerationNodeHandle, ctypes.c_int64 value)
    addfunc(lib, "PEAK_EnumerationNode_SetCurrentEntryByValue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_ENUMERATION_NODE_HANDLE, ctypes.c_int64],
            argnames = ["enumerationNodeHandle", "value"] )
    #  PEAK_RETURN_CODE PEAK_EnumerationNode_FindEntryBySymbolicValue(PEAK_ENUMERATION_NODE_HANDLE enumerationNodeHandle, ctypes.c_char_p symbolicValue, ctypes.c_size_t symbolicValueSize, ctypes.POINTER(PEAK_ENUMERATION_ENTRY_NODE_HANDLE) enumerationEntryNodeHandle)
    addfunc(lib, "PEAK_EnumerationNode_FindEntryBySymbolicValue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_ENUMERATION_NODE_HANDLE, ctypes.c_char_p, ctypes.c_size_t, ctypes.POINTER(PEAK_ENUMERATION_ENTRY_NODE_HANDLE)],
            argnames = ["enumerationNodeHandle", "symbolicValue", "symbolicValueSize", "enumerationEntryNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_EnumerationNode_FindEntryByValue(PEAK_ENUMERATION_NODE_HANDLE enumerationNodeHandle, ctypes.c_int64 value, ctypes.POINTER(PEAK_ENUMERATION_ENTRY_NODE_HANDLE) enumerationEntryNodeHandle)
    addfunc(lib, "PEAK_EnumerationNode_FindEntryByValue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_ENUMERATION_NODE_HANDLE, ctypes.c_int64, ctypes.POINTER(PEAK_ENUMERATION_ENTRY_NODE_HANDLE)],
            argnames = ["enumerationNodeHandle", "value", "enumerationEntryNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_EnumerationNode_GetNumEntries(PEAK_ENUMERATION_NODE_HANDLE enumerationNodeHandle, ctypes.POINTER(ctypes.c_size_t) numEntries)
    addfunc(lib, "PEAK_EnumerationNode_GetNumEntries", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_ENUMERATION_NODE_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["enumerationNodeHandle", "numEntries"] )
    #  PEAK_RETURN_CODE PEAK_EnumerationNode_GetEntry(PEAK_ENUMERATION_NODE_HANDLE enumerationNodeHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_ENUMERATION_ENTRY_NODE_HANDLE) enumerationEntryNodeHandle)
    addfunc(lib, "PEAK_EnumerationNode_GetEntry", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_ENUMERATION_NODE_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_ENUMERATION_ENTRY_NODE_HANDLE)],
            argnames = ["enumerationNodeHandle", "index", "enumerationEntryNodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_EnumerationEntryNode_ToNode(PEAK_ENUMERATION_ENTRY_NODE_HANDLE enumerationEntryNodeHandle, ctypes.POINTER(PEAK_NODE_HANDLE) nodeHandle)
    addfunc(lib, "PEAK_EnumerationEntryNode_ToNode", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_ENUMERATION_ENTRY_NODE_HANDLE, ctypes.POINTER(PEAK_NODE_HANDLE)],
            argnames = ["enumerationEntryNodeHandle", "nodeHandle"] )
    #  PEAK_RETURN_CODE PEAK_EnumerationEntryNode_GetIsSelfClearing(PEAK_ENUMERATION_ENTRY_NODE_HANDLE enumerationEntryNodeHandle, ctypes.POINTER(PEAK_BOOL8) isSelfClearing)
    addfunc(lib, "PEAK_EnumerationEntryNode_GetIsSelfClearing", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_ENUMERATION_ENTRY_NODE_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["enumerationEntryNodeHandle", "isSelfClearing"] )
    #  PEAK_RETURN_CODE PEAK_EnumerationEntryNode_GetSymbolicValue(PEAK_ENUMERATION_ENTRY_NODE_HANDLE enumerationEntryNodeHandle, ctypes.c_char_p symbolicValue, ctypes.POINTER(ctypes.c_size_t) symbolicValueSize)
    addfunc(lib, "PEAK_EnumerationEntryNode_GetSymbolicValue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_ENUMERATION_ENTRY_NODE_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["enumerationEntryNodeHandle", "symbolicValue", "symbolicValueSize"] )
    #  PEAK_RETURN_CODE PEAK_EnumerationEntryNode_GetValue(PEAK_ENUMERATION_ENTRY_NODE_HANDLE enumerationEntryNodeHandle, ctypes.POINTER(ctypes.c_int64) value)
    addfunc(lib, "PEAK_EnumerationEntryNode_GetValue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_ENUMERATION_ENTRY_NODE_HANDLE, ctypes.POINTER(ctypes.c_int64)],
            argnames = ["enumerationEntryNodeHandle", "value"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetInfo(PEAK_PORT_HANDLE portHandle, ctypes.c_int32 infoCommand, ctypes.POINTER(ctypes.c_int32) infoDataType, ctypes.POINTER(ctypes.c_uint8) info, ctypes.POINTER(ctypes.c_size_t) infoSize)
    addfunc(lib, "PEAK_Port_GetInfo", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["portHandle", "infoCommand", "infoDataType", "info", "infoSize"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetID(PEAK_PORT_HANDLE portHandle, ctypes.c_char_p id, ctypes.POINTER(ctypes.c_size_t) idSize)
    addfunc(lib, "PEAK_Port_GetID", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["portHandle", "id", "idSize"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetName(PEAK_PORT_HANDLE portHandle, ctypes.c_char_p name, ctypes.POINTER(ctypes.c_size_t) nameSize)
    addfunc(lib, "PEAK_Port_GetName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["portHandle", "name", "nameSize"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetVendorName(PEAK_PORT_HANDLE portHandle, ctypes.c_char_p vendorName, ctypes.POINTER(ctypes.c_size_t) vendorNameSize)
    addfunc(lib, "PEAK_Port_GetVendorName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["portHandle", "vendorName", "vendorNameSize"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetModelName(PEAK_PORT_HANDLE portHandle, ctypes.c_char_p modelName, ctypes.POINTER(ctypes.c_size_t) modelNameSize)
    addfunc(lib, "PEAK_Port_GetModelName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["portHandle", "modelName", "modelNameSize"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetVersion(PEAK_PORT_HANDLE portHandle, ctypes.c_char_p version, ctypes.POINTER(ctypes.c_size_t) versionSize)
    addfunc(lib, "PEAK_Port_GetVersion", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["portHandle", "version", "versionSize"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetTLType(PEAK_PORT_HANDLE portHandle, ctypes.c_char_p tlType, ctypes.POINTER(ctypes.c_size_t) tlTypeSize)
    addfunc(lib, "PEAK_Port_GetTLType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["portHandle", "tlType", "tlTypeSize"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetModuleName(PEAK_PORT_HANDLE portHandle, ctypes.c_char_p moduleName, ctypes.POINTER(ctypes.c_size_t) moduleNameSize)
    addfunc(lib, "PEAK_Port_GetModuleName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["portHandle", "moduleName", "moduleNameSize"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetDataEndianness(PEAK_PORT_HANDLE portHandle, ctypes.POINTER(PEAK_ENDIANNESS) dataEndianness)
    addfunc(lib, "PEAK_Port_GetDataEndianness", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.POINTER(PEAK_ENDIANNESS)],
            argnames = ["portHandle", "dataEndianness"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetIsReadable(PEAK_PORT_HANDLE portHandle, ctypes.POINTER(PEAK_BOOL8) isReadable)
    addfunc(lib, "PEAK_Port_GetIsReadable", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["portHandle", "isReadable"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetIsWritable(PEAK_PORT_HANDLE portHandle, ctypes.POINTER(PEAK_BOOL8) isWritable)
    addfunc(lib, "PEAK_Port_GetIsWritable", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["portHandle", "isWritable"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetIsAvailable(PEAK_PORT_HANDLE portHandle, ctypes.POINTER(PEAK_BOOL8) isAvailable)
    addfunc(lib, "PEAK_Port_GetIsAvailable", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["portHandle", "isAvailable"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetIsImplemented(PEAK_PORT_HANDLE portHandle, ctypes.POINTER(PEAK_BOOL8) isImplemented)
    addfunc(lib, "PEAK_Port_GetIsImplemented", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["portHandle", "isImplemented"] )
    #  PEAK_RETURN_CODE PEAK_Port_Read(PEAK_PORT_HANDLE portHandle, ctypes.c_uint64 address, ctypes.POINTER(ctypes.c_uint8) bytesToRead, ctypes.c_size_t bytesToReadSize)
    addfunc(lib, "PEAK_Port_Read", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.c_uint64, ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t],
            argnames = ["portHandle", "address", "bytesToRead", "bytesToReadSize"] )
    #  PEAK_RETURN_CODE PEAK_Port_Write(PEAK_PORT_HANDLE portHandle, ctypes.c_uint64 address, ctypes.POINTER(ctypes.c_uint8) bytesToWrite, ctypes.c_size_t bytesToWriteSize)
    addfunc(lib, "PEAK_Port_Write", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.c_uint64, ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t],
            argnames = ["portHandle", "address", "bytesToWrite", "bytesToWriteSize"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetNumURLs(PEAK_PORT_HANDLE portHandle, ctypes.POINTER(ctypes.c_size_t) numUrls)
    addfunc(lib, "PEAK_Port_GetNumURLs", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["portHandle", "numUrls"] )
    #  PEAK_RETURN_CODE PEAK_Port_GetURL(PEAK_PORT_HANDLE portHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_PORT_URL_HANDLE) portUrlHandle)
    addfunc(lib, "PEAK_Port_GetURL", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_PORT_URL_HANDLE)],
            argnames = ["portHandle", "index", "portUrlHandle"] )
    #  PEAK_RETURN_CODE PEAK_PortURL_GetInfo(PEAK_PORT_URL_HANDLE portUrlHandle, ctypes.c_int32 infoCommand, ctypes.POINTER(ctypes.c_int32) infoDataType, ctypes.POINTER(ctypes.c_uint8) info, ctypes.POINTER(ctypes.c_size_t) infoSize)
    addfunc(lib, "PEAK_PortURL_GetInfo", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_URL_HANDLE, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["portUrlHandle", "infoCommand", "infoDataType", "info", "infoSize"] )
    #  PEAK_RETURN_CODE PEAK_PortURL_GetURL(PEAK_PORT_URL_HANDLE portUrlHandle, ctypes.c_char_p url, ctypes.POINTER(ctypes.c_size_t) urlSize)
    addfunc(lib, "PEAK_PortURL_GetURL", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_URL_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["portUrlHandle", "url", "urlSize"] )
    #  PEAK_RETURN_CODE PEAK_PortURL_GetScheme(PEAK_PORT_URL_HANDLE portUrlHandle, ctypes.POINTER(PEAK_PORT_URL_SCHEME) scheme)
    addfunc(lib, "PEAK_PortURL_GetScheme", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_URL_HANDLE, ctypes.POINTER(PEAK_PORT_URL_SCHEME)],
            argnames = ["portUrlHandle", "scheme"] )
    #  PEAK_RETURN_CODE PEAK_PortURL_GetFileName(PEAK_PORT_URL_HANDLE portUrlHandle, ctypes.c_char_p fileName, ctypes.POINTER(ctypes.c_size_t) fileNameSize)
    addfunc(lib, "PEAK_PortURL_GetFileName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_URL_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["portUrlHandle", "fileName", "fileNameSize"] )
    #  PEAK_RETURN_CODE PEAK_PortURL_GetFileRegisterAddress(PEAK_PORT_URL_HANDLE portUrlHandle, ctypes.POINTER(ctypes.c_uint64) fileRegisterAddress)
    addfunc(lib, "PEAK_PortURL_GetFileRegisterAddress", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_URL_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["portUrlHandle", "fileRegisterAddress"] )
    #  PEAK_RETURN_CODE PEAK_PortURL_GetFileSize(PEAK_PORT_URL_HANDLE portUrlHandle, ctypes.POINTER(ctypes.c_uint64) fileSize)
    addfunc(lib, "PEAK_PortURL_GetFileSize", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_URL_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["portUrlHandle", "fileSize"] )
    #  PEAK_RETURN_CODE PEAK_PortURL_GetFileSHA1Hash(PEAK_PORT_URL_HANDLE portUrlHandle, ctypes.POINTER(ctypes.c_uint8) fileSha1Hash, ctypes.POINTER(ctypes.c_size_t) fileSha1HashSize)
    addfunc(lib, "PEAK_PortURL_GetFileSHA1Hash", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_URL_HANDLE, ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["portUrlHandle", "fileSha1Hash", "fileSha1HashSize"] )
    #  PEAK_RETURN_CODE PEAK_PortURL_GetFileVersionMajor(PEAK_PORT_URL_HANDLE portUrlHandle, ctypes.POINTER(ctypes.c_int32) fileVersionMajor)
    addfunc(lib, "PEAK_PortURL_GetFileVersionMajor", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_URL_HANDLE, ctypes.POINTER(ctypes.c_int32)],
            argnames = ["portUrlHandle", "fileVersionMajor"] )
    #  PEAK_RETURN_CODE PEAK_PortURL_GetFileVersionMinor(PEAK_PORT_URL_HANDLE portUrlHandle, ctypes.POINTER(ctypes.c_int32) fileVersionMinor)
    addfunc(lib, "PEAK_PortURL_GetFileVersionMinor", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_URL_HANDLE, ctypes.POINTER(ctypes.c_int32)],
            argnames = ["portUrlHandle", "fileVersionMinor"] )
    #  PEAK_RETURN_CODE PEAK_PortURL_GetFileVersionSubminor(PEAK_PORT_URL_HANDLE portUrlHandle, ctypes.POINTER(ctypes.c_int32) fileVersionSubminor)
    addfunc(lib, "PEAK_PortURL_GetFileVersionSubminor", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_URL_HANDLE, ctypes.POINTER(ctypes.c_int32)],
            argnames = ["portUrlHandle", "fileVersionSubminor"] )
    #  PEAK_RETURN_CODE PEAK_PortURL_GetFileSchemaVersionMajor(PEAK_PORT_URL_HANDLE portUrlHandle, ctypes.POINTER(ctypes.c_int32) fileSchemaVersionMajor)
    addfunc(lib, "PEAK_PortURL_GetFileSchemaVersionMajor", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_URL_HANDLE, ctypes.POINTER(ctypes.c_int32)],
            argnames = ["portUrlHandle", "fileSchemaVersionMajor"] )
    #  PEAK_RETURN_CODE PEAK_PortURL_GetFileSchemaVersionMinor(PEAK_PORT_URL_HANDLE portUrlHandle, ctypes.POINTER(ctypes.c_int32) fileSchemaVersionMinor)
    addfunc(lib, "PEAK_PortURL_GetFileSchemaVersionMinor", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_URL_HANDLE, ctypes.POINTER(ctypes.c_int32)],
            argnames = ["portUrlHandle", "fileSchemaVersionMinor"] )
    #  PEAK_RETURN_CODE PEAK_PortURL_GetParentPort(PEAK_PORT_URL_HANDLE portUrlHandle, ctypes.POINTER(PEAK_PORT_HANDLE) portHandle)
    addfunc(lib, "PEAK_PortURL_GetParentPort", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_PORT_URL_HANDLE, ctypes.POINTER(PEAK_PORT_HANDLE)],
            argnames = ["portUrlHandle", "portHandle"] )
    #  PEAK_RETURN_CODE PEAK_EventSupportingModule_EnableEvents(PEAK_EVENT_SUPPORTING_MODULE_HANDLE eventSupportingModuleHandle, PEAK_EVENT_TYPE eventType, ctypes.POINTER(PEAK_EVENT_CONTROLLER_HANDLE) eventControllerHandle)
    addfunc(lib, "PEAK_EventSupportingModule_EnableEvents", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_SUPPORTING_MODULE_HANDLE, PEAK_EVENT_TYPE, ctypes.POINTER(PEAK_EVENT_CONTROLLER_HANDLE)],
            argnames = ["eventSupportingModuleHandle", "eventType", "eventControllerHandle"] )
    #  PEAK_RETURN_CODE PEAK_EventController_GetInfo(PEAK_EVENT_CONTROLLER_HANDLE eventControllerHandle, ctypes.c_int32 infoCommand, ctypes.POINTER(ctypes.c_int32) infoDataType, ctypes.POINTER(ctypes.c_uint8) info, ctypes.POINTER(ctypes.c_size_t) infoSize)
    addfunc(lib, "PEAK_EventController_GetInfo", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_CONTROLLER_HANDLE, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["eventControllerHandle", "infoCommand", "infoDataType", "info", "infoSize"] )
    #  PEAK_RETURN_CODE PEAK_EventController_GetNumEventsInQueue(PEAK_EVENT_CONTROLLER_HANDLE eventControllerHandle, ctypes.POINTER(ctypes.c_size_t) numEventsInQueue)
    addfunc(lib, "PEAK_EventController_GetNumEventsInQueue", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_CONTROLLER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["eventControllerHandle", "numEventsInQueue"] )
    #  PEAK_RETURN_CODE PEAK_EventController_GetNumEventsFired(PEAK_EVENT_CONTROLLER_HANDLE eventControllerHandle, ctypes.POINTER(ctypes.c_uint64) numEventsFired)
    addfunc(lib, "PEAK_EventController_GetNumEventsFired", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_CONTROLLER_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["eventControllerHandle", "numEventsFired"] )
    #  PEAK_RETURN_CODE PEAK_EventController_GetEventMaxSize(PEAK_EVENT_CONTROLLER_HANDLE eventControllerHandle, ctypes.POINTER(ctypes.c_size_t) eventMaxSize)
    addfunc(lib, "PEAK_EventController_GetEventMaxSize", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_CONTROLLER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["eventControllerHandle", "eventMaxSize"] )
    #  PEAK_RETURN_CODE PEAK_EventController_GetEventDataMaxSize(PEAK_EVENT_CONTROLLER_HANDLE eventControllerHandle, ctypes.POINTER(ctypes.c_size_t) eventDataMaxSize)
    addfunc(lib, "PEAK_EventController_GetEventDataMaxSize", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_CONTROLLER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["eventControllerHandle", "eventDataMaxSize"] )
    #  PEAK_RETURN_CODE PEAK_EventController_GetControlledEventType(PEAK_EVENT_CONTROLLER_HANDLE eventControllerHandle, ctypes.POINTER(PEAK_EVENT_TYPE) controlledEventType)
    addfunc(lib, "PEAK_EventController_GetControlledEventType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_CONTROLLER_HANDLE, ctypes.POINTER(PEAK_EVENT_TYPE)],
            argnames = ["eventControllerHandle", "controlledEventType"] )
    #  PEAK_RETURN_CODE PEAK_EventController_WaitForEvent(PEAK_EVENT_CONTROLLER_HANDLE eventControllerHandle, ctypes.c_uint64 timeout_ms, ctypes.POINTER(PEAK_EVENT_HANDLE) eventHandle)
    addfunc(lib, "PEAK_EventController_WaitForEvent", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_CONTROLLER_HANDLE, ctypes.c_uint64, ctypes.POINTER(PEAK_EVENT_HANDLE)],
            argnames = ["eventControllerHandle", "timeout_ms", "eventHandle"] )
    #  PEAK_RETURN_CODE PEAK_EventController_KillWait(PEAK_EVENT_CONTROLLER_HANDLE eventControllerHandle)
    addfunc(lib, "PEAK_EventController_KillWait", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_CONTROLLER_HANDLE],
            argnames = ["eventControllerHandle"] )
    #  PEAK_RETURN_CODE PEAK_EventController_FlushEvents(PEAK_EVENT_CONTROLLER_HANDLE eventControllerHandle)
    addfunc(lib, "PEAK_EventController_FlushEvents", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_CONTROLLER_HANDLE],
            argnames = ["eventControllerHandle"] )
    #  PEAK_RETURN_CODE PEAK_EventController_Destruct(PEAK_EVENT_CONTROLLER_HANDLE eventControllerHandle)
    addfunc(lib, "PEAK_EventController_Destruct", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_CONTROLLER_HANDLE],
            argnames = ["eventControllerHandle"] )
    #  PEAK_RETURN_CODE PEAK_Event_GetInfo(PEAK_EVENT_HANDLE eventHandle, ctypes.c_int32 infoCommand, ctypes.POINTER(ctypes.c_int32) infoDataType, ctypes.POINTER(ctypes.c_uint8) info, ctypes.POINTER(ctypes.c_size_t) infoSize)
    addfunc(lib, "PEAK_Event_GetInfo", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_HANDLE, ctypes.c_int32, ctypes.POINTER(ctypes.c_int32), ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["eventHandle", "infoCommand", "infoDataType", "info", "infoSize"] )
    #  PEAK_RETURN_CODE PEAK_Event_GetID(PEAK_EVENT_HANDLE eventHandle, ctypes.POINTER(ctypes.c_uint64) id)
    addfunc(lib, "PEAK_Event_GetID", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_HANDLE, ctypes.POINTER(ctypes.c_uint64)],
            argnames = ["eventHandle", "id"] )
    #  PEAK_RETURN_CODE PEAK_Event_GetData(PEAK_EVENT_HANDLE eventHandle, ctypes.POINTER(ctypes.c_uint8) data, ctypes.POINTER(ctypes.c_size_t) dataSize)
    addfunc(lib, "PEAK_Event_GetData", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_HANDLE, ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["eventHandle", "data", "dataSize"] )
    #  PEAK_RETURN_CODE PEAK_Event_GetType(PEAK_EVENT_HANDLE eventHandle, ctypes.POINTER(PEAK_EVENT_TYPE) type)
    addfunc(lib, "PEAK_Event_GetType", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_HANDLE, ctypes.POINTER(PEAK_EVENT_TYPE)],
            argnames = ["eventHandle", "type"] )
    #  PEAK_RETURN_CODE PEAK_Event_GetRawData(PEAK_EVENT_HANDLE eventHandle, ctypes.POINTER(ctypes.c_uint8) rawData, ctypes.POINTER(ctypes.c_size_t) rawDataSize)
    addfunc(lib, "PEAK_Event_GetRawData", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_HANDLE, ctypes.POINTER(ctypes.c_uint8), ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["eventHandle", "rawData", "rawDataSize"] )
    #  PEAK_RETURN_CODE PEAK_Event_Destruct(PEAK_EVENT_HANDLE eventHandle)
    addfunc(lib, "PEAK_Event_Destruct", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_EVENT_HANDLE],
            argnames = ["eventHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdater_Construct(ctypes.POINTER(PEAK_FIRMWARE_UPDATER_HANDLE) firmwareUpdaterHandle)
    addfunc(lib, "PEAK_FirmwareUpdater_Construct", restype = PEAK_RETURN_CODE,
            argtypes = [ctypes.POINTER(PEAK_FIRMWARE_UPDATER_HANDLE)],
            argnames = ["firmwareUpdaterHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdater_CollectAllFirmwareUpdateInformation(PEAK_FIRMWARE_UPDATER_HANDLE firmwareUpdaterHandle, ctypes.c_char_p gufPath, ctypes.c_size_t gufPathSize)
    addfunc(lib, "PEAK_FirmwareUpdater_CollectAllFirmwareUpdateInformation", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATER_HANDLE, ctypes.c_char_p, ctypes.c_size_t],
            argnames = ["firmwareUpdaterHandle", "gufPath", "gufPathSize"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdater_CollectFirmwareUpdateInformation(PEAK_FIRMWARE_UPDATER_HANDLE firmwareUpdaterHandle, ctypes.c_char_p gufPath, ctypes.c_size_t gufPathSize, PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle)
    addfunc(lib, "PEAK_FirmwareUpdater_CollectFirmwareUpdateInformation", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATER_HANDLE, ctypes.c_char_p, ctypes.c_size_t, PEAK_DEVICE_DESCRIPTOR_HANDLE],
            argnames = ["firmwareUpdaterHandle", "gufPath", "gufPathSize", "deviceDescriptorHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdater_GetNumFirmwareUpdateInformation(PEAK_FIRMWARE_UPDATER_HANDLE firmwareUpdaterHandle, ctypes.POINTER(ctypes.c_size_t) numFirmwareUpdateInformation)
    addfunc(lib, "PEAK_FirmwareUpdater_GetNumFirmwareUpdateInformation", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATER_HANDLE, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["firmwareUpdaterHandle", "numFirmwareUpdateInformation"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdater_GetFirmwareUpdateInformation(PEAK_FIRMWARE_UPDATER_HANDLE firmwareUpdaterHandle, ctypes.c_size_t index, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE) firmwareUpdateInformationHandle)
    addfunc(lib, "PEAK_FirmwareUpdater_GetFirmwareUpdateInformation", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATER_HANDLE, ctypes.c_size_t, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE)],
            argnames = ["firmwareUpdaterHandle", "index", "firmwareUpdateInformationHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdater_UpdateDevice(PEAK_FIRMWARE_UPDATER_HANDLE firmwareUpdaterHandle, PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE firmwareUpdateInformationHandle, PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle)
    addfunc(lib, "PEAK_FirmwareUpdater_UpdateDevice", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATER_HANDLE, PEAK_DEVICE_DESCRIPTOR_HANDLE, PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE, PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE],
            argnames = ["firmwareUpdaterHandle", "deviceDescriptorHandle", "firmwareUpdateInformationHandle", "firmwareUpdateProgressObserverHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdater_UpdateDeviceWithResetTimeout(PEAK_FIRMWARE_UPDATER_HANDLE firmwareUpdaterHandle, PEAK_DEVICE_DESCRIPTOR_HANDLE deviceDescriptorHandle, PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE firmwareUpdateInformationHandle, PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle, ctypes.c_uint64 deviceResetDiscoveryTimeout_ms)
    addfunc(lib, "PEAK_FirmwareUpdater_UpdateDeviceWithResetTimeout", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATER_HANDLE, PEAK_DEVICE_DESCRIPTOR_HANDLE, PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE, PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE, ctypes.c_uint64],
            argnames = ["firmwareUpdaterHandle", "deviceDescriptorHandle", "firmwareUpdateInformationHandle", "firmwareUpdateProgressObserverHandle", "deviceResetDiscoveryTimeout_ms"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdater_Destruct(PEAK_FIRMWARE_UPDATER_HANDLE firmwareUpdaterHandle)
    addfunc(lib, "PEAK_FirmwareUpdater_Destruct", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATER_HANDLE],
            argnames = ["firmwareUpdaterHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateInformation_GetIsValid(PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE firmwareUpdateInformationHandle, ctypes.POINTER(PEAK_BOOL8) isValid)
    addfunc(lib, "PEAK_FirmwareUpdateInformation_GetIsValid", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE, ctypes.POINTER(PEAK_BOOL8)],
            argnames = ["firmwareUpdateInformationHandle", "isValid"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateInformation_GetFileName(PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE firmwareUpdateInformationHandle, ctypes.c_char_p fileName, ctypes.POINTER(ctypes.c_size_t) fileNameSize)
    addfunc(lib, "PEAK_FirmwareUpdateInformation_GetFileName", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["firmwareUpdateInformationHandle", "fileName", "fileNameSize"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateInformation_GetDescription(PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE firmwareUpdateInformationHandle, ctypes.c_char_p description, ctypes.POINTER(ctypes.c_size_t) descriptionSize)
    addfunc(lib, "PEAK_FirmwareUpdateInformation_GetDescription", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["firmwareUpdateInformationHandle", "description", "descriptionSize"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateInformation_GetVersion(PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE firmwareUpdateInformationHandle, ctypes.c_char_p version, ctypes.POINTER(ctypes.c_size_t) versionSize)
    addfunc(lib, "PEAK_FirmwareUpdateInformation_GetVersion", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["firmwareUpdateInformationHandle", "version", "versionSize"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateInformation_GetVersionExtractionPattern(PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE firmwareUpdateInformationHandle, ctypes.c_char_p versionExtractionPattern, ctypes.POINTER(ctypes.c_size_t) versionExtractionPatternSize)
    addfunc(lib, "PEAK_FirmwareUpdateInformation_GetVersionExtractionPattern", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["firmwareUpdateInformationHandle", "versionExtractionPattern", "versionExtractionPatternSize"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateInformation_GetVersionStyle(PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE firmwareUpdateInformationHandle, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_VERSION_STYLE) versionStyle)
    addfunc(lib, "PEAK_FirmwareUpdateInformation_GetVersionStyle", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_VERSION_STYLE)],
            argnames = ["firmwareUpdateInformationHandle", "versionStyle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateInformation_GetReleaseNotes(PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE firmwareUpdateInformationHandle, ctypes.c_char_p releaseNotes, ctypes.POINTER(ctypes.c_size_t) releaseNotesSize)
    addfunc(lib, "PEAK_FirmwareUpdateInformation_GetReleaseNotes", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["firmwareUpdateInformationHandle", "releaseNotes", "releaseNotesSize"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateInformation_GetReleaseNotesURL(PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE firmwareUpdateInformationHandle, ctypes.c_char_p releaseNotesUrl, ctypes.POINTER(ctypes.c_size_t) releaseNotesUrlSize)
    addfunc(lib, "PEAK_FirmwareUpdateInformation_GetReleaseNotesURL", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE, ctypes.c_char_p, ctypes.POINTER(ctypes.c_size_t)],
            argnames = ["firmwareUpdateInformationHandle", "releaseNotesUrl", "releaseNotesUrlSize"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateInformation_GetUserSetPersistence(PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE firmwareUpdateInformationHandle, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_PERSISTENCE) userSetPersistence)
    addfunc(lib, "PEAK_FirmwareUpdateInformation_GetUserSetPersistence", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_PERSISTENCE)],
            argnames = ["firmwareUpdateInformationHandle", "userSetPersistence"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateInformation_GetSequencerSetPersistence(PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE firmwareUpdateInformationHandle, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_PERSISTENCE) sequencerSetPersistence)
    addfunc(lib, "PEAK_FirmwareUpdateInformation_GetSequencerSetPersistence", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_INFORMATION_HANDLE, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_PERSISTENCE)],
            argnames = ["firmwareUpdateInformationHandle", "sequencerSetPersistence"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateProgressObserver_Construct(ctypes.POINTER(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE) firmwareUpdateProgressObserverHandle)
    addfunc(lib, "PEAK_FirmwareUpdateProgressObserver_Construct", restype = PEAK_RETURN_CODE,
            argtypes = [ctypes.POINTER(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE)],
            argnames = ["firmwareUpdateProgressObserverHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateProgressObserver_RegisterUpdateStartedCallback(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle, PEAK_FIRMWARE_UPDATE_STARTED_CALLBACK callback, ctypes.c_void_p callbackContext, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_STARTED_CALLBACK_HANDLE) callbackHandle)
    addfunc(lib, "PEAK_FirmwareUpdateProgressObserver_RegisterUpdateStartedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE, PEAK_FIRMWARE_UPDATE_STARTED_CALLBACK, ctypes.c_void_p, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_STARTED_CALLBACK_HANDLE)],
            argnames = ["firmwareUpdateProgressObserverHandle", "callback", "callbackContext", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateProgressObserver_UnregisterUpdateStartedCallback(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle, PEAK_FIRMWARE_UPDATE_STARTED_CALLBACK_HANDLE callbackHandle)
    addfunc(lib, "PEAK_FirmwareUpdateProgressObserver_UnregisterUpdateStartedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE, PEAK_FIRMWARE_UPDATE_STARTED_CALLBACK_HANDLE],
            argnames = ["firmwareUpdateProgressObserverHandle", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateProgressObserver_RegisterUpdateStepStartedCallback(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle, PEAK_FIRMWARE_UPDATE_STEP_STARTED_CALLBACK callback, ctypes.c_void_p callbackContext, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_STEP_STARTED_CALLBACK_HANDLE) callbackHandle)
    addfunc(lib, "PEAK_FirmwareUpdateProgressObserver_RegisterUpdateStepStartedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE, PEAK_FIRMWARE_UPDATE_STEP_STARTED_CALLBACK, ctypes.c_void_p, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_STEP_STARTED_CALLBACK_HANDLE)],
            argnames = ["firmwareUpdateProgressObserverHandle", "callback", "callbackContext", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateProgressObserver_UnregisterUpdateStepStartedCallback(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle, PEAK_FIRMWARE_UPDATE_STEP_STARTED_CALLBACK_HANDLE callbackHandle)
    addfunc(lib, "PEAK_FirmwareUpdateProgressObserver_UnregisterUpdateStepStartedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE, PEAK_FIRMWARE_UPDATE_STEP_STARTED_CALLBACK_HANDLE],
            argnames = ["firmwareUpdateProgressObserverHandle", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateProgressObserver_RegisterUpdateStepProgressChangedCallback(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle, PEAK_FIRMWARE_UPDATE_STEP_PROGRESS_CHANGED_CALLBACK callback, ctypes.c_void_p callbackContext, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_STEP_PROGRESS_CHANGED_CALLBACK_HANDLE) callbackHandle)
    addfunc(lib, "PEAK_FirmwareUpdateProgressObserver_RegisterUpdateStepProgressChangedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE, PEAK_FIRMWARE_UPDATE_STEP_PROGRESS_CHANGED_CALLBACK, ctypes.c_void_p, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_STEP_PROGRESS_CHANGED_CALLBACK_HANDLE)],
            argnames = ["firmwareUpdateProgressObserverHandle", "callback", "callbackContext", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateProgressObserver_UnregisterUpdateStepProgressChangedCallback(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle, PEAK_FIRMWARE_UPDATE_STEP_PROGRESS_CHANGED_CALLBACK_HANDLE callbackHandle)
    addfunc(lib, "PEAK_FirmwareUpdateProgressObserver_UnregisterUpdateStepProgressChangedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE, PEAK_FIRMWARE_UPDATE_STEP_PROGRESS_CHANGED_CALLBACK_HANDLE],
            argnames = ["firmwareUpdateProgressObserverHandle", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateProgressObserver_RegisterUpdateStepFinishedCallback(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle, PEAK_FIRMWARE_UPDATE_STEP_FINISHED_CALLBACK callback, ctypes.c_void_p callbackContext, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_STEP_FINISHED_CALLBACK_HANDLE) callbackHandle)
    addfunc(lib, "PEAK_FirmwareUpdateProgressObserver_RegisterUpdateStepFinishedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE, PEAK_FIRMWARE_UPDATE_STEP_FINISHED_CALLBACK, ctypes.c_void_p, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_STEP_FINISHED_CALLBACK_HANDLE)],
            argnames = ["firmwareUpdateProgressObserverHandle", "callback", "callbackContext", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateProgressObserver_UnregisterUpdateStepFinishedCallback(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle, PEAK_FIRMWARE_UPDATE_STEP_FINISHED_CALLBACK_HANDLE callbackHandle)
    addfunc(lib, "PEAK_FirmwareUpdateProgressObserver_UnregisterUpdateStepFinishedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE, PEAK_FIRMWARE_UPDATE_STEP_FINISHED_CALLBACK_HANDLE],
            argnames = ["firmwareUpdateProgressObserverHandle", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateProgressObserver_RegisterUpdateFinishedCallback(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle, PEAK_FIRMWARE_UPDATE_FINISHED_CALLBACK callback, ctypes.c_void_p callbackContext, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_FINISHED_CALLBACK_HANDLE) callbackHandle)
    addfunc(lib, "PEAK_FirmwareUpdateProgressObserver_RegisterUpdateFinishedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE, PEAK_FIRMWARE_UPDATE_FINISHED_CALLBACK, ctypes.c_void_p, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_FINISHED_CALLBACK_HANDLE)],
            argnames = ["firmwareUpdateProgressObserverHandle", "callback", "callbackContext", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateProgressObserver_UnregisterUpdateFinishedCallback(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle, PEAK_FIRMWARE_UPDATE_FINISHED_CALLBACK_HANDLE callbackHandle)
    addfunc(lib, "PEAK_FirmwareUpdateProgressObserver_UnregisterUpdateFinishedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE, PEAK_FIRMWARE_UPDATE_FINISHED_CALLBACK_HANDLE],
            argnames = ["firmwareUpdateProgressObserverHandle", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateProgressObserver_RegisterUpdateFailedCallback(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle, PEAK_FIRMWARE_UPDATE_FAILED_CALLBACK callback, ctypes.c_void_p callbackContext, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_FAILED_CALLBACK_HANDLE) callbackHandle)
    addfunc(lib, "PEAK_FirmwareUpdateProgressObserver_RegisterUpdateFailedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE, PEAK_FIRMWARE_UPDATE_FAILED_CALLBACK, ctypes.c_void_p, ctypes.POINTER(PEAK_FIRMWARE_UPDATE_FAILED_CALLBACK_HANDLE)],
            argnames = ["firmwareUpdateProgressObserverHandle", "callback", "callbackContext", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateProgressObserver_UnregisterUpdateFailedCallback(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle, PEAK_FIRMWARE_UPDATE_FAILED_CALLBACK_HANDLE callbackHandle)
    addfunc(lib, "PEAK_FirmwareUpdateProgressObserver_UnregisterUpdateFailedCallback", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE, PEAK_FIRMWARE_UPDATE_FAILED_CALLBACK_HANDLE],
            argnames = ["firmwareUpdateProgressObserverHandle", "callbackHandle"] )
    #  PEAK_RETURN_CODE PEAK_FirmwareUpdateProgressObserver_Destruct(PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE firmwareUpdateProgressObserverHandle)
    addfunc(lib, "PEAK_FirmwareUpdateProgressObserver_Destruct", restype = PEAK_RETURN_CODE,
            argtypes = [PEAK_FIRMWARE_UPDATE_PROGRESS_OBSERVER_HANDLE],
            argnames = ["firmwareUpdateProgressObserverHandle"] )


