import pygame


running = True

count = 1

pygame.init()

while running:
    print(count)
    count += 1

    pygame.time.wait(1000)

    if pygame.time.get_ticks() > 10000:
        running = False
