class RiskEngine:

    def __init__(self):

        self.weights = {

            "persistent_following": 25,

            "aggressive_approach": 35,

            "encirclement": 40,

            "loitering": 20,

            "rapid_movement": 15,

            "crowd": 25,

            "violence": 60,

            "weapon": 80
        }

    def calculate(
        self,
        events,
        fight_prob=None
    ):

        score = 0

        for event in events:

            event_type = event.get(
                "type",
                ""
            )

            score += self.weights.get(
                event_type,
                0
            )

        if fight_prob is not None:

            score += int(
                fight_prob * 60
            )

        score = min(
            score,
            100
        )

        if score >= 90:

            level = "CRITICAL"

        elif score >= 70:

            level = "HIGH"

        elif score >= 40:

            level = "MEDIUM"

        else:

            level = "LOW"

        return {

            "score": score,

            "level": level,

            "fight_probability": (
                round(fight_prob, 2)
                if fight_prob is not None
                else None
            ),

            "trigger_alert": (
                level in [
                    "HIGH",
                    "CRITICAL"
                ]
            )
        }