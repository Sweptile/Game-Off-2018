import pygame

pygame.init()

display_width = 1000
display_height = 700
s_x = 0
s_y = 0
screen_width = 1000
screen_height = 700

gameDisplay = pygame.display.set_mode((display_width,display_height))

def name(name):
    pygame.display.set_caption(name)
