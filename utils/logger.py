from datetime import datetime

class Logger:

    def log(self, message):

        timestamp = datetime.now()

        with open(
            "events.log",
            "a"
        ) as file:

            file.write(
                f"{timestamp} : {message}\n"
            )