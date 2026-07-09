import pygame

# Initialize
pygame.init()

# Configure game window
screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)

# Game title
pygame.display.set_caption("Brick Breaker Game")

# Game variables
ball_size = 15
ball = pygame.Rect(100, 500, ball_size, ball_size)

player_width = 100
player = pygame.Rect(0, 750, player_width, ball_size)

blocks_per_row = 8
block_rows = 5
total_blocks = blocks_per_row * block_rows


def create_blocks(blocks_per_row, block_rows):
    screen_height = screen_size[1]
    screen_width = screen_size[0]

    block_spacing = 5
    block_width = screen_width / blocks_per_row - block_spacing
    block_height = 15
    row_spacing = block_height + 15

    blocks = []

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


# Colors
colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "yellow": (255, 255, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
}

# Game management variables
game_over = False
score = 0
ball_direction = [1, -1]


# Game functions
def move_player(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if player.x + player_width < screen_size[0]:
                player.x += 2.5

        if event.key == pygame.K_LEFT:
            if player.x > 0:
                player.x -= 2.5


def move_ball(ball):
    direction = ball_direction

    ball.x += direction[0]
    ball.y += direction[1]

    # Ball hits screen edges
    if ball.x <= 0:
        direction[0] = -direction[0]

    if ball.y <= 0:
        direction[1] = -direction[1]

    if ball.x + ball_size >= screen_size[0]:
        direction[0] = -direction[0]

    if ball.y + ball_size >= screen_size[1]:
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


def update_score(score):
    font = pygame.font.Font(None, 30)
    text = font.render(f"Score: {score}", True, colors["yellow"])
    screen.blit(text, (0, 750))

    return score >= total_blocks


# Draw game elements
def draw_game():
    screen.fill(colors["black"])
    pygame.draw.rect(screen, colors["blue"], player)
    pygame.draw.rect(screen, colors["white"], ball)


def draw_blocks(blocks):
    for block in blocks:
        pygame.draw.rect(screen, colors["green"], block)


# Create blocks
blocks = create_blocks(blocks_per_row, block_rows)


def draw_intro_screen():
    screen.fill(colors["black"])

    title_font = pygame.font.Font(None, 50)
    instruction_font = pygame.font.Font(None, 30)

    title = title_font.render("BRICK BREAKER", True, colors["yellow"])
    instruction = instruction_font.render(
        "Press SPACE to start", True, colors["white"]
    )

    screen.blit(title, (screen_size[0] // 2 - title.get_width() // 2, 100))
    screen.blit(
        instruction,
        (screen_size[0] // 2 - instruction.get_width() // 2, 200),
    )

    pygame.display.flip()


# Intro screen
intro_active = True

while intro_active:
    draw_intro_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro_active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                intro_active = False

    pygame.time.wait(1)


# Main game loop
while not game_over:
    draw_game()
    draw_blocks(blocks)

    game_over = update_score(total_blocks - len(blocks))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    move_player(event)

    ball_direction = move_ball(ball)

    if not ball_direction:
        game_over = True

    pygame.time.wait(1)
    pygame.display.flip()


# Quit game
pygame.quit()