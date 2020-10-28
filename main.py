import pygame
import ctypes
# import sys
# import time
# from pygame.locals import *


user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0),  user32.GetSystemMetrics(1)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.font.init()
pygame.display.set_caption("minimal program")

myfont = pygame.font.SysFont('Comic Sans MS', 20)

text = "help"
textsurface = myfont.render(text, False, WHITE)

screen = pygame.display.set_mode(screensize)

running = True

screen.blit(textsurface, (0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKQUOTE:
                running = False
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            elif event.key == pygame.K_TAB:
                text += "    "
            elif event.key == pygame.K_RETURN:
                text += "\n"
            elif event.key == pygame.K_SPACE:
                text += " "
            elif event.key == pygame.K_EQUALS:
                screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            else:
                text += pygame.key.name(event.key)

        screen.fill(BLACK)
        textsurface = myfont.render(text, False, WHITE)
        screen.blit(textsurface, (0, 0))
        pygame.display.update()

# if __name__ == "__main__":
#     main()


