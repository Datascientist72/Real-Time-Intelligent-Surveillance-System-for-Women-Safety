"""
Risk Assessment Module

This module calculates the overall safety risk level by combining
outputs from multiple behavior detection components.

Responsibilities:
    - Assign importance weights to detected behaviors.
    - Combine multiple risk indicators.
    - Integrate violence/fight model probability.
    - Generate final risk score.
    - Classify incident severity.
    - Decide whether an alert should be triggered.

Pipeline Position:

Behavior Detection
        |
        ↓
Risk Engine
        |
        ├── Risk Score
        ├── Risk Level
        └── Alert Decision

"""


class RiskEngine:
    """
    Calculates threat severity from detected behaviors.

    The RiskEngine uses a weighted scoring approach where each
    detected behavior contributes differently to the final risk score.

    Higher severity behaviors receive higher weights.

    Attributes:
        weights (dict):
            Mapping between detected event types and their
            risk contribution values.
    """


    def __init__(self):
        """
        Initialize risk scoring weights.

        Each behavior is assigned a severity value based on
        its potential safety impact.

        Higher values indicate higher risk.
        """

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
        """
        Calculate the final risk score and severity level.

        The function combines:
            1. Rule-based behavior risk scores.
            2. Violence prediction probability.

        Args:
            events (list):
                List of detected behavior events.

                Example:

                [
                    {
                        "type": "following"
                    },
                    {
                        "type": "aggressive_approach"
                    }
                ]

            fight_prob (float, optional):
                Probability produced by violence/action model.

                Range:
                    0.0 - 1.0

        Returns:
            dict:
                Risk assessment result containing:

                score:
                    Final risk score (0-100)

                level:
                    Severity category

                fight_probability:
                    Violence model confidence

                trigger_alert:
                    Whether notification should be generated
        """


        score = 0


        # Add risk contribution from detected behaviors
        for event in events:

            event_type = event.get(
                "type",
                ""
            )


            score += self.weights.get(
                event_type,
                0
            )



        # Add contribution from violence detection model
        if fight_prob is not None:

            score += int(
                fight_prob * 60
            )



        # Limit score to maximum value
        score = min(
            score,
            100
        )



        # Convert numerical score into severity category
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