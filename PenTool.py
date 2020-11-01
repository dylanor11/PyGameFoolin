import pygame


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
width = 800
height = 600
screensize = width, height

last_pos = None
cur_pos = None
drawing = False
pen_size = 1

screen = pygame.display.set_mode(screensize)

pygame.display.set_caption("Pen Tool")

font = pygame.font.SysFont('Comic Sans MS', 18)

text = font.render('Test Text', True, GREEN, BLUE)
screen.fill(BLACK)
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None
            cur_pos = None
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = False
            elif event.key == pygame.K_1:
                pen_size = 1
            elif event.key == pygame.K_2:
                pen_size = 2
            elif event.key == pygame.K_3:
                pen_size = 3
            elif event.key == pygame.K_4:
                pen_size = 4
            elif event.key == pygame.K_5:
                pen_size = 5
            elif event.key == pygame.K_6:
                pen_size = 6
            elif event.key == pygame.K_7:
                pen_size = 7
            elif event.key == pygame.K_8:
                pen_size = 8
            elif event.key == pygame.K_9:
                pen_size = 9
                print("hello")
    if drawing:
        cur_pos = pygame.mouse.get_pos()
        pygame.draw.line(screen, WHITE, last_pos, cur_pos, pen_size)
        last_pos = cur_pos
        # Circle pen is optimal but draws a bunch of dots in its state below
        # I think I should make it draw a line of circles between last_pos and cur_pos
        # pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), pen_size)

    pygame.display.update()
