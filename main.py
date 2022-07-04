import pygame

pygame.init()

background_color = (0, 0, 0)
(width, height) = (500, 500)
pygame.display.set_caption('Space Invaders!')
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)

tick = pygame.time.Clock()
x = (width * 0.45)
y = (height * 0.8)

running = True

# sprite declaration:

playerSprite = pygame.image.load('src/player.png')

def player(x,y):
	screen.blit(playerSprite, (x,y))
	pygame.display.update()
	tick.tick(60)
while running:
    player(x,y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
