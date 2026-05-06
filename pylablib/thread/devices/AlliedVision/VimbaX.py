from ..generic import camera


class AlliedVisionVimbaXCameraThread(camera.GenericCameraThread):
    """
    Generic Allied Vision VimbaX camera device thread.

    See :class:`.camera.GenericCameraThread`.
    """
    # parameter_variables=camera.GenericCameraThread.parameter_variables|{"detector_size","roi_limits","roi","buffer_size","missed_frames"}
    parameter_variables=camera.GenericCameraThread.parameter_variables|{"detector_size","roi_limits","roi","buffer_size","exposure","frame_period"}
    def _get_camera_attributes(self):  # pylint: disable=arguments-differ
        return super()._get_camera_attributes(enum_as_str=False)
    def connect_device(self):
        with self.using_devclass("AlliedVision.AlliedVisionVimbaXCamera",host=self.remote) as cls:
            self.device=cls(idx=self.vimbax_idx,name=self.vimbax_name,serial=self.vimbax_serial)  # pylint: disable=not-callable
    def setup_task(self, idx=0, name=None, serial=None, remote=None, misc=None):  # pylint: disable=arguments-differ, arguments-renamed
        self.vimbax_idx=idx
        self.vimbax_name=name
        self.vimbax_serial=serial
        super().setup_task(remote=remote,misc=misc)