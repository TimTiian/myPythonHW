import pygame


# Base class
class Home(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.homes = ['./images/home/home1.png', './images/home/home2.png', './images/home/home_destroyed.png']
		self.home = pygame.image.load(self.homes[0])
		self.rect = self.home.get_rect()
		self.rect.left, self.rect.top = (3 + 12 * 24, 3 + 24 * 24)
		self.alive = True
	# Base camp is set to destroy
	def set_dead(self):
		self.home = pygame.image.load(self.homes[-1])
		self.alive = False