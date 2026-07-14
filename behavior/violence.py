from pathlib import Path
import cv2

DATASET_DIR = Path("data/rwf2000")


def load_videos():

    fight_videos = list((DATASET_DIR / "Fight").glob("*.avi"))
    nonfight_videos = list((DATASET_DIR / "NonFight").glob("*.avi"))

    return fight_videos, nonfight_videos


def extract_frames(video_path, step=5):

    cap = cv2.VideoCapture(str(video_path))

    frames = []
    frame_id = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        if frame_id % step == 0:
            frames.append(frame)

        frame_id += 1

    cap.release()

    return frames


if __name__ == "__main__":

    fight, nonfight = load_videos()

    print(f"Fight videos: {len(fight)}")
    print(f"NonFight videos: {len(nonfight)}")

    if len(fight) > 0:

        frames = extract_frames(fight[0])

        print(f"Extracted {len(frames)} frames")

        if len(frames) > 0:
            print("Frame shape:", frames[0].shape)
            if len(fight) > 0:

                frames = extract_frames(fight[0])

    print(f"Extracted {len(frames)} frames")

    if len(frames) > 0:

        print("Frame shape:", frames[0].shape)

        print("Height:", frames[0].shape[0])
        print("Width :", frames[0].shape[1])
        print("Channels:", frames[0].shape[2])

        print("Data type:", frames[0].dtype)