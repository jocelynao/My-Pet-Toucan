
import pygame
from pet import *
from pygame import *
import os.path
import sys
from spriteSheet import *
import WelcomeScreen
import classUno

class mainScreen:

	def __init__(self):
		pygame.init()
		self.__screenSize = (640, 480)
		# self.__screenSize = (800, 500)
		self.__screen = pygame.display.set_mode(self.__screenSize)
		self.__font = pygame.font.SysFont("Helvetica", 18, bold = False, italic = False)

		self.__clock = pygame.time.Clock()
		self.__completed = False
		self.__font = pygame.font.SysFont("Arial", 20)
		pygame.display.update()

		# self.__hunger = pygame.draw.rect(self.__screen,
		 # (255, 255, 0), (30, 30, 90, 90))

		self.__brushPos = None
		self.__bowlPos = None
		self.__gamePos = None
		self.__unoBoxPos = None

		self.__hungerCount = 0
		self.__cleanCount = 0
		self.__funCount = 0

		self.__hungerLevel = 8
		self.__cleanLevel = 8
		self.__funLevel = 9

		self.__toucan = pet(200, 200)
		self.__toucanGroup = pygame.sprite.Group(self.__toucan)

	def loadMusic(self):
		try:
			pygame.mixer.music.load(os.path.join("Sound", "background.ogg"))
			pygame.mixer.music.set_volume(.5)
			pygame.mixer.music.play(-1)
			homeScreen = pygame.image.load(os.path.join('Images', 'livingRoom.jpg'))
			homeScreen = pygame.transform.scale(homeScreen, (640, 480))
			self.__screen.blit(homeScreen, (0, 0))
		except pygame.error as err:
			print(err)


	def makeBackground(self):
		try:
			homeScreen = pygame.image.load(os.path.join('Images', 'livingRoom.jpg'))
			homeScreen = pygame.transform.scale(homeScreen, (640, 480))
			self.__screen.blit(homeScreen, (0, 0))
		except pygame.error as err:
			print(err)

	
	def loadBrush(self):
		brush = pygame.image.load(os.path.join("Images", "hairbrush.png"))
		brush = pygame.transform.scale(brush, (40, 60))
		brush = pygame.transform.rotate(brush, 110)
		brush = pygame.transform.flip(brush, True, False)
		transColor = brush.get_at((0, 0))
		brush.set_colorkey((transColor))
		self.__brushPos = self.__screen.blit(brush, (20, 94))

	def loadItems(self):
		bowl = pygame.image.load(os.path.join("Images", "fruitBowl.jpg"))
		bowl = pygame.transform.scale(bowl, (70, 50))
		transColor = bowl.get_at((0, 0))
		bowl.set_colorkey((transColor))
		self.__bowlPos = self.__screen.blit(bowl, (340, 280))

		gameboy = pygame.image.load(os.path.join("Images", "gameboy.png"))
		gameboy = pygame.transform.scale(gameboy, (40, 20))
		transColor = gameboy.get_at((0, 0))
		gameboy.set_colorkey((transColor))
		self.__gameboyPos = self.__screen.blit(gameboy, (400, 225))

		unoBox = pygame.image.load(os.path.join("Images", "unoBox.jpg"))
		unoBox = pygame.transform.scale(unoBox, (20, 30))
		transColor = gameboy.get_at((0, 0))
		unoBox.set_colorkey((255, 255, 255))
		self.__unoBoxPos = self.__screen.blit(unoBox, (440, 210))

		# self.__unoBoxPos = self.__screen.blit(unoBox, (85, 105))

	def loadBars(self):
		whiteCleanLevel = (10 - self.__cleanLevel) * 18
		blueCleanLevel = 180 - whiteCleanLevel
		self.__cleanWhite = pygame.draw.rect(self.__screen, (255, 255, 255), 
			(400, 40, 180, 20))
		self.__cleanBlue = pygame.draw.rect(self.__screen, (176, 224, 230), 
			(400, 40, blueCleanLevel, 20))
		self.__cleanBorder = pygame.draw.rect(self.__screen, (0, 0, 0), 
			(400, 40, 180, 20), 3)
		self.__screen.blit(self.__font.render("Hygiene", 1, (0, 0, 0)),
			(335, 35))

		whiteHungerLevel = (10 - self.__hungerLevel) * 18
		blueHungerLevel = 180 - whiteHungerLevel
		self.__hungerWhite = pygame.draw.rect(self.__screen, (255, 255, 255), 
			(400, 10, 180, 20))
		self.__hungerBlue = pygame.draw.rect(self.__screen, (176, 224, 230), 
			(400, 10, blueHungerLevel, 20))
		self.__hungerBorder = pygame.draw.rect(self.__screen, (0, 0, 0), 
			(400, 10, 180, 20), 3)
		self.__screen.blit(self.__font.render("Hunger", 1, (0, 0, 0)),
			(340, 5))

		whiteFunLevel = (10 - self.__funLevel) * 18
		blueFunLevel = 180 - whiteFunLevel
		self.__funWhite = pygame.draw.rect(self.__screen, (255, 255, 255), 
			(400, 70, 180, 20))
		self.__funBlue = pygame.draw.rect(self.__screen, (176, 224, 230), 
			(400, 70, blueFunLevel, 20))
		self.__funBorder = pygame.draw.rect(self.__screen, (0, 0, 0), 
			(400, 70, 180, 20), 3)
		self.__screen.blit(self.__font.render("Fun", 1, (0, 0, 0)),
			(365, 68))

	def loadEverything(self):
		self.makeBackground()
		self.loadBrush()
		self.loadItems()
		self.loadBars()

	def runMainScreen(self):	
		# toucanGroup.update()
		# toucanGroup.draw(self.__screen)
		self.loadMusic()
		while not self.__completed:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						self.__completed = True
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					mousePos = pygame.mouse.get_pos()
					if (self.__brushPos.collidepoint(mousePos)):
						self.brushPet()
					if (self.__bowlPos.collidepoint(mousePos)):
						self.feedPet()
					if (self.__gameboyPos.collidepoint(mousePos)):
						self.runSpanishGame()
					if (self.__unoBoxPos.collidepoint(mousePos)):
						self.runUno()
			self.loadEverything()
			self.__toucanGroup.update()
			self.__toucanGroup.draw(self.__screen)
			pygame.display.flip()

			self.__hungerCount = self.__hungerCount + 1
			if (self.__hungerCount == 25):
				self.__hungerCount = 0
				if (self.__hungerLevel != 0):
					self.__hungerLevel = self.__hungerLevel - 1
			# print("H" + str(self.__hungerCount))

			self.__cleanCount = self.__cleanCount + 1
			if (self.__cleanCount == 35):
				self.__cleanCount = 0
				if (self.__cleanLevel != 0):
					self.__cleanLevel = self.__cleanLevel - 1
			# print("C" + str(self.__cleanCount))

			self.__funCount = self.__funCount + 1
			if (self.__funCount == 40):
				self.__funCount = 0
				if (self.__funLevel != 0):
					self.__funLevel = self.__funLevel - 1

			self.__clock.tick(2)

	def feedPet(self):
		if self.__toucan.getDirect() == "L":
			eatImages = self.__toucan.getLeftEat()
		else:
			eatImages = self.__toucan.getRightEat()
		for i in eatImages:
			self.makeBackground()
			self.loadItems()
			self.loadBars()
			self.loadBrush()
			yCoords = self.__toucan.getY() + 10
			self.__screen.blit(i, (self.__toucan.getX(), yCoords))
			pygame.display.flip()
			self.__clock.tick(5)
		if (self.__hungerLevel != 10):
			self.__hungerLevel = self.__hungerLevel + 1

	def brushPet(self):
		count = 0
		brush = pygame.image.load(os.path.join("Images", "hairbrush.png"))
		brush = pygame.transform.scale(brush, (40, 60))
		brush = pygame.transform.rotate(brush, 110)
		transColor = brush.get_at((0, 0))
		brush.set_colorkey((transColor))

		yCoords = self.__toucan.getY() + 20
		if (self.__toucan.getDirect() == "L"):
			brush = pygame.transform.flip(brush, True, False)
			xCoords = self.__toucan.getX() + 50
		else:
			xCoords = self.__toucan.getX() - 30

		changeX = xCoords
		changeY = yCoords

		while (count < 2):
			self.makeBackground()
			self.loadItems()
			self.loadBars()
			self.__toucanGroup.draw(self.__screen)

			if (self.__toucan.getDirect() == "L" and 
				self.__toucan.getX() != 500):
				if changeY < yCoords + 20:
					changeY = changeY + 1
				elif ((changeY >= (yCoords + 20)) and changeY < (yCoords + 35)):
					changeY = changeY + .5
					changeX = changeX + .2
				else:
					changeY = yCoords
					changeX = xCoords
					count = count + 1
			else:
				if changeY < yCoords + 20:
					changeY = changeY + 1
				elif ((changeY >= (yCoords + 20)) and changeY < (yCoords + 35)):
					changeY = changeY + .5
					changeX = changeX - .2
				else:
					changeY = yCoords
					changeX = xCoords
					count = count + 1				# if (xCoords == 30):
				# 	yCoords = self.toucan.getY() + 15
			self.__brushPos = self.__screen.blit(brush, (changeX, changeY))
			pygame.display.flip()
			self.__clock.tick(50)
			# self.__screen.blit(self.__brush, (100, 100))
		happyImage = self.__toucan.loadHappy()
		self.makeBackground()
		self.loadBars()
		self.loadItems()

		xCoords = self.__toucan.getX() + 2
		self.__screen.blit(happyImage, (xCoords, self.__toucan.getY()))
		pygame.display.flip()
		self.__clock.tick(1)
		if (self.__cleanLevel != 10):
			self.__cleanLevel = self.__cleanLevel + 1

	def runSpanishGame(self):
		game = WelcomeScreen.WelcomeScreen()
		game.runWelcomeScreen()

		self.loadMusic()
		self.loadEverything()

		xCoords = self.__toucan.getX() + 2
		self.__screen.blit(self.__toucan.getImage(), (xCoords, self.__toucan.getY()))
		pygame.display.flip()
		self.__clock.tick(.8)

		self.loadEverything()

		happyImage = self.__toucan.loadHappy()
		xCoords = self.__toucan.getX() + 2
		self.__screen.blit(happyImage, (xCoords, self.__toucan.getY()))

		pygame.display.flip()
		self.__clock.tick(.8)

		if (self.__funLevel != 10):
			self.__funLevel = self.__funLevel + 1

	def runUno(self):
		game = classUno.Uno()
		game.runScreen()

		self.loadMusic()
		pygame.display.set_mode(self.__screenSize)

		self.loadEverything()

		xCoords = self.__toucan.getX() + 2
		self.__screen.blit(self.__toucan.getImage(), (xCoords, self.__toucan.getY()))
		pygame.display.flip()
		self.__clock.tick(.8)

		self.loadEverything()

		loveImage = self.__toucan.loadLove()
		self.__screen.blit(loveImage, (xCoords, self.__toucan.getY()))
		pygame.display.flip()
		self.__clock.tick(.8)

		if (self.__funLevel != 10):
			self.__funLevel = self.__funLevel + 1
# http://programarcadegames.com/python_examples/en/sprite_sheets/
# http://stackoverflow.com/questions/10560446/how-do-you-select-a-sprite-image-from-a-sprite-sheet-in-python
# https://www.pygame.org/wiki/Spritesheet
# http://stackoverflow.com/questions/14044147/animated-sprite-from-few-images
# http://stackoverflow.com/questions/19336585/how-to-blit-an-image-in-python-inside-the-area-of-a-specific-image


# https://www.gamedev.net/topic/674171-issues-with-enemy-class/