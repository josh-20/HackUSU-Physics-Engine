import pygame
from line import line
from circle import circle
from helper import *


class simulator:
    def __init__(self):
        self.physics_objects = []
        self.physics_objects.append(circle(pos=(120.0, 0.0), velocity=(4.0, 4.0), mass=1.0, static=False, netForce=(0.0, 0.0), radius=100.0))
        self.physics_objects.append(line(startpos=(0.0, 700.0), endpos=(1100.0, 700.0), static=True))

    def render(self, screen):
        for physics_object in self.physics_objects:
            physics_object.draw(screen)

    def update(self):
        for physics_object in self.physics_objects:
            physics_object.update()
            for other_object in self.physics_objects:
                if physics_object != other_object:
                    self.do_they_collide(physics_object, other_object)

    def do_they_collide(self, object1, object2):
        if object1.type() == "circle" and object2.type() == "circle":
            prev_d = distance(Tadd(object1.pos, scalar_mult(-1, object1.velocity)), object2.pos)
            new_d = distance(object1.pos, object2.pos)
            target_d = object1.radius + object2.radius
            if new_d < target_d:
                go_back_factor = 1 - abs(prev_d - target_d) / abs(new_d - prev_d)
                object1.pos = Tadd(object1.pos, scalar_mult(-go_back_factor, object1.velocity))
                return True
        if object1.type() == "circle" and object2.type() == "line":
            if object2.startpos[0] < object1.pos[0] < object2.endpos[0]:
                new_d = abs(object1.pos[1] - object2.startpos[1])
                prev_d = abs(Tadd(object1.pos, scalar_mult(-1, object1.velocity))[1] - object2.startpos[1])
                target_d = object1.radius
                if new_d < target_d:
                    go_back_factor = 1 - abs(prev_d - target_d) / abs(new_d - prev_d)
                    object1.pos = Tadd(object1.pos, scalar_mult(-go_back_factor, object1.velocity))

                    angle = get_angle(object1.velocity, Tadd(object2.endpos, scalar_mult(-1, object2.startpos)))
                    print(angle)
                    add_angle(angle, object1.velocity)

    def add_physics_object(self, physics_object):
        self.physics_objects.append(physics_object)
