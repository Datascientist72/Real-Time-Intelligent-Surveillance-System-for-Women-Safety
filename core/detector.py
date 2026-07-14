"""
Object Detection Module

This module performs real-time object detection using the YOLOv8
deep learning model.

Purpose:
    - Detect objects present in video frames.
    - Extract bounding boxes.
    - Calculate confidence scores.
    - Provide detection results to the tracking module.

The detector acts as the first AI perception layer in the
surveillance pipeline.

Pipeline Position:

Camera Frame
      |
      ↓
YOLO Detection
      |
      ↓
Bounding Boxes + Confidence
      |
      ↓
Object Tracking
"""

from ultralytics import YOLO


class PersonDetector:
    """
    Performs object detection using YOLOv8.

    The detector receives frames from the camera module and
    identifies objects present in each frame.

    Attributes:
        model (YOLO):
            Loaded YOLOv8 deep learning model.

    Output:
        List of detected objects containing:
            - Class ID
            - Confidence score
            - Bounding box coordinates
    """


    def __init__(self):
        """
        Initialize the YOLO object detection model.

        Loads the pretrained YOLOv8 nano model used for
        real-time object detection.

        Model:
            yolov8n.pt

        Location:
            models/yolov8n.pt
        """

        self.model = YOLO(
            "models/yolov8n.pt"
        )


    def detect(self, frame):
        """
        Detect objects in a video frame.

        The function passes the input frame through YOLO
        and extracts detection information from the results.

        Args:
            frame (numpy.ndarray):
                Current video frame captured from camera.

        Returns:
            list:
                List of detected objects.

        Example output:

        [
            {
                "class": 0,
                "confidence": 0.91,
                "bbox": [
                    120.5,
                    80.2,
                    250.7,
                    400.3
                ]
            }
        ]

        """


        # Run YOLO inference on current frame
        results = self.model(
            frame,
            verbose=False
        )


        detections = []


        # Process detection results
        for r in results:

            for box in r.boxes:


                # Extract class ID
                cls = int(box.cls[0])


                # Extract confidence score
                conf = float(
                    box.conf[0]
                )


                # Extract bounding box coordinates
                x1, y1, x2, y2 = map(
                    float,
                    box.xyxy[0]
                )


                detections.append(

                    {
                        "class": cls,

                        "confidence": conf,

                        "bbox": [
                            x1,
                            y1,
                            x2,
                            y2
                        ]
                    }

                )


        return detections