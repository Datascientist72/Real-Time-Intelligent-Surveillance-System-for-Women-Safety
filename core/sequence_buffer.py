from collections import defaultdict

class SequenceBuffer:

    def __init__(self):

        self.buffer = defaultdict(list)

    def update(
        self,
        track_id,
        pose_vector
    ):

        self.buffer[track_id].append(
            pose_vector
        )

        if len(
            self.buffer[track_id]
        ) > 30:

            self.buffer[track_id].pop(0)

        return (
            len(
                self.buffer[track_id]
            ) == 30
        )

    def get(
        self,
        track_id
    ):

        return self.buffer[track_id]