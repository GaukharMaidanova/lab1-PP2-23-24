import pygame
import random

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Размеры экрана
WIDTH, HEIGHT = 800, 600

# Скорость машинок
PLAYER_SPEED = 2
ENEMY_SPEED = 2

# Класс для игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab_9/Player_1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        # Ограничение движения игрока по границам экрана
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))

# Класс для монеток
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = random.choice([1, 3])
        self.image = pygame.image.load(f"lab_9\coins_{self.size}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size*10, self.size*10))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)

# Класс для врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab_9/Enemy_1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-200, -100)
        self.speedy = ENEMY_SPEED

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-200, -100)

# Инициализация экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Car Game')

# Загрузка заднего фона
background = pygame.image.load("lab_9\Animatedroad_1.png").convert()

# Группы спрайтов
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()

# Создание игрока
player = Player()
all_sprites.add(player)

# Создание врага
enemy = Enemy()
all_sprites.add(enemy)

# Параметры игры
score = 0
level = 1
coin_counter = 0

# Главный цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Генерация монеток
    if random.random() < 0.01:
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)

    # Обновление положения монеток и врага
    all_sprites.update()

    # Проверка столкновения игрока с монетками
    hits = pygame.sprite.spritecollide(player, coins, True)
    for hit in hits:
        if hit.size == 1:
            score += 1
        else:
            score += 3
        coin_counter += 1
        if coin_counter % 5 == 0:
            ENEMY_SPEED += 1
        if score % 3 == 0:
            level += 1

    # Проверка столкновения игрока с врагом
    if pygame.sprite.spritecollide(player, [enemy], False):
        pygame.mixer.Sound('lab_9\Sonne.mp3').play()
        running = False

    # Отрисовка заднего фона
    screen.blit(background, (0, 0))

    # Отрисовка спрайтов
    all_sprites.draw(screen)

    # Отображение количества монеток и уровня
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))
    text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(text, (10, 50))

    # Обновление экрана
    pygame.display.flip()

# Вывод сообщения "Game Over"
font = pygame.font.Font(None, 72)
text = font.render("Game Over", True, RED)
screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
pygame.display.flip()

# Задержка перед завершением программы
pygame.time.wait(2000)

# Выход из игры
pygame.quit()



