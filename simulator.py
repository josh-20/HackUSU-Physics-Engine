import pygame
from line import line
from circle import circle
from helper import *


class simulator:
    def __init__(self):
        self.physics_objects = []
        self.physics_objects.append(circle(pos=(50.0, 50.0), velocity=(4.0, 4.0), mass=1.0, static=False, netForce=(0.0, 6.0), radius=50.0))
        self.physics_objects.append(line(startpos=(1.0, 0.0), endpos=(0.0, 700.0), static=True))
        self.physics_objects.append(line(startpos=(0.0, 701.0), endpos=(1100.0, 700.0), static=True))
        self.physics_objects.append(line(startpos=(1101.0, 0.0), endpos=(1100.0, 700.0), static=True))
        self.physics_objects.append(line(startpos=(0.0, 1.0), endpos=(1100.0, 0.0), static=True))
        self.physics_objects.append(line(startpos=(0.0, 1.0), endpos=(1100.0, 0.0), static=True))

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
            # find the nearest point on the line
            m = (object2.endpos[1] - object2.startpos[1]) / (object2.endpos[0] - object2.startpos[0])
            b = object2.startpos[1] - m * object2.startpos[0]
            x = (object1.pos[1] + object1.pos[0]/m - b) / (m + 1/m)
            y = m * x + b
            if (object2.startpos[0] < x < object2.endpos[0] or object2.startpos[1] < y < object2.endpos[1]) and distance(object1.pos, tuple([x, y])) < object1.radius:
                # put circle exactly on the line
                new_d = distance(object1.pos, tuple([x, y]))
                prev_d = distance(Tadd(object1.pos, scalar_mult(-1, object1.velocity)), tuple([x, y]))
                target_d = object1.radius
                if new_d < target_d:
                    go_back_factor = 1 - abs(prev_d - target_d) / abs(new_d - prev_d)
                    object1.pos = Tadd(object1.pos, scalar_mult(-go_back_factor, object1.velocity))
                    # reflect velocity angle
                    wall = Tadd(object2.endpos, scalar_mult(-1, object2.startpos))
                    normal = normalize(wall)
                    object1.velocity = Tadd(object1.velocity, scalar_mult(-2 * dot_product(normal, object1.velocity), normal))

    def add_physics_object(self, physics_object):
        self.physics_objects.append(physics_object)
