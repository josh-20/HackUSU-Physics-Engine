import pygame
import pygame.locals


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((100, 100))

    while pygame.event.wait().type != pygame.locals.QUIT:
        pass

