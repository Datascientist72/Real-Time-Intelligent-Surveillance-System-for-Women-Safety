import supervision as sv
import numpy as np


class PersonTracker:

    def __init__(self):

        self.tracker = sv.ByteTrack()


    def update(self, detections):

        if len(detections) == 0:
            return []


        boxes = []
        confidences = []
        class_ids = []


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


        # Convert lists to numpy arrays

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


        sv_detections = sv.Detections(

            xyxy=boxes,

            confidence=confidences,

            class_id=class_ids

        )


        tracked = self.tracker.update_with_detections(
            sv_detections
        )


        results = []


        if tracked.tracker_id is None:
            return results



        for xyxy, class_id, tracker_id in zip(

            tracked.xyxy,

            tracked.class_id,

            tracked.tracker_id

        ):


            x1, y1, x2, y2 = xyxy


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