import pygame
from hjh import Player
from dd import Player2


window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()
background = pygame.transform.scale(
    pygame.image.load("lebronsunshinecover.jpg"), (700, 500)
)
roma = Player(100, 100, 50, 50, "lebronsunshinecover.jpg", 10)
roma2 = Player2(100, 100, 50, 50, "you-are-my-sunshine-dark-lebron-james.webp", 10)
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