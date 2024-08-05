from openai import OpenAI

client = OpenAI(api_key="sk-5NeEtRi9DuRq_-aVZmHg2sbLdLogDK3MhhVieb62Q5T3BlbkFJ1ZYO-einMEgbDmg_vJOwLBdWrpWWHLrbTA2yakEDkA")

file_path=r'audio\Sample_Audio_EN.wav'

audio_file= open(file_path, "rb")

transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)
