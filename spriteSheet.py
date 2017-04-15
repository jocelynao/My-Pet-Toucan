import pygame
import os.path

BLACK = (0, 0, 0)

class spriteSheet:

	# def __init__(self, filename):
	# 	try:
	# 		self.__spriteSheet = pygame.image.load(os.path.join('Images', filename)).convert()
	# 	except pygame.error:
	# 		print("Unable to load sprite sheet image", filename)
	# 		raise SystemExit

	# def imageAt(self, rectangle, colorkey = None):
	# 	rect = pygame.Rect(rectangle)
	# 	image = pygame.Surface(rect.size).convert(self.__spriteSheet)
	# 	#image.blit(self.__spriteSheet, (0, 0), rect)
	# 	if colorkey is not None:
	# 		if colorkey is -1:
	# 			colorkey = image.get_at((0, 0))
	# 		#image.set_colorkey(colorkey.pygame.RLEACCEL)
	# 	return image

	def __init__(self, filename):
		try:
			self.spriteSheet = pygame.image.load(os.path.join('Images', filename)).convert()
		except pygame.error:
			print("Unable to load sprite sheet image", filename)
			raise SystemExit

	def getImage(self, x, y, width, height):
		image = pygame.Surface([width, height]).convert()
		image.blit(self.spriteSheet, (0, 0), (x, y, width, height))
		image.set_colorkey(BLACK)
		return image

	# 	self.__theImage = pygame.transform.scale(theImage, (125, 125))
	# 	theImage.set_colorkey((0, 0, 0))
	# 	return theImage

	# def image_At(self, rectangle):
	# 	rect = pygame.Rect(rectangle)
	# 	image = pygame.Surface(rect.size).convert(self.__theImage)
	# 	image.blit(self.__theImage, rect)


