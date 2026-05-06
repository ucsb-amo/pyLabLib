import numpy as np



def _uint12_combine_le(b00, b01, b10, b11):
    v0=b00|((b01&0x0F)<<8)
    v1=(b10>>4)|(b11<<4)
    return v0,v1
def _uint12_combine_be(b00, b01, b10, b11):
    v0=(b00<<4)|(b01>>4)
    v1=((b10&0x0F)<<8)|b11
    return v0,v1
def _uint12_combine_andor(b00, b01, b10, b11):
    v0=(b00<<4)|(b01&0x0F)
    v1=(b10>>4)|(b11<<4)
    return v0,v1
_uint_combine_funcs={"little_endian":_uint12_combine_le,"big_endian":_uint12_combine_be,"andor":_uint12_combine_andor}
def convert_uint12(raw_data, mode="little_endian", width=None):
    """
    Convert packed 12bit data (3 bytes per 2 pixels) into unpacked 16bit data (2 bytes per pixel).

    `raw_data` is a 2D numpy array with the raw frame data of dimensions ``(nrows, stride)``, where ``stride`` is the size of one row in bytes.
    `mode` is the packing mode; can be ``"little_endian"`` (end-to-end little-endian packing), ``"big_endian"`` (end-to-end big-endian packing),
    or ``"andor"`` (Andor camera-specific mode).
    `width` is the size of the resulting row in pixels; if it is 0 or ``None``, assumed to be maximal possible size.
    """
    data=raw_data.astype("<u2")
    fst_uint8,mid_uint8,lst_uint8=data[...,::3],data[...,1::3],data[...,2::3]
    result=np.empty(shape=fst_uint8.shape[:-1]+(lst_uint8.shape[-1]+mid_uint8.shape[-1],),dtype="<u2")
    b00=fst_uint8[...,:mid_uint8.shape[-1]]
    b01=mid_uint8
    b10=mid_uint8[...,:lst_uint8.shape[-1]]
    b11=lst_uint8
    result[...,::2],result[...,1::2]=_uint_combine_funcs[mode](b00,b01,b10,b11)
    return result[...,:width] if width else result