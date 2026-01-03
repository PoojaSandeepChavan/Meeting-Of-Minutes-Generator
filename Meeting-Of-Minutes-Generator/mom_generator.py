from datetime import date

with open("outputs/meeting_transcript.txt", "r", encoding="utf-8") as f:
    transcript = f.read()

with open("outputs/action_items.txt", "r", encoding="utf-8") as f:
    actions = f.read()

mom = f"""
MINUTES OF MEETING
Date: {date.today()}

Agenda:
- Project discussion

Summary:
{transcript[:600]}...

Action Items:
{actions}
"""

with open("outputs/MoM.txt", "w", encoding="utf-8") as f:
    f.write(mom)

print("MoM file created")
