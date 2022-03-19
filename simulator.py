import pygame
from circle import circle
from helper import *


class simulator:
    def __init__(self):
        self.physics_objects = []
        self.physics_objects.append(circle())
        print(type(self.physics_objects))
        pass

    def update(self):
        for physics_object in self.physics_objects:
            physics_object.update()
            for other_object in self.physics_objects:
                if physics_object != other_object:
                    self.do_they_collide(physics_object, other_object)

    def render(self, screen):
        for physics_object in self.physics_objects:
            physics_object.draw(screen)

    def do_they_collide(self, object1, object2):
        if object1.type() == "circle" and object2.type() == "circle":
            if distance(object1.pos, object2.pos) < object1.radius + object2.radius:
                return True

    def add_physics_object(self, physics_object):
        self.physics_objects.append(physics_object)
