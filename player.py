import pygame

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 1
        self.sprite = pygame.image.load("Sprites/pl.plg")

    def draw(self, display):
        pass
