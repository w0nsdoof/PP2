import pygame, random, time
from pygame.locals import *

RES = WIDTH, HEIGHT = (400, 600) # resolution

pygame.init()

score = 0 
speed = 10 # speed of enemy
coins_total = 1 # cnt of coins

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
        self.rect.center=(random.randint(0,400),random.randint(0, 5)) # rand(x, y = (0,5)) 
 
    def movement(self):
        global score, speed
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > 610): # Чуть больше чтобы выезжать за экран
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            score += 1 # Когда enemy выезжает за экран
 
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

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < 400 and pressed_keys[K_RIGHT]:        
            self.rect.move_ip(5, 0)
        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom < HEIGHT and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
 
    def output(self, screen):
        screen.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(0,WIDTH),random.randint(100, HEIGHT)) # rand(x, y)
    
    def output(self,screen):
        screen.blit(self.image, self.rect)

    def reset(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)

class Rubin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rubin.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(0,WIDTH),random.randint(50, HEIGHT)) # rand(x, y)

    def output(self,screen):
        screen.blit(self.image, self.rect)

    def reset(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)

p1 = Player()
e1 = Enemy()

c1 = Coin()

r1 = Rubin()

rubins = pygame.sprite.Group()
rubins.add(r1)
coins = pygame.sprite.Group()
coins.add(c1)
enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(e1, p1, c1)

INC_SPEED = pygame.USEREVENT + 1 
pygame.time.set_timer(INC_SPEED, 5000) # per 1 sec => speed++

pygame.mixer.music.load("SWERVE - CITY LIGHT.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

while True:
    clock.tick(60) # FPS

    scores = font.render(str(score), True, (0,0,255)) # blue color, passed enemy on screen
    t_coins = font.render(str(coins_total - 1), True, (255, 215, 0)) # gold color, coins total on screen
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == INC_SPEED:
            speed += 1
    
    screen.blit(background, (0,0))
    screen.blit(scores, (10,10))
    screen.blit(t_coins, (350, 10))

    e1.movement()
    e1.output(screen)

    p1.movement()
    p1.output(screen)

    c1.output(screen)
    r1.output(screen)

    if pygame.sprite.spritecollideany(p1, enemies):
        screen.fill((0,0,0))
        screen.blit(text, (30, 200)) 
        screen.blit(final, (30, 280))
        screen.blit(scores, (100, 350))
        screen.blit(t_coins, (220, 350))

        pygame.display.flip()

        pygame.mixer.Sound("crash.wav").play()

        for entity in all_sprites:
            entity.kill()
        
        time.sleep(2)
        exit()
        
    if pygame.sprite.spritecollideany(p1, coins):
        coins_total += 1
        
        for coin in coins:
            coin.reset()
    
    if pygame.sprite.spritecollideany(p1, rubins):
        coins_total += random.randint(0, 3)

        for rubin in rubins:
            rubin.reset()

    if coins_total % 7 == 0:
        speed += 1
        

    pygame.display.flip()