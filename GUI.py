import tkinter as tk
from tkinter import ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    outpup_string.set(km_output)

# window
window = tk.Tk()
window.title("Yt convert")
window.geometry("400x250")

#Title
title_label = ttk.Label(master = window, 
                        text = "YouTube Transcribe", 
                        font = "Roboto 16")
title_label.pack(pady = 20) 

#Input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left", padx = 10)
input_frame.pack(pady = 20)

#Output 
outpup_string = tk.StringVar()
outpu_label = ttk.Label(master = window, 
                        text = "Output",
                        font = "Roboto 18",
                        textvariable = outpup_string)
outpu_label.pack(pady = 10)



window.mainloop()