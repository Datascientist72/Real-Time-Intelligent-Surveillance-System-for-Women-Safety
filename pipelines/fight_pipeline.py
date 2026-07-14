from collections import deque

import numpy as np
import torch

from core.pose import PoseEstimator
from training.model import FightLSTM


class FightPipeline:

    def __init__(self):

        self.pose = PoseEstimator()

        self.model = FightLSTM()

        self.model.load_state_dict(
            torch.load(
                "models/fight_lstm.pth",
                map_location="cpu"
            )
        )

        self.model.eval()

        self.sequence = deque(
            maxlen=30
        )

    def process_frame(self, frame):

        vector = self.pose.get_vector(frame)

        if vector is None:
            print("No pose detected")
            return None

        self.sequence.append(vector)

        print(
            "Sequence Length:",
            len(self.sequence)
        )

        if len(self.sequence) < 30:
            return None

        x = np.array(
            self.sequence,
            dtype=np.float32
        )

        x = torch.tensor(
            x,
            dtype=torch.float32
        ).unsqueeze(0)

        with torch.no_grad():

            output = self.model(x)

            probs = torch.softmax(
                output,
                dim=1
            )

            fight_prob = probs[
                0,
                1
            ].item()

        print(
            "Fight Probability:",
            fight_prob
        )

        return fight_prob