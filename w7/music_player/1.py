import pygame

pygame.init()
screen = pygame.display.set_mode((500,200))

user_volume = 0.2

playlist = ['music/Rayquaza - Ex Exodia.mp3', 'music/ENCASSATOR - NEVER MET.mp3', 'music/SWERVE - CITY LIGHT.mp3', 'music/Japanese Stutter - Suave Lee .mp3']

font = pygame.font.SysFont('arial', 20)

next = 0
previous = 0
on = True
off = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on == True:
                pygame.mixer.music.pause()
                on = False
            elif event.key == pygame.K_SPACE and off == False:
                pygame.mixer.music.unpause()
                on = True
            if event.key == pygame.K_RIGHT:
                next += 1
                if next == len(playlist):
                    next = 0
                pygame.mixer.music.load(playlist[next])
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                previous -= 1
                if previous == -1:
                    previous == len(playlist)
                pygame.mixer.music.load(playlist[previous])
                pygame.mixer.music.play()
            if event.key == pygame.K_UP:
                if user_volume <= 1:
                    user_volume += 0.05
                    pygame.mixer.music.set_volume(user_volume)
            if event.key == pygame.K_DOWN:
                if user_volume >= 0:
                    user_volume -= 0.05
                    pygame.mixer.music.set_volume(user_volume)


    screen.fill((255,255,255))

    text = font.render(playlist[next][6:-4], True, (0,0,0))
    screen.blit(text, (50, 70))
    
    pygame.display.flip()