.

📝 Meeting Of Minutes Generator

A Python-based application that records meetings, converts speech to text, extracts key discussion points and action items, and generates well-formatted Meeting Minutes in text or PDF format.

🚀 Features

🎙️ Record meeting audio

🧠 Convert speech to text

📌 Automatically extract action items

🗂️ Generate structured Meeting Minutes

📄 Export output as TXT / PDF

🐍 Simple Python-based implementation

🛠️ Tech Stack

Programming Language: Python

Libraries Used:

Whisper (Speech-to-Text)

sounddevice

scipy

python-docx

reportlab

File Handling: TXT, PDF

Version Control: Git & GitHub

Project Structure

MEETING-OF-MINUTES-GENERATOR
│

├── .venv/

│   └── (Virtual Environment – should NOT be pushed to GitHub)

│

├── outputs/

│   ├── action_items.txt        # Extracted action items

│   ├── meeting_transcript.txt  # Full meeting transcription

│   ├── meeting.wav             # Recorded meeting audio

│   ├── MoM.docx                # Minutes of Meeting (Word)

│   ├── MoM.pdf                 # Minutes of Meeting (PDF)
│   └── MoM.txt                 # Minutes of Meeting (Text)
│
├── action_items.py              # Logic to extract action items
├── export_pdf.py                # Export MoM to PDF
├── export_word.py               # Export MoM to Word
├── mom_generator.py             # Main script to generate MoM
├── record_meeting.py            # Records audio from microphone
├── transcribe.py                # Converts audio to text
│
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── .gitignore                   # Files/folders to ignore
