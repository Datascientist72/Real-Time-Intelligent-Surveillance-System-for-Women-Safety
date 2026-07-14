class IncidentClassifier:


    def classify(self, score):

        if score >= 70:

            return "HIGH"


        elif score >= 40:

            return "MEDIUM"


        else:

            return "LOW"