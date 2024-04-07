# Faça um programa que leia um arquivo MP3

import pygame
pygame.init()
pygame.mixer.music.load('MC POZE NOS ANOS 80.mp3')
pygame.mixer.music.play()
pygame.event.wait()