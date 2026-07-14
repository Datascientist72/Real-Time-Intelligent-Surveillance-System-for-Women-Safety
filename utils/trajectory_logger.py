"""
Trajectory Logger Module

This module records and stores movement trajectories of
tracked persons detected in video streams.

Purpose:

    - Maintain movement history of tracked objects.
    - Store position coordinates over time.
    - Generate trajectory files for later analysis.
    - Support behavior understanding algorithms.



Trajectory:

A trajectory represents the movement path of an object
across multiple video frames.


Example:

Person ID: 5


Frame 1:

    (120,200)


Frame 2:

    (130,210)


Frame 3:

    (150,240)



Stored trajectory:

[
    [120,200],
    [130,210],
    [150,240]
]



Input:

Tracked objects from ByteTrack:

[
    {
        "id": 1,
        "center": (x,y)
    }
]



Output:

data/

└── trajectories/

        ├── track_1.json

        ├── track_2.json



Pipeline:


Camera

   ↓

YOLO Detection

   ↓

ByteTrack Tracking

   ↓

Person Coordinates

   ↓

Trajectory Logger

   ↓

Movement History



"""



import json

from pathlib import Path

from collections import defaultdict





class TrajectoryLogger:
    """
    Stores movement trajectories of tracked persons.

    The class maintains a history dictionary where
    every tracked ID has its own sequence of positions.

    Example:

        history = {

            1: [
                [100,200],
                [120,230]
            ]

        }

    """



    def __init__(self):
        """
        Initialize trajectory storage.

        Creates:

            1. Memory storage for trajectories.
            2. Output directory for saved files.

        """



        # Stores movement history
        #
        # Key:
        #     Track ID
        #
        # Value:
        #     List of positions
        #

        self.history = defaultdict(list)




        # Directory where trajectory files
        # will be stored

        self.output_dir = Path(

            "data/trajectories"

        )




        # Create directory if it does not exist

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
        """
        Update movement history with new detections.

        Called for every video frame.

        Args:

            tracks (list):

                List of tracked objects.

                Each track contains:

                    id

                    center position



        Processing:

            1. Extract person ID.
            2. Extract center coordinates.
            3. Append position to history.


        Example:


            Input:

            [
                {
                    "id":1,
                    "center":(100,200)
                }
            ]


            Stored:


            history[1]

            [

                [100,200]

            ]

        """



        print(

            "UPDATE CALLED"

        )



        print(

            "Tracks received:",

            len(tracks)

        )




        # Process every tracked person

        for track in tracks:



            # Unique tracker identifier

            track_id = track["id"]




            # Person center coordinate

            center = track["center"]




            # Store current position

            self.history[track_id].append(

                list(center)

            )




            print(

                f"Track {track_id}:",

                len(

                    self.history[track_id]

                ),

                "points"

            )





    def save(self):
        """
        Save stored trajectories into JSON files.

        Each tracked person receives a separate file.

        Output format:


            track_<id>.json


        Example:


            track_5.json


            [
                [100,200],
                [120,220],
                [150,250]
            ]


        """



        print(

            "\nSAVING TRAJECTORIES..."

        )



        print(

            "Total Tracks:",

            len(self.history)

        )




        # Save every tracked person's path

        for track_id, trajectory in self.history.items():



            print(

                f"Track {track_id} ->",

                len(trajectory),

                "points"

            )




            # Ignore very short trajectories
            #
            # Short movements do not provide
            # meaningful behavior information.

            if len(trajectory) < 5:



                print(

                    f"Skipping Track {track_id}"

                )



                continue




            # Create output filename

            file_path = (

                self.output_dir /

                f"track_{track_id}.json"

            )




            # Save trajectory as JSON

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