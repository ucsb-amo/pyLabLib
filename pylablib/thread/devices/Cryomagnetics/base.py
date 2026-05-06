from ... import device_thread



class LM5xxThread(device_thread.DeviceThread):
    """
    Cryomagnetics LM500/510 level monitor device thread.

    Device args:
        - ``conn``: device connection; usually serial connection parameters (port or a tuple containing port and baudrate)
        - ``channel``: either a single channel (1 or 2) or a list of channels whose readings and settings are periodically updated;
            if several channels are involved, then specific channels are the last nodes in the values
            (e.g. ``"level"`` for channel 1 is stored at ``"level/1"``)

    Variables:
        - ``level``: last measured level, or a dictionary of levels if ``channel`` is a list or a tuple
        - ``parameters``: device parameters: gauge kind, fill status
    """
    full_info_variables={"cls","conn","level","configuration"}
    _model="LM500"
    def connect_device(self):
        with self.using_devclass("Cryomagnetics.{}".format(self._model),host=self.remote) as cls:
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
            for ch in self.channels:
                self.v["parameters/kind",(ch if self.multichannel else "")]=self.device.get_type(ch)
                self.v["parameters/fill_status",(ch if self.multichannel else "")]=self.device.get_fill_status(ch)
            self.close()
        else:
            for ch in self.channels:
                self.v["parameters/kind",(ch if self.multichannel else "")]=None
                self.v["parameters/fill_status",(ch if self.multichannel else "")]="none"
            self.sleep(1.)

class LM500Thread(LM5xxThread):
    pass
class LM510Thread(LM5xxThread):
    _model="LM510"