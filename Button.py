import pygame


class Button:

    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.rectangle = pygame.Rect(x, y, width, height)

    def is_within(self, x, y):
        if self.x < x < (self.x + self.width) and self.y < y < (self.y + self.height):
            return True
        return False

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Button Testing")
screen.fill((0, 0, 0))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                running = False
        if event.type == pygame.KEYDOWN:
            screen.fill((255, 255, 255))
    pygame.display.update()
