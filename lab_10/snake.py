import pygame
import psycopg2
from psycopg2 import sql
import random
from datetime import datetime
import sys

# Database connection parameters
DB_NAME = 'suppliers'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'localhost'

# Establish connection
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
cur = conn.cursor()

# Pygame initialization
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
SNAKE_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


# Set up the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up font
font = pygame.font.Font(None, 36)

# Get the username from the user
username = input("Enter your username: ")

# Function to create a new user
def create_user(username):
    cur.execute("INSERT INTO user (username, current_level) VALUES (%s, 1) ON CONFLICT (username) DO NOTHING;", (username,))
    conn.commit()

# Function to get the user's current level
def get_user_level(username):
    cur.execute("SELECT current_level FROM user WHERE username = %s;", (username,))
    level = cur.fetchone()
    return level[0] if level else 1

# Function to save user score
def save_user_score(username, score, level):
    cur.execute("INSERT INTO user_score (username, score, level) VALUES (%s, %s, %s);", (username, score, level))
    conn.commit()

# Create a new user if they don't exist
create_user(username)

# Get the current level of the user
current_level = get_user_level(username)
print(f"Current level: {current_level}")

# Snake game variables
clock = pygame.time.Clock()
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, WIDTH // SNAKE_SIZE) * SNAKE_SIZE,
            random.randrange(1, HEIGHT // SNAKE_SIZE) * SNAKE_SIZE]
food_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0

# Game loop
running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Check for quitting the game
            if event.key == pygame.K_ESCAPE:
                running = False
            # Check for pausing the game
            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    print("Game paused.")
                else:
                    print("Game resumed.")
            # Change direction based on input
            if not paused:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

    # Move the snake in the specified direction
    if not paused:
        if change_to == 'UP':
            snake_pos[1] -= SNAKE_SIZE
        elif change_to == 'DOWN':
            snake_pos[1] += SNAKE_SIZE
        elif change_to == 'LEFT':
            snake_pos[0] -= SNAKE_SIZE
        elif change_to == 'RIGHT':
            snake_pos[0] += SNAKE_SIZE
        
        # Update direction
        direction = change_to
        
        # Add the new head position to the snake body
        snake_body.insert(0, list(snake_pos))
        
        # Check if the snake eats the food
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            food_spawn = False
            score += 10  # Increase score by 10
        else:
            # Remove the last part of the snake body
            snake_body.pop()
        
        # Spawn new food if necessary
        if not food_spawn:
            food_pos = [random.randrange(1, WIDTH // SNAKE_SIZE) * SNAKE_SIZE, random.randrange(1, HEIGHT // SNAKE_SIZE) * SNAKE_SIZE]
        food_spawn = True
        
        # Clear the screen
        window.fill(BLACK)
        
        # Draw the snake body
        for pos in snake_body:
            pygame.draw.rect(window, GREEN, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))
        
        # Draw the food
        pygame.draw.rect(window, RED, pygame.Rect(food_pos[0], food_pos[1], SNAKE_SIZE, SNAKE_SIZE))
        
        # Check for collisions with the snake body or edges
        if snake_pos in snake_body[1:] or snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
            print("Game Over!")
            save_user_score(username, score, current_level)
            running = False
        
        # Display the score
        score_text = font.render(f"Score: {score}", True, WHITE)
        window.blit(score_text, (10, 10))
        
        # Update the display
        pygame.display.update()
        
        # Control the game speed
        clock.tick(FPS + current_level)  # Increase speed with level

# Close database connection
cur.close()
conn.close()

# Quit pygame
pygame.quit()