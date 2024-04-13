import pygame
import random
import time
class Player2:
    def __init__(self, x, y, w, h, img, speed_x=0,speed_y=00):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.lastchange = time.time()
    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), self.hitbox)
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))


    def move(self):
         if time.time()-self.lastchange> 1:
             self.speed_x=random.randint(-5,5)
             self.speed_y=random.randint(-5,5)
             self.lastchange = time.time()
         self.hitbox.x += self.speed_x
         self.hitbox.y += self.speed_y

         if self.hitbox.x>700:
             self.speed_x*=-1
         if self.hitbox.y>500:
             self.speed_y*=-1

         if self.hitbox.y < 0:
            self.speed_y *= -1

         if self.hitbox.x < 0:
            self.speed_x *= -1