import json
from pathlib import Path
from datetime import datetime


class EventLogger:

    def __init__(self):
        self.log_file = Path("data/logs/events.jsonl")

        self.log_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def save(
        self,
        events,
        score,
        level,
        camera_id="camera_01",
        location="Unknown",
        frame_id=None
    ):

        if not events:
            return

        record = {
            "timestamp": datetime.now().isoformat(),
            "camera_id": camera_id,
            "location": location,
            "frame_id": frame_id,
            "score": round(float(score), 4),
            "level": level,
            "events": events
        }

        try:
            with open(
                self.log_file,
                "a",
                encoding="utf-8"
            ) as f:
                f.write(
                    json.dumps(record)
                    + "\n"
                )

        except Exception as e:
            print(
                f"[LOGGER ERROR] {e}"
            )