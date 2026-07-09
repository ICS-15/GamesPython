# Initial configurations
import pygame
import random
import os
from utils.scoreManager import *
from utils.intro import show_intro
from utils.config import *

score_file = get_score_file(os.path.dirname(__file__))

## Initialize pygame
pygame.init()

## Initialize screen
pygame.display.set_caption("Snake game")
width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

# Define colors for the snake
snake_colors = {
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "orange": (255, 165, 0),
    "white": (255, 255, 255)
}

## Parameters for the snake
square_size = 20
game_speed = 10

def create_food():
    ## Use round for aligning items
    food_x = round(random.randrange(0, width - square_size) / float(square_size)) * float(square_size)
    food_y = round(random.randrange(0, height - square_size) / float(square_size)) * float(square_size)
    return food_x, food_y

# Function to draw the food on the screen
def draw_food(size, food_x, food_y):
    pygame.draw.rect(screen, colors["green"], [food_x, food_y, size, size])

# Function to draw the snake on the screen
def draw_snake(size, pixels, snake_color):
    for pixel in pixels:
        pygame.draw.rect(screen, snake_color, [pixel[0], pixel[1], size, size])

# Function to draw the score on the screen
def draw_score(score):
    font = pygame.font.SysFont("Helvetica", 35)
    text = font.render(f"Score: {score}", True, colors["red"])
    screen.blit(text, [5, 1])

# Function to select the speed and direction of the snake based on user input
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

def start_game():
    ## Game start variables
    game_over = False

    x = width / 2
    y = height / 2

    speed_x = square_size
    speed_y = 0

    snake_size = 1
    ## Allows the snake to grow
    pixels = []
    food_x, food_y =  create_food()
    last_direction = 'RIGHT'
    snake_color = random.choice(list(snake_colors.values()))
    color_changed = False
    new_snake_color = snake_color
    game_speed = 10
    
    ## Create infinite loop
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

        ## Update snake
        x += speed_x
        y += speed_y

        ## Snake hits the wall
        if x < 0 or x >= width or y < 0 or y >= height:
            game_over = True

        # Draw objects on screen
        ## Food
        draw_food(square_size, food_x, food_y)
        ## Snake
        pixels.append([x,y])
        ## Snake movement
        if len(pixels) > snake_size:
            del pixels[0] 

        ## Snake hits itself 
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                game_over = True

        draw_snake(square_size, pixels,snake_color)

        ## Score
        score = draw_score(snake_size - 1)
        if (snake_size - 1) % 5 == 0 and snake_size != 1 and not color_changed:
            while snake_color == new_snake_color: 
                new_snake_color = random.choice(list(snake_colors.values()))
                game_speed += 2
            snake_color = new_snake_color
            color_changed = True

        if (snake_size - 1) % 5 != 0:
            color_changed = False

        ## Update screen
        pygame.display.update()

        ## Create new food
        if x == food_x and y == food_y:
            snake_size += 1
            food_x, food_y = create_food()

        # Check if the game is over to update the score and show the intro screen
        if game_over:
            update_score(score_file, snake_size - 1)
            show_intro(
                screen,
                "Snake",
                score_file,
                [
                    "Press any key to start",
                    "Use arrows or WASD to play"
                ],
                start_game
            )
        ## Control game speed
        clock.tick(game_speed)

# Main function to start the game and show the intro screen
def main():
    show_intro(
        screen,
        "Snake",
        score_file,
        [
            "Press any key to start",
            "Use arrows or WASD to play"
        ],
        start_game
    )

if __name__ == "__main__":
    main()
