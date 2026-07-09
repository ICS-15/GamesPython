import pygame
from utils.config import *

pygame.init()

# Window size
width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Python Games")

# Function to draw the main menu
def draw_menu():

    screen.fill(colors["black"])

    title_font = pygame.font.Font(None, 60)
    font = pygame.font.Font(None, 40)

    # Render the text for the menu options
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

    # Draw the text on the screen
    screen.blit(
        title,
        (width//2 - title.get_width()//2,100))

    screen.blit(
        snake_text,
        (width//2 - snake_text.get_width()//2,250))

    screen.blit(
        breaker_text,
        (width//2 - breaker_text.get_width()//2,320))

    screen.blit(
        exit_text,
        (width//2 - exit_text.get_width()//2,390))
    
    pygame.display.flip()

# Function to launch the selected game
def launch_game(game):

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

        # Handle events - key presses and window close
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