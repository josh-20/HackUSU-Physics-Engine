import pygame
from helper import *


class circle:
    def __init__(self, pos=(0.0, 0.0), velocity=(0.0, 0.0), mass=1.0, static=False, netForce=(0.0, 0.0), radius=100.0):
        self.pos = pos
        self.velocity = velocity
        self.mass = mass
        self.static = static
        self.netForce = netForce
        self.radius = radius
    
    def applyforce(self, forceVector):
        self.netForce += forceVector

    def update(self):

        self.pos = Tadd(self.velocity, self.pos)
        acceleration = TdivF(self.netForce, self.mass)
        self.velocity = Tadd(self.velocity, acceleration)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), tuple(map(int, self.pos)), int(self.radius))

    def type(self):
        return "circle"


