import pygame, random, time
from pygame.locals import *

RES = WEIGHT, HEIGHT = (400, 600) # resolution

pygame.init()

score = 0

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 60)
text = font.render("Game Over", True, (255,255,255))
final = font.render("Final Score:", True, (255,255,255))

background = pygame.image.load("AnimatedStreet.png") # (400,600)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(0,400),random.randint(0, 5)) # rand(x, y) 
 
    def movement(self):
        global score
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 610): # Чуть больше чтобы выезжать за экран
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            score += 1
 
    def output(self, screen):
        screen.blit(self.image, self.rect) 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def movement(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < 400:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def output(self, screen):
        screen.blit(self.image, self.rect)

p1 = Player()
e1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(e1, p1)

# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)

pygame.mixer.music.load("SWERVE - CITY LIGHT.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

while True:
    clock.tick(60) # FPS


    scores = font.render(str(score), True, (0,0,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    screen.blit(background, (0,0))
    screen.blit(scores, (10,10))

    e1.movement()
    e1.output(screen)

    p1.movement()
    p1.output(screen)

    if pygame.sprite.spritecollideany(p1, enemies):
        screen.fill((0,0,0))
        screen.blit(text, (30, 200)) 
        screen.blit(final, (30, 280))
        screen.blit(scores, (150, 350))

        pygame.display.flip()

        pygame.mixer.Sound("crash.wav").play()

        for entity in all_sprites:
            entity.kill()
        
        time.sleep(2)
        exit()
        


    pygame.display.flip()