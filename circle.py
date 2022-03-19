import pygame
class circle:
    def __init__(self, pos=0, velocity=0, mass=0, static=False, netForce=0, radius=100):
         self.pos = pos
         self.velocity = velocity
         self.mass = mass
         self.static = static
         self.netForce = netForce
         self.radius = radius
    
    def applyforce(self, forceVector):
        self.netForce += forceVector

    def draw(self):
       # pygame.draw.circle(Surface, color, self.pos, radius, width=0)
       pass

