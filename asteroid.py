from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return

        rand_angle = random.uniform(20, 50)

        print(self.velocity)
        vec1 = self.velocity.rotate(rand_angle)
        vec2 = self.velocity.rotate(-rand_angle)

        rad_down = self.radius - ASTEROID_MIN_RADIUS

        x_ax = self.position[0]
        y_ax = self.position[1]

        aster1 = Asteroid(x_ax, y_ax, rad_down)
        aster2 = Asteroid(x_ax, y_ax, rad_down)

        aster1.velocity = vec1
        aster2.velocity = vec2
