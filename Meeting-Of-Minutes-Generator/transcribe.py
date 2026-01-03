import whisper
import os

os.makedirs("outputs", exist_ok=True)

model = whisper.load_model("base")

print("Transcribing audio...")
result = model.transcribe("outputs/meeting.wav")

with open("outputs/meeting_transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Transcript file created")
