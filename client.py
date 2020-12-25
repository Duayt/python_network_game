from dataclasses import dataclass, field

import pygame
from pygame.locals import (K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, KEYDOWN,
                           QUIT)
from network import Network


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
    rect: pygame.Rect = field(init=False)

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


def read_pos(txt):
    txt = txt.split(",")
    return int(txt[0]), int(txt[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redraw_window(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    running = True
    n = Network()
    start_pos = read_pos(n.get_pos())
    p = Player(x=start_pos[0], y=start_pos[1], width=100,
               height=100, color=(0, 255, 0))

    p2 = Player(x=0, y=0, width=100,
                height=100, color=(0, 0, 255))
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        p2_pos = read_pos(n.send(make_pos((p.rect.x, p.rect.y))))
        p2.rect.x = p2_pos[0]
        p2.rect.y = p2_pos[1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redraw_window(win, p, p2)


if __name__ == "__main__":
    main()
