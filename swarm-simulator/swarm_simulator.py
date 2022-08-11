import pygame
from math import sin, radians, degrees, copysign
from pygame.math import Vector2

print("Swarm Bots Simulator")

# Initialise pygame
pygame.init()

MAX_X = 900
MAX_Y = 600
# create the screen
icon = pygame.image.load("bots/robot_0.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((MAX_X,MAX_Y));
pygame.display.set_caption("Swarm Robots Simulator")

class Bot:
    def __init__(self, image, x , y):
        self.image = image
        self.position = Vector2(x, y)
    def update(self, x, y):
    	self.position = Vector2(x,y)

robot_0 = Bot("bots/robot_0.png", 250, 510)
robot_1 = Bot("bots/robot_1.png", 300, 510)
robot_2 = Bot("bots/robot_2.png", 350, 510)
robot_3 = Bot("bots/robot_3.png", 400, 510)
robot_4 = Bot("bots/robot_4.png", 450, 510)
robot_5 = Bot("bots/robot_5.png", 500, 510)
robot_6 = Bot("bots/robot_6.png", 550, 510)
robot_7 = Bot("bots/robot_7.png", 600, 510)

bots = [robot_0,robot_1,robot_2,robot_3,robot_4,robot_5,robot_6,robot_7]


def put(robot):
	image = pygame.image.load(robot.image)
	screen.blit(image,robot.position)

# Game Loop
running = True
global i
i = 0

pygame.font.init()

def maketext():
	myfont = pygame.font.SysFont('Comic Sans MS', 30)
	textsurface = myfont.render('Bot Control: {}'.format(i), False, (255, 255, 255))
	return textsurface

while running:
	for event in pygame.event.get():
		# print(event)
		# print(pygame.QUIT)
		if event.type == pygame.QUIT:
			running == False
	# RGB
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]:
		y = bots[i].position[1]
		y -=1
		bots[i].update(bots[i].position[0],y)
	elif pressed[pygame.K_DOWN]:
		y = bots[i].position[1]
		y +=0.1
		bots[i].update(bots[i].position[0],y)
	elif pressed[pygame.K_RIGHT]:
		x = bots[i].position[0]
		x +=0.1
		bots[i].update(x, bots[i].position[1])
	elif pressed[pygame.K_LEFT]:
		x = bots[i].position[0]
		x -=0.1
		bots[i].update(x, bots[i].position[1])
	else:
		# print("else")
		pass

	if bots[i].position[0] <=0:
		bots[i].position[0] = 0
	elif bots[i].position[0] >= MAX_X:
		bots[i].position[0] = MAX_X
	elif bots[i].position[1] <=0:
		bots[i].position[1] = 0
	elif bots[i].position[1] >= MAX_Y:
		bots[i].position[1] = MAX_Y
	else:
		pass


	if pressed[pygame.K_0]:
		# global i
		i = 0
	if pressed[pygame.K_1]:
		# global i
		i = 1
	if pressed[pygame.K_2]:
		# global i
		i = 2
	if pressed[pygame.K_3]:
		# global i
		i = 3
	if pressed[pygame.K_4]:
		# global i
		i = 4
	if pressed[pygame.K_5]:
		# global i
		i = 5
	if pressed[pygame.K_6]:
		# global i
		i = 6
	if pressed[pygame.K_7]:
		# global i
		i = 7


	screen.fill((10,10,10))
	screen.blit(maketext(),(0,0))
	Color_line=(255,0,0)
	# pygame.draw.line(screen, Color_line, (60, 80), (130, 100))
	pygame.draw.line(screen, Color_line, (100, 80), (800, 80))
	pygame.draw.line(screen, Color_line, (100, 500), (800, 500))
	put(robot_0)
	put(robot_1)
	put(robot_2)
	put(robot_3)
	put(robot_4)
	put(robot_5)
	put(robot_6)
	put(robot_7)
	pygame.display.update()