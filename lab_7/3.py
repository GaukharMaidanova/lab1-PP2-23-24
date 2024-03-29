import pygame
import sys

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

BALL_RADIUS = 25
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_speed = 20

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - ball_speed, BALL_RADIUS)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + ball_speed, WINDOW_HEIGHT - BALL_RADIUS)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - ball_speed, BALL_RADIUS)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + ball_speed, WINDOW_WIDTH - BALL_RADIUS)

    pygame.display.flip()


pygame.quit()
sys.exit()
