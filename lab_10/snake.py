import psycopg2
from psycopg2 import sql
import pygame
import random

def create_connection():
    """ CREATE CONNECTION WITH DATABASE PostgreSQL """
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="snake_game", 
            user="postgres", 
            password="postgres", 
            host="localhost", 
            port="5432"
        )
        return conn
    except Exception as e:
        print(e)
    return conn

def create_table(conn):
    """ Create table of users in PostgreSQL """
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username TEXT NOT NULL,
                score INTEGER DEFAULT 0
            )
        """)
        conn.commit()
        cur.close()
    except Exception as e:
        print(e)

# Подключаемся к базе данных и создаем таблицу
conn = create_connection()
create_table(conn)

def add_user(conn, username):
    """ Insert a user in database PostgreSQL """
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        return user_id
    except Exception as e:
        print(e)
        return None

# Регистрация нового пользователя
username = input("Введите ваше имя: ")
user_id = add_user(conn, username)
if user_id:
    print(f"Пользователь {username} добавлен с ID {user_id}")

# Инициализация пайгейм
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


BLOCK_SIZE = 20

initial_speed = 5
speed_increment = 2
speed = initial_speed

level = 1
score = 0

# Инициализация экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Функция для отображения текста на экране
def display_text(text, color, x, y, font_size=30):
    font = pygame.font.SysFont(None, font_size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

# Функция для отображения кол-ва очков и уровня
def display_stats():
    display_text("Score: " + str(score), WHITE, 10, 10)
    display_text("Level: " + str(level), WHITE, SCREEN_WIDTH - 150, 10)

# Генерация рандомной позиции еды
def generate_food():
    food_x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    food_y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    return food_x, food_y


# функция игры
def game():
    global score, level, initial_speed, speed 

    # изначальная позиция и траектория движения змейки
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

        # движение змейки
        new_head = ((snake[0][0] + snake_direction[0] * BLOCK_SIZE) % SCREEN_WIDTH,(snake[0][1] + snake_direction[1] * BLOCK_SIZE) % SCREEN_HEIGHT)
        snake.insert(0, new_head)


        # столкновение с едой
        if snake[0][0] == food_x and snake[0][1] == food_y:
            score += 1
            food_x, food_y = generate_food()

            # увеличение уровня в зависимости от кол-ва очков
            if score % 3 == 0:
                level += 1
                speed = initial_speed + (level - 1) * speed_increment

        else:
            snake.pop()

        # столкновения со стеной
        if (snake[0][0] < 0 or snake[0][0] >= SCREEN_WIDTH or
            snake[0][1] < 0 or snake[0][1] >= SCREEN_HEIGHT):
            running = False

        # столкновения с собой
        if snake[0] in snake[1:]:
            running = False

        # отрисовывание змейки
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

        # отрисовывание еды
        pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

        # отображение уровня и кол-ва очков
        display_stats()

        pygame.display.update()

        # контроль скорости игры
        clock.tick(speed)

    pygame.quit()
    return score

scores = game()
print(f"Вы заработали {scores} очков!")

def update_score(conn, user_id, score):
    """ Обновить счет пользователя в PostgreSQL """
    try:
        cur = conn.cursor()
        cur.execute("UPDATE users SET score = %s WHERE id = %s", (score, user_id))
        conn.commit()
        cur.close()
    except Exception as e:
        print(e)

# Обновляем счет после игры
update_score(conn, user_id, scores)