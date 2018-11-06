import pygame
import GUI

import ground
import player


pygame.init()
GUI.name("Insert Name Here")

clock = pygame.time.Clock()
FPS = 10


def gameLoop():
    gameExit = False
    gameOver = False

    back = ground.back(1)

    while not gameExit:
        GUI.gameDisplay.fill((0, 0, 0))    
        back.draw(GUI.gameDisplay)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        pygame.display.update()
        clock.tick(FPS)


gameLoop()
pygame.quit()
quit()
