import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)

# Размеры экрана
WIDTH, HEIGHT = 800, 600

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Paint')

# Шрифт
font = pygame.font.SysFont(None, 30)

# Переменные для фигур
start_pos = None
end_pos = None
drawing = False
current_color = BLACK
current_tool = 'line'
current_shape = 'rect'

shapes = []

start_pos = (0, 0)  # Инициализация переменной start_pos
# Главный цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                end_pos = pygame.mouse.get_pos()
                drawing = False
                if current_tool == 'line':
                    pygame.draw.line(screen, current_color, start_pos, end_pos, 2)
                    shapes.append(('line', current_color, start_pos, end_pos))
                elif current_tool == 'rectangle':
                    rect = pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                    pygame.draw.rect(screen, current_color, rect)
                    shapes.append(('rect', current_color, rect))
                elif current_tool == 'circle':
                    radius = math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                    pygame.draw.circle(screen, current_color, start_pos, int(radius))
                    shapes.append(('circle', current_color, start_pos, int(radius)))
                elif current_tool == 'rect_triangle':
                    rect = pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                    pygame.draw.rect(screen, current_color, rect)
                    shapes.append(('rect_triangle', current_color, rect))
                elif current_shape == 'equi_triangle':
                    x, y = (start_pos[0] + end_pos[0]) / 2, start_pos[1]
                    pygame.draw.polygon(screen, current_color, [(x, y), start_pos, end_pos])
                    shapes.append(('equi_triangle', current_color, [(x, y), start_pos, end_pos]))
                elif current_shape == 'rhombus':
                    pygame.draw.polygon(screen, current_color, [start_pos, (end_pos[0], start_pos[1]), end_pos, (start_pos[0], end_pos[1])])
                    shapes.append(('rhombus', current_color, [start_pos, (end_pos[0], start_pos[1]), end_pos, (start_pos[0], end_pos[1])]))
                elif current_tool == 'eraser':
                    rect_1 = pygame.Rect(end_pos[0] - 5, end_pos[1] - 5, 10, 10)
                    pygame.draw.rect(screen, WHITE, rect)
                    shapes.append(('eraser', screen, WHITE, rect_1))

    # Отрисовка на экране
    screen.fill(WHITE)

    # Отображение инструментов
    line_button = pygame.draw.rect(screen, BLACK, (10, 10, 40, 40))
    rect_button = pygame.draw.rect(screen, BLACK, (60, 10, 40, 40))
    circle_button = pygame.draw.rect(screen, BLACK, (110, 10, 40, 40))
    eraser_button = pygame.draw.rect(screen, BLACK, (210, 10, 40, 40))
    rect_triangle_button = pygame.draw.rect(screen, BLACK, (260, 10, 40, 40))
    equi_triangle_button = pygame.draw.rect(screen, BLACK, (310, 10, 40, 40))
    rhombus_button = pygame.draw.rect(screen, BLACK, (360, 10, 40, 40))

    # Отображение цветов
    pygame.draw.rect(screen, RED, (410, 10, 40, 40))
    pygame.draw.rect(screen, GREEN, (460, 10, 40, 40))
    pygame.draw.rect(screen, BLUE, (510, 10, 40, 40))
    pygame.draw.rect(screen, LIGHT_BLUE, (560, 10, 40, 40))


    # Отображение текущего инструмента
    if current_tool == 'line':
        pygame.draw.rect(screen, RED, line_button, 3)
    elif current_tool == 'rectangle':
        pygame.draw.rect(screen, RED, rect_button, 3)
    elif current_tool == 'circle':
        pygame.draw.rect(screen, RED, circle_button, 3)
    elif current_tool == 'rect_triangle':
        pygame.draw.rect(screen, RED, rect_triangle_button, 3)
    elif current_tool == 'equi_triangle':
        pygame.draw.rect(screen, RED, equi_triangle_button, 3)
    elif current_tool == 'eraser':
        pygame.draw.rect(screen, RED, eraser_button, 3)
    elif current_tool == 'rhombus':
        pygame.draw.rect(screen, RED, rhombus_button, 3)

    # Обработка нажатий на кнопки
    mouse_pos = pygame.mouse.get_pos()
    if line_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            current_tool = 'line'
    elif rect_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            current_tool = 'rectangle'
    elif circle_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            current_tool = 'circle'
    elif rect_triangle_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            current_tool = 'rect_triangle'
    elif equi_triangle_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            current_tool = 'equi_triangle'
    elif rhombus_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            current_tool = 'rhombus'
    elif eraser_button.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            current_tool = 'eraser'
    elif pygame.Rect(410, 10, 40, 40).collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            current_color = RED
    elif pygame.Rect(460, 10, 40, 40).collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            current_color = GREEN
    elif pygame.Rect(510, 10, 40, 40).collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            current_color = BLUE
    elif pygame.Rect(560, 10, 40, 40).collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            current_color = LIGHT_BLUE

    # Отображение текущего цвета
    pygame.draw.rect(screen, current_color, (500, HEIGHT - 40, 40, 40))

    # Отображение текущего инструмента
    if current_tool == 'line':
        pygame.draw.line(screen, current_color, start_pos, pygame.mouse.get_pos(), 2)
    elif current_tool == 'rectangle':
        if drawing:
            rect = pygame.Rect(start_pos[0], start_pos[1], pygame.mouse.get_pos()[0] - start_pos[0], pygame.mouse.get_pos()[1] - start_pos[1])
            pygame.draw.rect(screen, current_color, rect)
    elif current_tool == 'circle':
        if drawing:
            radius = math.hypot(pygame.mouse.get_pos()[0] - start_pos[0], pygame.mouse.get_pos()[1] - start_pos[1])
            pygame.draw.circle(screen, current_color, start_pos, int(radius))
    elif current_tool == 'rect_triangle':
            if start_pos[0] < pygame.mouse.get_pos()[0]:
                rect = pygame.Rect(start_pos[0], start_pos[1], pygame.mouse.get_pos()[0] - start_pos[0], pygame.mouse.get_pos()[1] - start_pos[1])
                pygame.draw.rect(screen, current_color, rect)
            else:
                rect = pygame.Rect(pygame.mouse.get_pos()[0], start_pos[1], start_pos[0] - pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - start_pos[1])
                pygame.draw.rect(screen, current_color, rect)
    elif current_tool == 'equi_triangle':
            if start_pos[0] < pygame.mouse.get_pos()[0]:
                x, y = (start_pos[0] + pygame.mouse.get_pos()[0]) / 2, start_pos[1]
                pygame.draw.polygon(screen, current_color, [(x, y), start_pos, pygame.mouse.get_pos()])
            else:
                x, y = (start_pos[0] + pygame.mouse.get_pos()[0]) / 2, start_pos[1]
                pygame.draw.polygon(screen, current_color, [(x, y), pygame.mouse.get_pos(), start_pos])
    elif current_shape == 'rhombus':
            pygame.draw.polygon(screen, current_color, [start_pos, (pygame.mouse.get_pos()[0], start_pos[1]), pygame.mouse.get_pos(), (start_pos[0], pygame.mouse.get_pos()[1])])
    elif current_tool == 'eraser':
        if drawing:
            rect_1 = pygame.Rect(pygame.mouse.get_pos()[0] - 5, pygame.mouse.get_pos()[1] - 5, 10, 10)
            pygame.draw.rect(screen, WHITE, rect_1)

    for shape in shapes:
        if shape[0] == 'line':
            pygame.draw.line(screen, shape[1], shape[2], shape[3])
        elif shape[0] == 'rect':
            pygame.draw.rect(screen, shape[1], shape[2])
        elif shape[0] == 'circle':
            pygame.draw.circle(screen, shape[1], shape[2], shape[3])
        elif shape[0] == 'rect_triangle':
            pygame.draw.rect(screen, shape[1], shape[2])
        elif shape[0] == 'equi_triangle':
            pygame.draw.polygon(screen, shape[1], shape[2])
        elif shape[0] == 'rhombus':
            pygame.draw.polygon(screen, shape[1], shape[2])
        elif shape[0] == 'eraser':
            pygame.draw.rect(screen, shape[1], shape[2])

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()
