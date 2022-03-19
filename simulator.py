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
            prev_d = distance(Tadd(object1.pos, scalar_mult(-1, object1.velocity)), object2.pos)
            new_d = distance(object1.pos, object2.pos)
            target_d = object1.radius + object2.radius
            if new_d < target_d:
                go_back_factor = 1 - abs(prev_d - target_d) / abs(new_d - prev_d)
                object1.pos = Tadd(object1.pos, scalar_mult(-go_back_factor, object1.velocity))
                return True
    

    def add_physics_object(self, physics_object):
        self.physics_objects.append(physics_object)
