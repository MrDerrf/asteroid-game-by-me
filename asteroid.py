from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen):
        center = self.position
        pygame.draw.circle(screen,"white",center,self.radius, LINE_WIDTH)
    def update(self, dt: float):
        self.position = self.position + (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_between = random.uniform(20.0, 50.0)
        positive_direction = self.velocity.rotate(split_between)
        negative_direction = self.velocity.rotate(-split_between)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = positive_direction * 1.2
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid.velocity = negative_direction * 1.2
