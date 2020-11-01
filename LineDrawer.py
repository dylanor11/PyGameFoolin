# SUCCESS!!!

import pygame


pygame.init()

stored_pos = None
new_pos = None

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
width = 800
height = 600
center = (width//2, height//2)
screensize = width, height

screen = pygame.display.set_mode(screensize)

pygame.display.set_caption("Close with k")

font = pygame.font.SysFont('Comic Sans MS', 18)

text = font.render('Test Text', True, GREEN, BLUE)
screen.fill(BLACK)
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if stored_pos is None:
                stored_pos = pygame.mouse.get_pos()
            else:
                new_pos = pygame.mouse.get_pos()
                pygame.draw.line(screen, WHITE, stored_pos, new_pos)
                stored_pos = new_pos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                running = False

    pygame.display.update()
