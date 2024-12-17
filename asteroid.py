import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            launch_angle = random.uniform(20, 50)
            positive_vector = self.velocity.rotate(launch_angle)
            negative_vector = self.velocity.rotate(-launch_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child_1, child_2 = Asteroid(self.position.x, self.position.y, new_radius), Asteroid(self.position.x, self.position.y, new_radius)
            child_1.velocity = positive_vector * 1.2
            child_2.velocity = negative_vector * 1.2


