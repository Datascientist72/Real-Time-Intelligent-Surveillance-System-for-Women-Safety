from core.detector import PersonDetector
from core.tracker import PersonTracker
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from pipelines.fight_pipeline import FightPipeline
from behavior.analyzer import BehaviorAnalyzer

from pipelines.fight_pipeline import FightPipeline
from core.event_logger import EventLogger
from core.risk_engine import RiskEngine

from core.alert import AlertManager

import inspect

print(
    inspect.signature(
        AlertManager.send
    )
)
class SurveillancePipeline:

    def __init__(self):

        self.detector = PersonDetector()
        self.logger = EventLogger()
        self.tracker = PersonTracker()

        self.behavior_analyzer = (
            BehaviorAnalyzer()
        )

        self.fight_pipeline = (
            FightPipeline()
        )

        self.risk_engine = (
            RiskEngine()
        )

        self.alert_manager = (
            AlertManager()
        )

    def process_frame(self, frame):

        detections = self.detector.detect(
            frame
        )

        tracks = self.tracker.update(
            detections
        )

        events = (
            self.behavior_analyzer.analyze(
                tracks,
                detections
            )
        )

        fight_prob = (
            self.fight_pipeline.process_frame(
                frame
            )
        )

        risk = self.risk_engine.calculate(
            events,
            fight_prob
        )
        self.logger.save(
    events,
    risk["score"],
    risk["level"]
)

        if risk["trigger_alert"]:

            report = {

                "events": events,

                "risk_score":
                    risk["score"],

                "risk_level":
                    risk["level"],

                "fight_probability":
                    risk[
                        "fight_probability"
                    ]
            }

            self.alert_manager.send(
                frame,
                report
            )

        return {

            "tracks": tracks,

            "events": events,

            "fight_probability":
                fight_prob,

            "risk": risk
        }