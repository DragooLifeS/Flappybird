import pygame
import random

class Bird:
    
   # def tube(self):
   # нужно сделать 2 трубы сверху и снизу и по логике через рандом указывать высоту промежутка где будет птичка лететь
   # и указать расстояние между ними через x - "число"


    def menu(self, score, name, games):
        self.score = score
        self.name = name
        self.game = game


    def key(self, x, y):
        
        keys = pygame.key.get_pressed()

        if keys(pygame.K_ESC): #потом тут будет еще "and "died" died = будет команда когда птичка умирает или чтото такое
            open(menu1)
        
        elif keys(pygame.K_ENTER):
            open(main)
        
        #elif keys(pygame.K_SPACE):
        #ТУТ БУДЕТ ФИЗИКА СРАНАЯ
