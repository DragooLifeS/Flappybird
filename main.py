import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
bc = (255,255,255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill(bc)

    pygame.display.update()

    pygame.time.delay(10)