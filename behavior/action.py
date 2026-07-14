class ActionRecognizer:

    def predict(self, clip):

        action = model.predict(clip)

        return action