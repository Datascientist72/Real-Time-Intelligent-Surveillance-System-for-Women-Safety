from pathlib import Path
import numpy as np

POSE_DIR = Path("data/pose_sequences")

MAX_FRAMES = 30
FEATURES = 132

X = []
y = []


def load_sequence(path):

    seq = np.load(path)

    if len(seq) == 0:
        return None

    # truncate

    if len(seq) > MAX_FRAMES:
        seq = seq[:MAX_FRAMES]

    # pad

    if len(seq) < MAX_FRAMES:

        pad = np.zeros(
            (
                MAX_FRAMES - len(seq),
                FEATURES
            ),
            dtype=np.float32
        )

        seq = np.vstack(
            [seq, pad]
        )

    return seq


# Fight = 1

for file in (POSE_DIR / "Fight").glob("*.npy"):

    seq = load_sequence(file)

    if seq is not None:

        X.append(seq)

        y.append(1)


# NonFight = 0

for file in (POSE_DIR / "NonFight").glob("*.npy"):

    seq = load_sequence(file)

    if seq is not None:

        X.append(seq)

        y.append(0)


X = np.array(
    X,
    dtype=np.float32
)

y = np.array(
    y,
    dtype=np.int64
)

print("X shape:", X.shape)
print("y shape:", y.shape)

np.save(
    "data/training/X.npy",
    X
)

np.save(
    "data/training/y.npy",
    y
)

print("Saved dataset.")