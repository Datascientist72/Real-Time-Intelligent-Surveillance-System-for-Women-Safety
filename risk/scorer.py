class RiskScorer:

    def calculate(self, events):

        score = 0

        for event in events:

            etype = event["type"]

            if etype == "rapid_movement":
                score += 10

            elif etype == "loitering":
                score += 15

            elif etype == "following":
                score += 25

            elif etype == "persistent_following":
                score += 40

            elif etype == "crowd":
                score += 20

            elif etype == "violence":
                score += 60

        return min(score, 100)