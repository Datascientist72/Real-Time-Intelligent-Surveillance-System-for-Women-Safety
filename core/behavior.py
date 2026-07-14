from collections import defaultdict

class BehaviorAnalyzer:

    def __init__(self):
        self.position_history = defaultdict(list)

    def analyze(self, tracks):

        events = []

        for person in tracks:

            person_id = person["id"]
            center = person["center"]

            self.position_history[person_id].append(center)

            if len(self.position_history[person_id]) > 100:

                positions = self.position_history[person_id][-100:]

                xs = [p[0] for p in positions]
                ys = [p[1] for p in positions]

                movement = (
                    max(xs) - min(xs)
                ) + (
                    max(ys) - min(ys)
                )

                if movement < 50:

                    events.append({
                        "type": "loitering",
                        "person": person_id
                    })

        return events