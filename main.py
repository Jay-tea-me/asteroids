import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updateable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updateable_group:
            obj.update(dt)


        # render
        screen.fill("black")
        for obj in drawable_group:
            obj.draw(screen)
        # player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ =='__main__':
    main()
