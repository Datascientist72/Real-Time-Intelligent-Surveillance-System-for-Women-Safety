"""
Event Logger Utility Module

This module provides a simple logging mechanism for
recording system events and messages.

Purpose:

    - Store runtime events.
    - Maintain a history of system activities.
    - Support debugging and monitoring.
    - Keep track of important messages generated
      during surveillance operation.



Output:

    events.log


Example:

    2026-07-14 10:30:25.123456 :
    Violence detected for person ID 5



Pipeline:

AI Detection System

        ↓

Event Generation

        ↓

Logger

        ↓

events.log



"""



from datetime import datetime





class Logger:
    """
    Simple file-based event logger.

    This class writes timestamped messages
    into a log file.

    Attributes:

        Log file:

            events.log


    Usage:

        logger = Logger()

        logger.log(
            "Person detected"
        )

    """



    def log(self, message):
        """
        Save a message with timestamp.

        Args:

            message (str):

                Event or information message
                that needs to be recorded.


        Process:

            1. Generate current timestamp.
            2. Open log file.
            3. Append message.
            4. Save record.


        Example:


            Input:

                "Suspicious activity detected"


            Output in events.log:


                2026-07-14 10:30:25 :
                Suspicious activity detected

        """



        # Get current date and time

        timestamp = datetime.now()



        # Open log file in append mode
        #
        # Previous logs are preserved.
        #

        with open(

            "events.log",

            "a"

        ) as file:



            # Write timestamped event

            file.write(

                f"{timestamp} : {message}\n"

            )