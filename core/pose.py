import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class PoseEstimator:

    def __init__(self):

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

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        results = self.pose.detect(
            mp_image
        )

        return results

    def get_vector(self, frame):

        results = self.estimate(frame)

        if len(results.pose_landmarks) == 0:
            return None

        landmarks = []

        for lm in results.pose_landmarks[0]:

            landmarks.extend([
                lm.x,
                lm.y,
                lm.z,
                lm.visibility
            ])

        return landmarks