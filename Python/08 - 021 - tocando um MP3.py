# Aula 08 (Usando Módulos do Python)

import pygame

pygame.init()
pygame.mixer_music.load('mario.mp3')
pygame.mixer_music.play()
pygame.event.wait()
