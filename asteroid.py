import circleshape
from constants import *
import pygame
import random

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

    def split(self, screen):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            velocity_1 = self.velocity.rotate(random_angle)
            velocity_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity_1 * 1.2
            asteroid2.velocity = velocity_2 * 1.2
        

    