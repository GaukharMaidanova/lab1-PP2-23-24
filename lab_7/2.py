import pygame
import string
import os

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Music Player")

WHITE = (255, 255, 255)

font = pygame.font.Font(None, 36)

def load_music(directory):
    music_files = []
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            music_files.append(os.path.join(directory, file))
    return music_files

def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    play_music(playlist[current_song_index])

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(playlist)
    play_music(playlist[current_song_index])

playlist_directory = "C:\\Users\\Gauhar\\Desktop\\Music"
playlist = load_music(playlist_directory)
current_song_index = 0


running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music(playlist[current_song_index])
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                prev_song()

    current_song_text = font.render(os.path.basename(playlist[current_song_index]), True, (0, 0, 0))
    screen.blit(current_song_text, (10, 10))

    pygame.display.flip()


pygame.quit()
