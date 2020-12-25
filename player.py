import pygame
from pygame.locals import (K_DOWN, K_LEFT, K_RIGHT, K_UP)


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int,
                 y: int,
                 width: int,
                 height: int,
                 color: (int, int, int),
                 vel: int = 3):
        super(Player, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = vel
        # self.surf = pygame.Surface((self.width, self.height))

        self.set_rect()

    def set_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surf):
        """Drawing player on window (pygame.Surface)

        Args:
            win (pygame.Surface): pygame window surface
        """
        pygame.draw.rect(surf, self.color, self.rect)

    def move(self, max_width, max_height):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            self.rect.move_ip(-self.vel, 0)
        if keys[K_RIGHT]:
            self.rect.move_ip(self.vel, 0)
        if keys[K_UP]:
            self.rect.move_ip(0, -self.vel)
        if keys[K_DOWN]:
            self.rect.move_ip(0, self.vel)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > max_width:
            self.rect.right = max_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= max_height:
            self.rect.bottom = max_height
