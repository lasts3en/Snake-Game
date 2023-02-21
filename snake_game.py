import pygame
import random

# Initialize Pygame
pygame.init()

# Define game constants
WIDTH = 600
HEIGHT = 600
FPS = 10

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the game display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


# Define the Snake class
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 10
        self.dy = 0
        self.body = [(x, y), (x - 10, y), (x - 20, y)]

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.body.insert(0, (self.x, self.y))
        self.body.pop()

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], 10, 10))


# Define the Food class
class Food:
    def __init__(self):
        self.x = random.randrange(0, WIDTH - 10, 10)
        self.y = random.randrange(0, HEIGHT - 10, 10)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, 10, 10))


# Set up the game objects
snake = Snake(WIDTH / 2, HEIGHT / 2)
food = Food()

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.dx != 10:
                snake.dx = -10
                snake.dy = 0
            elif event.key == pygame.K_RIGHT and snake.dx != -10:
                snake.dx = 10
                snake.dy = 0
            elif event.key == pygame.K_UP and snake.dy != 10:
                snake.dx = 0
                snake.dy = -10
            elif event.key == pygame.K_DOWN and snake.dy != -10:
                snake.dx = 0
                snake.dy = 10

    # Move the snake
    snake.move()

    # Check for collisions with the food
    if snake.body[0][0] == food.x and snake.body[0][1] == food.y:
        food = Food()
        snake.body.append(snake.body[-1])

    # Check for collisions with the walls
    if snake.body[0][0] < 0 or snake.body[0][0] >= WIDTH or snake.body[0][1] < 0 or snake.body[0][1] >= HEIGHT:
        running = False

    # Check for collisions with the snake's body
    for segment in snake.body[1:]:
        if snake.body[0][0] == segment[0] and snake.body[0][1] == segment[1]:
            running = False

    # Draw the game objects
    screen.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.update()

    # Set the game clock
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
