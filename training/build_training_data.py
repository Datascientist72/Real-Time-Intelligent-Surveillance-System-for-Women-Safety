"""
Pose Sequence Dataset Preparation Module

This module prepares extracted human pose sequences for training
a temporal deep learning model (LSTM).

Purpose:
    - Load stored pose sequences.
    - Normalize sequence length.
    - Apply truncation and padding.
    - Generate training features and labels.
    - Save processed NumPy datasets.

Task:
    Binary Classification

        Fight      -> 1
        NonFight   -> 0


Input Structure:

data/
 |
 └── pose_sequences/
        |
        ├── Fight/
        |      ├── sequence1.npy
        |      └── sequence2.npy
        |
        └── NonFight/
               ├── sequence1.npy
               └── sequence2.npy


Output:

data/
 |
 └── training/
        |
        ├── X.npy   -> Pose sequences
        |
        └── y.npy   -> Class labels


Pipeline:

Video Dataset
      |
      ↓
Pose Extraction (MediaPipe)
      |
      ↓
Pose Sequences (.npy)
      |
      ↓
Dataset Preparation
      |
      ↓
LSTM Training
      |
      ↓
Violence Recognition Model


Pose Representation:

MediaPipe provides:

    33 body landmarks

Each landmark contains:

    x coordinate
    y coordinate
    z coordinate
    visibility

Therefore:

    33 landmarks × 4 values = 132 features/frame

LSTM Input:

    Frames  : 30
    Features: 132

Input shape:

    (30,132)

"""


from pathlib import Path
import numpy as np



# Directory containing extracted pose sequences
POSE_DIR = Path(
    "data/pose_sequences"
)



# Number of frames required by LSTM model
# Every sample must contain exactly 30 frames

MAX_FRAMES = 30



# Number of pose features per frame
#
# 33 landmarks ×
# (x,y,z,visibility)

FEATURES = 132



# Dataset storage

# X stores pose sequences
# y stores corresponding labels

X = []

y = []



def load_sequence(path):
    """
    Load and normalize a single pose sequence.

    LSTM models require all input samples
    to have the same temporal dimension.

    This function performs:

        1. Loading numpy sequence.
        2. Removing extra frames.
        3. Adding zero padding for short sequences.


    Args:

        path (Path):
            Path of .npy pose sequence file.


    Returns:

        numpy.ndarray:
            Fixed size sequence of shape:

                (30,132)


        None:
            If sequence is empty.


    Example:

        Input:

            45 frames


        Output:

            First 30 frames


        Input:

            20 frames


        Output:

            20 frames + 10 zero padding frames

    """



    # Load pose sequence from numpy file

    seq = np.load(path)



    # Ignore empty sequences

    if len(seq) == 0:

        return None



    # ------------------------------------------------
    # Truncation
    #
    # If sequence contains more than 30 frames,
    # keep only first 30 frames.
    # ------------------------------------------------

    if len(seq) > MAX_FRAMES:

        seq = seq[:MAX_FRAMES]



    # ------------------------------------------------
    # Padding
    #
    # If sequence contains fewer than 30 frames,
    # add zero frames until required length is reached.
    # ------------------------------------------------

    if len(seq) < MAX_FRAMES:


        pad = np.zeros(

            (
                MAX_FRAMES - len(seq),
                FEATURES
            ),

            dtype=np.float32

        )


        seq = np.vstack(

            [
                seq,
                pad
            ]

        )


    return seq





# ==================================================
# Loading Fight Samples
# ==================================================
#
# Fight sequences are assigned label:
#
#       Fight = 1
#
# ==================================================


for file in (
    POSE_DIR / "Fight"
).glob("*.npy"):


    seq = load_sequence(file)


    if seq is not None:


        # Add processed sequence

        X.append(seq)


        # Add fight label

        y.append(1)




# ==================================================
# Loading NonFight Samples
# ==================================================
#
# NonFight sequences are assigned label:
#
#       NonFight = 0
#
# ==================================================


for file in (
    POSE_DIR / "NonFight"
).glob("*.npy"):


    seq = load_sequence(file)


    if seq is not None:


        # Add processed sequence

        X.append(seq)


        # Add non-fight label

        y.append(0)




# Convert Python lists into NumPy arrays
#
# Final shapes:
#
# X:
#   (samples,30,132)
#
# y:
#   (samples,)





X = np.array(

    X,

    dtype=np.float32

)



y = np.array(

    y,

    dtype=np.int64

)



# Display dataset information

print(
    "X shape:",
    X.shape
)


print(
    "y shape:",
    y.shape
)




# Save processed dataset
#
# X.npy:
#       Input pose sequences
#
# y.npy:
#       Corresponding labels
#

np.save(

    "data/training/X.npy",

    X

)


np.save(

    "data/training/y.npy",

    y

)


print(
    "Saved dataset."
)