# import sounddevice as sd
# from scipy.io.wavfile import write

# fs = 44100
# duration = 30  # seconds

# print("Recording started...")
# audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
# sd.wait()

# write("outputs/meeting.wav", fs, audio)
# print("Recording saved")

import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

# Sample rate
fs = 44100

# To store audio chunks
recorded_audio = []

print("🎙️ Press ENTER to start recording")
input()

print("🔴 Recording... Press Ctrl + C to stop")

# This function runs continuously while recording
def callback(indata, frames, time, status):
    recorded_audio.append(indata.copy())

try:
    # Open microphone stream
    with sd.InputStream(samplerate=fs, channels=1, callback=callback):
        while True:
            pass

except KeyboardInterrupt:
    print("\n Recording stopped")

# Combine all chunks into one array
audio = np.concatenate(recorded_audio, axis=0)

# Save audio file
write("outputs/meeting.wav", fs, audio)

print(" Audio saved successfully at outputs/meeting.wav")