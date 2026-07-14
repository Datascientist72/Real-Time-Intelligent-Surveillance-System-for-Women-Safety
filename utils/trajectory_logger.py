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

        print(
            "Saving to:",
            self.output_dir.absolute()
        )

    def update(self, tracks):

        print(
            "UPDATE CALLED"
        )

        print(
            "Tracks received:",
            len(tracks)
        )

        for track in tracks:

            track_id = track["id"]

            center = track["center"]

            self.history[track_id].append(
                list(center)
            )

            print(
                f"Track {track_id}:",
                len(
                    self.history[
                        track_id
                    ]
                ),
                "points"
            )

    def save(self):

        print(
            "\nSAVING TRAJECTORIES..."
        )

        print(
            "Total Tracks:",
            len(self.history)
        )

        for track_id, trajectory in self.history.items():

            print(
                f"Track {track_id} ->",
                len(trajectory),
                "points"
            )

            if len(trajectory) < 5:

                print(
                    f"Skipping Track {track_id}"
                )

                continue

            file_path = (
                self.output_dir /
                f"track_{track_id}.json"
            )

            with open(
                file_path,
                "w"
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
            