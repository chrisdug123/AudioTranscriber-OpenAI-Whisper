from openai import OpenAI

client = OpenAI(api_key="sk-5NeEtRi9DuRq_-aVZmHg2sbLdLogDK3MhhVieb62Q5T3BlbkFJ1ZYO-einMEgbDmg_vJOwLBdWrpWWHLrbTA2yakEDkA")

file_path=r'audio\translation.wav'

audio_file= open(file_path, "rb")

translation = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file
)
print(translation.text)
