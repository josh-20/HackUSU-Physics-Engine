import pygame
from helper import *


class line:
    def __init__(self, startpos=(0.0, 0.0), endpos=(0.0, 0.0), static=True, color=""):
        self.startpos = startpos
        self.endpos = endpos
        self.color = color
        self.velocity = (0.0, 0.0)
        self.mass = 0.0
        self.static = static
        self.netForce = (0.0, 0.0)

    # def applyforce(self, forceVector):
    #     self.netForce += forceVector
    #
    def update(self, time_step=1.0):
        # self.pos = Tadd(self.velocity, self.pos)
        #
        # acceleration = TdivF(self.netForce / self.mass)
        # self.velocity = Tadd(self.velocity, acceleration)
        pass

    def draw(self, screen):
        pygame.draw.line(screen, (255, 255, 255), self.startpos, self.endpos)

    def type(self):
        return "line"


