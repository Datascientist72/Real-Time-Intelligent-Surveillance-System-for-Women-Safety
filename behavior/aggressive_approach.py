from collections import defaultdict
import math


class AggressiveApproachDetector:

    def __init__(self):

        self.history = defaultdict(list)

    def distance(self, p1, p2):

        return math.sqrt(

            (p1[0] - p2[0]) ** 2 +

            (p1[1] - p2[1]) ** 2

        )

    def update(self, tracks):

        events = []

        for t in tracks:

            self.history[
                t["id"]
            ].append(
                t["center"]
            )

            self.history[
                t["id"]
            ] = self.history[
                t["id"]
            ][-10:]

        ids = list(self.history.keys())

        for a in ids:

            for b in ids:

                if a == b:
                    continue

                h1 = self.history[a]
                h2 = self.history[b]

                if len(h1) < 5:
                    continue

                old_d = self.distance(
                    h1[0],
                    h2[0]
                )

                new_d = self.distance(
                    h1[-1],
                    h2[-1]
                )

                if old_d - new_d > 80:

                    events.append({

                        "type":
                        "aggressive_approach",

                        "source": a,

                        "target": b,

                        "distance_change":
                        round(
                            old_d - new_d
                        )
                    })

        return events