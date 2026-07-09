import pygame
import os
from utils.scoreManager import *
from utils.config import *
from utils.intro import show_intro

score_file = get_score_file(os.path.dirname(__file__))

# Initialize
pygame.init()

# Configure game window
width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode((width, height))

# Game title
pygame.display.set_caption("Brick Breaker Game")

# Game variables
ball_size = 15
ball = pygame.Rect(100, 300, ball_size, ball_size)

player_width = 100
player = pygame.Rect(0, 550, player_width, ball_size)

blocks_per_row = 8
block_rows = 5
total_blocks = blocks_per_row * block_rows

# Function to create blocks for the game
def create_blocks(blocks_per_row, block_rows):
    screen_height = height
    screen_width = width

    block_spacing = 5
    block_width = screen_width / blocks_per_row - block_spacing
    block_height = 15
    row_spacing = block_height + 15

    blocks = []
    # Create blocks in a grid pattern
    for row in range(block_rows):
        for column in range(blocks_per_row):
            block = pygame.Rect(
                column * (block_width + block_spacing),
                row * row_spacing,
                block_width,
                block_height,
            )
            blocks.append(block)

    return blocks

# Game management variables
game_over = False
score = 0
ball_direction = [1, -1]

# Game functions
def move_player():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if player.x + player_width < width:
            player.x += 2.5

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if player.x > 0:
            player.x -= 2.5

# Function to move the ball and handle collisions
def move_ball(ball):
    direction = ball_direction

    ball.x += direction[0]
    ball.y += direction[1]

    # Ball hits screen edges
    if ball.x <= 0:
        direction[0] = -direction[0]

    if ball.y <= 0:
        direction[1] = -direction[1]

    if ball.x + ball_size >= width:
        direction[0] = -direction[0]

    if ball.y + ball_size >= height:
        direction = None

    # Ball hits paddle
    if player.collidepoint(ball.x, ball.y):
        direction[1] = -direction[1]

    # Ball hits blocks
    for block in blocks:
        if block.collidepoint(ball.x, ball.y):
            blocks.remove(block)
            direction[1] = -direction[1]

    return direction

# Function to draw the score on the screen
def draw_score(score):
    font = pygame.font.Font(None, 30)
    text = font.render(f"Score: {score}", True, colors["yellow"])
    screen.blit(text, (0, 575))

    return score >= total_blocks

# Draw game elements
def draw_game():
    screen.fill(colors["black"])
    pygame.draw.rect(screen, colors["blue"], player)
    pygame.draw.rect(screen, colors["white"], ball)

# Function to draw the blocks on the screen
def draw_blocks(blocks):
    for block in blocks:
        pygame.draw.rect(screen, colors["green"], block)

# Create blocks
blocks = create_blocks(blocks_per_row, block_rows)

# Main game loop
def start_game():

    global blocks, ball, player, ball_direction

    # Reset game
    ball = pygame.Rect(100, 300, ball_size, ball_size)
    player = pygame.Rect(0, 550, player_width, ball_size)
    ball_direction = [1, -1]
    blocks = create_blocks(blocks_per_row, block_rows)

    game_over = False

    while not game_over:
        draw_game()
        draw_blocks(blocks)

        game_over = draw_score(total_blocks - len(blocks))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        move_player()
        ball_direction = move_ball(ball)

        # Check if the ball is lost (goes below the screen)
        if not ball_direction:
            current_score = total_blocks - len(blocks)

            update_score(
                score_file,
                current_score
            )
            game_over = True
        
        # Check if the player has won (all blocks are destroyed)
        if game_over:
            update_score(score_file, current_score)
            show_intro(
                screen,
                "Brick Breaker",
                score_file,
                [
                    "Press any key to start",
                    "Use arrows or WASD to play"
                ],
                start_game
            )
            return

        pygame.time.wait(1)
        pygame.display.flip()

# Main function to start the game and show the intro screen
def main():
    show_intro(
        screen,
        "Brick Breaker",
        score_file,
        [
            "Press any key to start",
            "Use arrows or WASD to play"
        ],
        start_game
    )

if __name__ == "__main__":
    main()


