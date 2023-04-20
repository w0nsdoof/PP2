from os import scandir
from select import select
import pygame , random , time
from datetime import datetime

pygame.init()

# FONTS, text to display
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

# RESOLUTION, FPS
RES = WIDTH, HEIGHT = (400,400)
FPS = 5

# To draw a grid, snake
BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
BLOCK_SIZE = 20

# Colors
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

# Counters for lvl, score
score = 0
lvl = 0

def game_over(screen):
        gameover = font.render("Game over", True, WHITE)
        score_text = font_small.render("Score: " + str(score), True, WHITE)
        lvl_text = font_small.render("level: " + str(lvl), True, WHITE)

        screen.fill(BLACK)
        screen.blit(gameover, (30,10))
        screen.blit(lvl_text, (100,85))
        screen.blit(score_text, (100, 120))

        pygame.display.update()

        time.sleep(3)
        exit()

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Wall:
    def __init__(self, level):
        self.body = []
        f = open("levels/level{}.txt".format(level), "r")
        
        for y in range(0, HEIGHT//BLOCK_SIZE + 1):
            for x in range(0, WIDTH//BLOCK_SIZE + 1):
                if f.read(1) == '#':
                    self.body.append(Point(x, y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (226,135,67), rect)

class Food:
    def __init__(self):
        x = random.randint(0, WIDTH) // BLOCK_SIZE
        y = random.randint(0, HEIGHT) // BLOCK_SIZE
        self.location = Point(x, y)

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, (0, 255, 0), rect)

    def reset_position(self): #
        x = random.randint(0, WIDTH ) // BLOCK_SIZE 
        y = random.randint(0, HEIGHT) // BLOCK_SIZE 
        self.location = Point(x, y) 

    def check_wall(self, wall, snake):
        for point in wall.body:
            if (point.x == self.location.x) and (point.y == self.location.y) :
                self.reset_position()
        
        for point in snake.body:
            if (point.x == self.location.x) and (point.y == self.location.y) :
                self.reset_position()

    def debug_pos(self):
        print(self.location.x , self.location.y)

class Food2():
    def __init__(self):
        x = random.randint(0, WIDTH) // BLOCK_SIZE
        y = random.randint(0, HEIGHT) // BLOCK_SIZE
        self.location = Point(x, y)

    def reset_position(self): #
        x = random.randint(0, WIDTH ) // BLOCK_SIZE 
        y = random.randint(0, HEIGHT) // BLOCK_SIZE 
        self.location = Point(x, y) 

    def check_wall(self, wall, snake):
        for point in wall.body:
            if (point.x == self.location.x) and (point.y == self.location.y) :
                self.reset_position()
        
        for point in snake.body:
            if (point.x == self.location.x) and (point.y == self.location.y) :
                self.reset_position()
    
    def disappearing(self):
        for i in range(0, 5):
            rect = pygame.Rect(BLOCK_SIZE * self.location.x, BLOCK_SIZE * self.location.y, BLOCK_SIZE, BLOCK_SIZE)

            pygame.draw.rect(screen, (0, 255, 0), rect)
            pygame.draw.rect(screen, (0, 255, 0, 50), rect)

        self.reset_position()
        

class Snake:
    def __init__(self):
        self.body = [Point(11, 11)]
        self.dx = 0
        self.dy = 0
        self.level = 1

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 

        if self.body[0].x * BLOCK_SIZE > WIDTH:
            self.body[0].x = 0
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = WIDTH / BLOCK_SIZE
        
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT / BLOCK_SIZE

    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, (255, 0, 0), rect)


        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (0, 255, 0), rect)

    def check_collision(self, food, wall): # wall
        global score
        if (self.body[0].x == food.location.x) and (self.body[0].y == food.location.y):
                self.body.append(Point(food.location.x, food.location.y))
                food.reset_position()
                score += 1 
        for point in wall.body: 
            if (self.body[0].x == point.x) and (self.body[0].y == point.y):
                game_over(screen)

def main():
    global snake, screen, lvl, FPS, score

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    screen.fill(BLACK)

    snake = Snake()
    food = Food()
    wall = Wall(snake.level)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d: # RIGHT
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_a: # LEFT
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_w: # UP
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_s: # DOWN
                    snake.dx = 0
                    snake.dy = 1
        
        snake.move()
        snake.check_collision(food, wall)

        food.check_wall(wall, snake)
        # food.debug_pos()

        if len(snake.body) and len(snake.body) % 2 == 1:
            lvl += 1
            wall = Wall(lvl % 4)

            snake = Snake()

            FPS += 1

        screen.fill(BLACK)
        drawGrid()

        Score = font_small.render("Score:" + str(score), True, (255,255,255))
        Lvl = font_small.render("Lvl: " + str(lvl), True, (255,255,255))
        
        snake.draw()
        food.draw()
        wall.draw()
        
        screen.blit(Score, (10,10))
        screen.blit(Lvl, (10, 30))

        pygame.display.update()
        CLOCK.tick(FPS)


def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, LINE_COLOR, rect, 1)


main()