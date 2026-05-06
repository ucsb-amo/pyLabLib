import cython
from libc.string cimport memcpy

ctypedef unsigned long uint32_t
ctypedef unsigned long long uint64_t
ctypedef int (*pVmbCaptureFrameQueue)(void *handle, void *frame, void *callback) noexcept nogil

@cython.cdivision(True)
cdef void ccallback(void *camhandle, void *strmhandle, char *frame) noexcept nogil:
    cdef char *fbuff=(<char**>(frame+0))[0]
    cdef size_t *context=(<size_t**>(frame+16))[0]
    cdef size_t *funcs=<size_t*>(context[0])
    cdef size_t *ctl=<size_t*>(context[1])
    cdef size_t *buff=<size_t*>(context[2])
    cdef size_t *stat=<size_t*>(context[3])
    stat[0]+=1
    cdef pVmbCaptureFrameQueue VmbCaptureFrameQueue=<pVmbCaptureFrameQueue>(funcs[0])
    cdef void *callback=<void*>(funcs[1])
    if (not ctl[0]) or (ctl[2]!=0):
        return
    cdef int err=0
    cdef size_t idx=<size_t>(fbuff-buff[3])/buff[1]
    cdef size_t *pfibuff=<size_t*>(buff[4]+idx*buff[2])
    if ctl[1]:
        pfibuff[0]=(<size_t*>(frame+56))[0]
        pfibuff[1]=(<size_t*>(frame+64))[0]
        pfibuff[2]=(<uint32_t*>(frame+88))[0]
        pfibuff[3]=(<uint32_t*>(frame+92))[0]
        pfibuff[4]=(<uint32_t*>(frame+96))[0]
        pfibuff[5]=(<uint32_t*>(frame+100))[0]
    err=VmbCaptureFrameQueue(camhandle,frame,callback)
    if err:
        ctl[2]=err
        return
def get_callback():
    return <size_t>(&ccallback)
