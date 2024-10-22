import pygame
import sys

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Game")

class Player:
    def __init__(self, x , y):
        self.speed = 5
        self.width = 2
        self.height = 3
        self.rect = pygame.Rect(x, y, 50, 50)
        self.color = white

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width
        
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - self.rect.height
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Fruit:
    def __init__(self, x, y)
    

player = Player(WIDTH // 2, HEIGHT // 2)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player.move(5, 0)
    if keys[pygame.K_LEFT]:
        player.move(-5, 0)
    if keys[pygame.K_UP]:
        player.move(0, -5)
    if keys[pygame.K_DOWN]:
        player.move(0, 5)
    
    screen.fill(black)
    player.draw(screen)
    pygame.display.flip()

    clock.tick(60)