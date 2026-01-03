keywords = ["will", "should", "need to", "assigned", "responsible"]

with open("outputs/meeting_transcript.txt", "r", encoding="utf-8") as f:
    text = f.read()

sentences = text.split(".")
actions = []

for s in sentences:
    for k in keywords:
        if k in s.lower():
            actions.append(s.strip())

with open("outputs/action_items.txt", "w", encoding="utf-8") as f:
    for i, a in enumerate(actions, 1):
        f.write(f"{i}. {a}\n")

print("Action items extracted")
