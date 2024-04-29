import whisper

# Función que transcribe a partir del archivo de audio mp3
def tran(audio_file, nivel):
    model = whisper.load_model(nivel)
    result = model.transcribe(audio_file, language = "es", fp16 = False)

    name_text = audio_file.replace(".mp3", "")
    
    with open(f"{name_text}.txt", "w") as f:
        f.write(result["text"])