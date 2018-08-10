import pygame, sys
from pygame.locals import *

pygame.init()

display_width = 800
display_height = 600
global gameDisplay
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('The Thrilling Chronicles of Thana')
size = [770, 480]
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
# i n t r o d u c t i o n s c r e e n #
def gameIntro():
    intro = True
basicfont = pygame.font.SysFont("04b03", 35)
text = basicfont.render('The Thrilling Chronicles of Thana', True, (225, 225, 225), (0, 0, 0))
textrect = text.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery


screen.fill((0, 0, 0))
screen.blit(text, textrect)

#########################################################
def text_objects(text, font):
    textSurface = font.render(text, True, (225, 225, 225))
    return textSurface, textSurface.get_rect()

def message_display(text, coordinate):
    smallText = pygame.font.SysFont('04b03', 20)
    TextSurf, TextRect = text_objects(text, smallText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

def gameStart ():
    gameDisplay.fill((0, 0, 0))
    gameStart = True
##########################################################

pygame.display.update()

message_display('Press ENTER to play. Press esc to exit.', 180)

pygame.display.update()

while gameIntro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                gameIntro = False
                gameStart()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

### i m a g e s s o u r c e s ####
choose_chara = pygame.image.load("startScreen.png")


##defining????###############
def game_running () :
    global running
    running = True
    while running :
        global gameOver
        gameOver = False
        while gameOver != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
#########################################

###transition to story screen HOPEFULLY CAN GET THIS TO WORK
    ##screen.fill(0)
    ##screen.blit(choose_chara, (0,0))
    ##pygame.display.flip()
message_display('Once there was a town called Thana in the Whiteridge county...')
message_display('It had a bad reputation in the past, people mysteriously disappearing...')
message_display('Nobody knew where they went...But there is one story...')
message_display('On June 6, 666 Thana went missing. She was a carefree girl all and one day she')
message_display('went missing, nobody could find her. People believe that she was kidnapped.')
message_display('People eventually gave up looking for her, and said she was probably dead.')
message_display('Since she was cared by all they decide to name the town after her…')

while gameStart:
    for event in pygame.event.get(): #the choice to quit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                gameIntro = False
                game_running()
                start = False
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

clock.tick(5)
if event.type == pygame.QUIT:
    pygame.quit()
    exit(0)
