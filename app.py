"""
Women Safety AI - Main Application Pipeline

This module is the entry point of the surveillance system.

It integrates all AI components:

    - Camera Input
    - Person Detection (YOLO)
    - Person Tracking (ByteTrack)
    - Trajectory Logging
    - Behavior Analysis
    - Risk Assessment
    - Incident Classification
    - Report Generation
    - Alert Management
    - Event Logging


System Pipeline:


Camera

   ↓

YOLO Person Detection

   ↓

ByteTrack Tracking

   ↓

Trajectory Logging

   ↓

Behavior Analysis

   ↓

Risk Scoring

   ↓

Incident Classification

   ↓

AI Report Generation

   ↓

Alert System



Purpose:

    Continuously analyze live video frames and
    detect potentially dangerous situations.



Input:

    Live camera stream


Output:

    - Annotated video feed
    - Risk level
    - Detected events
    - Incident reports
    - Saved alerts
    - Movement trajectories



"""



print("APP STARTED")



import cv2

# Import System Components



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





# -----------------------------
# Initialize Components
# -----------------------------


# Camera input

camera = Camera(0)



# YOLO person detector

detector = PersonDetector()



# ByteTrack object tracker

tracker = PersonTracker()



# Stores movement paths

trajectory_logger = TrajectoryLogger()



# Detects suspicious behaviors

behavior = BehaviorAnalyzer()



# Calculates numerical risk score

risk_engine = RiskScorer()



# Converts score into incident level

classifier = IncidentClassifier()



# Generates human-readable report

reporter = ReportGenerator()



# Sends alerts

alerter = AlertManager()



# Stores events

logger = EventLogger()





# Prevent repeated printing
# of identical reports

last_report = None



frame_count = 0





# =================================================
# Main Real-Time Surveillance Loop
# =================================================


while True:



    # -----------------------------------------
    # Capture Frame
    # -----------------------------------------


    ret, frame = camera.read()



    if not ret:


        print(

            "Failed to read camera"

        )


        break



    frame_count += 1





    # -----------------------------------------
    # Person Detection
    # -----------------------------------------
    #
    # YOLO identifies persons present
    # in the current frame.
    #
    # Output:
    #
    # Bounding boxes and confidence scores
    #
    # -----------------------------------------


    detections = detector.detect(frame)





    # Draw detected persons

    for det in detections:



        x1, y1, x2, y2 = map(

            int,

            det["bbox"]

        )



        cv2.rectangle(

            frame,

            (x1,y1),

            (x2,y2),

            (0,255,0),

            2

        )



        cv2.putText(

            frame,

            "Person",

            (x1,y1-10),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.6,

            (0,255,0),

            2

        )





    # -----------------------------------------
    # Person Tracking
    # -----------------------------------------
    #
    # Assigns unique IDs to detected persons.
    #
    # -----------------------------------------


    tracks = tracker.update(

        detections

    )





    # Store movement history

    trajectory_logger.update(

        tracks

    )





    # Display tracking IDs

    for track in tracks:



        cx,cy = track["center"]



        cv2.putText(

            frame,

            f"ID:{track['id']}",

            (cx,cy),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.6,

            (255,0,0),

            2

        )





    # -----------------------------------------
    # Behavior Analysis
    # -----------------------------------------
    #
    # Detects suspicious activities:
    #
    #   - Loitering
    #   - Following
    #   - Aggressive movement
    #
    # -----------------------------------------


    events = behavior.analyze(

        tracks,

        detections

    )





    # -----------------------------------------
    # Risk Assessment
    # -----------------------------------------


    score = risk_engine.calculate(

        events

    )



    level = classifier.classify(

        score

    )





    # -----------------------------------------
    # Store Events
    # -----------------------------------------


    logger.save(

        events,

        score,

        level

    )





    # -----------------------------------------
    # Generate Incident Report
    # -----------------------------------------


    report = reporter.generate(

        events,

        score,

        level

    )




    if report != last_report:


        print("\n")

        print(report)


        last_report = report





    # -----------------------------------------
    # Display Risk Information
    # -----------------------------------------


    cv2.putText(

        frame,

        f"Risk: {score}",

        (20,30),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.8,

        (0,0,255),

        2

    )



    cv2.putText(

        frame,

        f"Level: {level}",

        (20,65),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.8,

        (0,0,255),

        2

    )





    # -----------------------------------------
    # Display Detected Events
    # -----------------------------------------


    y = 100



    for event in events[:5]:


        cv2.putText(

            frame,

            event["type"],

            (20,y),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.6,

            (0,255,255),

            2

        )


        y += 30





    # -----------------------------------------
    # Trigger Alert
    # -----------------------------------------


    if score >= 70:


        alerter.send(

            frame,

            report

        )





    # Display live surveillance window


    cv2.imshow(

        "Community Safety AI",

        frame

    )





    key = cv2.waitKey(1)



    if key & 0xFF == ord("q"):


        break





# =================================================
# Shutdown Procedure
# =================================================



# Save collected movement paths

trajectory_logger.save()



print(

    "Trajectories saved."

)



# Release camera

camera.release()



# Close OpenCV windows

cv2.destroyAllWindows()