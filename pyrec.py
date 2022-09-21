'''
MIT License

Copyright (c) 2022 Juan Carlos Bindez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Author: https://github.com/JuanBindez
'''



import sounddevice as sd 
from scipy.io.wavfile import write 
import wavio as wv
import os
import random
import numpy as np


class Color():
    VERDE = '\033[92m'
    VERDE_CLARO = '\033[1;92m'
    VERMELHO = '\033[91m'
    AMARELO = '\033[93m'
    AZUL = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    NEGRITO = '\033[;1m'
    CYANO = '\033[1;36m'
    CYANO_CLARO = '\033[1;96m'
    CINZA_CLARO = '\033[1;37m'
    CINZA_ESCURO = '\033[1;90m'
    PRETO = '\033[1;30m'
    BRANCO = '\033[1;97m'
    INVERTE = '\033[;7m'
    RESET = '\033[0m'


def banner():
    print(Color.VERMELHO +

        '''
                                    
                     ____  _____ ____ 
         _ __  _   _|  _ \| ____/ ___|
        | '_ \| | | | |_) |  _|| |    
        | |_) | |_| |  _ <| |__| |___ 
        | .__/ \__, |_| \_\_____\____|
        |_|    |___/                   v1.2.0
                               
        Copyright (c) 2022 Juan Carlos Bindez

         *[Ctrl + C] Para Sair do Programa

        '''
    + Color.RESET)


banner()
freq = 44100
duration = int(input(Color.VERMELHO + "Digite quantos segundos de gravação você quer >>" + Color.RESET))
recording = sd.rec(int(duration * freq),  
                   samplerate=freq, channels=2)

name_file = str(random.random())

sd.wait()
write("pyrec1_" + name_file, freq, recording) 
wv.write("pyrec2_" + name_file, recording, freq, sampwidth=2)

os.system("clear")
print(Color.VERDE + "            GRAVAÇÃO CONCLUÍDA!" + Color.RESET)
print("Salvo com o nome: pyrec1_" + name_file + ".wav")
