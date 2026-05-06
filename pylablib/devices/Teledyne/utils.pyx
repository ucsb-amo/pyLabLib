import cython
from libc.string cimport memcpy

ctypedef unsigned long long uint64_t
ctypedef int (*pspinImageGetSize)(void *hImage, size_t *pImageSize) noexcept nogil
ctypedef int (*pspinImageIsIncomplete)(void *hImage, size_t *pbIsIncomplete) noexcept nogil
ctypedef int (*pspinImageGetWidth)(void *hImage, size_t *pWidth) noexcept nogil
ctypedef int (*pspinImageGetHeight)(void *hImage, size_t *pHeight) noexcept nogil
ctypedef int (*pspinImageGetData)(void *hImage, char **data) noexcept nogil
ctypedef int (*pspinImageGetFrameID)(void *hImage, uint64_t *pFrameID) noexcept nogil
ctypedef int (*pspinImageGetTimeStamp)(void *hImage, uint64_t *pTimeStamp) noexcept nogil

@cython.cdivision(True)
cdef void ccallback(void *hImage, size_t *data) noexcept nogil:
    cdef size_t *funcs=<size_t*>(data[0])
    cdef size_t *ctl=<size_t*>(data[1])
    cdef size_t *buff=<size_t*>(data[2])
    cdef size_t *stat=<size_t*>(data[3])
    cdef pspinImageIsIncomplete spinImageIsIncomplete=<pspinImageIsIncomplete>(funcs[0])
    cdef pspinImageGetSize spinImageGetSize=<pspinImageGetSize>(funcs[1])
    cdef pspinImageGetWidth spinImageGetWidth=<pspinImageGetWidth>(funcs[2])
    cdef pspinImageGetHeight spinImageGetHeight=<pspinImageGetHeight>(funcs[3])
    cdef pspinImageGetData spinImageGetData=<pspinImageGetData>(funcs[4])
    cdef pspinImageGetFrameID spinImageGetFrameID=<pspinImageGetFrameID>(funcs[5])
    cdef pspinImageGetTimeStamp spinImageGetTimeStamp=<pspinImageGetTimeStamp>(funcs[6])
    if (not ctl[0]) or (ctl[2]!=0):
        return
    cdef size_t incomplete=0, nbytes=0, width=0, height=0
    cdef int err=0
    err=spinImageIsIncomplete(hImage,&incomplete)
    if err:
        ctl[2]=err
        return
    if incomplete:
        stat[1]+=1
        return
    err=spinImageGetSize(hImage,&nbytes)
    if err:
        ctl[2]=err
        return
    if (nbytes!=buff[1]) or (nbytes==0):
        stat[2]+=1
        return
    cdef size_t nbuff=buff[0]
    cdef size_t idx=stat[0]%nbuff
    cdef char *pbuff=<char*>(buff[2]+idx*nbytes)
    cdef char *imdata=NULL
    err=spinImageGetData(hImage,&imdata)
    if err:
        ctl[2]=err
        return
    memcpy(pbuff,imdata,nbytes)
    cdef uint64_t fid, ts
    cdef uint64_t *pfibuff=<uint64_t*>(buff[3]+idx*2*8)
    if ctl[1]:
        err=spinImageGetFrameID(hImage,&fid)
        if not err:
            err=spinImageGetTimeStamp(hImage,&ts)
        if not err:
            pfibuff[0]=fid
            pfibuff[1]=ts
        else:
            pfibuff[0]=0
            pfibuff[1]=0
    stat[0]+=1
def get_callback():
    return <size_t>(&ccallback)
