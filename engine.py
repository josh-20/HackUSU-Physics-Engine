import pygame
from pygame.locals import *
import sys
from simulator import simulator

DISPLAY_WIDTH = 1100
DISPLAY_HEIGHT = 700

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    speed = 60
    clock = pygame.time.Clock()

    physics_sim = simulator()

    x = 10
    while True:
        physics_sim.update()
        physics_sim.render(screen)

        clock.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
