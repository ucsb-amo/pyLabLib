ctypedef unsigned long long int uint64_t

ctypedef int (*pPEAK_DataStream_QueueBuffer)(void *dataStreamHandle, void *bufferHandle) noexcept nogil
ctypedef int (*pPEAK_DataStream_WaitForFinishedBuffer)(void *dataStreamHandle, uint64_t timeout_ms, void **bufferHandle) noexcept nogil

cdef enum:
    PEAK_RETURN_CODE_SUCCESS=0
    PEAK_RETURN_CODE_TIMEOUT=13

cdef int clooper(void *dataStreamHandle, unsigned *looping,
            pPEAK_DataStream_QueueBuffer PEAK_DataStream_QueueBuffer, pPEAK_DataStream_WaitForFinishedBuffer PEAK_DataStream_WaitForFinishedBuffer) nogil:
    cdef int code=0
    cdef void *buff
    while looping[0]:
        code=PEAK_DataStream_WaitForFinishedBuffer(dataStreamHandle,10,&buff)
        if code==PEAK_RETURN_CODE_TIMEOUT:
            continue
        if code!=PEAK_RETURN_CODE_SUCCESS:
            return code|0x10000
        code=PEAK_DataStream_QueueBuffer(dataStreamHandle,buff)
        if code!=PEAK_RETURN_CODE_SUCCESS:
            return code
    return PEAK_RETURN_CODE_SUCCESS

def looper(size_t dataStreamHandle, size_t looping, size_t PEAK_DataStream_QueueBuffer, size_t PEAK_DataStream_WaitForFinishedBuffer):
    cdef int result=PEAK_RETURN_CODE_SUCCESS
    with nogil:
        result=clooper(<void*>dataStreamHandle,<unsigned*>looping,
                    <pPEAK_DataStream_QueueBuffer>PEAK_DataStream_QueueBuffer,<pPEAK_DataStream_WaitForFinishedBuffer>PEAK_DataStream_WaitForFinishedBuffer)
    return result