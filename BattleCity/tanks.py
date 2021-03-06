import pygame
import random
from bullet import Bullet


# Our tank class
class myTank(pygame.sprite.Sprite):
	def __init__(self, player):
		pygame.sprite.Sprite.__init__(self)
		# Player number (1/2)
		self.player = player
		# Different players use different tanks (different levels correspond to different pictures)
		if player == 1:
			self.tanks = ['./images/myTank/tank_T1_0.png', './images/myTank/tank_T1_1.png', './images/myTank/tank_T1_2.png']
		elif player == 2:
			self.tanks = ['./images/myTank/tank_T2_0.png', './images/myTank/tank_T2_1.png', './images/myTank/tank_T2_2.png']
		else:
			raise ValueError('myTank class -> player value error.')
		# Tank level (initial 0)
		self.level = 0
		# Load (two tank for wheel effects)
		self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
		self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
		self.rect = self.tank_0.get_rect()
		# shielding
		self.protected_mask = pygame.image.load('./images/others/protect.png').convert_alpha()
		self.protected_mask1 = self.protected_mask.subsurface((0, 0), (48, 48))
		self.protected_mask2 = self.protected_mask.subsurface((48, 0), (48, 48))
		# Direction of the tank
		self.direction_x, self.direction_y = 0, -1
		# Different players are born in different locations
		if player == 1:
			self.rect.left, self.rect.top = 3 + 24 * 8, 3 + 24 * 24
		elif player == 2:
			self.rect.left, self.rect.top = 3 + 24 * 16, 3 + 24 * 24
		else:
			raise ValueError('myTank class -> player value error.')
		# Tanks speed
		self.speed = 3
		# Whether to live
		self.being = True
		# There are a few lives
		self.life = 3
		# Whether in a protected state
		self.protected = False
		# bullet
		self.bullet = Bullet()
	# shoot
	def shoot(self):
		self.bullet.being = True
		self.bullet.turn(self.direction_x, self.direction_y)
		if self.direction_x == 0 and self.direction_y == -1:
			self.bullet.rect.left = self.rect.left + 20
			self.bullet.rect.bottom = self.rect.top - 1
		elif self.direction_x == 0 and self.direction_y == 1:
			self.bullet.rect.left = self.rect.left + 20
			self.bullet.rect.top = self.rect.bottom + 1
		elif self.direction_x == -1 and self.direction_y == 0:
			self.bullet.rect.right = self.rect.left - 1
			self.bullet.rect.top = self.rect.top + 20
		elif self.direction_x == 1 and self.direction_y == 0:
			self.bullet.rect.left = self.rect.right + 1
			self.bullet.rect.top = self.rect.top + 20
		else:
			raise ValueError('myTank class -> direction value error.')
		if self.level == 0:
			self.bullet.speed = 8
			self.bullet.stronger = False
		elif self.level == 1:
			self.bullet.speed = 12
			self.bullet.stronger = False
		elif self.level == 2:
			self.bullet.speed = 12
			self.bullet.stronger = True
		elif self.level == 3:
			self.bullet.speed = 16
			self.bullet.stronger = True
		else:
			raise ValueError('myTank class -> level value error.')
	# upgrade level
	def up_level(self):
		if self.level < 3:
			self.level += 1
		try:
			self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
		except:
			self.tank = pygame.image.load(self.tanks[-1]).convert_alpha()
	# reduce level
	def down_level(self):
		if self.level > 0:
			self.level -= 1
		self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
	# up
	def move_up(self, tankGroup, brickGroup, ironGroup, myhome):
		self.direction_x, self.direction_y = 0, -1
		# Move before you judge
		self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
		self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
		# Can I move it
		is_move = True
		# The top of the map
		if self.rect.top < 3:
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# Hit a stone/steel wall
		if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
			pygame.sprite.spritecollide(self, ironGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# Hit other tanks
		if pygame.sprite.spritecollide(self, tankGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# base
		if pygame.sprite.collide_rect(self, myhome):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		return is_move
	# move down
	def move_down(self, tankGroup, brickGroup, ironGroup, myhome):
		self.direction_x, self.direction_y = 0, 1
		# Move before you judge
		self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
		self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
		# Can I move it
		is_move = True
		# The bottom of the map
		if self.rect.bottom > 630 - 3:
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# Hit a stone/steel wall
		if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
			pygame.sprite.spritecollide(self, ironGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# Hit other tanks
		if pygame.sprite.spritecollide(self, tankGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# base
		if pygame.sprite.collide_rect(self, myhome):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		return is_move
	# move left
	def move_left(self, tankGroup, brickGroup, ironGroup, myhome):
		self.direction_x, self.direction_y = -1, 0
		# Move before you judge
		self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
		self.tank_0 = self.tank.subsurface((0, 96), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 96), (48, 48))
		# Can I move it
		is_move = True
		# the left of the map
		if self.rect.left < 3:
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# Hit a stone/steel wall
		if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
			pygame.sprite.spritecollide(self, ironGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# Hit other tanks
		if pygame.sprite.spritecollide(self, tankGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False		
		# base
		if pygame.sprite.collide_rect(self, myhome):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		return is_move
	# move right
	def move_right(self, tankGroup, brickGroup, ironGroup, myhome):
		self.direction_x, self.direction_y = 1, 0
		# move before you judge
		self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
		self.tank_0 = self.tank.subsurface((0, 144), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 144), (48, 48))
		# Can I move it
		is_move = True
		# the right of the map
		if self.rect.right > 630 - 3:
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		#  Hit a stone/steel wall
		if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
			pygame.sprite.spritecollide(self, ironGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# Hit other tanks
		if pygame.sprite.spritecollide(self, tankGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		# base
		if pygame.sprite.collide_rect(self, myhome):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			is_move = False
		return is_move
	# After the death of a reset
	def reset(self):
		self.level = 0
		self.protected = False
		self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
		self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
		self.rect = self.tank_0.get_rect()
		self.direction_x, self.direction_y = 0, -1
		if self.player == 1:
			self.rect.left, self.rect.top = 3 + 24 * 8, 3 + 24 * 24
		elif self.player == 2:
			self.rect.left, self.rect.top = 3 + 24 * 16, 3 + 24 * 24
		else:
			raise ValueError('myTank class -> player value error.')
		self.speed = 3


# Enemy tanks class
class enemyTank(pygame.sprite.Sprite):
	def __init__(self, x=None, kind=None, is_red=None):
		pygame.sprite.Sprite.__init__(self)
		# Used to play birth effects on newly generated tanks
		self.born = True
		self.times = 90
		# Type number of tank
		if kind is None:
			self.kind = random.randint(0, 3)
		else:
			self.kind = kind
		# all the tanks
		self.tanks1 = ['./images/enemyTank/enemy_1_0.png', './images/enemyTank/enemy_1_1.png', './images/enemyTank/enemy_1_2.png', './images/enemyTank/enemy_1_3.png']
		self.tanks2 = ['./images/enemyTank/enemy_2_0.png', './images/enemyTank/enemy_2_1.png', './images/enemyTank/enemy_2_2.png', './images/enemyTank/enemy_2_3.png']
		self.tanks3 = ['./images/enemyTank/enemy_3_0.png', './images/enemyTank/enemy_3_1.png', './images/enemyTank/enemy_3_2.png', './images/enemyTank/enemy_3_3.png']
		self.tanks4 = ['./images/enemyTank/enemy_4_0.png', './images/enemyTank/enemy_4_1.png', './images/enemyTank/enemy_4_2.png', './images/enemyTank/enemy_4_3.png']
		self.tanks = [self.tanks1, self.tanks2, self.tanks3, self.tanks4]
		# Do you carry food (red tank carries food)
		if is_red is None:
			self.is_red = random.choice((True, False, False, False, False))
		else:
			self.is_red = is_red
		# The same kind of tank has different colors, the red tank has a little more health than the same kind of tank
		if self.is_red:
			self.color = 3
		else:
			self.color = random.randint(0, 2)
		# HP
		self.blood = self.color
		# Load (two tank for wheel effects)
		self.tank = pygame.image.load(self.tanks[self.kind][self.color]).convert_alpha()
		self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
		self.rect = self.tank_0.get_rect()
		# Tank location
		if x is None:
			self.x = random.randint(0, 2)
		else:
			self.x = x
		self.rect.left, self.rect.top = 3 + self.x * 12 * 24, 3
		# Whether the tank can move
		self.can_move = True
		# speed of tank
		self.speed = max(3 - self.kind, 1)
		# direction
		self.direction_x, self.direction_y = 0, 1
		# Whether to live
		self.being = True
		# bullet
		self.bullet = Bullet()
	# shoot
	def shoot(self):
		self.bullet.being = True
		self.bullet.turn(self.direction_x, self.direction_y)
		if self.direction_x == 0 and self.direction_y == -1:
			self.bullet.rect.left = self.rect.left + 20
			self.bullet.rect.bottom = self.rect.top - 1
		elif self.direction_x == 0 and self.direction_y == 1:
			self.bullet.rect.left = self.rect.left + 20
			self.bullet.rect.top = self.rect.bottom + 1
		elif self.direction_x == -1 and self.direction_y == 0:
			self.bullet.rect.right = self.rect.left - 1
			self.bullet.rect.top = self.rect.top + 20
		elif self.direction_x == 1 and self.direction_y == 0:
			self.bullet.rect.left = self.rect.right + 1
			self.bullet.rect.top = self.rect.top + 20
		else:
			raise ValueError('enemyTank class -> direction value error.')
	# Moving randomly
	def move(self, tankGroup, brickGroup, ironGroup, myhome):
		self.rect = self.rect.move(self.speed*self.direction_x, self.speed*self.direction_y)
		is_move = True
		if self.direction_x == 0 and self.direction_y == -1:
			self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
			self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
			if self.rect.top < 3:
				self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
				self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
				is_move = False
		elif self.direction_x == 0 and self.direction_y == 1:
			self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
			self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
			if self.rect.bottom > 630 - 3:
				self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
				self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
				is_move = False
		elif self.direction_x == -1 and self.direction_y == 0:
			self.tank_0 = self.tank.subsurface((0, 96), (48, 48))
			self.tank_1 = self.tank.subsurface((48, 96), (48, 48))
			if self.rect.left < 3:
				self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
				self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
				is_move = False
		elif self.direction_x == 1 and self.direction_y == 0:
			self.tank_0 = self.tank.subsurface((0, 144), (48, 48))
			self.tank_1 = self.tank.subsurface((48, 144), (48, 48))
			if self.rect.right > 630 - 3:
				self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
				self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
				is_move = False
		else:
			raise ValueError('enemyTank class -> direction value error.')
		if pygame.sprite.spritecollide(self, brickGroup, False, None) \
			or pygame.sprite.spritecollide(self, ironGroup, False, None) \
			or pygame.sprite.spritecollide(self, tankGroup, False, None):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
			is_move = False
		if pygame.sprite.collide_rect(self, myhome):
			self.rect = self.rect.move(self.speed*-self.direction_x, self.speed*-self.direction_y)
			self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
			is_move = False
		return is_move
	# Reload the tank
	def reload(self):
		self.tank = pygame.image.load(self.tanks[self.kind][self.color]).convert_alpha()
		self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
		self.tank_1 = self.tank.subsurface((48, 48), (48, 48))