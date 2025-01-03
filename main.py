import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (shots, updateable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for item in updateable:
            item.update(dt)

        for asteroid in asteroids:
           if CircleShape.collision_check(asteroid, player):
               print("Game over!")
               sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if CircleShape.collision_check(asteroid, shot):
                    asteroid.split()
                    shot.kill()

        screen.fill((1,1,1))

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()

        player.draw(screen)

        dt = game_clock.tick(60) / 1000

        
        

if __name__ == "__main__":
    main()
