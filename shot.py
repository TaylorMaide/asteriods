import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
        def __init__(self, position):
            super().__init__(position.x, position.y, SHOT_RADIUS)
            self.position = position
            self.radius = SHOT_RADIUS

        def update(self, dt):
            self.position += self.velocity * dt

        def draw(self, screen):
            pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)