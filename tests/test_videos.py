import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from collections import deque

import cv2
import numpy as np
import torch

from core.pose import PoseEstimator
from training.model import FightLSTM


# VIDEO_PATH = (
#     "data/rwf2000/fight/eifiXLWYul8_0.avi"
# )
cap = cv2.VideoCapture(0)

pose = PoseEstimator()

model = FightLSTM()

model.load_state_dict(
    torch.load(
        "models/fight_lstm.pth",
        map_location="cpu"
    )
)

model.eval()

sequence = deque(
    maxlen=30
)

cap = cv2.VideoCapture(
    VIDEO_PATH
)

print(
    "Video Opened:",
    cap.isOpened()
)

frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1

    vector = pose.get_vector(frame)

    if vector is None:
        print(
            f"Frame {frame_count}: No pose"
        )
        continue

    print(
        f"Frame {frame_count}: Pose detected"
    )

    sequence.append(vector)

    if len(sequence) < 30:
        continue

    x = np.array(
        sequence,
        dtype=np.float32
    )

    x = torch.tensor(
        x,
        dtype=torch.float32
    ).unsqueeze(0)

    with torch.no_grad():

        output = model(x)

        probs = torch.softmax(
            output,
            dim=1
        )

        fight_prob = probs[
            0,
            1
        ].item()

    print(
        f"Frame {frame_count} "
        f"Fight Probability: "
        f"{fight_prob:.3f}"
    )