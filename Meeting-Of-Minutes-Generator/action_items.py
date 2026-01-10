# keywords = ["will", "should", "need to", "assigned", "responsible"]

# with open("outputs/meeting_transcript.txt", "r", encoding="utf-8") as f:
#     text = f.read()

# sentences = text.split(".")
# actions = []

# for s in sentences:
#     for k in keywords:
#         if k in s.lower():
#             actions.append(s.strip())

# with open("outputs/action_items.txt", "w", encoding="utf-8") as f:
#     for i, a in enumerate(actions, 1):
#         f.write(f"{i}. {a}\n")

# print("Action items extracted")


import re

# Action keywords (can be expanded)
KEYWORDS = [
    "will", "should", "need to", "needs to",
    "assigned", "responsible", "have to",
    "must", "action item", "to be done"
]

INPUT_FILE = "outputs/meeting_transcript.txt"
OUTPUT_FILE = "outputs/action_items.txt"

# Read transcript
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Clean text
text = re.sub(r"\s+", " ", text).strip()

# Split into sentences properly
sentences = re.split(r'(?<=[.!?])\s+', text)

actions = set()  # avoids duplicates

for sentence in sentences:
    sentence_lower = sentence.lower()
    for keyword in KEYWORDS:
        if re.search(rf"\b{re.escape(keyword)}\b", sentence_lower):
            actions.add(sentence.strip())
            break  # avoid repeated keyword matches

# Write action items
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    if actions:
        for i, action in enumerate(sorted(actions), 1):
            f.write(f"{i}. {action}\n")
    else:
        f.write("No action items found.\n")

print(f" {len(actions)} action items extracted successfully")
