import pygame
import subprocess
import sys

pygame.init()

# Window
width = 800
height = 600

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Python Games")

# Colors
colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "yellow": (255, 255, 0),
    "green": (0, 255, 0)
}

def draw_menu():

    screen.fill(colors["black"])

    title_font = pygame.font.Font(None, 60)
    font = pygame.font.Font(None, 40)

    title = title_font.render(
        "Python Games",
        True,
        colors["yellow"]
    )

    snake_text = font.render(
        "1 - Snake",
        True,
        colors["white"]
    )

    breaker_text = font.render(
        "2 - Brick Breaker",
        True,
        colors["white"]
    )

    exit_text = font.render(
        "ESC - Exit",
        True,
        colors["green"]
    )

    screen.blit(
        title,
        (
            width//2 - title.get_width()//2,
            100
        )
    )

    screen.blit(
        snake_text,
        (
            width//2 - snake_text.get_width()//2,
            250
        )
    )

    screen.blit(
        breaker_text,
        (
            width//2 - breaker_text.get_width()//2,
            320
        )
    )

    screen.blit(
        exit_text,
        (
            width//2 - exit_text.get_width()//2,
            390
        )
    )
    pygame.display.flip()

def launch_game(game):
    pygame.quit()

    if game == "snake":
        from snake.gameSnake import main
        main()

    elif game == "brickBreaker":
        from brickBreaker.gameBrickBreaker import main
        main()

    pygame.init()

    global screen

    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption("Python Games")


def main():

    running = True

    while running:

        draw_menu()

        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    launch_game("snake")

                elif event.key == pygame.K_2:
                    launch_game("brickBreaker")

                elif event.key == pygame.K_ESCAPE:
                    running = False

    pygame.quit()

main()