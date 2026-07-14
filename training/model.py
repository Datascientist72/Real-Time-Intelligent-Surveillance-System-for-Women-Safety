"""
Fight LSTM Model Architecture

This module defines the LSTM-based deep learning model
used for violence/action recognition.

The model receives temporal human pose sequences and
learns movement patterns over time to classify actions.

Task:

Binary Classification:

    0 → NonFight

    1 → Fight



Input:

Pose sequence:

    Shape:

        (sequence_length, features)


Current configuration:

    Frames:
        30

    Features:
        132


Example input:

    (30,132)



Architecture:

Input Pose Sequence

        ↓

LSTM Layer 1

        ↓

LSTM Layer 2

        ↓

Hidden State Extraction

        ↓

Fully Connected Layer

        ↓

Class Prediction



Network Details:

LSTM:

    Input features:
        132

    Hidden units:
        128

    Layers:
        2


Classifier:

    Linear layer:

        128 → 2


Output:

Two values representing:

    Class 0 probability

    Class 1 probability



Pipeline:

Pose Extraction
       |
       ↓
Pose Sequence
       |
       ↓
FightLSTM
       |
       ↓
Fight / NonFight Prediction

"""



# Import PyTorch libraries

import torch

import torch.nn as nn





class FightLSTM(nn.Module):
    """
    LSTM-based violence recognition model.

    This model learns temporal patterns from
    human pose sequences.

    Input:

        Batch of pose sequences

        Shape:

            (batch_size,30,132)


    Output:

        Two-class prediction scores:

            0 → NonFight

            1 → Fight

    """



    def __init__(self):
        """
        Initialize LSTM architecture.

        Components:

            1. Two-layer LSTM
            2. Fully connected classifier

        """



        # Initialize parent PyTorch module

        super().__init__()




        # -----------------------------------------
        # LSTM Feature Extractor
        # -----------------------------------------
        #
        # input_size:
        #
        #       132 pose features per frame
        #
        #
        # hidden_size:
        #
        #       128 learned motion features
        #
        #
        # num_layers:
        #
        #       Two stacked LSTM layers
        #
        #
        # batch_first=True:
        #
        # Input format:
        #
        #       (batch,sequence,features)
        #
        # -----------------------------------------


        self.lstm = nn.LSTM(

            input_size=132,

            hidden_size=128,

            num_layers=2,

            batch_first=True

        )





        # -----------------------------------------
        # Classification Layer
        # -----------------------------------------
        #
        # Converts learned LSTM representation
        # into two class scores.
        #
        # Output:
        #
        #       0 → NonFight
        #
        #       1 → Fight
        #
        # -----------------------------------------


        self.fc = nn.Linear(

            128,

            2

        )





    def forward(self, x):
        """
        Forward pass of the model.

        Args:

            x:

                Input pose sequence tensor.


                Shape:

                    (batch_size,30,132)


        Processing:

            1. Pass sequence through LSTM.
            2. Extract final hidden state.
            3. Pass hidden representation
               through classifier.


        Returns:

            Output class scores.

            Shape:

                (batch_size,2)

        """



        # LSTM returns:
        #
        # output:
        #     Sequence outputs
        #
        # hidden:
        #     Final hidden states
        #
        # cell:
        #     Final cell states
        #

        _, (hidden, _) = self.lstm(x)




        # Use final LSTM layer hidden state
        #
        # hidden[-1]:
        #
        #     Last layer representation
        #
        # Shape:
        #
        #     (batch_size,128)
        #

        features = hidden[-1]




        # Convert learned features into
        # class predictions

        output = self.fc(

            features

        )




        return output