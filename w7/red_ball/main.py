import pygame as pg
from redball import Ball
from controller import events

pg.init()

screen = pg.display.set_mode((640,480))
ball = Ball(screen)

while True:
    events(screen, ball)

    screen.fill((255,255,255))

    ball.output()

    pg.display.flip()
    