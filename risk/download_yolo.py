from ultralytics import YOLO

print("Downloading YOLO model...")

model = YOLO("yolov8n.pt")

print("Downloaded successfully")