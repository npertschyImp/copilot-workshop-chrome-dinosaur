# dinosaur.py
import pygame
from constants import HEIGHT, BLACK, GRAVITY

class Dinosaur:
    def __init__(self):
        self.surface = pygame.Surface((50, 50))
        self.surface.fill(BLACK)
        self.rect = self.surface.get_rect(midbottom=(80, HEIGHT - 30))
        self.velocity = 0

    def jump(self):
        self.velocity = -15

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity
        if self.rect.bottom >= HEIGHT - 30:
            self.rect.bottom = HEIGHT - 30

    def draw(self, screen):
        screen.blit(self.surface, self.rect)

    def reset(self):
        self.rect.midbottom = (80, HEIGHT - 30)
        self.velocity = 0