import os
import cv2
import time
from datetime import datetime


class AlertManager:

    def __init__(self):

        self.folder = "data/alerts"

        os.makedirs(
            self.folder,
            exist_ok=True
        )

        self.last_alert_time = 0

        self.cooldown = 10

    def send(
        self,
        frame,
        report
    ):

        current_time = time.time()

        if (
            current_time -
            self.last_alert_time
            < self.cooldown
        ):
            return

        self.last_alert_time = current_time

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        image_path = os.path.join(
            self.folder,
            f"alert_{timestamp}.jpg"
        )

        cv2.imwrite(
            image_path,
            frame
        )

        print("\n ALERT")
        print(report)
        print("Saved:", image_path)
   