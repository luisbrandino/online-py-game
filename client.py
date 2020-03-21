import pygame
import network
import json

width = 500
height = 500
player_x = 50
player_y = 50
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Player():
	def __init__(self, x, y, width, height, color):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.rect = (self.x, self.y, self.width, self.height)
		self.color = color
		self.vel = 3

	def draw(self, window):
		pygame.draw.rect(window, self.color, self.rect)

	def move(self, n):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.x += self.vel

		if keys[pygame.K_LEFT]:
			self.x -= self.vel

		if keys[pygame.K_UP]:
			self.y -= self.vel

		if keys[pygame.K_DOWN]:
			self.y += self.vel

		self.rect = (self.x, self.y, self.width, self.height)

		data = '{"rect": (' + str(self.x) + ', ' + str(self.y) + ', 100, 100)}'

		n.send_data(data)

class Players():
	def __init__(self, x, y, width, height, color):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.rect = (self.x, self.y, self.width, self.height)
		self.color = color

	def draw(self, window):
		pygame.draw.rect(window, self.color, self.rect)

	def move(self, data):
		self.rect = data["rect"]


def redraw(player, players):
	window.fill((255,255,255))
	player.draw(window)
	players.draw(window)
	pygame.display.update()

def main():
	run = True
	n = network.Network(("0.0.0.0", 4444))
	p = Player(player_x, player_y, 100, 100, (0,255,0))

	data_serialized = '{"rect": (' + str(player_x) + ', ' + str(player_y) + ', 100, 100)}'
	print(data_serialized)
	n.send_data(data_serialized)

	p.draw(window)

	players = Players(0, 0, 100, 100, (0,255,0))

	clock = pygame.time.Clock()

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

		pos = n.get_data()
		if pos != None:
			print(pos)
			players.move(pos)

		p.move(n)
		redraw(p, players)

		clock.tick(60)

main()