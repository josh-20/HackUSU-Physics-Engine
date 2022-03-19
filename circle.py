import pygame
class circle:
    def __init__(self, pos=(0.0, 0.0), velocity=(0.0, 0.0), mass=1.0, static=False, netForce=0.0, radius=100.0):
         self.pos = pos
         self.velocity = velocity
         self.mass = mass
         self.static = static
         self.netForce = netForce
         self.radius = radius
    
    def applyforce(self, forceVector):
        self.netForce += forceVector

    def update(self):
        acceleration = self.netForce/self.mass
        self.velocity += acceleration
        

    def draw(self):
       # pygame.draw.circle(Surface, color, self.pos, radius, width=0)
       pass

