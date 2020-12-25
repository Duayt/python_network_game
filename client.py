
from player import Player
from network import Network
import pygame


WIDTH, HEIGHT = 500, 500

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Client')

client_number = 0


def redraw_window(win, sprite_group, p2):
    win.fill((255, 255, 255))
    for sprite in sprite_group:
        sprite.draw(win)
    p2.draw(win)
    pygame.display.update()


def main():
    running = True
    n = Network()
    p = n.get_p()
    clock = pygame.time.Clock()
    all_players = pygame.sprite.Group()
    all_players.add(p)

    while running:
        clock.tick(60)
        p2 = n.send(p)

        # all_players.add(p2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        p.move(WIDTH, HEIGHT)
        redraw_window(win, all_players, p2)


if __name__ == "__main__":
    main()
