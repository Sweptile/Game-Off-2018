import pygame

class back:
    def __init__(self, lvl):
        self.lvl = "lvl"+str(lvl)+".txt"
        self.file = open(self.lvl, "r")
        self.data = self.file.read()
        self.pxl = 32

    def draw(self, disp):
##        print(1)
        tile = 0

        x = 0
        y = 0
        
        
        for i in self.data:
            if(i=='\n'):
                y+=self.pxl
                x=0
                continue
            tile = pygame.image.load("Tiles/t"+str(int(i)+1)+".png")

            disp.blit(tile, (x, y))
            x+=32
