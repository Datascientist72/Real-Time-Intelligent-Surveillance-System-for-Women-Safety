"""
Behavior Analysis Module

This module analyzes the movement patterns of tracked individuals
to identify suspicious behaviors.

Currently implemented behavior:
    - Loitering detection

The module maintains historical positions of each tracked person
and analyzes their movement over a sequence of frames.

Pipeline Position:

Object Tracking
        |
        ↓
BehaviorAnalyzer
        |
        ↓
Detected Events
        |
        ↓
Risk Assessment
        |
        ↓
Alert Generation
"""

from collections import defaultdict


class BehaviorAnalyzer:
    """
    Analyzes tracked person behavior using movement history.

    The analyzer stores the trajectory of each tracked person and
    detects abnormal movement patterns.

    Current Detection:
        - Loitering

    Attributes:
        position_history (defaultdict):
            Stores historical center positions for each tracked person.
            Key:
                Person ID
            Value:
                List of coordinate positions.
    """


    def __init__(self):
        """
        Initialize the behavior analyzer.

        Creates a storage structure for maintaining
        person movement trajectories.
        """

        self.position_history = defaultdict(list)


    def analyze(self, tracks):
        """
        Analyze current tracked objects and detect behaviors.

        The function updates the movement history of each person
        and calculates the amount of movement over the last 100 frames.

        If a person's movement remains below a defined threshold,
        the system identifies the behavior as loitering.

        Args:
            tracks (list):
                List of tracked persons.

                Expected format:

                [
                    {
                        "id": 1,
                        "center": (x, y)
                    }
                ]

        Returns:
            list:
                Detected behavior events.

                Example:

                [
                    {
                        "type": "loitering",
                        "person": 1
                    }
                ]
        """

        events = []


        # Analyze each tracked person
        for person in tracks:

            person_id = person["id"]

            center = person["center"]


            # Store current position for trajectory analysis
            self.position_history[person_id].append(center)


            # Keep only the latest 100 frames
            if len(self.position_history[person_id]) > 100:


                positions = self.position_history[person_id][-100:]


                # Extract x and y coordinates
                xs = [p[0] for p in positions]

                ys = [p[1] for p in positions]


                # Calculate total movement range
                movement = (
                    max(xs) - min(xs)
                ) + (
                    max(ys) - min(ys)
                )


                # Low movement indicates possible loitering
                if movement < 50:

                    events.append(
                        {
                            "type": "loitering",
                            "person": person_id
                        }
                    )


        return events