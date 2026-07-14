from collections import defaultdict
import math


class FollowingDetector:

    def __init__(self):

        self.history = defaultdict(list)

    def distance(self, p1, p2):

        return math.sqrt(
            (p1[0] - p2[0]) ** 2 +
            (p1[1] - p2[1]) ** 2
        )

    def direction(self, history):

        if len(history) < 10:
            return None

        start = history[-10]
        end = history[-1]

        return (
            end[0] - start[0],
            end[1] - start[1]
        )

    def cosine_similarity(self, v1, v2):

        mag1 = math.sqrt(
            v1[0]**2 + v1[1]**2
        )

        mag2 = math.sqrt(
            v2[0]**2 + v2[1]**2
        )

        if mag1 == 0 or mag2 == 0:
            return 0

        dot = (
            v1[0] * v2[0] +
            v1[1] * v2[1]
        )

        return dot / (mag1 * mag2)

    def update(self, tracks):

        events = []

        for track in tracks:

            tid = track["id"]

            self.history[tid].append(
                track["center"]
            )

            self.history[tid] = (
                self.history[tid][-60:]
            )

        ids = list(
            self.history.keys()
        )

        for i in range(len(ids)):

            for j in range(i + 1, len(ids)):

                id1 = ids[i]
                id2 = ids[j]

                h1 = self.history[id1]
                h2 = self.history[id2]

                if len(h1) < 20:
                    continue

                if len(h2) < 20:
                    continue

                close_frames = 0

                for p1, p2 in zip(
                    h1[-20:],
                    h2[-20:]
                ):

                    d = self.distance(
                        p1,
                        p2
                    )

                    if d < 100:
                        close_frames += 1

                v1 = self.direction(h1)
                v2 = self.direction(h2)

                if not v1 or not v2:
                    continue

                similarity = self.cosine_similarity(
                    v1,
                    v2
                )

                if (
                    close_frames > 15
                    and similarity > 0.8
                ):

                    events.append({

                        "type":
                        "persistent_following",

                        "person1":
                        id1,

                        "person2":
                        id2,

                        "frames":
                        close_frames,

                        "direction_similarity":
                        round(similarity, 2)

                    })

        return events