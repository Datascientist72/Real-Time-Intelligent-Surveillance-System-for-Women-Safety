class CrowdPanicDetector:

    def detect(self, tracks):

        running_count = 0

        for person in tracks:

            if person.get("action") == "running":

                running_count += 1

        if running_count >= 5:

            return [{
                "type": "crowd_panic",
                "count": running_count
            }]

        return []