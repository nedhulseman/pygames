import pygame, sys, time
from pygame.locals import *
from math import pi
from random import randint

RIGHT='right'
STEPSIZE=8


pygame.init()

WINDOWWIDTH=700
WINDOWHEIGHT=700
windowSurface=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('The Space Battle')

#creation of colors
BLACK=(0,0,0)
OBSIDIAN=(61,53,75)
WHITE=(255, 255, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
SATURN=(222,184,135)
MOON_GREY=(220,220,220)
CRATER_GREY=(125, 125, 125)
ROBOT=(70,130,180)


def drawRobot(windowSurface):
    pygame.draw.rect(windowSurface, ROBOT, (70, 325, 40, 40)) #head
    pygame.draw.rect(windowSurface, RED, (90, 335, 20, 10)) #eye
    pygame.draw.rect(windowSurface, ROBOT, (60, 365, 60, 70)) #body
    pygame.draw.line(windowSurface, ROBOT, (90, 325), (90, 305)) #antenna stem
    pygame.draw.circle(windowSurface, ROBOT, (90, 305), 6, 0) #antenna
    pygame.draw.rect(windowSurface, ROBOT, (70, 435, 10, 40)) #leg 1.1
    pygame.draw.rect(windowSurface, ROBOT, (30, 465, 40, 10)) #leg 1.2
    pygame.draw.polygon(windowSurface, ROBOT, ((39, 470), (22, 480), (22,460)), 0) #foot 1
    pygame.draw.rect(windowSurface, ROBOT, (120, 425, 40, 10)) #leg 2.1
    pygame.draw.rect(windowSurface, ROBOT, (150, 435, 10, 40)) #leg 2.2
    pygame.draw.polygon(windowSurface, ROBOT, ((155, 466), (145, 483), (165, 483)), 0) #foot 2
    pygame.draw.rect(windowSurface, ROBOT, (120, 375, 40, 10)) #arm
    #gun
    pygame.draw.rect(windowSurface, RED, (150, 385, 7, 5))
    pygame.draw.circle(windowSurface, RED, (154, 360), 15, 0)
    pygame.draw.rect(windowSurface, RED, (165, 357, 15, 5))
    pygame.draw.circle(windowSurface, RED, (185, 360), 7, 0)

def drawAlien(windowSurface, LEFT=500):
    #ufo
    pygame.draw.circle(windowSurface, CRATER_GREY, (LEFT+50, 390), 60, 0) #UFO
    pygame.draw.rect(windowSurface, OBSIDIAN, (LEFT-10, 330, 120, 60)) #covering
    pygame.draw.arc(windowSurface, WHITE, (LEFT, 300, 100, 200), 0, pi, 2) #shield
    pygame.draw.line(windowSurface, CRATER_GREY, (LEFT+50, 430), (LEFT+50, 470)) #leg1
    pygame.draw.line(windowSurface, CRATER_GREY, (LEFT+30, 430), (LEFT+5, 480)) #leg2
    pygame.draw.line(windowSurface, CRATER_GREY, (LEFT+70, 430), (LEFT+85, 480)) #leg3
    pygame.draw.circle(windowSurface, CRATER_GREY, (LEFT+50, 470), 5, 3)
    pygame.draw.circle(windowSurface, CRATER_GREY, (LEFT+5, 480), 5, 3)
    pygame.draw.circle(windowSurface, CRATER_GREY, (LEFT+85, 480), 5, 3)
    
    #alien
    pygame.draw.circle(windowSurface, GREEN, (LEFT+50, 340), 20, 0) #head
    pygame.draw.arc(windowSurface, GREEN, (LEFT+50, 320, 30, 20), pi/3, pi, 1) #antenna stem
    pygame.draw.circle(windowSurface, GREEN, (LEFT+75, 325), 4, 0) #antenna
    pygame.draw.circle(windowSurface, WHITE, (LEFT+35, 332), 8, 0) #eye
    pygame.draw.circle(windowSurface, BLACK, (LEFT+31, 332), 4, 0) #pupil
    pygame.draw.rect(windowSurface, GREEN, (LEFT+40, 355, 20, 35)) #body


   
laser1= {'rect':pygame.Rect(285, 356, 8, 10), 'color':RED, 'dir':RIGHT, 
         'delay':0, 'shot':False}
laser2 = {'rect':pygame.Rect(285, 356, 8, 10), 'color':RED, 'dir':RIGHT, 
          'delay':7, 'shot':False}
laser3 = {'rect':pygame.Rect(285, 356, 8, 10), 'color':RED, 'dir':RIGHT, 
          'delay':15, 'shot':False}
laser4 = {'rect':pygame.Rect(285, 356, 8, 10), 'color':RED, 'dir':RIGHT, 
          'delay':23, 'shot':False}
   
lasers=[laser1, laser2, laser3, laser4]
iterator=0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(OBSIDIAN)
    drawRobot(windowSurface)
    drawAlien(windowSurface, LEFT=530)
    
    shield=False   
    for laser in lasers:
        if iterator==laser['delay']:
            laser['shot']=True
        if laser['shot']==True:    
            laser['rect'].left += STEPSIZE
            laser['rect'].top -= 1
            laser['rect'].height += 2

    
    
    pygame.draw.rect(windowSurface, laser1['color'], laser1['rect'])
    pygame.draw.rect(windowSurface, laser2['color'], laser2['rect'])
    pygame.draw.rect(windowSurface, laser3['color'], laser3['rect'])
    pygame.draw.rect(windowSurface, laser4['color'], laser4['rect'])

    iterator+=1
    pygame.display.update()
    time.sleep(.02)
    



