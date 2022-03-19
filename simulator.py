import pygame

from circle import circle


class simulator:
    def __init__(self):
        self.physics_objects = []
        self.physics_objects.append(circle())
        pass

    def update(self):
        pass

    def render(self, screen):
        for physics_object in self.physics_objects:
            physics_object.draw(screen)
