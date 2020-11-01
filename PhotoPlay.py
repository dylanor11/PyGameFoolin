import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

cam = pygame.camera.Camera("/dev/video0", (640, 480))
cam.start()
image = cam.get_image()

# display_surface = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("HI!")

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ENTER:
                running = False


cameras = pygame.camera.list_cameras()
print(cameras)
