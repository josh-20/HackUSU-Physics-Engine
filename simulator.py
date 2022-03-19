import pygame


class simulator:
    def __init__(self):
        self.physics_objects = []
        pass

    def update(self):
        pass

    def render(self, screen):
        pygame.draw.circle(screen, (123, 45, 98), (57, 68), 25)
        for physics_object in self.physics_objects:
            physics_object.draw()
