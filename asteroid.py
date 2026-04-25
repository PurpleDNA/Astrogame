import pygame
import circleshape
from constants import *
from logger import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <  ASTEROID_MIN_RADIUS :
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            first_vector = self.velocity.rotate(angle)

            second_vector = self.velocity.rotate(360 - angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_1.velocity = first_vector * 1.2
            asteroid_2.velocity = second_vector * 1.2
