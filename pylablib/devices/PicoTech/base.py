from ...core.devio import comm_backend

class PicoTechError(comm_backend.DeviceError):
    """Generic PicoTechnology device error"""
class PicoTechBackendError(PicoTechError,comm_backend.DeviceBackendError):
    """Generic PicoTechnology backend communication error"""