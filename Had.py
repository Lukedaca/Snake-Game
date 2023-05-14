import pygame
import sys
import random

pygame.init()

# Nastavení okna
WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game")

# Barvy
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Nastavení hada a jídla
snake_size = 20
snake_speed = 10
snake_pos = [[100, 100], [100 - snake_size, 100], [100 - 2 * snake_size, 100]]
food_pos = [random.randrange(1, (WIDTH - snake_size) // snake_size) * snake_size, random.randrange(1, (HEIGHT - snake_size) // snake_size) * snake_size]
food_spawn = True

# Směr hada
direction = "RIGHT"

# Hodiny pro omezení FPS
clock = pygame.time.Clock()

# Pauza
paused = False
def draw_snake(snake_pos):
    for pos in snake_pos:
        pygame.draw.rect(WIN, GREEN, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

def draw_food(food_pos):
    pygame.draw.rect(WIN, RED, pygame.Rect(food_pos[0], food_pos[1], snake_size, snake_size))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != "DOWN" and not paused:
                direction = "UP"
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != "UP" and not paused:
                direction = "DOWN"
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != "RIGHT" and not paused:
                direction = "LEFT"
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != "LEFT" and not paused:
                direction = "RIGHT"
            if event.key == pygame.K_ESCAPE:
                paused = not paused
    if not paused:
        if direction == "UP":
            snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] - snake_speed])
        if direction == "DOWN":
            snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] + snake_speed])
        if direction == "LEFT":
            snake_pos.insert(0, [snake_pos[0][0] - snake_speed, snake_pos[0][1]])
        if direction == "RIGHT":
            snake_pos.insert(0, [snake_pos[0][0] + snake_speed, snake_pos[0][1]])

# Kontrola kolize s jídlem
        if abs(snake_pos[0][0] - food_pos[0]) < snake_size and abs(snake_pos[0][1] - food_pos[1]) < snake_size:
            food_spawn = False
        else:
            snake_pos.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (WIDTH - snake_size) // snake_size) * snake_size, random.randrange(1, (HEIGHT - snake_size) // snake_size) * snake_size]
            food_spawn = True

    WIN.fill(BLACK)
    draw_snake(snake_pos)
    draw_food(food_pos)
    pygame.display.flip()

    # Kontrola kolize s okrajem obrazovky a s tělem hada
    if len(snake_pos) > 0 and (snake_pos[0][0] >= WIDTH or snake_pos[0][0] < 0 or snake_pos[0][1] >= HEIGHT or snake_pos[0][1] < 0):
        pygame.quit()
        sys.exit()
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            pygame.quit()
            sys.exit()

    # Omezení FPS
    clock.tick(10)

