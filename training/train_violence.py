"""
Fight LSTM Model Architecture

This module defines the LSTM-based deep learning model used
for human action recognition and violence detection.

The model analyzes temporal pose sequences extracted from
video frames and classifies them into two categories:

    0 → NonFight

    1 → Fight


Purpose:

    - Learn movement patterns from body pose sequences.
    - Capture temporal dependencies using LSTM.
    - Prevent overfitting using dropout regularization.
    - Generate binary action predictions.



Input:

Pose sequence:

    Shape:

        (batch_size, sequence_length, features)


Current configuration:

    Sequence length:
        30 frames

    Features per frame:
        132


Input example:

    (16,30,132)

    where:

        16  → batch size

        30  → video frames

        132 → pose features/frame



Architecture:

Pose Sequence

      ↓

2-Layer LSTM

      ↓

Final Hidden State

      ↓

Fully Connected Classifier

      ↓

Fight / NonFight Prediction



Network:

LSTM:

    input_size:
        132

    hidden_size:
        128

    layers:
        2

    dropout:
        0.3


Classifier:

    Linear:
        128 → 64

    Activation:
        ReLU

    Dropout:
        0.3

    Linear:
        64 → 2



Output:

    Two class scores:

        [NonFight score, Fight score]


"""



import torch

import torch.nn as nn





class FightLSTM(nn.Module):
    """
    LSTM-based violence recognition model.

    The model receives sequences of human pose
    landmarks and learns temporal movement patterns.

    Input:

        Tensor:

            (batch_size,30,132)


    Output:

        Tensor:

            (batch_size,2)


    Classes:

        0 -> NonFight

        1 -> Fight

    """



    def __init__(self):
        """
        Initialize the LSTM network.

        The architecture contains:

            1. LSTM feature extractor
            2. Fully connected classifier

        """

        super().__init__()




        # ------------------------------------------------
        # LSTM Temporal Feature Extractor
        # ------------------------------------------------
        #
        # Learns movement patterns across frames.
        #
        # input_size:
        #       Number of pose features per frame.
        #
        # hidden_size:
        #       Number of learned motion features.
        #
        # num_layers:
        #       Two stacked LSTM layers.
        #
        # dropout:
        #       Prevents overfitting by randomly disabling
        #       neurons during training.
        #
        # batch_first=True:
        #
        # Input format:
        #
        #       (batch, sequence, features)
        #
        # ------------------------------------------------


        self.lstm = nn.LSTM(

            input_size=132,

            hidden_size=128,

            num_layers=2,

            batch_first=True,

            dropout=0.3

        )




        # ------------------------------------------------
        # Classification Head
        # ------------------------------------------------
        #
        # Converts LSTM learned representation
        # into final class predictions.
        #
        # Structure:
        #
        #       128 features
        #              |
        #              ↓
        #       64 hidden features
        #              |
        #              ↓
        #       2 classes
        #
        #
        # ReLU:
        #       Adds non-linearity.
        #
        # Dropout:
        #       Reduces overfitting.
        #
        # ------------------------------------------------


        self.fc = nn.Sequential(

            nn.Linear(

                128,

                64

            ),


            nn.ReLU(),


            nn.Dropout(

                0.3

            ),


            nn.Linear(

                64,

                2

            )

        )





    def forward(self, x):
        """
        Forward propagation.

        Steps:

            1. Pass pose sequence through LSTM.
            2. Extract final hidden state.
            3. Pass representation through classifier.


        Args:

            x:

                Input pose sequence.


                Shape:

                    (batch_size,30,132)


        Returns:

            Class prediction scores.


            Shape:

                (batch_size,2)

        """



        # Run sequence through LSTM
        #
        # hidden contains the final hidden states
        # from all LSTM layers.
        #

        _, (hidden, _) = self.lstm(x)




        # Take hidden state from final LSTM layer.
        #
        # Shape:
        #
        #       (batch_size,128)
        #

        features = hidden[-1]




        # Generate class scores

        output = self.fc(

            features

        )



        return output