import torch
import torch.nn as nn


class FightLSTM(nn.Module):

    def __init__(self):

        super().__init__()

        self.lstm = nn.LSTM(
            input_size=132,
            hidden_size=128,
            num_layers=2,
            batch_first=True
        )

        self.fc = nn.Linear(
            128,
            2
        )

    def forward(self, x):

        _, (hidden, _) = self.lstm(x)

        output = self.fc(
            hidden[-1]
        )

        return output