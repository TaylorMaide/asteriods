import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *

def main():

	pygame.init()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (shots, updatable)

	asteroid_field = AsteroidField()

	my_clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		updatable.update(dt)
		for asteroid in asteroids:
			if player.check_for_collisions(asteroid):
				print("Game Over!")
				sys.exit()
		for a in asteroids:
			for s in shots:
				if a.check_for_collisions(s):
					s.kill()
					a.split()
		screen.fill((0, 0, 0))
		for shot in shots:
			shot.draw(screen)
		for sprite in drawable:
			sprite.draw(screen)
		pygame.display.flip()
		dt = my_clock.tick(60) / 1000 

if __name__ == "__main__":
	main()

