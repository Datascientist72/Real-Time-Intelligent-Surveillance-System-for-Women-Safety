from collections import defaultdict

class LoiteringDetector:

    def __init__(self):
        self.positions = defaultdict(list)

    def update(self, tracks):

        events = []

        for person in tracks:

            pid = person["id"]

            self.positions[pid].append(
                person["center"]
            )

            if len(self.positions[pid]) > 300:

                positions = self.positions[pid][-300:]

                xs = [p[0] for p in positions]
                ys = [p[1] for p in positions]

                spread = (
                    max(xs) - min(xs)
                ) + (
                    max(ys) - min(ys)
                )

                if spread < 80:

                    events.append({
                        "type": "loitering",
                        "person": pid
                    })

        return events