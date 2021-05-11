import pygame
from flap import Bird
pygame.init()

win_size = 700
win = pygame.display.set_mode((500,500))
bc = (255,255,255)

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        self.image = pygame.image.load("")
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 350
    def update(self):
        

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu(win)

    win.fill(bc)

    pygame.display.update()

    pygame.time.delay(10)
