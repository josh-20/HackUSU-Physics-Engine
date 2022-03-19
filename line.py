import pygame
from helper import *


class line:
    def __init__(self, startpos=(0.0, 0.0), endpos=(0.0, 0.0), static=True):
        self.startpos = startpos
        self.endpos = endpos
        # self.velocity = velocity
        # self.mass = mass
        self.static = static
        # self.netForce = netForce
        # self.radius = radius

    # def applyforce(self, forceVector):
    #     self.netForce += forceVector
    #
    def update(self):
        # self.pos = Tadd(self.velocity, self.pos)
        #
        # acceleration = TdivF(self.netForce / self.mass)
        # self.velocity = Tadd(self.velocity, acceleration)
        pass

    def draw(self, screen):
        pygame.draw.line(screen, (255, 255, 255), self.startpos, self.endpos)


