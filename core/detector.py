from ultralytics import YOLO


class PersonDetector:

    def __init__(self):

        self.model = YOLO(
            "models/yolov8n.pt"
        )

    def detect(self, frame):

        results = self.model(
            frame,
            verbose=False
        )

        detections = []

        for r in results:

            for box in r.boxes:

                cls = int(box.cls[0])

                conf = float(
                    box.conf[0]
                )

                x1, y1, x2, y2 = map(
                    float,
                    box.xyxy[0]
                )

                detections.append({

                    "class": cls,

                    "confidence": conf,

                    "bbox": [
                        x1,
                        y1,
                        x2,
                        y2
                    ]

                })

        return detections