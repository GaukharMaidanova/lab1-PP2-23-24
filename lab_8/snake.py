import pygame
import random

# Initialize pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Set colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Set snake and food size
BLOCK_SIZE = 20

# Set game speed
initial_speed = 5
speed_increment = 2
speed = initial_speed

# Set initial level and score
level = 1
score = 0

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Function to display text on screen
def display_text(text, color, x, y, font_size=30):
    font = pygame.font.SysFont(None, font_size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

# Function to display score and level
def display_stats():
    display_text("Score: " + str(score), WHITE, 10, 10)
    display_text("Level: " + str(level), WHITE, SCREEN_WIDTH - 150, 10)

# Function to generate random food position
def generate_food():
    food_x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    food_y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    return food_x, food_y

# Main function for the game
def game():
    global score, level, initial_speed, speed 

    # Snake initial position and direction
    snake = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
    snake_direction = (1, 0)

    food_x, food_y = generate_food()

    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)

        # Move the snake
        new_head = ((snake[0][0] + snake_direction[0] * BLOCK_SIZE) % SCREEN_WIDTH,(snake[0][1] + snake_direction[1] * BLOCK_SIZE) % SCREEN_HEIGHT)
        snake.insert(0, new_head)


        # Check for collision with food
        if snake[0][0] == food_x and snake[0][1] == food_y:
            score += 1
            food_x, food_y = generate_food()

            # Increase level based on score
            if score % 3 == 0:
                level += 1
                speed = initial_speed + (level - 1) * speed_increment

        else:
            snake.pop()

        # Check for collision with wall
        if (snake[0][0] < 0 or snake[0][0] >= SCREEN_WIDTH or
            snake[0][1] < 0 or snake[0][1] >= SCREEN_HEIGHT):
            running = False

        # Check for collision with itself
        if snake[0] in snake[1:]:
            running = False

        # Draw the snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

        # Draw the food
        pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

        # Display score and level
        display_stats()

        pygame.display.update()

        # Control game speed
        clock.tick(speed)

    pygame.quit()

# Run the game
game()
