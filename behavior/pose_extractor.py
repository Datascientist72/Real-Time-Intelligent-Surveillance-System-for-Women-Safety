import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose

pose_detector = mp_pose.Pose(
    static_image_mode=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def extract_pose_landmarks(frame):

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = pose_detector.process(rgb)

    if not result.pose_landmarks:
        return None

    landmarks = []

    for lm in result.pose_landmarks.landmark:
        landmarks.extend([
            lm.x,
            lm.y,
            lm.z,
            lm.visibility
        ])

    return landmarks