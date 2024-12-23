import sys
import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #GUI screen
    clock = pygame.time.Clock()
    dt = 0 #delta
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers =(asteroids, updatable, drawable)#every instance is automatically added to the groups
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    

    while True: #game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()    

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()        
       
        #player.update(dt)    
        pygame.Surface.fill(screen, (0,0,0))#fill screen surface with black color , or screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        #player.draw(screen)
        pygame.display.flip() #refresh screen

        dt = clock.tick(60)/1000 #limit framerate to 60



if __name__ == "__main__":
    main()    