import pygame



class Wall:

    def __init__(self,x ,y ,w ,h):
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self,window):
        pygame.draw.rect(window, (255,255,0), self.rect)

