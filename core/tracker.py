"""
Object Tracking Module

This module performs multi-object tracking using ByteTrack.

Purpose:
    - Assign unique IDs to detected objects.
    - Maintain object identity across video frames.
    - Generate tracking information required for behavior analysis.

The tracker converts frame-level detections into continuous
object trajectories.

Pipeline Position:

YOLO Detection
        |
        ↓
ByteTrack Tracker
        |
        ↓
Tracked Objects
        |
        ↓
Behavior Understanding
"""

import supervision as sv
import numpy as np


class PersonTracker:
    """
    Tracks detected persons across consecutive video frames.

    This class uses ByteTrack to associate detections from
    different frames and assign persistent tracking IDs.

    Attributes:
        tracker:
            ByteTrack tracking algorithm instance.

    Output:
        List of tracked objects containing:

            - Unique ID
            - Object class
            - Bounding box
            - Center position
    """


    def __init__(self):
        """
        Initialize ByteTrack tracker.

        ByteTrack associates objects based on their movement
        and detection information.
        """

        self.tracker = sv.ByteTrack()



    def update(self, detections):
        """
        Update tracker with new object detections.

        The function converts YOLO detection outputs into
        supervision format and updates object tracks.

        Args:
            detections (list):
                Detection results from PersonDetector.

                Example:

                [
                    {
                        "class": 0,
                        "confidence": 0.92,
                        "bbox": [
                            x1,y1,x2,y2
                        ]
                    }
                ]

        Returns:
            list:
                Tracked object information.

                Example:

                [
                    {
                        "id": 1,
                        "class": 0,
                        "center": (250,300),
                        "bbox": [
                            100,150,300,450
                        ]
                    }
                ]

        """


        # No detections available
        if len(detections) == 0:
            return []



        boxes = []

        confidences = []

        class_ids = []



        # Extract detection information
        for det in detections:

            boxes.append(
                det["bbox"]
            )

            confidences.append(
                det["confidence"]
            )

            class_ids.append(
                det["class"]
            )



        # Convert to numpy arrays required by ByteTrack
        boxes = np.array(
            boxes,
            dtype=np.float32
        )


        confidences = np.array(
            confidences,
            dtype=np.float32
        )


        class_ids = np.array(
            class_ids,
            dtype=int
        )



        # Create supervision detection object
        sv_detections = sv.Detections(

            xyxy=boxes,

            confidence=confidences,

            class_id=class_ids

        )



        # Update object tracking
        tracked = self.tracker.update_with_detections(
            sv_detections
        )



        results = []



        # No active tracks
        if tracked.tracker_id is None:
            return results



        # Extract tracked object information
        for xyxy, class_id, tracker_id in zip(

            tracked.xyxy,

            tracked.class_id,

            tracked.tracker_id

        ):


            x1, y1, x2, y2 = xyxy



            # Calculate object center point
            center = (

                int((x1+x2)/2),

                int((y1+y2)/2)

            )



            results.append({

                "id": int(tracker_id),

                "class": int(class_id),

                "center": center,

                "bbox": [

                    int(x1),

                    int(y1),

                    int(x2),

                    int(y2)

                ]

            })


        return results