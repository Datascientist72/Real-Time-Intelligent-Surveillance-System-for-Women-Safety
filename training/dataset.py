from pathlib import Path

import numpy as np
import torch

from torch.utils.data import Dataset


class FightDataset(Dataset):

    def __init__(self, root):

        self.samples = []

        fight_dir = Path(root) / "Fight"
        nonfight_dir = Path(root) / "NonFight"

        for file in fight_dir.glob("*.npy"):

            self.samples.append(
                (file, 1)
            )

        for file in nonfight_dir.glob("*.npy"):

            self.samples.append(
                (file, 0)
            )

        print(
            "Loaded samples:",
            len(self.samples)
        )

    def __len__(self):

        return len(self.samples)

    def __getitem__(self, idx):

        file, label = self.samples[idx]

        x = np.load(file)

        MAX_LEN = 30

        seq_len = x.shape[0]

        # Pad short sequences
        if seq_len < MAX_LEN:

            padding = np.zeros(
                (
                    MAX_LEN - seq_len,
                    132
                ),
                dtype=np.float32
            )

            x = np.vstack(
                [x, padding]
            )

        # Trim long sequences
        elif seq_len > MAX_LEN:

            x = x[:MAX_LEN]

        x = torch.tensor(
            x,
            dtype=torch.float32
        )

        y = torch.tensor(
            label,
            dtype=torch.long
        )

        return x, y