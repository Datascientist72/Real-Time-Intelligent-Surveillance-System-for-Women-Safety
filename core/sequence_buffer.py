"""
Temporal Sequence Buffer Module

This module stores sequential pose information for tracked
individuals before passing it to temporal deep learning models.

Purpose:
    - Maintain pose history for each tracked person.
    - Create fixed-length temporal sequences.
    - Provide input data for LSTM-based action recognition.

Why it is needed:

A single pose frame cannot describe an action.

Example:

Frame 1:
    Arm position

Frame 15:
    Arm movement

Frame 30:
    Body impact position

Together these frames describe an action such as fighting.

Pipeline Position:

Pose Estimator
        |
        ↓
Sequence Buffer
        |
        ↓
30-frame Pose Sequence
        |
        ↓
LSTM Model
"""

from collections import defaultdict


class SequenceBuffer:
    """
    Maintains temporal pose sequences for tracked individuals.

    Each person has an independent sequence buffer identified
    by their tracking ID.

    Attributes:
        buffer (defaultdict):
            Stores pose vectors for each tracked person.

            Key:
                Track ID

            Value:
                List of pose vectors
    """


    def __init__(self):
        """
        Initialize the sequence storage.

        Creates an empty buffer for storing pose sequences
        of multiple tracked persons.
        """

        self.buffer = defaultdict(list)



    def update(
        self,
        track_id,
        pose_vector
    ):
        """
        Add a new pose vector to a person's sequence.

        The buffer maintains a fixed sequence length of 30 frames.
        Older frames are removed when the limit is exceeded.

        Args:
            track_id (int):
                Unique identifier assigned by the tracking system.

            pose_vector (list):
                Extracted pose feature vector from PoseEstimator.

        Returns:
            bool:
                True if enough frames are available for model
                prediction, otherwise False.

        Example:

            update(
                track_id=5,
                pose_vector=[0.2,0.3,...]
            )

        """

        # Add current pose information
        self.buffer[track_id].append(
            pose_vector
        )


        # Maintain fixed sequence length
        if len(
            self.buffer[track_id]
        ) > 30:

            self.buffer[track_id].pop(0)


        # LSTM requires 30 consecutive frames
        return (
            len(
                self.buffer[track_id]
            ) == 30
        )



    def get(
        self,
        track_id
    ):
        """
        Retrieve stored pose sequence for a person.

        Args:
            track_id (int):
                Person tracking ID.

        Returns:
            list:
                Sequence of pose vectors.

        Example:

            [
                pose_frame_1,
                pose_frame_2,
                ...
                pose_frame_30
            ]

        """

        return self.buffer[track_id]