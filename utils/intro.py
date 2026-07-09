import pygame
from utils.scoreManager import max_score, reset_score
from utils.config import *


def draw_intro_screen(screen,title,score_file,instructions):

    screen.fill(colors["black"])

    title_font = pygame.font.Font(None, 50)
    text_font = pygame.font.Font(None, 30)

    title_text = title_font.render(
        title,
        True,
        colors["white"]
    )

    screen.blit(
        title_text,
        (
            screen.get_width() // 2 - title_text.get_width() // 2,
            100
        )
    )


    y = 200

    for instruction in instructions:

        text = text_font.render(
            instruction,
            True,
            colors["white"]
        )

        screen.blit(
            text,
            (
                screen.get_width() // 2 - text.get_width() // 2,
                y
            )
        )

        y += 30


    score = max_score(score_file)

    score_text = text_font.render(
        f"Top Score: {score}",
        True,
        colors["white"]
    )

    screen.blit(
        score_text,
        (
            screen.get_width() // 2 - score_text.get_width() // 2,
            y + 30
        )
    )


    reset_text = text_font.render(
        "Press R to reset score",
        True,
        colors["white"]
    )

    screen.blit(
        reset_text,
        (
            screen.get_width() // 2 - reset_text.get_width() // 2,
            y + 60
        )
    )

    pygame.display.flip()



def show_intro(screen,title,score_file,instructions,start_game):
    intro_active = True

    while intro_active:

        draw_intro_screen(screen,title,score_file,instructions)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                elif event.key == pygame.K_r:
                    reset_score(score_file)

                else:
                    intro_active = False


    start_game()