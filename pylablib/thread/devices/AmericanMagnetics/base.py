from ... import device_thread



class AM1700Thread(device_thread.DeviceThread):
    """
    American Magnetics 1700 level monitor device thread.

    Device args:
        - ``conn``: device connection; usually port or a tuple containing port and baudrate for serial connection,
            or a network/IP address and port (if not specified, use default 7180 port) for Ethernet connection
        - ``channel``: either a single channel (``"He"`` or ``"N2"``) or a list of channels whose readings and settings are periodically updated;
            if several channels are involved, then specific channels are the last nodes in the values
            (e.g. ``"level"`` for a He channel is stored at ``"level/He"``);
            if ``None``, assume a single channel (when device is connected, use the default channel)

    Variables:
        - ``level``: last measured level, or a dictionary of levels if ``channel`` is a list or a tuple
        - ``parameters``: device parameters: gauge kind
    """
    full_info_variables={"cls","conn","level","configuration"}
    def connect_device(self):
        with self.using_devclass("AmericanMagnetics.AM1700",host=self.remote) as cls:
            self.device=cls(conn=self.conn)  # pylint: disable=not-callable
    def setup_task(self, conn, remote=None, channel=None):  # pylint: disable=arguments-differ
        self.device_reconnect_tries=5
        self.conn=conn
        self.remote=remote
        self.multichannel=isinstance(channel,(list,tuple))
        self.channels=list(channel) if self.multichannel else [channel]
        self.add_job("update_measurements",self.update_measurements,2.5)
        self.add_job("update_parameters",self.update_parameters,10)
    def update_measurements(self):
        """Update current measurements"""
        if self.open():
            for ch in self.channels:
                try:
                    self.v["level",(ch if self.multichannel else "")]=self.device.get_level(channel=ch)
                except self.device.Error:
                    self.v["level",(ch if self.multichannel else "")]=0
        else:
            for ch in self.channels:
                self.v["level",(ch if self.multichannel else "")]=0
            self.sleep(1.)
    def update_parameters(self):
        """Update current measurements"""
        if self.open():
            self.v["parameters/connected_channels"]=self.device.get_connected_channels()
            for ch in self.channels:
                self.v["parameters/configuration",(ch if self.multichannel else "")]=self.device.get_channel_configuration(ch)
            self.close()
        else:
            self.v["parameters/connected_channels"]=[]
            for ch in self.channels:
                self.v["parameters/configuration",(ch if self.multichannel else "")]="none"
            self.sleep(1.)
