'''
--------------------------------------------------------------------------------
Description:

Roadmap:

Written by W.R. Jackson <wrjackso@bu.edu>, DAMP Lab 2020
--------------------------------------------------------------------------------
'''
from collections import deque
import ctypes
import sys

import numpy as np

from camera import XsCamera

class MicroscopeCamera:
	'''

	'''
	def __init__(self):
		# We might want to guard from doubly-loading the driver by declaring
		# a metaclass singletion.
		XsCamera.XsLoadDriver(0)
		self.handle = self.open_camera()
		self.param_key = XsCamera.XS_PARAM()
		self.config_key = XsCamera.XsReadCameraSettings(self.handle)
		# We assume that we're not going to be reconfiguring the dimensions
		# of the ROI.
		self.width_pixels, self.height_pixels, self.pixel_depth = \
			self.get_camera_dimensions()
		self.set_exposure_and_acquisition_period()
		self.frame_size, self.acquisition_frames = self.calculate_and_allocate_frame_buffer()

	@staticmethod
	def open_camera():
		# We are assuming that there is only one camera hooked up when this
		# is happening.
		ef = XsCamera.XS_ENUM_FLT()
		py_item_list = XsCamera.XsEnumCameras(ef)
		# Open the first camera in the list.
		handle = XsCamera.XsOpenCamera(py_item_list[0])
		return handle

	def set_exposure_and_acquisition_period(
			self,
			exp_time_ns: int = 1000000,
			acq_time_ns: int = 1000000,
	):
		'''

		Args:
			exp_time_ns:
			acq_time_ns:

		Returns:

		'''
		cfg = XsCamera.XsReadCameraSettings(self.handle)
		xs_param_key = XsCamera.XS_PARAM()
		XsCamera.XsSetParameter(
			self.handle,
			cfg,
			xs_param_key.XSP_EXPOSURE,
			exp_time_ns,
		)
		XsCamera.XsSetParameter(
			self.handle,
			cfg,
			xs_param_key.XSP_PERIOD,
			acq_time_ns,
		)

	def get_camera_dimensions(self):

		# Width of ROI, in pixels
		width_pixels = XsCamera.XsGetParameter(
			self.handle,
			self.config_key,
			self.param_key.XSP_ROIWIDTH,
		)

		# Height of ROI, in pixels
		height_pixels = XsCamera.XsGetParameter(
			self.handle,
			self.config_key,
			self.param_key.XSP_ROIHEIGHT,
		)
		pixel_depth = 24 # Pixel depth: 8 to 36
		XsCamera.XsSetParameter(
			self.handle,
			self.config_key,
			self.param_key.XSP_PIX_DEPTH,
			pixel_depth,
		)
		return width_pixels, height_pixels, pixel_depth

	def set_trigger_source(self, trigger_source: int = 0):
		# Trigger Source (see XS_REC_MODE)
		XsCamera.XsSetParameter(
			self.handle,
			self.config_key,
			self.param_key.XSP_REC_MODE,
			trigger_source,
		)
		XsCamera.XsRefreshCameraSettings(self.handle, self.config_key)


	def calculate_and_allocate_frame_buffer(self, frame_buffer_size: int = 100):
		p_size = 8 if sys.maxsize > 2 ** 32 else 4
		c_char_p = ctypes.POINTER(ctypes.c_char_p)
		frame_size = self.width_pixels * self.height_pixels * p_size
		destination_frame = (
				(ctypes.c_char_p * self.width_pixels) * self.height_pixels
		)()
		ctypes.memset(destination_frame, 0, frame_size)
		# We allocate the singular frame above:
		# - We need to allocate a number of frames for the external copy.
		# FUTURE JACKSON: MAKE SURE THESE ALLOCATE CORRECTLY. I THINK YOU ARE
		# JUST READING AND COPYING TO FRAMES.
		low_th, high_th = XsCamera.XsGetCameraInfo(
			self.handle,
			self.config_key.XSI_LIVE_BUF_SIZE,
		)
		# I don't see an enquing function. Is it abstracted?
		acq_frames = deque(maxlen=frame_buffer_size)
		for i in range(frame_buffer_size):
			frame = np.zeros(self.width_pixels, self.height_pixels)
			# This is probably wrong as we want pointers.
			frame = frame.astype(np.char)
			acq_frames.append(frame.ctypes.data_as(c_char_p))
		return frame_size, acq_frames

	def acquire_frames(self):

	def close(self):
		XsCamera.XsCloseCamera(self.handle)
		XsCamera.XsUnloadDriver()






xs_frame_c = XsCamera.XS_FRAME()
xs_frame_c.pBuffer

# minimum buffer in camera memory to avoid overwrite of acquisition during live

nAddLo, nAddHi = XsCamera.XsGetCameraInfo(handle, xs_info_key.XSI_LIVE_BUF_SIZE)

nFrames = 100 # number of frames to read
nPreTrigFrames = 0 # number of frames to be acquired before the trigger
pfnCallback = NULL # callback routine pointer - can be NULL
nFlags = 0 # callback flags
pUserData = 0 # a parameter passed back in the callback. may be a pointerto user data.
XsCamera.XsMemoryStartGrab(handle, nAddLo, nAddHi, nFrames, nPreTrigFrames, pfnCallback, nFlags, pUserData)

# add while loop in here
nIsBusy, nStatus, nErrCode, nInfo1, nInfo2, nInfo3 = XsCamera.XsGetCameraStatus(handle)


### NEED THE pBuf FROM MALLOC.... BUT UNSURE HOW TO GET THAT RIGHT NOW
# read 10 frames
for x in range(10):
	XsCamera.XsMemoryReadFrame(handle, nAddLo, nAddHi, x, pBuf)

# free the memory
free(pBuf)

XsCamera.XsCloseCamera(handle)

XsCamera.XsUnloadDriver()


#
