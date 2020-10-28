import pygame


class Button:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rectangle = pygame.Rectangle(x, y, width, height)

    def is_within(self, x, y):
        if self.x <= x <= self.x+self.width and self.y <= y <= self.y+self.height:
            return True
        return False
