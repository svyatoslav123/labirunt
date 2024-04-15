import pygame

class Finish3:
    def __init__(self, x, y, w, h, img):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.rect = pygame.Rect(x, y, w, h,img)

        def draw(self, window):
            pygame.draw.rect(window, (255, 255, 0), self.rect)