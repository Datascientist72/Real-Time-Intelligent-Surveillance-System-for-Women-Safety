from collections import defaultdict

from behavior.following import FollowingDetector
from behavior.loitering import LoiteringDetector
from behavior.aggressive_approach import (
    AggressiveApproachDetector
)
from behavior.encirclement import (
    EncirclementDetector
)


class BehaviorAnalyzer:

    def __init__(self):

        self.history = defaultdict(list)
        self.start_time = {}

        self.following_detector = (
            FollowingDetector()
        )

        self.loitering_detector = (
            LoiteringDetector()
        )

        self.aggressive_detector = (
            AggressiveApproachDetector()
        )

        self.encirclement_detector = (
            EncirclementDetector()
        )

    def analyze(
        self,
        tracks,
        detections=None
    ):

        events = []

        events.extend(
            self.following_detector.update(
                tracks
            )
        )

        events.extend(
            self.loitering_detector.update(
                tracks
            )
        )

        events.extend(
            self.aggressive_detector.update(
                tracks
            )
        )

        events.extend(
            self.encirclement_detector.update(
                tracks
            )
        )

        if len(tracks) >= 5:

            events.append({

                "type": "crowd",

                "count": len(tracks)

            })

        return events