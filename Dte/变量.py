import pygame
import random
import math

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Dig through the earth')
running = True
background = [20, 20, 20]
clock = pygame.time.Clock()
key = pygame.key.get_pressed()
x, y = pygame.mouse.get_pos()
mouse = 0
icon = 0
move = 0

# 未来添加
maps = []

font = pygame.font.SysFont('time', 40)
title = font.render('', True, (255, 255, 255))
start = pygame.USEREVENT + 1
pygame.time.set_timer(start, 3000)
