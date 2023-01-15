from pytube import YouTube
import time
from colorama import Fore, Back, Style
from pathlib import Path
import pyautogui as pt
import pyperclip as pc
import os
from colorama import just_fix_windows_console
import time
# use Colorama to make Termcolor work on Windows too
just_fix_windows_console()


def download(link):
    tempo_inicial = time.time()
    print(Fore.GREEN + "Qual o formato desejado? ")
    print("[1] - Vídeo")
    print('[2] - Música')
    formato = int(input("-> "))

    if formato == 1:
        youtubeobject = YouTube(link)
        youtubeobject = youtubeobject.streams.get_highest_resolution()
        existe = os.path.exists(r'C:\YouTube\Youtube\Videos')
        local_arquivo = r'C:\YouTube\Youtube\Videos'
        if existe == True:
            print(Fore.GREEN + "Fazendo download do arquivo...")
            youtubeobject.download(local_arquivo)
        else:
            print(Fore.GREEN + "Fazendo download do arquivo...")
            os.makedirs(r'C:\YouTube\Youtube\Videos')
            youtubeobject.download(local_arquivo)
    else:
        youtubeobject = YouTube(link)
        youtubeobject = youtubeobject.streams.get_audio_only()
        existe = os.path.exists(r'C:\YouTube\Youtube\Músicas')
        local_arquivo = r'C:\YouTube\Youtube\Músicas'
        if existe == True:
            print(Fore.GREEN + "Fazendo download do arquivo...")
            youtubeobject.download(local_arquivo)
        else:
            print(Fore.GREEN + "Fazendo download do arquivo...")
            os.makedirs(r'C:\YouTube\Youtube\Músicas')
            youtubeobject.download(local_arquivo)

    tempo_final = time.time()
    print(Fore.GREEN + f"O Download foi concluido em", Fore.RED + f'{tempo_final - tempo_inicial:.2f}', Fore.GREEN +
              f'segundos! \nO arquivo foi salvo na pasta {local_arquivo}')
    abrir_local_arquivo = input(Fore.YELLOW + Style.BRIGHT + "Deseja abrir o local do aquivo? [s] [n]\n-> ")
    if abrir_local_arquivo == 's':
        pt.press('Win')
        pc.copy(local_arquivo)
        pt.hotkey('ctrl', 'v')
        pt.press('Enter')
    else:
        print(Fore.BLUE + "Ok, depois você olha!")
        time.sleep(2)


link = input(Fore.LIGHTGREEN_EX + "Digite o link do vídeo aqui. \nURL: ")
download(link)
