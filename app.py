print("APP STARTED")

import cv2

from utils.event_logger import EventLogger
from utils.trajectory_logger import TrajectoryLogger

from core.camera import Camera
from core.detector import PersonDetector
from core.tracker import PersonTracker

from behavior.analyzer import BehaviorAnalyzer

from risk.scorer import RiskScorer
from risk.classifier import IncidentClassifier

from explain.llm_report import ReportGenerator
from alert.manager import AlertManager



camera = Camera(0)

detector = PersonDetector()

tracker = PersonTracker()

trajectory_logger = TrajectoryLogger()

behavior = BehaviorAnalyzer()

risk_engine = RiskScorer()

classifier = IncidentClassifier()

reporter = ReportGenerator()

alerter = AlertManager()

logger = EventLogger()

last_report = None

frame_count = 0


# Main Loop


while True:

    ret, frame = camera.read()

    if not ret:

        print("Failed to read camera")

        break

    frame_count += 1

  
    # YOLO Detection
   

    detections = detector.detect(frame)

    # Draw detections

    for det in detections:

        x1, y1, x2, y2 = map(
            int,
            det["bbox"]
        )

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Person",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )
    # Tracking
    

    tracks = tracker.update(
        detections
    )

    # Save trajectories
    trajectory_logger.update(
        tracks
    )

    # Draw IDs

    for track in tracks:

        cx, cy = track["center"]

        cv2.putText(
            frame,
            f"ID:{track['id']}",
            (cx, cy),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )

    # -----------------------------
    # Behavior Analysis
    # -----------------------------

    events = behavior.analyze(
        tracks,
        detections
    )

    # -----------------------------
    # Risk Scoring
    # -----------------------------

    score = risk_engine.calculate(
        events
    )

    level = classifier.classify(
        score
    )

    # -----------------------------
    # Event Logging
    # -----------------------------

    logger.save(
        events,
        score,
        level
    )

    # -----------------------------
    # Generate Report
    # -----------------------------

    report = reporter.generate(
        events,
        score,
        level
    )

    if report != last_report:

        print("\n")
        print(report)

        last_report = report

    # -----------------------------
    # Display Risk Info
    # -----------------------------

    cv2.putText(
        frame,
        f"Risk: {score}",
        (20, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        f"Level: {level}",
        (20, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    # -----------------------------
    # Display Events
    # -----------------------------

    y = 100

    for event in events[:5]:

        cv2.putText(
            frame,
            event["type"],
            (20, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2
        )

        y += 30

   
    # Alerts
  

    if score >= 70:

        alerter.send(
            frame,
            report
        )


    # Show Window
   

    cv2.imshow(
        "Community Safety AI",
        frame
    )

    key = cv2.waitKey(1)

    if key & 0xFF == ord("q"):

        break

# Save Trajectories

trajectory_logger.save()

print("Trajectories saved.")

camera.release()

cv2.destroyAllWindows()