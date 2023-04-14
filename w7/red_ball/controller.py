import pygame as pg
from redball import Ball

def events(screen, Ball):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                Ball.mright = True
            elif event.key == pg.K_LEFT:
                Ball.mleft = True
            if event.key == pg.K_UP:
                Ball.mup = True
            elif event.key == pg.K_DOWN:
                Ball.mdown = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                Ball.mright = False
            elif event.key == pg.K_LEFT:
                Ball.mleft = False
            if event.key == pg.K_UP:
                Ball.mup = False
            elif event.key == pg.K_DOWN:
                Ball.mdown = False
        
