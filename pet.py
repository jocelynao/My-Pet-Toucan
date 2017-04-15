import pygame
from spriteSheet import *

class pet(pygame.sprite.Sprite):

	def __init__(self, x, y):
		pygame.init()
		super(pet, self).__init__()
		self.x = 500
		self.y = 350

		self.walkLeft = []
		self.walkRight = []
		self.rightEat = []
		self.leftEat = []

		self.direction = "L"

		self.toucanSheet = spriteSheet("Toucan.png")

		xCoord = 0
		for i in range(2):
			image = self.loadLeft(xCoord)
			self.walkLeft.append(image)
			xCoord = xCoord + 50

		for pic in self.walkLeft:
			pic = pygame.transform.flip(pic, True, False)
			self.walkRight.append(pic)

		self.loadLeftEat()

		for pic in self.leftEat:
			pic = pygame.transform.flip(pic, True, False)
			self.rightEat.append(pic)

		self.index = 0
		self.image = self.walkLeft[0]
		self.rect = ((self.x, self.y))
		# shaymin = spriteSheet.spriteSheet("shayminLeft.jpg")

	def getRect(self):
		return self.rect

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getDirect(self):
		return self.direction

	def getLeftEat(self):
		return self.leftEat

	def getRightEat(self):
		return self.rightEat

	def getImage(self):
		return self.image

	# def loadEat(self):
	# 	eatImage = self.toucanSheet.getImage(0, 325, 45, 50)

	def loadHappy(self):
		happyImage = self.toucanSheet.getImage(105, 0, 50, 50)
		happyImage = pygame.transform.scale(happyImage, (80, 80))
		if self.direction == "R":
			happyImage = pygame.transform.flip(happyImage, True, False)
		return happyImage

	def loadLove(self):
		heartImage = self.toucanSheet.getImage(0, 510, 50, 50)
		heartImage = pygame.transform.scale(heartImage, (75, 75))
		if self.direction == "R":
			heartImage = pygame.transform.flip(heartImage, True, False)
		return heartImage

	def loadLeft(self, xCoord):
		image = self.toucanSheet.getImage(xCoord, 150, 55, 55)
		image = pygame.transform.scale(image, (90, 90))
		return image

	def loadLeftEat(self):
		eatImage = self.toucanSheet.getImage(0, 380, 50, 50)
		eatImage = pygame.transform.scale(eatImage, (80, 80))
		self.leftEat.append(eatImage)
		eatImage = self.toucanSheet.getImage(55, 380, 50, 50)
		eatImage = pygame.transform.scale(eatImage, (80, 80))
		self.leftEat.append(eatImage)
		eatImage = self.toucanSheet.getImage(105, 380, 50, 50)
		eatImage = pygame.transform.scale(eatImage, (80, 80))
		self.leftEat.append(eatImage)
		eatImage = self.toucanSheet.getImage(160, 380, 50, 50)
		eatImage = pygame.transform.scale(eatImage, (80, 80))
		self.leftEat.append(eatImage)
		eatImage = self.toucanSheet.getImage(210, 380, 50, 50)
		eatImage = pygame.transform.scale(eatImage, (80, 80))
		self.leftEat.append(eatImage)
		eatImage = self.toucanSheet.getImage(260, 380, 50, 50)
		eatImage = pygame.transform.scale(eatImage, (80, 80))
		self.leftEat.append(eatImage)
		for i in range(4):
			self.leftEat.append(self.loadLove())

	def update(self):
		self.rect = ((self.x, self.y))
		if (self.x == 100):
			self.direction = "R"
		if (self.x == 500):
			self.direction = "L"

		if self.direction == "L":
			if self.index >= len(self.walkLeft):
				self.index = 0
			self.image = self.walkLeft[self.index]
			self.index = self.index + 1
			self.x = self.x - 10
			
		else:
			if self.index >= len(self.walkRight):
				self.index = 0
			self.image = self.walkRight[self.index]
			self.index = self.index + 1
			self.x = self.x + 10
			



		# if self.index >= len(self.walkLeft):
		# 	self.index = 0
		# # print(self.index)
		# # print(len(self.walkRight))
		# if self.index == 0:
		# 	self.x = 500
		# self.image = self.walkLeft[self.index]
		# self.index = self.index + 1
		# self.rect = ((self.x, self.y))
		# self.x = 100


