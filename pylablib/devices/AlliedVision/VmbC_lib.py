# pylint: disable=wrong-spelling-in-comment

from . import VmbC_defs  # pylint: disable=unused-import
from .VmbC_defs import drVmbErrorType
from .VmbC_defs import CVmbVersionInfo_t
from .VmbC_defs import VmbCameraInfo_t, CVmbCameraInfo_t
from .VmbC_defs import VmbFeatureInfo_t, CVmbFeatureInfo_t
from .VmbC_defs import CVmbFeatureEnumEntry_t
from .VmbC_defs import CVmbFrame_t
from .VmbC_defs import define_functions

from ...core.utils import ctypes_wrap
from .base import AlliedVisionError
from ..utils import load_lib

import ctypes
import os


class AlliedVisionVimbaXError(AlliedVisionError):
    """Generic Allied Vision Vimba X error"""
class AlliedVisionVimbaXLibError(AlliedVisionVimbaXError):
    """Generic Allied Vision Vimba X library error"""
    def __init__(self, func, code):
        self.func=func
        self.code=code
        self.name=drVmbErrorType.get(code,"N/A")
        self.msg="function '{}' raised error {}({})".format(func,code,self.name)
        super().__init__(self.msg)
def errcheck(passing=None):
    """
    Build an error checking function.

    Return a function which checks return codes of IDS peak library functions.
    `passing` is a list specifying which return codes are acceptable (by default only 0, which is success code, is acceptable).
    """
    if passing is None:
        passing={0}
    def errchecker(result, func, arguments):  # pylint: disable=unused-argument
        if result not in passing:
            raise AlliedVisionVimbaXLibError(func.__name__,result)
        return result
    return errchecker


class AlliedVisionVmbCLib:
    def __init__(self):
        self._initialized=False

    def initlib(self):
        if self._initialized:
            return
        sdk_path=os.environ.get("VIMBA_X_HOME")
        if sdk_path is None:
            sdk_path=load_lib.get_program_files_folder(os.path.join("Allied Vision","Vimba X"))
        lib_path=os.path.join(sdk_path,"bin")
        error_message="The library is automatically supplied with Allied Vision Vimba X software\n"+load_lib.par_error_message.format("alliedvision_vimbax")
        self.lib=load_lib.load_lib("VmbC.dll",locations=("parameter/alliedvision_vimbax",lib_path,"global"),error_message=error_message,call_conv="cdecl",locally=True)
        lib=self.lib
        define_functions(lib)

        wrapper=ctypes_wrap.CFunctionWrapper(errcheck=errcheck(),default_rvals="pointer")
        #  VmbError_t VmbVersionQuery(ctypes.POINTER(VmbVersionInfo_t) versionInfo, VmbUint32_t sizeofVersionInfo)
        self.VmbVersionQuery=wrapper(lib.VmbVersionQuery, args=[], rvals=["versionInfo"],
                argprep={"versionInfo":CVmbVersionInfo_t.prep_struct,"sizeofVersionInfo":CVmbVersionInfo_t.size}, rconv={"versionInfo":CVmbVersionInfo_t.tup_struct})
        #  VmbError_t VmbStartup(ctypes.c_wchar_p pathConfiguration)
        self.VmbStartup=wrapper(lib.VmbStartup)
        #  None VmbShutdown()
        self.VmbShutdown=ctypes_wrap.CFunctionWrapper()(lib.VmbShutdown)

        #  VmbError_t VmbCamerasList(ctypes.POINTER(VmbCameraInfo_t) cameraInfo, VmbUint32_t listLength, ctypes.POINTER(VmbUint32_t) numFound, VmbUint32_t sizeofCameraInfo)
        self.VmbCamerasList_lib=wrapper(lib.VmbCamerasList, args=["cameraInfo","listLength"], rvals=["numFound"],
                argprep={"sizeofCameraInfo":CVmbCameraInfo_t.size})
        #  VmbError_t VmbCameraInfoQueryByHandle(VmbHandle_t cameraHandle, ctypes.POINTER(VmbCameraInfo_t) info, VmbUint32_t sizeofCameraInfo)
        self.VmbCameraInfoQueryByHandle=wrapper(lib.VmbCameraInfoQueryByHandle, args=["cameraHandle"], rvals=["info"],
                argprep={"info":CVmbCameraInfo_t.prep_struct,"sizeofCameraInfo":CVmbCameraInfo_t.size}, rconv={"info":CVmbCameraInfo_t.tup_struct})
        #  VmbError_t VmbCameraInfoQuery(ctypes.c_char_p idString, ctypes.POINTER(VmbCameraInfo_t) info, VmbUint32_t sizeofCameraInfo)
        self.VmbCameraInfoQuery=wrapper(lib.VmbCameraInfoQuery, args=["idString"], rvals=["info"],
                argprep={"info":CVmbCameraInfo_t.prep_struct,"sizeofCameraInfo":CVmbCameraInfo_t.size}, rconv={"info":CVmbCameraInfo_t.tup_struct})
        
        
        
        #  VmbError_t VmbCameraOpen(ctypes.c_char_p idString, VmbAccessMode_t accessMode, ctypes.POINTER(VmbHandle_t) cameraHandle)
        self.VmbCameraOpen=wrapper(lib.VmbCameraOpen)
        #  VmbError_t VmbCameraClose(VmbHandle_t cameraHandle)
        self.VmbCameraClose=wrapper(lib.VmbCameraClose)

        #  VmbError_t VmbFeaturesList(VmbHandle_t handle, ctypes.POINTER(VmbFeatureInfo_t) featureInfoList, VmbUint32_t listLength, ctypes.POINTER(VmbUint32_t) numFound, VmbUint32_t sizeofFeatureInfo)
        self.VmbFeaturesList_lib=wrapper(lib.VmbFeaturesList, args=["handle","featureInfoList","listLength"], rvals=["numFound"],
                argprep={"sizeofFeatureInfo":CVmbFeatureInfo_t.size})
        #  VmbError_t VmbFeatureInfoQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbFeatureInfo_t) featureInfo, VmbUint32_t sizeofFeatureInfo)
        self.VmbFeatureInfoQuery=wrapper(lib.VmbFeatureInfoQuery, args=["handle","name"], rvals=["featureInfo"],
                argprep={"featureInfo":CVmbFeatureInfo_t.prep_struct,"sizeofFeatureInfo":CVmbFeatureInfo_t.size}, rconv={"featureInfo":CVmbFeatureInfo_t.tup_struct})
        #  VmbError_t VmbFeatureAccessQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbBool_t) isReadable, ctypes.POINTER(VmbBool_t) isWriteable)
        self.VmbFeatureAccessQuery=wrapper(lib.VmbFeatureAccessQuery)

        #  VmbError_t VmbFeatureIntGet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbInt64_t) value)
        self.VmbFeatureIntGet=wrapper(lib.VmbFeatureIntGet)
        #  VmbError_t VmbFeatureIntSet(VmbHandle_t handle, ctypes.c_char_p name, VmbInt64_t value)
        self.VmbFeatureIntSet=wrapper(lib.VmbFeatureIntSet)
        #  VmbError_t VmbFeatureIntRangeQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbInt64_t) min, ctypes.POINTER(VmbInt64_t) max)
        self.VmbFeatureIntRangeQuery=wrapper(lib.VmbFeatureIntRangeQuery)
        #  VmbError_t VmbFeatureIntIncrementQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbInt64_t) value)
        self.VmbFeatureIntIncrementQuery=wrapper(lib.VmbFeatureIntIncrementQuery)
        #  VmbError_t VmbFeatureIntValidValueSetQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbInt64_t) buffer, VmbUint32_t bufferSize, ctypes.POINTER(VmbUint32_t) setSize)
        self.VmbFeatureIntValidValueSetQuery_lib=wrapper(lib.VmbFeatureIntValidValueSetQuery, args=["handle","name","buffer","bufferSize"], rvals=["setSize"])

        #  VmbError_t VmbFeatureFloatGet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(ctypes.c_double) value)
        self.VmbFeatureFloatGet=wrapper(lib.VmbFeatureFloatGet)
        #  VmbError_t VmbFeatureFloatSet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_double value)
        self.VmbFeatureFloatSet=wrapper(lib.VmbFeatureFloatSet)
        #  VmbError_t VmbFeatureFloatRangeQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(ctypes.c_double) min, ctypes.POINTER(ctypes.c_double) max)
        self.VmbFeatureFloatRangeQuery=wrapper(lib.VmbFeatureFloatRangeQuery)
        #  VmbError_t VmbFeatureFloatIncrementQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbBool_t) hasIncrement, ctypes.POINTER(ctypes.c_double) value)
        self.VmbFeatureFloatIncrementQuery=wrapper(lib.VmbFeatureFloatIncrementQuery)

        #  VmbError_t VmbFeatureEnumGet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(ctypes.c_char_p) value)
        self.VmbFeatureEnumGet=wrapper(lib.VmbFeatureEnumGet)
        #  VmbError_t VmbFeatureEnumSet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_char_p value)
        self.VmbFeatureEnumSet=wrapper(lib.VmbFeatureEnumSet)
        #  VmbError_t VmbFeatureEnumRangeQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(ctypes.c_char_p) nameArray, VmbUint32_t arrayLength, ctypes.POINTER(VmbUint32_t) numFound)
        self.VmbFeatureEnumRangeQuery_lib=wrapper(lib.VmbFeatureEnumRangeQuery, args=["handle","name","nameArray","arrayLength"], rvals=["numFound"])
        #  VmbError_t VmbFeatureEnumIsAvailable(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_char_p value, ctypes.POINTER(VmbBool_t) isAvailable)
        self.VmbFeatureEnumIsAvailable=wrapper(lib.VmbFeatureEnumIsAvailable)
        #  VmbError_t VmbFeatureEnumAsInt(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_char_p value, ctypes.POINTER(VmbInt64_t) intVal)
        self.VmbFeatureEnumAsInt=wrapper(lib.VmbFeatureEnumAsInt)
        #  VmbError_t VmbFeatureEnumAsString(VmbHandle_t handle, ctypes.c_char_p name, VmbInt64_t intValue, ctypes.POINTER(ctypes.c_char_p) stringValue)
        self.VmbFeatureEnumAsString=wrapper(lib.VmbFeatureEnumAsString)
        #  VmbError_t VmbFeatureEnumEntryGet(VmbHandle_t handle, ctypes.c_char_p featureName, ctypes.c_char_p entryName, ctypes.POINTER(VmbFeatureEnumEntry_t) featureEnumEntry, VmbUint32_t sizeofFeatureEnumEntry)
        self.VmbFeatureEnumEntryGet=wrapper(lib.VmbFeatureEnumEntryGet, args=["handle","featureName","entryName"], rvals=["featureEnumEntry"],
                argprep={"featureEnumEntry":CVmbFeatureEnumEntry_t.prep_struct,"sizeofFeatureEnumEntry":CVmbFeatureEnumEntry_t.size},
                rconv={"featureEnumEntry":CVmbFeatureEnumEntry_t.tup_struct})

        #  VmbError_t VmbFeatureStringGet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_char_p buffer, VmbUint32_t bufferSize, ctypes.POINTER(VmbUint32_t) sizeFilled)
        self.VmbFeatureStringGet_lib=wrapper(lib.VmbFeatureStringGet, args=["handle","name","buffer","bufferSize"], rvals=["sizeFilled"])
        #  VmbError_t VmbFeatureStringSet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_char_p value)
        self.VmbFeatureStringSet=wrapper(lib.VmbFeatureStringSet)
        #  VmbError_t VmbFeatureStringMaxlengthQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbUint32_t) maxLength)
        self.VmbFeatureStringMaxlengthQuery=wrapper(lib.VmbFeatureStringMaxlengthQuery)

        #  VmbError_t VmbFeatureBoolGet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbBool_t) value)
        self.VmbFeatureBoolGet=wrapper(lib.VmbFeatureBoolGet)
        #  VmbError_t VmbFeatureBoolSet(VmbHandle_t handle, ctypes.c_char_p name, VmbBool_t value)
        self.VmbFeatureBoolSet=wrapper(lib.VmbFeatureBoolSet)

        #  VmbError_t VmbFeatureCommandRun(VmbHandle_t handle, ctypes.c_char_p name)
        self.VmbFeatureCommandRun=wrapper(lib.VmbFeatureCommandRun)
        #  VmbError_t VmbFeatureCommandIsDone(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbBool_t) isDone)
        self.VmbFeatureCommandIsDone=wrapper(lib.VmbFeatureCommandIsDone)

        #  VmbError_t VmbFeatureRawGet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_char_p buffer, VmbUint32_t bufferSize, ctypes.POINTER(VmbUint32_t) sizeFilled)
        self.VmbFeatureRawGet_lib=wrapper(lib.VmbFeatureRawGet)
        #  VmbError_t VmbFeatureRawSet(VmbHandle_t handle, ctypes.c_char_p name, ctypes.c_char_p buffer, VmbUint32_t bufferSize)
        self.VmbFeatureRawSet=wrapper(lib.VmbFeatureRawSet)
        #  VmbError_t VmbFeatureRawLengthQuery(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbUint32_t) length)
        self.VmbFeatureRawLengthQuery=wrapper(lib.VmbFeatureRawLengthQuery)

        #  VmbError_t VmbPayloadSizeGet(VmbHandle_t handle, ctypes.POINTER(VmbUint32_t) payloadSize)
        self.VmbPayloadSizeGet=wrapper(lib.VmbPayloadSizeGet)
        #  VmbError_t VmbFrameAnnounce(VmbHandle_t handle, ctypes.POINTER(VmbFrame_t) frame, VmbUint32_t sizeofFrame)
        self.VmbFrameAnnounce_lib=wrapper(lib.VmbFrameAnnounce, args=["handle","frame"], rvals=[],
                argprep={"sizeofFrame":CVmbFrame_t.size})
        #  VmbError_t VmbFrameRevoke(VmbHandle_t handle, ctypes.POINTER(VmbFrame_t) frame)
        self.VmbFrameRevoke=wrapper(lib.VmbFrameRevoke, args=["handle","frame"], rvals=[])
        #  VmbError_t VmbFrameRevokeAll(VmbHandle_t handle)
        self.VmbFrameRevokeAll=wrapper(lib.VmbFrameRevokeAll)
        #  VmbError_t VmbCaptureStart(VmbHandle_t handle)
        self.VmbCaptureStart=wrapper(lib.VmbCaptureStart)
        #  VmbError_t VmbCaptureEnd(VmbHandle_t handle)
        self.VmbCaptureEnd=wrapper(lib.VmbCaptureEnd)
        #  VmbError_t VmbCaptureFrameQueue(VmbHandle_t handle, ctypes.POINTER(VmbFrame_t) frame, VmbFrameCallback callback)
        self.VmbCaptureFrameQueue=wrapper(lib.VmbCaptureFrameQueue, args=["handle","frame","callback"], rvals=[])
        #  VmbError_t VmbCaptureFrameWait(VmbHandle_t handle, ctypes.POINTER(VmbFrame_t) frame, VmbUint32_t timeout)
        self.VmbCaptureFrameWait=wrapper(lib.VmbCaptureFrameWait, args=["handle","frame","timeout"], rvals=[])
        #  VmbError_t VmbCaptureQueueFlush(VmbHandle_t handle)
        self.VmbCaptureQueueFlush=wrapper(lib.VmbCaptureQueueFlush)

        # #  VmbError_t VmbTransportLayersList(ctypes.POINTER(VmbTransportLayerInfo_t) transportLayerInfo, VmbUint32_t listLength, ctypes.POINTER(VmbUint32_t) numFound, VmbUint32_t sizeofTransportLayerInfo)
        # self.VmbTransportLayersList=wrapper(lib.VmbTransportLayersList)
        # #  VmbError_t VmbInterfacesList(ctypes.POINTER(VmbInterfaceInfo_t) interfaceInfo, VmbUint32_t listLength, ctypes.POINTER(VmbUint32_t) numFound, VmbUint32_t sizeofInterfaceInfo)
        # self.VmbInterfacesList=wrapper(lib.VmbInterfacesList)
        # #  VmbError_t VmbMemoryRead(VmbHandle_t handle, VmbUint64_t address, VmbUint32_t bufferSize, ctypes.c_char_p dataBuffer, ctypes.POINTER(VmbUint32_t) sizeComplete)
        # self.VmbMemoryRead=wrapper(lib.VmbMemoryRead)
        # #  VmbError_t VmbMemoryWrite(VmbHandle_t handle, VmbUint64_t address, VmbUint32_t bufferSize, ctypes.c_char_p dataBuffer, ctypes.POINTER(VmbUint32_t) sizeComplete)
        # self.VmbMemoryWrite=wrapper(lib.VmbMemoryWrite)
        # #  VmbError_t VmbChunkDataAccess(ctypes.POINTER(VmbFrame_t) frame, VmbChunkAccessCallback chunkAccessCallback, ctypes.c_void_p userContext)
        # self.VmbChunkDataAccess=wrapper(lib.VmbChunkDataAccess)

        # #  VmbError_t VmbFeatureListSelected(VmbHandle_t handle, ctypes.c_char_p name, ctypes.POINTER(VmbFeatureInfo_t) featureInfoList, VmbUint32_t listLength, ctypes.POINTER(VmbUint32_t) numFound, VmbUint32_t sizeofFeatureInfo)
        # self.VmbFeatureListSelected=wrapper(lib.VmbFeatureListSelected)
        # #  VmbError_t VmbFeatureInvalidationRegister(VmbHandle_t handle, ctypes.c_char_p name, VmbInvalidationCallback callback, ctypes.c_void_p userContext)
        # self.VmbFeatureInvalidationRegister=wrapper(lib.VmbFeatureInvalidationRegister)
        # #  VmbError_t VmbFeatureInvalidationUnregister(VmbHandle_t handle, ctypes.c_char_p name, VmbInvalidationCallback callback)
        # self.VmbFeatureInvalidationUnregister=wrapper(lib.VmbFeatureInvalidationUnregister)
        # #  VmbError_t VmbSettingsSave(VmbHandle_t handle, ctypes.c_wchar_p filePath, ctypes.POINTER(VmbFeaturePersistSettings_t) settings, VmbUint32_t sizeofSettings)
        # self.VmbSettingsSave=wrapper(lib.VmbSettingsSave)
        # #  VmbError_t VmbSettingsLoad(VmbHandle_t handle, ctypes.c_wchar_p filePath, ctypes.POINTER(VmbFeaturePersistSettings_t) settings, VmbUint32_t sizeofSettings)
        # self.VmbSettingsLoad=wrapper(lib.VmbSettingsLoad)

        

    def VmbCamerasList(self):
        ncam=self.VmbCamerasList_lib(None,0)
        cams=(VmbCameraInfo_t*ncam)()
        self.VmbCamerasList_lib(cams,ncam)
        return [CVmbCameraInfo_t.tup_struct(cams[i]) for i in range(ncam)]
    def VmbFeaturesList(self, handle):
        nfeat=self.VmbFeaturesList_lib(handle,None,0)
        feats=(VmbFeatureInfo_t*nfeat)()
        self.VmbFeaturesList_lib(handle,feats,nfeat)
        return [CVmbFeatureInfo_t.tup_struct(feats[i]) for i in range(nfeat)]
    def VmbFeatureIntValidValueSetQuery(self, handle, name):
        nval=self.VmbFeatureIntValidValueSetQuery_lib(handle,name,None,0)
        vals=(VmbC_defs.VmbUint32_t*nval)()
        self.VmbFeatureIntValidValueSetQuery_lib(handle,name,vals,nval)
        return list(vals)
    def VmbFeatureEnumRangeQuery(self, handle, name):
        nval=self.VmbFeatureEnumRangeQuery_lib(handle,name,None,0)
        vals=(ctypes.c_char_p*nval)()
        self.VmbFeatureEnumRangeQuery_lib(handle,name,vals,nval)
        return [ctypes.string_at(vals[i]) for i in range(nval)]
    def VmbFeatureStringGet(self, handle, name):
        l=self.VmbFeatureStringGet_lib(handle,name,None,0)
        s=ctypes.create_string_buffer(l)
        self.VmbFeatureStringGet_lib(handle,name,ctypes.addressof(s),l)
        return ctypes.string_at(s)
    def VmbFeatureRawGet(self, handle, name):
        l=self.VmbFeatureRawLengthQuery(handle,name)
        s=ctypes.create_string_buffer(l)
        lset=self.VmbFeatureRawGet_lib(handle,name,ctypes.addressof(s),l)
        return ctypes.string_at(s,lset)
    def VmbFrameAnnounce(self, handle, buffer, size, context):
        frame=CVmbFrame_t.prep_struct_args(buffer=buffer,bufferSize=size)
        frame.context[0]=context
        self.VmbFrameAnnounce_lib(handle,ctypes.pointer(frame))
        return frame

wlib=AlliedVisionVmbCLib()