import pygame as pg

class Ball():
    def __init__(self,screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.body_surf = pg.Surface((50, 50), pg.SRCALPHA)
        pg.draw.circle(self.body_surf, (255, 0, 0), (25, 25), 25)
        self.body_rect = self.body_surf.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False



    def output(self):
            self.screen.blit(self.body_surf, self.body_rect)
    
    def movement(self):
        if self.mright == True and self.body.right < self.screen_rect.right:
            self.body.centerx += 1
        elif self.mleft and self.body.left > 0:
            self.body.centerx -= 1
        if self.mup == True and self.body.top < self.screen_rect.top:
            self.body.centery += 1
        elif self.mdown == True and self.body.bottom > self.screen_rect.bottom:
            self.body.centery -= 1


