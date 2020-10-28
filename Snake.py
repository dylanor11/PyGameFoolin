import pygame


# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen_size = (800, 600)

pygame.init()
pygame.font.init()
pygame.display.set_caption("Snek")

screen = pygame.display.set_mode(screen_size)

running = True

screen.fill(BLACK)

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


        pygame.display.update()