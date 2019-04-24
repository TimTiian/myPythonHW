import pygame
import random


# Food class, used to improve the tank's ability
class Food(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		# Destroy all current enemies
		self.food_boom = './images/food/food_boom.png'
		# All current enemies remain stationary for a period of time
		self.food_clock = './images/food/food_clock.png'
		# Makes tank bullets shred steel plates
		self.food_gun = './images/food/food_gun.png'
		# To turn the walls of the base camp into steel plates
		self.food_iron = './images/food/food_gun.png'
		# The tank gets a shield for a period of time
		self.food_protect = './images/food/food_protect.png'
		# Tanks to upgrade
		self.food_star = './images/food/food_star.png'
		# Tank health +1
		self.food_tank = './images/food/food_tank.png'
		# All the food
		self.foods = [self.food_boom, self.food_clock, self.food_gun, self.food_iron, self.food_protect, self.food_star, self.food_tank]
		self.kind = None
		self.food = None
		self.rect = None
		# whether exist
		self.being = False
		# There is time
		self.time = 1000
	# Produce food
	def generate(self):
		self.kind = random.randint(0, 6)
		self.food = pygame.image.load(self.foods[self.kind]).convert_alpha()
		self.rect = self.food.get_rect()
		self.rect.left, self.rect.top = random.randint(100, 500), random.randint(100, 500)
		self.being = True