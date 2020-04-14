import pyaudio
import speech_recognition as spr
from playsound import playsound
import pygame
import emoji
import playsound

a = ''
escolheu = True
print('=' * 30)
while escolheu == True:
        escolha = input('Escolha uma musica de 1 a 4: ')
        if (escolha == '1'):
            a = 'starwars.mp3'
            escolheu = False
            print('Star Wars Theme')
        elif (escolha == '2'):
            escolheu = False
            a = 'terminator1.mp3'
            print('Exterminator do Futuro')
        elif (escolha == '3'):
            escolheu = False
            a = 'terminator2.mp3'
            print('Exterminator do Futuro 2')
        elif (escolha == '4'):
            escolheu = False
            a = 'pantera.mp3'
            print('Pantera - Revolution is my Name')
        else:
            print('Você digitou algo errado, lembre-se que tem que ser um numero de 1 a 4')
            escolheu = True

pygame.mixer.init()
pygame.mixer.music.load(a)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    print('=' * 30)
    pause = int(input(emoji.emojize('[ 1 ] :gemini: pausar \n[ 2 ] :arrow_forward: Play \n[ 3 ] :white_large_square: Parar: \n', use_aliases=True)))
    print('=' * 30)
    if pause == 1:
        pygame.mixer.music.pause()
    elif pause == 2:
        pygame.mixer.music.unpause()
    elif pause == 3:
        pygame.mixer_music.stop()