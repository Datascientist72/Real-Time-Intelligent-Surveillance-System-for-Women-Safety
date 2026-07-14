import os
import cv2
from datetime import datetime


class AlertManager:


    def __init__(self):

        self.folder = "data/alerts"

        os.makedirs(
            self.folder,
            exist_ok=True
        )


    def send(self, frame, report):

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


        print("\n===== ALERT =====")

        print(report)

        print(
            "Saved:",
            image_path
        )

        print("=================\n")