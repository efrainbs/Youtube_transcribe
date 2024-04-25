from video_convertidor import video_convertidor
from pytube import YouTube
from wpr import tran


file_name = input("ponle un nombre al archivo: ")
link = input("Pega tu link de youtube aquí, URL: ")
nivel_modelo_whisper = "small" # las opciones son: "tiny", "base", "small", "medium", "large"


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

# Convierte el video a audio
video_convertidor(f"{file_name}.mp4", f"{file_name}.mp3")

# Convierte el audio a texto
tran(f"{file_name}.mp3", nivel_modelo_whisper)
        
       
       

