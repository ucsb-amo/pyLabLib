from ...core.utils import py3
from ...core.devio import SCPI, interface, comm_backend

import re

class AmericanMagneticsError(comm_backend.DeviceError):
    """Generic American Magnetics devices error"""
class AmericanMagneticsBackendError(AmericanMagneticsError,comm_backend.DeviceBackendError):
    """Generic American Magnetics backend communication error"""

class AM1700(SCPI.SCPIDevice):
    """
    American Magnetics 1700 level monitor.

    Args:
        conn: connection parameters; usually port or a tuple containing port and baudrate for serial connection,
            or a network/IP address and port (if not specified, use default 7180 port) for Ethernet connection
    """
    Error=AmericanMagneticsError
    ReraiseError=AmericanMagneticsBackendError
    _skip_empty_lines=False
    _relays=[1,2]
    def __init__(self, conn):
        super().__init__(conn,backend="network",term_read="\r\n",term_write="\n",backend_defaults={"serial":("COM1",115200,8,"N",1),"network":("127.0.0.1",7180)})
        with self._close_on_error():
            self._channel_conf={ch:self.get_channel_configuration(ch) for ch in ["HE","N2"]}
            if self._channel_conf["HE"]!="none":
                self._default_channel="He"
            elif self._channel_conf["N2"]!="none":
                self._default_channel="N2"
            else:
                self._default_channel=None
        channels=self.get_connected_channels()
        self._add_info_variable("channels",self.get_connected_channels)
        self._add_info_variable("configuration",lambda: dict(self._channel_conf))
        self._add_settings_variable("unit",self.get_unit,self.set_unit,mux=(channels,1),ignore_error=(AmericanMagneticsError,))
        self._add_status_variable("level",self.get_level,mux=(channels,),ignore_error=(AmericanMagneticsError,))
        self._add_settings_variable("refill_channel",self.get_refill_channel,self.set_refill_channel)
        self._add_settings_variable("high_level",self.get_high_level,self.set_high_level)
        self._add_settings_variable("low_level",self.get_low_level,self.set_low_level)
        self._add_settings_variable("relay_channel",self.get_relay_channel,self.set_relay_channel,mux=(self._relays,))
        self._add_settings_variable("relay_level",self.get_relay_level,self.set_relay_level,mux=(self._relays,))
        self._add_settings_variable("relay_mode",self.get_relay_mode,self.set_relay_mode,mux=(self._relays,))

    def _check_reply(self, reply, msg=None):
        reply=py3.as_str(reply).strip()
        if re.match(r"^-\d$",reply):
            err=int(reply)
            err_desc={-1:"LO setpoint out of range",-2:"Fill B setpoint out of range",-3:"Fill A setpoint out of range",-4:"HI setpoint out of range",
                      -5:"Attemped to set length in percent mode",-6:"Calibration value out of range",-7:"Interval value out of range",
                      -8:"Unrecognized command",-9:"Invalid argument",-10:"Calibration factor out of range",-11:"SCPI buffer overflow"}
            raise AmericanMagneticsError("request returned an error {}: {}".format(err,err_desc.get(err,"N/A")))
        return True
    _p_channel=interface.EnumParameterClass("channel",["N2","He"],value_case="upper")
    _n2_kind={0:"none",1:"int_osc",2:"ext_osc"}
    _he_kind={0:"none",1:"4.2_40in",2:"4.2_80in",3:"2.0_40in",5:"2.0_80in"}
    def _norm_channel(self, channel):
        if channel is None:
            channel=self._default_channel
        if channel is None:
            raise AmericanMagneticsError("no default channel is specified, since no connected channels are found")
        return {"ln":"N2","lhe":"He"}.get(channel,channel).upper()
    def _check_channel(self, channel):
        channel=self._norm_channel(channel)
        if self._channel_conf[channel]=="none":
            raise AmericanMagneticsError("channel {} is not connected".format(channel))
        return channel
    
    def get_default_channel(self):
        """Get the default channel (``"He"``, ``"LN"``, or ``None`` if no connected channel is found)"""
        return self._default_channel
    def get_connected_channels(self):
        """Get all connected channels"""
        return [ch for ch,c in self._channel_conf.items() if c!="none"]

    @interface.use_parameters
    def get_channel_configuration(self, channel=None):
        """Get the sensor configuration for the given channel (``"He"`` or ``"LN"``); ``"none"`` means that the channel is not connected"""
        channel=self._norm_channel(channel)
        kind=self.ask("{}?".format(channel),"int")
        kind=(self._n2_kind if channel=="N2" else self._he_kind).get(kind,kind)
        return kind
    
    _unit_aliases={"P":"perc","%":"perc","I":"inch","C":"cm"}
    _unit_values={"perc":0,"inch":1,"cm":2}
    _id_comm="SER_NUM?"
    def _ensure_unit(self, unit, channel):
        if unit is not None:
            unit=self._unit_values[unit]
            self.ask("CONF:{}:UNIT {}".format(channel,unit))
    @interface.use_parameters
    def get_unit(self, channel=None):
        """Get default units (``"perc"``, ``"in"``, or ``"cm"``) on the given channel (``"He"`` or ``"LN"``)"""
        channel=self._check_channel(channel)
        unit=self.ask("{}:UNIT?".format(channel))
        return self._unit_aliases.get(unit,unit)
    @interface.use_parameters
    def set_unit(self, unit="perc", channel=None):
        """Set default units (``"perc"``, ``"in"``, or ``"cm"``) on the given channel (``"He"`` or ``"LN"``)"""
        channel=self._check_channel(channel)
        unit=self._unit_values[unit]
        self.ask("CONF:{}:UNIT {}".format(channel,unit))
        return self.get_unit(channel=channel)
    
    @interface.use_parameters
    def get_level(self, channel=None, unit="perc"):
        """Get level reading on a given channel"""
        channel=self._check_channel(channel)
        self._ensure_unit(unit,channel)
        return self.ask("MEAS:{}:LEVEL?".format(channel),"float")
    
    _p_relay_channel=interface.EnumParameterClass("relay_channel",{"none":0,"N2":1,"He":2})
    @interface.use_parameters(_returns="relay_channel")
    def get_refill_channel(self):
        """Get channel for autofill control (``"He"``, ``"N2"``, or ``"none"`` if disabled)"""
        return self.ask("FILL:CH?","int")
    @interface.use_parameters(channel="relay_channel")
    def set_refill_channel(self, channel):
        """Set channel for autofill control (``"He"``, ``"N2"``, or ``"none"`` if disabled)"""
        self.ask("CONF:FILL:CH {}".format(channel))
        return self.get_refill_channel()
    
    @interface.use_parameters
    def get_low_level(self):
        """Get low level (automated refill start) setting in the current units"""
        return self.ask("B","float")
    @interface.use_parameters
    def set_low_level(self, level):
        """Set low level (automated refill start) setting in the current units"""
        self.ask("CONF:FILL:B {:.3f}".format(level))
        return self.get_low_level()
    @interface.use_parameters
    def get_high_level(self):
        """Get high level (automated refill stop) setting in the current units"""
        return self.ask("A","float")
    @interface.use_parameters
    def set_high_level(self, level):
        """Set high level (automated refill stop) setting in the current units"""
        self.ask("CONF:FILL:A {:.3f}".format(level))
        return self.get_high_level()
    
    _p_relay=interface.EnumParameterClass("relay",_relays)
    @interface.use_parameters(_returns="relay_channel")
    def get_relay_channel(self, relay):
        """Get channel for relay (1 or 2) control (``"He"``, ``"N2"``, or ``"none"`` if disabled)"""
        return self.ask("RELAY{}:CH?".format(relay),"int")
    @interface.use_parameters(channel="relay_channel")
    def set_relay_channel(self, relay, channel):
        """Set channel for for relay (1 or 2) control (``"He"``, ``"N2"``, or ``"none"`` if disabled)"""
        self.ask("CONF:RELAY{}:CH {}".format(relay,channel))
        return self.get_relay_channel(relay)
    
    @interface.use_parameters
    def get_relay_level(self, relay):
        """Get trigger level setting for a given relay (1 or 2) in the current units"""
        return self.ask("RELAY{}:SET?".format(relay),"float")
    @interface.use_parameters
    def set_relay_level(self, relay, level):
        """Set trigger level setting for a given relay (1 or 2) in the current units"""
        self.ask("CONF:RELAY{}:SET {:.3f}".format(relay,level))
        return self.get_relay_level(relay)
    _p_relay_mode=interface.EnumParameterClass("relay_mode",{"above":0,"below":1})
    @interface.use_parameters(_returns="relay_mode")
    def get_relay_mode(self, relay):
        """Get trigger level setting for a given relay (1 or 2)"""
        return self.ask("RELAY{}:OP?".format(relay),"int")
    @interface.use_parameters(mode="relay_mode")
    def set_relay_mode(self, relay, mode):
        """Set trigger level setting for a given relay (1 or 2)"""
        self.ask("CONF:RELAY{}:OP {}".format(relay,mode))
        return self.get_relay_mode(relay)