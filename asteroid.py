import random
import pygame
from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self,x,y,radius,asteroids):
        super().__init__(x,y,radius)
        self.asteroids = asteroids

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),(self.position.x,self.position.y),self.radius,2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20.0, 50.0)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_new_1 = Asteroid(self.position.x, self.position.y, new_radius,self.asteroids)
        asteroid_new_2 = Asteroid(self.position.x, self.position.y, new_radius,self.asteroids)
        asteroid_new_1.velocity = v1 * 1.2
        asteroid_new_2.velocity = v2 * 1.2
        self.asteroids.add(asteroid_new_1)
        self.asteroids.add(asteroid_new_2)
