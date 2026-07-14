"""
Dataset Verification Module

This script verifies that the prepared pose sequence dataset
can be successfully loaded using the FightDataset class.

Purpose:
    - Locate the project dataset directory.
    - Initialize the custom PyTorch dataset.
    - Check dataset size.
    - Verify sample loading.
    - Display input tensor shape and label.

This script is useful for debugging before model training.

Pipeline:

Pose Sequences
        |
        ↓
FightDataset Loader
        |
        ↓
Dataset Verification
        |
        ↓
LSTM Training


Expected Dataset Structure:

project/

 ├── data/
 │     |
 │     └── pose_sequences/
 │             |
 │             ├── Fight/
 │             |
 │             └── NonFight/
 │
 └── training/
       |
       └── dataset.py


Output Example:

Dataset path:
data/pose_sequences


Dataset size:
500


Input shape:
torch.Size([30,132])


Label:
1


"""



from pathlib import Path


# Import custom dataset loader
#
# FightDataset is responsible for:
#
#   - Loading pose sequence files
#   - Converting data into tensors
#   - Providing labels
#

from dataset import FightDataset




# Find project root directory
#
# __file__ gives current script location.
#
# parent.parent moves two directories upward
# to reach project root.
#

project_root = Path(
    __file__
).resolve().parent.parent




# Define dataset location
#
# Dataset contains:
#
#   Fight/
#       pose sequences
#
#   NonFight/
#       pose sequences
#

dataset_path = (

    project_root /
    "data" /
    "pose_sequences"

)



print(
    "Dataset path:",
    dataset_path
)




# Initialize PyTorch dataset
#
# This loads all available pose sequences
# and their corresponding labels.
#

dataset = FightDataset(

    dataset_path

)



# Check number of samples available

print(
    "Dataset size:",
    len(dataset)
)




# Retrieve first training example
#
# Dataset returns:
#
# x:
#     Pose sequence
#
# y:
#     Class label
#
# Example:
#
# x -> (30,132)
#
# y -> 0 or 1
#

x, y = dataset[0]




# Display sample information

print(
    "Input shape:",
    x.shape
)


print(
    "Label:",
    y
)