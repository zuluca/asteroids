import circleshape
from constants import *
import pygame

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):

        super().__init__(x, y, radius)
        # we will be using this later
        """ if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()  """
        
    
    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

    