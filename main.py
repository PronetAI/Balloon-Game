import pygame
from pygame.locals import *
import random
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Balloon Game")
class Balloon:
    def __init__(self):
        self.x = random.randint(30, 570)
        self.y = 700
        self.image = pygame.image.load("Balloon.jpeg")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.letter = chr(random.randint(97, 122))

    def Display(self):
        screen.blit(self.image, (self.x, self.y))


B1 = Balloon()
while True:
    screen.fill((0, 0, 0))
    B1.Display()
    B1.y = B1.y - 5
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
