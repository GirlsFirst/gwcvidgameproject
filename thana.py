import pygame, sys
from pygame.locals import *

pygame.init()

pygame.display.set_caption('The Thrilling Chronicles of Thana')
size = [640, 480]
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

basicfont = pygame.font.SysFont("04b03", 35)
text = basicfont.render('The Thrilling Chronicles of Thana', True, (225, 225, 225), (0, 0, 0))
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery

screen.fill((0, 0, 0))
screen.blit(text, textrect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(20)
