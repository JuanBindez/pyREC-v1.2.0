import sounddevice as sd 
from scipy.io.wavfile import write 
import wavio as wv
import os

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
        |_|    |___/                   v1.0.0
                               
           
        
        
        '''
    + Color.RESET)

def aguardo():
    x = 0

    while x < duration:
        banner()
        print("--")
        os.system("clear")
        banner()
        print("|")
        os.system("clear")
        banner()
        print("/")
        os.system("clear")
        x = x + 1


banner()
freq = 44100
duration = int(input(Color.VERMELHO + "Digite quantos segundos de gravação você quer >>" + Color.RESET))
recording = sd.rec(int(duration * freq),  
                   samplerate=freq, channels=2)
                 
sd.wait()
aguardo()
write("recording0.wav", freq, recording) 
wv.write("recording1.wav", recording, freq, sampwidth=2)
