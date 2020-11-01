import pygame
import ctypes


def create_rectangle(x1, y1, x2, y2):
    print("rectangle")


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
width = 800
height = 600
center = (width//2, height//2)
screensize = width, height

screen = pygame.display.set_mode(screensize)

pygame.display.set_caption("HI!")

font = pygame.font.SysFont('Comic Sans MS', 18)

text = font.render('Test Text', True, GREEN, BLUE)
screen.fill(BLACK)
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = False


    pygame.display.update()
