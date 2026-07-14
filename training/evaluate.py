from pathlib import Path

import torch
from torch.utils.data import random_split
from torch.utils.data import DataLoader

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from dataset import FightDataset
from model import FightLSTM


dataset = FightDataset(
    "../data/pose_sequences"
)

train_size = int(
    0.8 * len(dataset)
)

test_size = (
    len(dataset)
    - train_size
)

train_dataset, test_dataset = random_split(
    dataset,
    [train_size, test_size]
)

test_loader = DataLoader(
    test_dataset,
    batch_size=16,
    shuffle=False
)

device = (
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

model = FightLSTM().to(device)

model.load_state_dict(
    torch.load(
        "../models/fight_lstm.pth",
        map_location=device
    )
)

model.eval()

y_true = []
y_pred = []

with torch.no_grad():

    for x, y in test_loader:

        x = x.to(device)

        output = model(x)

        preds = torch.argmax(
            output,
            dim=1
        )

        y_true.extend(
            y.numpy()
        )

        y_pred.extend(
            preds.cpu().numpy()
        )

print(
    "\nAccuracy:",
    accuracy_score(
        y_true,
        y_pred
    )
)

print(
    "Precision:",
    precision_score(
        y_true,
        y_pred
    )
)

print(
    "Recall:",
    recall_score(
        y_true,
        y_pred
    )
)

print(
    "F1:",
    f1_score(
        y_true,
        y_pred
    )
)

print(
    "\nConfusion Matrix:"
)

print(
    confusion_matrix(
        y_true,
        y_pred
    )
)