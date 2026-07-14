import torch

from torch.utils.data import DataLoader
from torch.optim import Adam

from dataset import FightDataset
from model import FightLSTM


dataset = FightDataset(
    "../data/pose_sequences"
)

print("Dataset Size:", len(dataset))

loader = DataLoader(
    dataset,
    batch_size=16,
    shuffle=True
)

device = (
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

print("Device:", device)

model = FightLSTM().to(device)

optimizer = Adam(
    model.parameters(),
    lr=0.001
)

criterion = torch.nn.CrossEntropyLoss()

epochs = 20

for epoch in range(epochs):

    model.train()

    total_loss = 0

    correct = 0

    total = 0

    for x, y in loader:

        x = x.to(device)

        y = y.to(device)

        optimizer.zero_grad()

        output = model(x)

        loss = criterion(
            output,
            y
        )

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

        predictions = output.argmax(
            dim=1
        )

        correct += (
            predictions == y
        ).sum().item()

        total += y.size(0)

    accuracy = (
        100 * correct / total
    )

    print(
        f"Epoch {epoch+1}/{epochs} "
        f"Loss={total_loss:.4f} "
        f"Accuracy={accuracy:.2f}%"
    )

torch.save(
    model.state_dict(),
    "../models/fight_lstm.pth"
)

print(
    "\nTraining Complete"
)

print(
    "Saved:",
    "../models/fight_lstm.pth"
)