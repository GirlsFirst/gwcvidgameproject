import pygame, sys
from pygame.locals import *

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Our Video Game Project')
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

def text_objects(text, font):
    textSurface = font.render(text, True, (225, 225, 225))
    return textSurface, textSurface.get_rect()

def message_display(text):
    smallText = pygame.font.SysFont('04b03', 20)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)


pygame.display.update()

message_display('Press ENTER to play. Press esc to exit.')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(5)
