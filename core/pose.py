"""
Pose Estimation Module

This module extracts human body landmarks from video frames using
MediaPipe Pose Landmarker.

Purpose:
    - Detect human body keypoints.
    - Convert pose information into numerical feature vectors.
    - Provide pose data for action recognition and behavior analysis.

The pose representation can be used by temporal models such as
LSTM networks to recognize activities like violence or aggressive
movement patterns.

Pipeline Position:

Video Frame
      |
      ↓
MediaPipe Pose Model
      |
      ↓
Body Landmarks
      |
      ↓
Feature Vector
      |
      ↓
Action Recognition Model
"""

import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class PoseEstimator:
    """
    Extracts human pose landmarks from video frames.

    This class uses MediaPipe Pose Landmarker to estimate body
    keypoints and convert them into numerical representations.

    Attributes:
        pose:
            MediaPipe pose detection model.

    Output:
        - Pose landmarks
        - Flattened pose feature vector
    """


    def __init__(self):
        """
        Initialize MediaPipe Pose Landmarker.

        Loads the trained pose model and configures inference
        parameters.

        Model:
            models/pose_landmarker.task

        Configuration:
            - Running mode: IMAGE
            - Maximum detected poses: 5
        """


        base_options = python.BaseOptions(
            model_asset_path="models/pose_landmarker.task"
        )


        options = vision.PoseLandmarkerOptions(
            base_options=base_options,
            running_mode=vision.RunningMode.IMAGE,
            num_poses=5
        )


        self.pose = vision.PoseLandmarker.create_from_options(
            options
        )


    def estimate(self, frame):
        """
        Estimate human pose landmarks from an image frame.

        The input BGR image from OpenCV is converted into RGB format
        because MediaPipe expects RGB input.

        Args:
            frame (numpy.ndarray):
                Current video frame.

        Returns:
            PoseLandmarkerResult:
                MediaPipe pose detection output.
        """


        # Convert OpenCV BGR image to RGB
        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )


        # Convert numpy image into MediaPipe image format
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )


        # Run pose estimation
        results = self.pose.detect(
            mp_image
        )


        return results



    def get_vector(self, frame):
        """
        Convert pose landmarks into a numerical feature vector.

        The generated vector contains:

            x coordinate
            y coordinate
            z coordinate
            visibility score

        for each detected body landmark.

        This representation can be directly used as input
        for machine learning models.

        Args:
            frame (numpy.ndarray):
                Input video frame.

        Returns:
            list:
                Flattened pose feature vector.

            None:
                If no person pose is detected.

        Example:

        [
            x1, y1, z1, visibility1,
            x2, y2, z2, visibility2,
            ...
        ]

        """


        results = self.estimate(frame)


        # Return empty result if no pose detected
        if len(results.pose_landmarks) == 0:
            return None


        landmarks = []


        # Extract first person's landmarks
        for lm in results.pose_landmarks[0]:

            landmarks.extend(
                [
                    lm.x,
                    lm.y,
                    lm.z,
                    lm.visibility
                ]
            )


        return landmarks