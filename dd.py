import pygame
import random
class Player2:
    def __init__(self, x, y, w, h, img, speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), self.hitbox)
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))


    def move(self):
         self.hitbox.x += random.randint(-10, 10)
         self.hitbox.y += random.randint(-10, 10)