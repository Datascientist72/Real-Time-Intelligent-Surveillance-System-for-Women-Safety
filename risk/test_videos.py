import cv2
from pathlib import Path

fight_dir = Path(
    r"C:\Users\DELL\OneDrive\Desktop\community_safety_ai\data\rwf2000\Fight"
)

video = list(fight_dir.glob("*.avi"))[0]

print("Testing:", video)

cap = cv2.VideoCapture(str(video))

print("Opened:", cap.isOpened())

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1

print("Frames:", frame_count)

cap.release()