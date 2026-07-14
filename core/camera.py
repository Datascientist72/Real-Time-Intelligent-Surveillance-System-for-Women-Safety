"""
Camera Input Module

This module provides an interface for capturing video frames
from different sources such as:

    - Webcam
    - CCTV camera stream
    - Video files

The Camera class abstracts OpenCV video capture operations and
provides simple methods to read frames and release resources.

Pipeline Position:

Video Source
      |
      ↓
Camera Module
      |
      ↓
Frame Processing Pipeline
      |
      ↓
AI Models
"""

import cv2


class Camera:
    """
    Handles video input for the surveillance system.

    This class manages the connection with a video source and
    provides frames to downstream computer vision modules.

    Attributes:
        cap (cv2.VideoCapture):
            OpenCV video capture object.

    Args:
        source:
            Video source identifier.

            Examples:
                0       -> Default webcam
                "video.mp4" -> Video file
                RTSP URL -> CCTV stream
    """


    def __init__(self, source=0):
        """
        Initialize camera connection.

        Args:
            source:
                Input video source.

        """

        self.cap = cv2.VideoCapture(source)


    def read(self):
        """
        Read a frame from the video source.

        Returns:
            tuple:
                success (bool):
                    Indicates whether frame capture succeeded.

                frame (numpy.ndarray):
                    Captured image frame.

        Example:

            success, frame = camera.read()

        """

        return self.cap.read()


    def release(self):
        """
        Release the video capture resource.

        This should be called when the application stops
        to properly close the camera connection.
        """

        self.cap.release()