from pathlib import Path

from dataset import FightDataset

project_root = Path(__file__).resolve().parent.parent

dataset_path = (
    project_root /
    "data" /
    "pose_sequences"
)

print("Dataset path:", dataset_path)

dataset = FightDataset(
    dataset_path
)

print("Dataset size:", len(dataset))

x, y = dataset[0]

print("Input shape:", x.shape)
print("Label:", y)