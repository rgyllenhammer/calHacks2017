import pygame
import pyscreenshot as ImageGrab
import os
from PIL import Image
import shelve

# sets position of pygame window to know where to take the screenshot
startX = 0;
startY = 0;
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (startX,startY)

# variables surrounding images
screenshotPath = '/Users/ReeseGyllenhammer/desktop/calHacks2017/screenShots/'

# initializes pygame
pygame.init()

# global variables
screenWidth = 800
screenHeight = 600
clock = pygame.time.Clock()
mouse = pygame.mouse
FPS = 60

# colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

# sets up pygame window
gameDisplay = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('draw on me!')

def exitGame():
    pygame.quit()
    quit()

def circle(x, y, r, color):
    pygame.draw.circle(gameDisplay, color, [x,y], r)

def drawDot(x, y):
    circle(x, y, 10, black)

def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame()

        gameDisplay.fill(black)

        mouseClicks = mouse.get_pressed()
        if mouseClicks[0] == 1:
            intro = False

        pygame.display.update()
        clock.tick(FPS)

def main():
    # variables / functions surrounding the drawing app
    dots = []
    speed = 0
    timer = 60 # gives some time for the app to count down before clicks are registered

    if timer <= 0:
        timer = 0

    drawing = True
    while drawing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if len(dots) >= 1:
                        speed = 1

                elif event.key == pygame.K_p:

                    d = shelve.open('imgNum.txt')
                    fileNum = d['fileNum']

                    im = ImageGrab.grab(bbox=(startX, startY + 50, startX + screenWidth, startY + screenHeight))
                    fileOut = screenshotPath + 'im{}.png'.format(str(fileNum))
                    im.save(fileOut)

                    fileNum = int(fileNum)
                    fileNum += 1
                    d['fileNum'] = fileNum
                    d.close()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    speed = 0;

        if speed > 0:
            dots = dots[:-1]

        gameDisplay.fill(white)

        mouseClicks = mouse.get_pressed()
        mousePos = mouse.get_pos()

        if mouseClicks[0] == 1 and timer <= 0:
            dots.append([mousePos[0], mousePos[1]])

        for dot in dots:
            drawDot(dot[0], dot[1])

        timer -= 1
        pygame.display.update()
        clock.tick(FPS)

intro()
main()
