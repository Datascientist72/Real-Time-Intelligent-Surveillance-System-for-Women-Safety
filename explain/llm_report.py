"""
Incident Report Generation Module

This module generates human-readable safety reports from
AI system outputs.

Purpose:
    - Convert detected events into understandable descriptions.
    - Combine risk score and severity information.
    - Provide structured reports for alerts and dashboards.

Pipeline Position:

AI Predictions
       |
       ↓
Risk Assessment
       |
       ↓
Report Generator
       |
       ↓
Human-readable Incident Report
"""


class ReportGenerator:
    """
    Generates safety incident reports.

    The class transforms machine-generated information into
    a readable format for security operators.

    Generated reports contain:

        - Risk score
        - Risk level
        - Detected events
    """


    def generate(
        self,
        events,
        score,
        level
    ):
        """
        Generate an incident report.

        Args:
            events (list):
                List of detected suspicious behaviors.

                Example:

                [
                    {
                        "type": "loitering",
                        "person": 3
                    }
                ]


            score (int):
                Calculated risk score from RiskEngine.


            level (str):
                Risk severity category.

                Examples:

                    LOW
                    MEDIUM
                    HIGH
                    CRITICAL


        Returns:
            str:
                Formatted safety report.

        """


        report = f"""

Community Safety AI Report

Risk Score:
{score}

Risk Level:
{level}

Detected Events:
"""


        # Handle case where no events are detected
        if not events:

            report += (
                "\nNo suspicious behavior detected."
            )


        else:

            # Add each detected event
            for e in events:

                report += f"\n- {e}"


        return report