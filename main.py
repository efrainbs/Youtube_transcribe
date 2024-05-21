from video_convertidor import video_convertidor
from pytube import YouTube
from wpr import tran


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

# Convierte el video a audio
video_convertidor(f"{file_name}.mp4", f"{file_name}.mp3")

# Convierte el audio a texto
tran(f"{file_name}.mp3", nivel_modelo_whisper)
        
       
       

