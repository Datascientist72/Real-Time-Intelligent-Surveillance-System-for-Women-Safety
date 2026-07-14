"""
Trajectory Logger Module

Stores movement trajectories of tracked persons.

Output:

    data/trajectories/
"""

import json

from pathlib import Path

from collections import defaultdict


class TrajectoryLogger:

    def __init__(self):

        self.history = defaultdict(list)

        self.output_dir = Path(
            "data/trajectories"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        print(
            "Trajectory Logger Initialized"
        )

    def update(
        self,
        tracks
    ):

        for track in tracks:

            track_id = track["id"]

            center = track["center"]

            self.history[
                track_id
            ].append(
                list(center)
            )

    def save(self):

        print(
            "\nSaving trajectories..."
        )

        for track_id, trajectory in self.history.items():

            if len(trajectory) < 5:

                continue

            file_path = (

                self.output_dir /

                f"track_{track_id}.json"

            )

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    trajectory,
                    f,
                    indent=4
                )

            print(
                "Saved:",
                file_path
            )