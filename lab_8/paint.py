import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    drawing_rect = False
    drawing_circle = False
    drawing_erase = False
    erase_radius = 15
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_c:
                    drawing_circle = True
                    drawing_rect = False
                    drawing_erase = False
                elif event.key == pygame.K_e:
                    drawing_erase = True
                    drawing_circle = False
                    drawing_rect = False
                elif event.key == pygame.K_d:
                    drawing_rect = True
                    drawing_circle = False
                    drawing_erase = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    if drawing_circle or drawing_erase:
                        radius = min(200, radius + 1)
                    elif drawing_rect:
                        x, y = event.pos
                        points.append((x, y))
                elif event.button == 3: # right click shrinks radius
                    if drawing_circle or drawing_erase:
                        radius = max(1, radius - 1)
                    elif drawing_rect:
                        points = []
            
            if event.type == pygame.MOUSEBUTTONUP:
                if drawing_rect:
                    x2, y2 = event.pos
                    points.append((x2, y2))
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, x2 - x, y2 - y))
                    points = []
                    
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if drawing_erase:
                    erase_position = event.pos
                    pygame.draw.circle(screen, (0, 0, 0), erase_position, erase_radius)
                elif drawing_rect:
                    if len(points) > 0:
                        x2, y2 = event.pos
                        screen.fill((0, 0, 0))
                        pygame.draw.rect(screen, (255, 255, 255), (x, y, x2 - x, y2 - y))
                
        screen.fill((0, 0, 0))
        
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
