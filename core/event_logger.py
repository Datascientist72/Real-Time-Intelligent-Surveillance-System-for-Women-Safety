"""
Event Logging Module

This module stores detected safety events and risk assessments
for future analysis.

Responsibilities:
    - Create an event log storage location.
    - Record detected behaviors.
    - Store risk scores and severity levels.
    - Maintain timestamped incident history.

The logger uses JSON Lines (.jsonl) format, where each line
represents one independent event record.

Pipeline Position:

Risk Assessment
        |
        ↓
Event Logger
        |
        ↓
events.jsonl
        |
        ↓
Dashboard / Investigation / Reports
"""

import json
from pathlib import Path
from datetime import datetime


class EventLogger:
    """
    Maintains a persistent log of detected surveillance events.

    Each event record contains:
        - Timestamp
        - Detected behaviors
        - Risk score
        - Risk severity level

    Attributes:
        log_file (Path):
            Location where event records are stored.
    """


    def __init__(self):
        """
        Initialize the event logger.

        Creates the log directory if it does not already exist.

        Log Format:
            JSON Lines (.jsonl)

        Storage Location:
            data/logs/events.jsonl
        """

        self.log_file = Path(
            "data/logs/events.jsonl"
        )


        # Create parent directories automatically
        self.log_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )


    def save(
        self,
        events,
        score,
        level
    ):
        """
        Save a detected event record.

        The function stores information about detected behaviors
        along with the calculated risk score and risk category.

        Args:
            events (list):
                List of detected behaviors.

                Example:
                [
                    {
                        "type": "loitering",
                        "person": 5
                    }
                ]

            score (int/float):
                Calculated risk score.

            level (str):
                Risk category.

                Examples:
                    LOW
                    MEDIUM
                    HIGH
                    CRITICAL

        Returns:
            None

        """

        # Ignore empty events
        if not events:
            return


        # Create structured event record
        record = {

            "timestamp":
            datetime.now().isoformat(),


            "events":
            events,


            "risk_score":
            score,


            "risk_level":
            level
        }


        # Append event record to JSONL file
        with open(
            self.log_file,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                json.dumps(record)
            )

            f.write("\n")