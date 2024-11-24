import sys
from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    
    player = Player(x,y)
    asteroidfield = AsteroidField()
    #asteroid = Asteroid(500,500,100)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = time.tick(60)/1000
        screen.fill((0,0,0))

        #asteroid.draw(screen)
        
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        
        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if a.colliding(player):
                print("Game over!")
                sys.exit()


if __name__ == "__main__":
    main()