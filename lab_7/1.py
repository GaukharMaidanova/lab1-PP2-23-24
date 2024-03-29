import pygame
import sys
import math
import datetime

pygame.init()

screen_width = 920
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Clock Animation")

clock_image = pygame.image.load("lab_7\clock.png").convert_alpha()
clock_rect = clock_image.get_rect(center=(screen_width // 2, screen_height // 2))
clock_image = pygame.transform.scale(clock_image, (920, 600))

clock_hand_minutes_image = pygame.image.load("lab_7\clockminute.png").convert_alpha()
clock_hand_minutes_original = clock_hand_minutes_image
clock_hand_minutes_rect = clock_hand_minutes_image.get_rect(center=(screen_width // 2, screen_height // 2))
clock_hand_minutes_image = pygame.transform.scale(clock_hand_minutes_image, (200, 200))

clock_hand_seconds_image = pygame.image.load("lab_7\clocksecond.png").convert_alpha()
clock_hand_seconds_original = clock_hand_seconds_image
clock_hand_seconds_rect = clock_hand_seconds_image.get_rect(center=(screen_width // 2, screen_height // 2))
clock_hand_seconds_image = pygame.transform.scale(clock_hand_seconds_image, (200, 200))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    screen.blit(clock_image, clock_rect)

    clock = pygame.time.Clock()
    current_time = pygame.time.get_ticks() / 1000
    angle_sec = (current_time % 60) / 60 * 360
    angle_minute = angle_sec/60

    rotated_hands_seconds = pygame.transform.rotate(clock_hand_seconds_image, -angle_sec)
    hands_rect1 = rotated_hands_seconds.get_rect(center=clock_hand_seconds_rect.center)

    rotated_hands_minutes = pygame.transform.rotate(clock_hand_minutes_image, -angle_minute)
    hands_rect2 = rotated_hands_minutes.get_rect(center=clock_hand_minutes_rect.center)


    screen.blit(rotated_hands_seconds, hands_rect1)
    screen.blit(rotated_hands_minutes, hands_rect2)

    pygame.display.flip()

    clock.tick(60)



