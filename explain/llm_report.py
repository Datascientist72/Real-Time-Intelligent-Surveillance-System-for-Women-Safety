class ReportGenerator:

    def generate(
        self,
        events,
        score,
        level
    ):

        report = f"""

Community Safety AI Report

Risk Score:
{score}

Risk Level:
{level}

Detected Events:
"""

        if not events:

            report += (
                "\nNo suspicious behavior detected."
            )

        else:

            for e in events:

                report += f"\n- {e}"

        return report