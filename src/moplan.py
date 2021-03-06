"""
Simple motion planning simulation
"""
import pygame
from pygame.locals import *
import numpy as np
from numpy import *

class World():
	
	def __init__(self):
		pygame.init()
		pygame.display.init()
		self.screen = pygame.display.set_mode((800,800),0,32)

		# Fill background
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((250, 250, 250))
	
	def draw_robot(self, robot):
		pygame.draw.circle(self.screen, robot.color, (robot.x,robot.y), robot.radius)


class Robot():
	x = 0
	y = 0

	radius = 50
	color = (100,100,100)

	def __init__(self, start_loc):
		(self.x, self.y) = start_loc
	
def main():
	w = World()

	# Blit everything to the screen
	w.screen.blit(w.background, (0, 0))
	pygame.display.flip()

	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

		r = Robot((100,100))
		w.draw_robot(r)

		#w.screen.blit(w.background, (0, 0))
		#pygame.display.update()

		pygame.display.flip()

if __name__ == '__main__':
	main()
