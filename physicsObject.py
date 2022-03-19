# Physics object interface

class physicsObj:
    def __init__(self):
         self.pos = 0.0
         self.velocity = 0.0
         self.mass = 0.0
         self.static = False
         self.netForce = 0.0
    
    def applyforce(self, forceVector):
        self.netForce += forceVector

    def draw(self):
        pass

