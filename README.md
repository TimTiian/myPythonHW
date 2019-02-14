# Introduction
This is my EE551 python individual project 

## Author ： Chenliang Tian

## Purposals
  For my project, I intend to use pygame module to design a 2D video game, it imitates “Battle City”, which is a multi-directional 
shooter video game for the Family Computer produced and published in 1985 by Namco.

  For this game, I designed two game modes, single player and double player, in which the player controls two tanks to attack the 
enemy tanks. Victory is conditional on the destruction of all enemy tanks, defeat is when our tank life is 0 or the base is broken by 
the enemy. At the same time, I designed the seven different class to store the different elements of the game, including myTank, enemyTank, bullet, food, home, scene, home, every kinds of elements in the meaning of each are not identical, myTank there are three different levels of tanks, there are four enemyTank, bullet set four directions of bullets, the food in the class is to provide the function of 7 different, boom can destroy all enemies within the screen, it can be the enemy still, gun can make tanks through steel plate, Iron can turn the base wall into a steel plate, protect can make the tank not afraid of enemy bullets, start can upgrade the tank, tank icon can make the tank life +1.

  The first step is to define the Sprite class. I don't need to instantiate it, just inherit it, and then write different classes
according to my needs. For example, we defined some attributes in the tank class, such as speed, rank of tank, whether in the protected 
state and so on. Once we have the status, we need to define the abilities of the tank, shooting, movement, level upgrades and downgrades, 
and post-mortem reset; Enemy tanks are set to move randomly and cannot be revived after death. The bullet class sets the speed, strength 
properties, and direction of movement. Base camp is divided into two states: normal and destroyed; Map barriers include brick walls, steel walls, forests, rivers and ice. The second step is to design the game map, the game background is black, and then pile some obstacles 
defined in step 1 on it to complete the map design. Among them, the steel wall can not be broken by ordinary bullets, the brick wall can 
be broken by arbitrary bullets, in addition to the wall, the tank can pass through any obstacle. The third step is to realize the main 
loop of the game. The code of the main loop is long, but the logic is clear. First, the game start interface is displayed. Players can 
enter the game after selecting the game mode on this interface. In the game, a series of collision detection is required and a series of 
events generated by the collision are triggered, and all existing objects are drawn. Finally, if the game fails, the game failure 
interface will be displayed; if the game is completed, the game success interface will be displayed.

  Meanwhile,  I think that the game also scales well, and if possible, features can be added to the game in the future, such as 
speeding up when the tank passes through the ice area, slowing down when it passes through the swamp, and adding maps.
