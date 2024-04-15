import pygame
import random
from hjh import Player
from dd import Player2
from finishh import Finish3
import wall
import finishh
window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()
background = pygame.transform.scale(
    pygame.image.load("1626173608_49-kartinkin-com-p-krasivii-fon-priroda-krasivo-60.jpg"), (700, 500)
)
roma = Player(20, 420,
              50, 50, "cuphead-art-run.png", 5)
roma2 = Player2(630, 280, 50, 50, "cuphead-lego-boss-how-to-minecraft-cuphead-flower-thumbnail.jpg", 2)


walls = []
walls.append(wall.Wall(100, 188, 20, 300))
walls.append(wall.Wall(200, 80, 300, 20))
walls.append(wall.Wall(100, 0, 20, 100))
walls.append(wall.Wall(610, 100, 20, 170))
walls.append(wall.Wall(580, 80, 50, 20))
walls.append(wall.Wall(480, 80, 20, 100))
walls.append(wall.Wall(200, 250, 410, 20))
walls.append(wall.Wall(290, 160, 200, 20))
walls.append(wall.Wall(200, 80, 20, 270))
walls.append(wall.Wall(200, 350, 500, 20))
walls.append(wall.Wall(100, 460, 690, 20))


finishs = []
finishs.append(finishh.Finish3(100, 188, 20, 300,"Финиш.png"))





game = True


while game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    for wall in walls:
        if wall.rect.colliderect(roma.hitbox):
            game = False
    for finishh in finishs:
        if finishs.rect.colliderect(finiku.hitbox):
            pygame.draw.rect(window, (0, 255, 0), self.rect)
    window.blit(background, (0, 0))
    roma.move()
    roma.draw(window)
    finiku.draw(window)
    roma2.move()
    roma2.draw(window)
    for wall in walls:
        wall.draw(window)
    pygame.display.flip()
    fps.tick(60)