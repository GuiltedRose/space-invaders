import pygame

background_color = (255, 255, 255)
(width, height) = (500, 500)
pygame.display.set_caption('Space Invaders!')
screen = pygame.display.set_mode((width, height))
screen.fill(background_color)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False