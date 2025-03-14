import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    hellfire = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (updatable, drawable, hellfire)
    AsteroidField.containers = (updatable)


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for canva in drawable:
            canva.draw(screen)
        for render in updatable:
            render.update(dt)
        for asteroid in asteroids:
            if(player.colisions(asteroid)):
                print("Game over!")
                sys.exit()
            for bullet in hellfire:
                if(bullet.colisions(asteroid)):
                    bullet.kill()
                    asteroid.kill()
        pygame.display.flip()
        dt =  clock.tick(60) / 1000




if __name__ == "__main__":
    main()
