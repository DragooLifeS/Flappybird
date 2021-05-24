import pygame
import random


class FlappyBird:
    # Переменные
    def __init__(self):

        self.screen = pygame.display.set_mode((400, 708))
        pygame.display.set_caption('Flappy Bird')
        self.bird = pygame.Rect(65, 50, 50, 50)
        self.background = pygame.image.load("images/background.png").convert()

        # Массив спрайтов
        self.birdSprites = [pygame.image.load("images/1.png").convert_alpha(),
                            pygame.image.load("images/2.png").convert_alpha(),
                            pygame.image.load("images/dead.png")]
        self.wallUp = pygame.image.load("images/bottom.png").convert_alpha()
        self.wallDown = pygame.image.load("images/top.png").convert_alpha()
        self.gap = 130
        self.wallx = 400
        self.birdY = 350

        # Параметры прыжка птицы
        self.jump = 0
        self.jumpSpeed = 10
        self.gravity = 5

        # Смерть
        self.dead = False
        self.sprite = 0
        self.counter = 0
        self.offset = random.randint(-110, 110)

    # Обновление стен
    def updateWalls(self):
        self.wallx -= 2
        if self.wallx < -80:
            self.wallx = 400
            self.counter += 1
            self.offset = random.randint(-110, 110)

    # Обновление птички
    def birdUpdate(self):

        if self.jump > 0:
            # Уменьшение скорости прыжка после прыжка
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            # Гравитация
            self.birdY += self.gravity
            self.gravity += 0.2
        self.bird[1] = self.birdY

        # Координаты стен
        upRect = pygame.Rect(self.wallx,
                             360 + self.gap - self.offset + 10,
                             self.wallUp.get_width() - 10,
                             self.wallUp.get_height())

        downRect = pygame.Rect(self.wallx,
                               0 - self.gap - self.offset - 10,
                               self.wallDown.get_width() - 10,
                               self.wallDown.get_height())

        # Столкновения
        if upRect.colliderect(self.bird):
            self.dead = True

        if downRect.colliderect(self.bird):
            self.dead = True

        # Сброс на начальные значение
        if not 0 < self.bird[1] < 720:
            self.bird[1] = 50
            self.birdY = 50
            self.dead = False
            self.counter = 0
            self.wallx = 400
            self.offset = random.randint(-110, 110)
            self.gravity = 5

    def run(self):

        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 50)
        
        # Основной цикл
        while True:
            # Скорость (FPS)
            clock.tick(40)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if (event.type == pygame.MOUSEBUTTONDOWN) and self.dead != True:
                    self.jump = 17
                    self.gravity = 5
                    self.jumpSpeed = 10

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background, (0, 0))

            # Стенка вверх
            self.screen.blit(self.wallUp,
                             (self.wallx, 360 + self.gap - self.offset))

            # Стенка вниз                 
            self.screen.blit(self.wallDown,
                             (self.wallx, 0 - self.gap - self.offset))

            # Счетчик                 
            self.screen.blit(font.render(str(self.counter),
                                         -1,
                                         (255, 255, 255)),
                             (200, 50))
                             
            if self.dead == True:
                self.sprite = 2
            elif self.jump:
                self.sprite = 1

            # Отрисовка птички
            self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))

            if self.dead == False:
                self.sprite = 0

            self.updateWalls()
            self.birdUpdate()
            
            pygame.display.update()

# Старт
FlappyBird().run()
