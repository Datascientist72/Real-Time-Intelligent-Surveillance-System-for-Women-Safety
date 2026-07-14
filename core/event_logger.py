import json
from pathlib import Path
from datetime import datetime


class EventLogger:

    def __init__(self):

        self.log_file = Path(
            "data/logs/events.jsonl"
        )

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

        if not events:
            return

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

        with open(
            self.log_file,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                json.dumps(record)
            )

            f.write("\n")