import pygame
from dataclasses import dataclass, field
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
WIDTH, HEIGHT = 500, 500

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Client')

client_number = 0


@dataclass
class Player(pygame.sprite.Sprite):
    x: int
    y: int
    width: int
    height: int
    color: (int, int, int)
    vel: int = 3
    surf: pygame.Surface = field(init=False)
    rect: (int, int, int, int) = field(init=False)

    def __post_init__(self):
        self.surf = pygame.Surface((self.width, self.height))
        self.set_rect()

    def set_rect(self):
        self.rect = self.surf.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def draw(self, win: pygame.Surface):
        """Drawing player on window (pygame.Surface)

        Args:
            win (pygame.Surface): pygame window surface
        """
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
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
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT


def redraw_window(win, player):
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()


def main():
    running = True
    p = Player(x=WIDTH//2, y=HEIGHT//2, width=100,
               height=100, color=(0, 255, 0))
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redraw_window(win, p)


if __name__ == "__main__":
    main()
