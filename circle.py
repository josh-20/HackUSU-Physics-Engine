import pygame
from helper import *


class circle:
    def __init__(self, pos=(0.0, 0.0), velocity=(0.0, 0.0), mass=0.0, static=False, netForce=(0.0, 0.0), radius=100.0, color=(255,255,255)):
        self.pos = pos
        self.color = color
        self.velocity = velocity
        self.mass = mass
        self.static = static
        self.netForce = netForce
        self.radius = radius
    
    def applyforce(self, forceVector):
        self.netForce += forceVector

    def update(self, time_step=1.0):
        if not self.static:
            self.pos = Tadd(scalar_mult(time_step, self.velocity), self.pos)
            acceleration = TdivF(self.netForce, self.mass)
            self.velocity = Tadd(self.velocity, scalar_mult(time_step, acceleration))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, tuple(map(int, self.pos)), int(self.radius))

    def type(self):
        return "circle"


