import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Размер экрана
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

# Направления
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Класс для змейки
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.length = 1

    def move(self):
        x, y = self.body[0]
        if self.direction == UP:
            y -= CELL_SIZE
        elif self.direction == DOWN:
            y += CELL_SIZE
        elif self.direction == LEFT:
            x -= CELL_SIZE
        elif self.direction == RIGHT:
            x += CELL_SIZE
        self.body.insert(0, (x, y))
        if len(self.body) > self.length:
            self.body.pop()

    def change_direction(self, direction):
        if direction == UP and self.direction != DOWN:
            self.direction = direction
        elif direction == DOWN and self.direction != UP:
            self.direction = direction
        elif direction == LEFT and self.direction != RIGHT:
            self.direction = direction
        elif direction == RIGHT and self.direction != LEFT:
            self.direction = direction

    def grow(self):
        self.length += 1

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Класс для еды
class Food:
    def __init__(self):
        self.x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        self.y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        self.size = random.choice([1, 3])
        self.spawn_time = time.time()

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.size * CELL_SIZE, self.size * CELL_SIZE))

# Функция для рисования текста на экране
def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

# Инициализация экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Инициализация игры
snake = Snake()
food = Food()
score = 0
level = 1
game_font = pygame.font.Font(None, 36)

# Таймер для еды
food_timer = time.time()

# Главный цикл игры
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(UP)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(DOWN)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(LEFT)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(RIGHT)

    # Проверка столкновения змейки с едой
    for segment in snake.body:
        if segment[0] == food.x and segment[1] == food.y:
            score += food.size  # Увеличиваем количество очков в зависимости от размера еды
            if score % 3 == 0:
                level += 1
            snake.grow()
            food = Food()
            break



    # Проверка времени жизни еды
    if time.time() - food.spawn_time > 10:
        food = Food()

    # Проверка столкновения с границами экрана
    if (snake.body[0][0] < 0 or snake.body[0][0] >= WIDTH or
        snake.body[0][1] < 0 or snake.body[0][1] >= HEIGHT):
        running = False

    # Перемещение и отрисовка змейки и еды
    snake.move()
    snake.draw(screen)
    food.draw(screen)

    # Отрисовка текста на экране
    draw_text(screen, f"Score: {score}", game_font, BLUE, WIDTH // 2, 10)
    draw_text(screen, f"Level: {level}", game_font, BLUE, WIDTH // 2, 50)

    # Обновление экрана
    pygame.display.flip()

    # Задержка и обновление таймера
    clock.tick(5 + level * 2)

# Вывод сообщения о завершении игры
game_over_font = pygame.font.Font(None, 72)
draw_text(screen, "Game Over", game_over_font, RED, WIDTH // 2, HEIGHT // 2)
pygame.display.flip()

# Задержка перед завершением программы
pygame.time.wait(2000)

# Выход из игры
pygame.quit()

