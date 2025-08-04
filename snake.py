import pygame
import random
import sys

# Grid and screen settings
CELL_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

# Colors
BLACK = (0, 0, 0)
GREY = (40, 40, 40)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()



def draw_grid():
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GREY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GREY, (0, y), (SCREEN_WIDTH, y))


# Snake starting position (3 segments long)
snake = [(5,5), (4,5), (3,5), (2,5), (1,5)]
direction = (1,0)

def draw_snake():
    for segment in snake:
        rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, rect)


def draw_food(position):
    x, y = position
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, rect)

# Generate initial food position
food_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
while food_pos in snake:
    food_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Moving
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)


    # Move the snake
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # Check for wall collisions
    if (
        new_head in snake or
        new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
        new_head[1] < 0 or new_head[1] >= GRID_HEIGHT
    ):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    # Check if snake eats food
    if new_head == food_pos:
        # Don’t remove tail to grow
        food_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        while food_pos in snake:
            food_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    # Drawing
    screen.fill(BLACK)
    draw_grid()
    draw_snake()
    draw_food(food_pos)
    pygame.display.flip()
    clock.tick(5)  # FPS