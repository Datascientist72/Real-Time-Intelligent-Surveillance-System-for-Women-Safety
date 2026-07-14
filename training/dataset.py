"""
Fight Dataset Loader Module

This module defines a custom PyTorch Dataset class for loading
pose sequence data used in the violence recognition model.

Purpose:
    - Load Fight and NonFight pose sequences.
    - Assign classification labels.
    - Normalize sequence length.
    - Convert NumPy arrays into PyTorch tensors.
    - Provide samples to the LSTM training pipeline.


Task:

Binary Classification:

    Fight      → 1

    NonFight   → 0



Dataset Structure:

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



Data Flow:

Pose Sequences (.npy)
          |
          ↓
FightDataset
          |
          ↓
PyTorch DataLoader
          |
          ↓
LSTM Model Training



Input Format:

Each sequence contains:

    Frames × Features


Current configuration:

    Frames:
        30

    Features:
        132


Output:

Returns:

    x:
        Pose sequence tensor

    y:
        Class label tensor


Example:

    x.shape:

        (30,132)


    y:

        1  -> Fight

        0  -> NonFight

"""



from pathlib import Path

import numpy as np
import torch

from torch.utils.data import Dataset




class FightDataset(Dataset):
    """
    Custom PyTorch Dataset for violence recognition.

    This class loads pose sequences from storage and
    prepares them for LSTM model training.

    Attributes:

        samples:
            List containing:

                (file_path, label)

            where:

                label 1 = Fight

                label 0 = NonFight

    """



    def __init__(self, root):
        """
        Initialize dataset.

        Args:

            root (str or Path):

                Path containing:

                    Fight/

                    NonFight/


        The constructor scans both folders and stores
        available samples with their labels.

        """



        # Stores file paths and labels

        self.samples = []



        # Dataset directories

        fight_dir = Path(root) / "Fight"

        nonfight_dir = Path(root) / "NonFight"




        # Load Fight samples
        #
        # Label:
        #       1
        #

        for file in fight_dir.glob("*.npy"):

            self.samples.append(

                (
                    file,
                    1
                )

            )




        # Load NonFight samples
        #
        # Label:
        #       0
        #

        for file in nonfight_dir.glob("*.npy"):

            self.samples.append(

                (
                    file,
                    0
                )

            )




        print(

            "Loaded samples:",

            len(self.samples)

        )





    def __len__(self):
        """
        Return total number of samples.

        Used by PyTorch DataLoader to determine
        dataset size.

        Returns:

            int:
                Number of pose sequences.

        """

        return len(self.samples)





    def __getitem__(self, idx):
        """
        Load one training sample.

        Args:

            idx (int):

                Index of sample.


        Processing:

            1. Load numpy pose sequence.
            2. Normalize sequence length.
            3. Convert to PyTorch tensor.
            4. Return input and label.


        Returns:

            x:

                Pose sequence tensor.


            y:

                Class label tensor.

        """



        # Retrieve file and label

        file, label = self.samples[idx]




        # Load pose sequence

        x = np.load(file)




        # Required LSTM sequence length

        MAX_LEN = 30




        # Current sequence length

        seq_len = x.shape[0]




        # ------------------------------------------------
        # Padding
        #
        # If sequence has fewer than 30 frames,
        # add zero frames.
        #
        # Example:
        #
        # 20 frames
        #
        # becomes:
        #
        # 20 frames + 10 zero frames
        #
        # ------------------------------------------------

        if seq_len < MAX_LEN:


            padding = np.zeros(

                (

                    MAX_LEN - seq_len,

                    132

                ),

                dtype=np.float32

            )


            x = np.vstack(

                [
                    x,
                    padding
                ]

            )




        # ------------------------------------------------
        # Truncation
        #
        # If sequence is longer than 30 frames,
        # keep only first 30 frames.
        #
        # ------------------------------------------------

        elif seq_len > MAX_LEN:


            x = x[:MAX_LEN]





        # Convert input sequence into PyTorch tensor

        x = torch.tensor(

            x,

            dtype=torch.float32

        )




        # Convert label into PyTorch tensor

        y = torch.tensor(

            label,

            dtype=torch.long

        )




        return x, y