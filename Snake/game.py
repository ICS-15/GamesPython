# Initial configurations
import pygame
import random

## initialize pygame
pygame.init()

## initialize screen
pygame.display.set_caption("Snake game")
width, height = 1200, 600
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

## colors to use in the game 
colors = {
    "white": (255, 255, 255), 
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0)
}

snake_colors = {
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "orange": (255, 165, 0),
    "white": (255, 255, 255)
}

## parameters for the snake
square_size = 20
game_speed = 10

def create_food():
    ## use round for aligning items
    food_x = round(random.randrange(0, width - square_size) / float(square_size)) * float(square_size)
    food_y = round(random.randrange(0, height - square_size) / float(square_size)) * float(square_size)
    return food_x, food_y

def draw_food(size, food_x, food_y):
    pygame.draw.rect(screen, colors["green"], [food_x, food_y, size, size])

def draw_snake(size, pixels, snake_color):
    for pixel in pixels:
        pygame.draw.rect(screen, snake_color, [pixel[0], pixel[1], size, size])

def draw_score(score):
    font = pygame.font.SysFont("Helvetica", 35)
    text = font.render(f"Score: {score}", True, colors["red"])
    screen.blit(text, [5, 1])

# Updates the score file with the highest score between the current score and the previous high score
def update_score(nscore):
    score = max_score()
    with open('scores.txt', 'w') as f:
        f.write(str(max(score, nscore)))


# Reads and returns the highest score from the score file
def max_score():
    with open('scores.txt', 'r') as f:
        return int(f.readline().strip())

def reset_score():
    with open('scores.txt', 'w') as f:
        f.write(str(0))

def select_speed(key, last_direction, speed_x, speed_y):
    if (key == pygame.K_s or key == pygame.K_DOWN) and last_direction != 'UP':
        speed_x = 0
        speed_y = square_size
        new_direction = 'DOWN'
    elif (key == pygame.K_w or key == pygame.K_UP) and last_direction != 'DOWN':
        speed_x = 0
        speed_y = -square_size
        new_direction = 'UP'
    elif (key == pygame.K_d or key == pygame.K_RIGHT) and last_direction != 'LEFT':
        speed_x = square_size
        speed_y = 0
        new_direction = 'RIGHT'
    elif (key == pygame.K_a or key == pygame.K_LEFT) and last_direction != 'RIGHT':
        speed_x = -square_size
        speed_y = 0
        new_direction = 'LEFT'
    else:
        # If any other key is pressed, the direction doesn't change
        speed_x = speed_x
        speed_y = speed_y
        new_direction = last_direction
    return speed_x, speed_y, new_direction

def draw_intro_screen():
    screen.fill(colors["black"])
    font = pygame.font.Font(None, 50)
    start_text = font.render("Snake", True, colors["white"])
    instruction_text = pygame.font.Font(None, 30).render("Press any key to start", True, colors["white"])
    instruction_text_2 = pygame.font.Font(None, 30).render("Use arrow keys or WASD to play", True, colors["white"])
    score = max_score()
    score_text = pygame.font.Font(None, 30).render(f"Top Score: {score}", True, colors["white"])
    score_reset_text = pygame.font.Font(None, 30).render(f"Use R to reset the top score", True, colors["white"])


    # Center the text
    screen.blit(start_text, (width // 2 - start_text.get_width() // 2, 100))
    screen.blit(instruction_text, (width // 2 - instruction_text.get_width() // 2, 200))
    screen.blit(instruction_text_2, (width // 2 - instruction_text_2.get_width() // 2, 225))
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 300))
    screen.blit(score_reset_text, (width // 2 - score_reset_text.get_width() // 2, 325))



    pygame.display.flip()

# Intro screen
def show_intro():
    intro_active = True

    while intro_active:
        draw_intro_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro_active = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_score()
            if event.type == pygame.KEYDOWN and event.key != pygame.K_r :
                #if event.key == pygame.K_SPACE:
                    intro_active = False  # Exit the intro screen
                    start_game()

    pygame.time.wait(1)

def start_game():
    ## game start variables
    game_over = False

    x = width / 2
    y = height / 2

    speed_x = square_size
    speed_y = 0

    snake_size = 1
    ## allows the snake to grow
    pixels = []
    food_x, food_y =  create_food()
    last_direction = 'RIGHT'
    snake_color = random.choice(list(snake_colors.values()))
    color_changed = False
    new_snake_color = snake_color
    game_speed = 10
    
    ## create infinite loop
    while not game_over :
        
        screen.fill(colors["black"])
        #pygame.draw.line(screen, colors["red"], (0, 0), (width, 0), 1)
        #pygame.draw.line(screen, colors["red"], (0, height - 1), (width, height - 1), 1)
        #pygame.draw.line(screen, colors["red"], (0, 0), (0, height), 1)
        #pygame.draw.line(screen, colors["red"], (width - 1, height), (width - 1, 0), 1)
        pygame.draw.rect(screen, colors["red"], (0, 0, width, height), 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                game_over = True 
            elif event.type == pygame.KEYDOWN:
                speed_x, speed_y, last_direction = select_speed(event.key, last_direction, speed_x, speed_y)  

        ## update snake
        x += speed_x
        y += speed_y

        ## snake hits the wall
        if x < 0 or x >= width or y < 0 or y >= height:
            game_over = True

        # draw objects on screen
        ## food
        draw_food(square_size, food_x, food_y)
        ## snake
        pixels.append([x,y])
        ## snake movement
        if len(pixels) > snake_size:
            del pixels[0] 

        ## snake hits itself 
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                game_over = True

        draw_snake(square_size, pixels,snake_color)

        ## score
        score = draw_score(snake_size - 1)
        if (snake_size - 1) % 5 == 0 and snake_size != 1 and not color_changed:
            while snake_color == new_snake_color: 
                new_snake_color = random.choice(list(snake_colors.values()))
                game_speed += 2
            snake_color = new_snake_color
            color_changed = True

        if (snake_size - 1) % 5 != 0:
            color_changed = False

        ## update screen
        pygame.display.update()

        ## create new food
        if x == food_x and y == food_y:
            snake_size += 1
            food_x, food_y = create_food()

        if game_over:
            update_score(snake_size - 1)
            show_intro()
        clock.tick(game_speed)

show_intro()
