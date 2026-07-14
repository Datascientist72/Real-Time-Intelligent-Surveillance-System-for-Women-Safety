class AbandonedObjectDetector:

    def detect(self, detections):

        events = []

        for obj in detections:

            if obj["class_name"] == "bag":

                events.append({
                    "type": "suspicious_bag"
                })

        return events