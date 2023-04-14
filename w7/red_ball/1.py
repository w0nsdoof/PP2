import pygame as pg
from pygame.color import THECOLORS

pg.init()

RES = WIDTH,HEIGHT = (500, 500)

screen = pg.display.set_mode(RES)
pg.display.set_caption("redball")

clock = pg.time.Clock()

x = WIDTH // 2
y = HEIGHT // 2
r = 25


while True:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    if pg.key.get_pressed()[pg.K_UP] and y - r > 5: # Oy
        y -= 20
    if pg.key.get_pressed()[pg.K_DOWN] and y + r + 15 < HEIGHT:  
        y += 20
    if pg.key.get_pressed()[pg.K_LEFT] and x - r > 5: # Ox
        x -= 20
    if pg.key.get_pressed()[pg.K_RIGHT] and x + r + 15 < WIDTH: 
        x += 20

    screen.fill((255,255,255))
    pg.draw.circle(screen, (255, 0, 0), (x, y), r)

    pg.display.flip()
