"""
Real-Time Surveillance Pipeline Runner

This module provides the execution interface for the
Community Safety AI surveillance system.

It connects the live video source with the complete
AI processing pipeline.

Purpose:

    - Capture real-time video frames.
    - Send frames to SurveillancePipeline.
    - Receive risk assessment results.
    - Display detected risk information.
    - Provide live surveillance visualization.



Processing Pipeline:


Camera / Video Input

        ↓

SurveillancePipeline

        ↓

Person Detection

        ↓

Tracking

        ↓

Pose Analysis

        ↓

Behavior Detection

        ↓

Risk Assessment

        ↓

Incident Classification

        ↓

Live Display



Input:

    Video source:

        - Webcam
        - CCTV camera
        - Video file



Output:

    Live window showing:

        - Risk level
        - Risk score
        - Processed video frames



Controls:

    Press:

        q

    to stop surveillance.



"""



import cv2



from pipelines.surveillance_pipeline import (

    SurveillancePipeline

)





# ------------------------------------------------
# Video Source Configuration
# ------------------------------------------------
#
# Default:
#
#       Webcam
#
# Can be replaced with:
#
#       CCTV stream
#
#       Video file path
#
# ------------------------------------------------



cap = cv2.VideoCapture(0)




# Initialize complete AI pipeline

pipeline = SurveillancePipeline()




print(

    "Video Opened:",

    cap.isOpened()

)





# Real-Time Processing Loop



while True:



    # Capture frame

    ret, frame = cap.read()



    # Stop if frame unavailable

    if not ret:

        break





    
    # Process Frame
   
    #
    # The pipeline performs:
    #
    #   Detection
    #   Tracking
    #   Behavior Analysis
    #   Risk Calculation
    #
 


    result = pipeline.process_frame(

        frame

    )





    # Display risk information

    if result:



        risk = result["risk"]




        # Display risk level


        cv2.putText(

            frame,

            f"Risk: {risk['level']}",

            (20,40),

            cv2.FONT_HERSHEY_SIMPLEX,

            1,

            (0,0,255),

            2

        )




        # Display numerical score


        cv2.putText(

            frame,

            f"Score: {risk['score']}",

            (20,80),

            cv2.FONT_HERSHEY_SIMPLEX,

            1,

            (0,255,255),

            2

        )





    # Show processed video


    cv2.imshow(

        "Community Safety AI",

        frame

    )





    # Exit condition

    if cv2.waitKey(1) & 0xFF == ord("q"):

        break





# Shutdown




# Release video source

cap.release()



# Close OpenCV windows

cv2.destroyAllWindows()