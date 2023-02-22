# pip install openai-whisper pyaudio
from pyaudio import PyAudio, paInt16
import wave, whisper, os
def microphone(name, seconds):
  with wave.open(name, 'wb') as wf:
    p = PyAudio()
    wf.setnchannels(1)
    sample = p.get_sample_size(paInt16)
    wf.setsampwidth(sample)
    wf.setframerate(44100)
    stream = p.open(format=paInt16,
                    channels=1,
                    rate=44100,
                    input=True)

    chunks = 44100//1024*seconds
    for _ in range(0, chunks):
      wf.writeframes(stream.read(1024))
    stream.close()
    p.terminate()
# record 5 seconds using the microphone
microphone("panic.wav", 5)
model = whisper.load_model("base.en")
r = model.transcribe("panic.wav")
with open("panic.txt", "w") as f:
  f.write(r["text"])
# send panic.txt to the default printer
os.startfile("panic.txt", "print")
os.remove("panic.txt")
os.remove("panic.wav")

