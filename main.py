import pygame
import random
from hjh import Player
from dd import Player2


window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()
background = pygame.transform.scale(
    pygame.image.load("1626173608_49-kartinkin-com-p-krasivii-fon-priroda-krasivo-60.jpg"), (700, 500)
)
roma = Player(100, 100,
              50, 50, "cuphead-art-run.png", 10)
roma2 = Player2(200, 250, 50, 50, "cuphead-lego-boss-how-to-minecraft-cuphead-flower-thumbnail.jpg", 2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    window.blit(background, (0, 0))
    roma.move()
    roma.draw(window)
    roma2.move()
    roma2.draw(window)

    pygame.display.flip()
    fps.tick(60)