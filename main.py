import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from posix import kill

def main():
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable,drawable)


    asteroid_field = AsteroidField(asteroids)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,shots)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.has_collided(shot):
                    asteroid.split()
                    shot.kill()
            if player.has_collided(asteroid):
                print("Game Over!")
                return
        # Draw all sprites individually
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__=="__main__":
    main()
