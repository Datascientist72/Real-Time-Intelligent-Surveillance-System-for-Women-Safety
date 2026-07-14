from pathlib import Path
import cv2
import numpy as np

from pose_extractor import (
    extract_pose_landmarks
)

DATASET_DIR = Path("data/rwf2000")

OUTPUT_DIR = Path(
    "data/pose_sequences"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def extract_frames(
    video_path,
    step=5
):

    cap = cv2.VideoCapture(
        str(video_path)
    )

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


def process_video(
    video_path
):

    frames = extract_frames(
        video_path
    )

    sequence = []

    for frame in frames:

        pose = (
            extract_pose_landmarks(
                frame
            )
        )

        if pose is not None:

            sequence.append(
                pose
            )

    return np.array(
        sequence,
        dtype=np.float32
    )


def process_folder(
    folder_name
):

    video_dir = (
        DATASET_DIR /
        folder_name
    )

    save_dir = (
        OUTPUT_DIR /
        folder_name
    )

    save_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    videos = list(
        video_dir.glob("*.avi")
    )

    print(
        f"\nProcessing {folder_name}"
    )

    for video in videos:

        try:

            sequence = process_video(
                video
            )

            if len(sequence) == 0:

                print(
                    f"Skipped {video.name}"
                )

                continue

            save_path = (
                save_dir /
                f"{video.stem}.npy"
            )

            np.save(
                save_path,
                sequence
            )

            print(
                f"Saved: {video.name}"
            )

        except Exception as e:

            print(
                f"Error: {video.name}"
            )

            print(e)


if __name__ == "__main__":

    process_folder("Fight")

    process_folder("NonFight")

    print(
        "\nDataset creation complete."
    )