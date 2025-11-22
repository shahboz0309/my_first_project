import pygame
import random
import sys

# Pygame boshlash
pygame.init()

# Ekran o‘lchami
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game by Shahboz")

# Ranglar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()

snake_size = 15
snake_speed = 12

font = pygame.font.SysFont(None, 30)

def message(text, color, x, y):
    msg = font.render(text, True, color)
    screen.blit(msg, (x, y))

def game_loop():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - snake_size) / 15) * 15
    food_y = round(random.randrange(0, HEIGHT - snake_size) / 15) * 15

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press R to Restart or Q to Quit", RED, 100, HEIGHT // 2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -snake_size
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = snake_size
                    x_change = 0

        # Harakat
        x += x_change
        y += y_change

        # Chegaradan chiqsa o‘yin tugaydi
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True

        screen.fill(BLACK)

        pygame.draw.rect(screen, RED, [food_x, food_y, snake_size, snake_size])

        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            snake_list.pop(0)

        # O‘z tanasiga tegsa — yutqazadi
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        for block in snake_list:
            pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_size, snake_size])

        pygame.display.update()

        # Ovqat yesa
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_size) / 15) * 15
            food_y = round(random.randrange(0, HEIGHT - snake_size) / 15) * 15
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

game_loop()
