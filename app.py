import os
from flask import Flask, request, jsonify,render_template
from openai import OpenAI

app=Flask(__name__)
client = OpenAI(api_key='sk-9-aaX7Oc45G_X05aHaMdaqoKtjjx7rR5QtaHgIgCwOT3BlbkFJKJX4AyzjqtPmHyeNhIIBiyXTZ4dtxAN3G8ciMhkC0A')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio_file' not in request.files:
        return jsonify(error='No audio file given'), 400
    
    file = request.files['audio_file']

    if file.filename=='':
        return jsonify(error='No selected file found'), 400
    
    if file:
        try:
            temp_file_path=os.path.join('audio', file.filename)
            file.save(temp_file_path)

            with open(temp_file_path, "rb") as audio_file:
                response = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
            os.remove(temp_file_path)

            return jsonify(transcription=response.text),200
        except Exception as e:
            return jsonify(error=str(e)), 500


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5123, debug=True)