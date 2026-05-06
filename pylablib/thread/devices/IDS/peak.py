from ..generic import camera


class IDSPeakCameraThread(camera.GenericCameraThread):
    """
    Generic IDS peak camera device thread.

    See :class:`.camera.GenericCameraThread`.
    """
    parameter_variables=camera.GenericCameraThread.parameter_variables|{"detector_size","roi_limits","roi","buffer_size","exposure","frame_period"}
    def _get_camera_attributes(self):  # pylint: disable=arguments-differ
        values=super()._get_camera_attributes(enum_as_str=False,ignore_errors=True)
        return {k:v for k,v in values.items() if v is not None}
    def connect_device(self):
        with self.using_devclass("IDS.IDSPeakCamera",host=self.remote) as cls:
            self.device=cls(idx=self.ids_idx,key=self.ids_key,serial=self.ids_serial)  # pylint: disable=not-callable
    def setup_task(self, idx=0, key=None, serial=None, remote=None, misc=None):  # pylint: disable=arguments-differ, arguments-renamed
        self.ids_idx=idx
        self.ids_key=key
        self.ids_serial=serial
        super().setup_task(remote=remote,misc=misc)