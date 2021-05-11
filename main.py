import pygame
from flap import Bird
pygame.init()

win_size = 700
win = pygame.display.set_mode((500,500))
bc = (255,255,255)
menu_color = (40,40,40)

font0 = pygame.font.SysFont("arial", 64)
red = (255,0,0)

def draw_text(text, font, color, frame, x, y):
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    frame.blit(textobj, textrect)

def menu(win):
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        win.fill(menu_color)
        draw_text("Menu", font0, red,)
        pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu(win)

    win.fill(bc)

    #pygame.score()
    #pygame.name("YOU")  нужно подумать как сделать подсчет инфы score и games после того как сделаю регенерацию труб
    #pygame.games()

    pygame.display.update()

    pygame.time.delay(10)

