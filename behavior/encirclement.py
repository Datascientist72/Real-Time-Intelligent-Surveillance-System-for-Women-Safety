import math


class EncirclementDetector:

    def distance(self, p1, p2):

        return math.sqrt(

            (p1[0] - p2[0]) ** 2 +

            (p1[1] - p2[1]) ** 2

        )

    def update(self, tracks):

        events = []

        for target in tracks:

            nearby = 0

            for other in tracks:

                if target["id"] == other["id"]:
                    continue

                d = self.distance(

                    target["center"],

                    other["center"]

                )

                if d < 120:

                    nearby += 1

            if nearby >= 3:

                events.append({

                    "type": "encirclement",

                    "target": target["id"],

                    "count": nearby

                })

        return events