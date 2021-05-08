import pygame
from flap import Bird
pygame.init()

win = pygame.display.set_mode((500,500))
bc = (255,255,255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(bc)

    #pygame.score()
    #pygame.name("YOU")  нужно подумать как сделать подсчет инфы score и games после того как сделаю регенерацию труб
    #pygame.games()

    pygame.display.update()

    pygame.time.delay(10)