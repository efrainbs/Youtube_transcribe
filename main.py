from pytube import YouTube
from wpr import tran
import subprocess
import whisper


file_name = input("ponle un nombre al archivo: ") # Elegir el nombre que tendrá el archivo de salida
link = input("Pega tu link de youtube aquí, URL: ") # Solicita link del video de youtube
nivel_modelo_whisper = "small" # las opciones son: "tiny", "base", "small", "medium", "large"

# Función que descarga el video de Youtube en .mp4
def Download(link):
  yt = YouTube(link)
  yt = yt.streams.get_lowest_resolution()
  try:
    yt.download(filename=f"{file_name}.mp4")
  except:
    print("Hubo un error al descargar el video del URL proporcionado...")
  print("¡Descarga completada con éxito!")
  
# Descarga el video
Download(link)

# Función que convierte el video mp4 en audio mp3
def video_convertidor(input_file, outpu_file):
    ffmpeg_cmd = ["ffmpeg", "-i", input_file, outpu_file]

    try:
        subprocess.run(ffmpeg_cmd, check = True)
        print("Convertido con éxito")
    except subprocess.CalledProcessError as e:
        print("La conversión falló")

# Convierte el video a audio
video_convertidor(f"{file_name}.mp4", f"{file_name}.mp3")

# Función que transcribe a partir del archivo de audio mp3
def tran(audio_file, nivel):
    model = whisper.load_model(nivel)
    result = model.transcribe(audio_file, language = "es", fp16 = False)

    name_text = audio_file.replace(".mp3", "")
    
    with open(f"{name_text}.txt", "w") as f:
        f.write(result["text"])

# Convierte el audio a texto
tran(f"{file_name}.mp3", nivel_modelo_whisper)

