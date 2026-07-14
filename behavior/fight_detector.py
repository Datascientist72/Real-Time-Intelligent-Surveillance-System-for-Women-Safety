import torch
import numpy as np

from training.model import FightLSTM
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from training.model import FightLSTM

class FightDetector:

    def __init__(self):

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.model = FightLSTM().to(
            self.device
        )

        self.model.load_state_dict(
            torch.load(
                "models/fight_lstm.pth",
                map_location=self.device
            )
        )

        self.model.eval()

    def predict(self, sequence):

        x = torch.tensor(
            sequence,
            dtype=torch.float32
        ).unsqueeze(0)

        x = x.to(self.device)

        with torch.no_grad():

            output = self.model(x)

            probs = torch.softmax(
                output,
                dim=1
            )

        return probs.cpu().numpy()[0]