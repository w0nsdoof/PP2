import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((829,836))

clock = pygame.time.Clock()

clock_image = pygame.image.load('images/main_clock.png').convert_alpha() # (829, 836) bg
m_arrow = pygame.image.load('images/right_hand.png').convert_alpha() # (410,180) minutes
s_arrow = pygame.image.load('images/left_hand.png').convert_alpha() # (546,140) seconds

def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)


while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(clock_image, (0, 0))

    time = datetime.now()
    angle_s = -6 * time.second
    angle_m = -6 * time.minute

    blitRotateCenter(screen,m_arrow, (210, 330), angle_m)
    blitRotateCenter(screen,s_arrow, (140, 350), angle_s)


    pygame.display.flip()
    
    


