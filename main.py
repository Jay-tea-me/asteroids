import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


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
    asteroid_group = pygame.sprite.Group()
    Asteroid.containers = (asteroid_group, updateable_group, drawable_group)
    Player.containers = (updateable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
    AsteroidField.containers = (updateable_group)
    asteroidField = AsteroidField()
    shot_group = pygame.sprite.Group()
    Shot.containers = (shot_group, updateable_group, drawable_group)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updateable_group:
            obj.update(dt)
        for a in asteroid_group:
            if a.is_colliding(player):
                print("Game Over")
                sys.exit()


        # render
        screen.fill("black")
        for obj in drawable_group:
            obj.draw(screen)
        # player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ =='__main__':
    main()
