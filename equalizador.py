import tkinter as tk
from tkinter import ttk
import sounddevice as sd
import librosa
import numpy as np

# Carrega o áudio
audio_path = "testetrabalho.mp3"
y1, sr = librosa.load(audio_path)

# Duração e taxa de amostragem
duracao = 61
fs = 22050

def filter_baixa(x):
    y=[0]*duracao*fs
    y2=[0]*duracao*fs
    for n in range(2,len(x)):
        y[n] = (x[n] + 2 * x[n-1] + x[n-2])*0.00176806124945325 + 1.92964726488150 * y[n-1] - 0.936719509879316 * y[n-2]
    for n in range(2,len(x)):
        y2[n] = (y[n] + 2 * y[n-1] + y[n-2])*0.00169233588037988 + 1.84700123021514 * y2[n-1] - 0.853770573736664 * y2[n-2]
    return y2

def filter_media(x):
    y=[0]*duracao*fs
    y2=[0]*duracao*fs
    for n in range(2,len(x)):
        y[n] = (x[n] - x[n-2])*0.208029472445516 + 1.88862611556793 * y[n-1] - 0.897224858020599 * y[n-2]
    for n in range(2,len(x)):
        y2[n] = (y[n] - y[n-2])*0.208029472445516 + 1.36038598510966 * y2[n-1] - 0.562352934020352 * y2[n-2]
    return y2

def filter_alta(x):
    y=[0]*duracao*fs
    y2=[0]*duracao*fs
    for n in range(2,len(x)):
        y[n] = (x[n] - 2 * x[n-1] + x[n-2])*0.76336013240773948 + 1.3957215810419235* y[n-1] - 0.65771894858903468* y[n-2]
    for n in range(2,len(x)):
        y2[n] = (y[n] - 2 * y[n-1] + y[n-2])*0.61460720901400101 + 1.1237429216785333 * y2[n-1] - 0.33468591437747047* y2[n-2]
    return y2

def apply_equalizer():
    k1 = int(scale1.get())
    k2 = int(scale2.get())
    k3 = int(scale3.get())
    k4 = int(scale4.get())

    sonido01 = [element * k1/100 for element in filter_baixa(y1)]
    sonido02 = [element * k2/100 for element in filter_media(y1)]
    sonido03 = [element * k3/100 for element in filter_alta(y1)]
    som = [0] * len(y1)
    for n in range(len(y1)):
        som[n] = sonido01[n] + sonido02[n] + sonido03[n]
    sonido04= [element * k4/100 for element in som]
    sd.play(sonido04, sr)

# Cria a janela principal
window = tk.Tk()
window.title("Equalizador de 3 Bandas")

# Cria os controles deslizantes
scale_label1 = tk.Label(window, text="Grave")
scale_label1.pack()
scale1 = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)
scale1.set(50)  # Valor inicial
scale1.pack()

scale_label2 = tk.Label(window, text="Médio")
scale_label2.pack()
scale2 = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)
scale2.set(50)  # Valor inicial
scale2.pack()

scale_label3 = tk.Label(window, text="Agudo")
scale_label3.pack()
scale3 = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)
scale3.set(50)  # Valor inicial
scale3.pack()

scale_label4 = tk.Label(window, text="Volume")
scale_label4.pack()
scale4 = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL)
scale4.set(50)  # Valor inicial
scale4.pack()

# Botão para aplicar as configurações do equalizador
apply_button = ttk.Button(window, text="Aplicar", command=apply_equalizer)
apply_button.pack()

# Inicia o loop principal da janela
window.mainloop()
