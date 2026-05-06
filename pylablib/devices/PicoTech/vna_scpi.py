import numpy as np

from ...core.devio import SCPI, interface
from ...core.utils import units

from .base import PicoTechError, PicoTechBackendError

import time

class PicoVNA(SCPI.SCPIDevice):
    """
    PicoVNA vector network analyzer.
    
    Args:
        addr: device address; usually an IP address or an address and a port (by default, use local PC and the default port 5025)
    """
    _default_backend_timeout=10.
    Error=PicoTechError
    ReraiseError=PicoTechBackendError

    def __init__(self, addr="localhost"):
        super().__init__(addr,backend=("auto","network"),backend_defaults={"network":("localhost",5025)},term_read="\n",term_write="\n")
        with self._close_on_error():
            self._setup_trace_format()
        self._add_settings_variable("bandwidth",self.get_bandwidth,self.set_bandwidth)
        self._add_settings_variable("points",self.get_trace_points,self.set_trace_points)
        self._add_settings_variable("frequency_range",self.get_frequency_range,self.set_frequency_range)
        self._add_status_variable("output_level",self.get_output_level)

    def _comm(self, comm):
        res=self.ask(comm)
        if res!="OK":
            time.sleep(1E-3)
            self.instr.read()
            raise PicoTechBackendError(res)
    def _query_frequency(self, comm):
        v,u=self.ask(comm,"value")
        return units.convert_frequency_units(v,u,result_unit="Hz")
    
    def acquire_single(self):
        """Initiate a single trace acquisition"""
        self._comm("INIT")
    def stop_acquisition(self):
        """Stop acquisition"""
        self._comm("ABORT")

    def get_output_level(self):
        """Get the power level the the given source channel (in dBm)"""
        v,u=self.ask("SENSE:LEVEL?","value")
        if u!="dBm":
            raise self.Error("unrecognized level units: {}; expected dBm".format(u))
        return v

    def get_bandwidth(self):
        """Get the IF bandwidth"""
        return self._query_frequency(":SENS:BAND?")
    def set_bandwidth(self, bandwidth):
        """Set the IF bandwidth"""
        self._comm(":SENS:BAND {:.0f}".format(bandwidth))
        return self.get_bandwidth()
    
    def get_frequency_range(self):
        """Get current sweep frequency range"""
        return tuple(self._query_frequency(":SENSe:FREQ:{}?".format(c)) for c in ["START","STOP"])
    def set_frequency_range(self, rng):
        """Set the current frequency range"""
        crng=self.get_frequency_range()
        order=[("START",rng[0]),("STOP",rng[1])]
        if rng[0]>crng[1]:
            order=order[::-1]
        for c,v in order:
            self._comm(":SENS:FREQ:{} {:.6f} MHz".format(c,float(v)/1E6))
        return self.get_frequency_range()
    
    def get_trace_points(self):
        """Get the number of currently acquired trace points"""
        return self.ask(":SENS:SWEEP:POINTS?","int")
    def set_trace_points(self, points):
        """Set the number of currently acquired trace points"""
        self._comm(":SENS:SWEEP:POINTS {}".format(int(points)))
        return self.get_trace_points()
    
    def _setup_trace_format(self):
        self._comm(":FORMAT REAL")
        self._comm(":FORMAT:BHEADER GPIB")
        self._comm(":FORMAT:BORDER LITTLE")
    def get_frequency_values(self):
        """Get frequency values for the currently acquired trace based on the current frequency range and number of points"""
        frng=self.get_frequency_range()
        npts=self.get_trace_points()
        return np.linspace(*frng,num=npts)
    def read_single_trace(self, src="S11", typ="LOGMAG", mem=None, timeout=None):
        """
        Read single trace at the given source and a given type. The trace is only read and returned once the sweep is finished.
        
        Args:
            src: S parameters source (e.g., ``"S11"`` or ``"S21"``)
            typ: trace type (e.g., ``"REAL"`` or ``"LOGMAG"``)
            mem: if not ``None``, read data from the memory at the given index
            timeout: specifies a different timeout; useful for waiting for longer sweeps
        """
        memc=":MEM{}".format(mem) if mem is not None else ""
        self.write(":CALC:DATA{} {},{}".format(memc,src,typ))
        try:
            bd=self.read_binary_array_data(timeout=timeout)
            return np.frombuffer(bd,"<f8")
        except interface.DeviceError:
            time.sleep(1E-3)
            self.instr.read()
            raise
    def _get_complex_trace(self, src, mem=None, timeout=None):
        data=self.read_single_trace(src,typ="POLAR",mem=mem,timeout=timeout)
        return data[0::2]+1j*data[1::2]
    def read_S_parameters(self, param=("S11","S12","S21","S22"), add_frequency=False, mem=None, timeout=None):
        """
        Get the S parameters trace for the given channel.
        
        `param` can be either a single string specifying the parameters (e.g., ``"S12"``), or a tuple or list of strings.
        `add_frequency` specifies whether the frequency axis should be added to the result.
        The other parameters are the same as in :meth:`read_single_trace`.

        If ``add_frequency==False``, return a single 1D complex array for the single channel, or a multi-column complex array for several channels.
        If ``add_frequency==True``, return a multi-column array, where the first column is the frequency, and the rest are the parameters.
        """
        if isinstance(param,(tuple,list)):
            values=np.column_stack([self._get_complex_trace(src,mem=mem,timeout=timeout) for src in param])
        else:
            values=self._get_complex_trace(param,mem=mem,timeout=timeout)
        if add_frequency:
            freqs=self.get_frequency_values()
            return np.column_stack([freqs,values])
        return values