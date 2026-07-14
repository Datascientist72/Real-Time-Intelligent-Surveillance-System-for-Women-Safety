import cv2

from pipelines.surveillance_pipeline import (
    SurveillancePipeline
)

# VIDEO_PATH = (
#     r"C:\Users\DELL\Downloads\fightvsnon\fightvsnon\Fight\eifiXLWYul8_0.avi"
# )
cap = cv2.VideoCapture(0)
pipeline = SurveillancePipeline()

# cap = cv2.VideoCapture(VIDEO_PATH)

print(
    "Video Opened:",
    cap.isOpened()
)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    result = pipeline.process_frame(frame)

    if result:

        risk = result["risk"]

        cv2.putText(
            frame,
            f"Risk: {risk['level']}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        cv2.putText(
            frame,
            f"Score: {risk['score']}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2
        )

    cv2.imshow(
        "Community Safety AI",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()