# pip install pyaudio win32printing
# use https://github.com/openai/whisper
# to see how to install whisper
from pyaudio import PyAudio, paInt16
import wave, whisper, os
from win32printing import Printer

def microphone(name, seconds):
  with wave.open(name, 'wb') as wf:
    p = PyAudio()
    wf.setnchannels(2)
    sample = p.get_sample_size(paInt16)
    wf.setsampwidth(sample)
    wf.setframerate(44100)
    stream = p.open(format=paInt16,
                    channels=2,
                    rate=44100,
                    input=True)
    chunks = 44100//1024*seconds
    for _ in range(0, chunks):
      wf.writeframes(stream.read(1024))
    stream.close()
    p.terminate()
# record 5 seconds into panic.wav
microphone("panic.wav", 5)
model = whisper.load_model("base.en")
r = model.transcribe(".\\panic.wav")
with Printer(linegap=1) as printer:
  printer.text(r["text"])
os.remove("panic.wav")

