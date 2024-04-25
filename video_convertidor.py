import subprocess

def video_convertidor(input_file, outpu_file):
    ffmpeg_cmd = ["ffmpeg", "-i", input_file, outpu_file]

    try:
        subprocess.run(ffmpeg_cmd, check = True)
        print("Convertido con éxito")
    except subprocess.CalledProcessError as e:
        print("La conversión falló")


