from ..generic import camera


class TeledyneSpinnakerCameraThread(camera.GenericCameraThread):
    """
    Generic Teledyne Spinnaker camera device thread.

    See :class:`.camera.GenericCameraThread`.
    """
    parameter_variables=camera.GenericCameraThread.parameter_variables|{"detector_size","roi_limits","roi","buffer_size","missed_frames","exposure","frame_period"}
    def _get_camera_attributes(self):  # pylint: disable=arguments-differ
        return super()._get_camera_attributes(enum_as_str=False)
    def connect_device(self):
        with self.using_devclass("Teledyne.TeledyneSpinnakerCamera",host=self.remote) as cls:
            self.device=cls(idx=self.spinnaker_idx,name=self.spinnaker_name,serial=self.spinnaker_serial)  # pylint: disable=not-callable
    def setup_task(self, idx=0, name=None, serial=None, remote=None, misc=None):  # pylint: disable=arguments-differ, arguments-renamed
        self.spinnaker_idx=idx
        self.spinnaker_name=name
        self.spinnaker_serial=serial
        super().setup_task(remote=remote,misc=misc)