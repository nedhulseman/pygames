import pygame, sys
from pygame.locals import *
from math import pi
from random import randint





pygame.init()
windowSurface=pygame.display.set_mode((1200, 700), 0, 32)
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




windowSurface.fill(OBSIDIAN) #fill the background for space

#draw stars
for i in range(400):
    x=randint(0, 1200)
    y=randint(0, 700)
    size=randint(0, 4)
    pygame.draw.circle(windowSurface, WHITE, (x, y), size, 0)

#drawing saturn
pygame.draw.circle(windowSurface, SATURN, (600, 75), 50, 0) #planet
pygame.draw.ellipse(windowSurface, RED, (500, 65, 200, 18), 3) #ring
pygame.draw.rect(windowSurface, SATURN, (553, 64, 95, 7)) #covers the backside of the ring

#drawing moon
pygame.draw.circle(windowSurface, MOON_GREY, (450, 1100), 700, 0) #moon
pygame.draw.circle(windowSurface, CRATER_GREY, (650, 550), 20, 0) #craters
pygame.draw.circle(windowSurface, CRATER_GREY, (550, 480), 24, 0)
pygame.draw.circle(windowSurface, CRATER_GREY, (750, 553), 12, 0)
pygame.draw.circle(windowSurface, CRATER_GREY, (300, 571), 18, 0)
pygame.draw.circle(windowSurface, CRATER_GREY, (417, 540), 30, 0)
pygame.draw.circle(windowSurface, CRATER_GREY, (327, 473), 16, 0)
pygame.draw.circle(windowSurface, CRATER_GREY, (160, 520), 21, 0)





#robot
pygame.draw.rect(windowSurface, ROBOT, (270, 325, 40, 40)) #head
pygame.draw.rect(windowSurface, RED, (290, 335, 20, 10)) #eye
pygame.draw.rect(windowSurface, ROBOT, (260, 365, 60, 70)) #body
pygame.draw.line(windowSurface, ROBOT, (290, 325), (290, 305)) #antenna stem
pygame.draw.circle(windowSurface, ROBOT, (290, 305), 6, 0) #antenna
pygame.draw.rect(windowSurface, ROBOT, (270, 435, 10, 40)) #leg 1.1
pygame.draw.rect(windowSurface, ROBOT, (230, 465, 40, 10)) #leg 1.2
pygame.draw.polygon(windowSurface, ROBOT, ((239, 470), (222, 480), (222,460)), 0) #foot 1
pygame.draw.rect(windowSurface, ROBOT, (320, 425, 40, 10)) #leg 2.1
pygame.draw.rect(windowSurface, ROBOT, (350, 435, 10, 40)) #leg 2.2
pygame.draw.polygon(windowSurface, ROBOT, ((355, 466), (345, 483), (365, 483)), 0) #foot 2
pygame.draw.rect(windowSurface, ROBOT, (320, 375, 40, 10)) #arm
#gun
pygame.draw.rect(windowSurface, RED, (350, 385, 7, 5))
pygame.draw.circle(windowSurface, RED, (354, 360), 15, 0)
pygame.draw.rect(windowSurface, RED, (365, 357, 15, 5))
pygame.draw.circle(windowSurface, RED, (385, 360), 7, 0)
# robot lasers
y1=364
y2=356
for i in range(397, 477, 10):
    pygame.draw.line(windowSurface, RED, (i, y1), (i, y2))
    y1+=4
    y2-=4
    
    

#ufo
pygame.draw.circle(windowSurface, CRATER_GREY, (700, 390), 60, 0) #UFO
pygame.draw.rect(windowSurface, OBSIDIAN, (640, 330, 120, 60)) #covering
pygame.draw.arc(windowSurface, WHITE, (650, 300, 100, 200), 0, pi, 2) #shield
pygame.draw.line(windowSurface, CRATER_GREY, (700, 430), (700, 470)) #leg1
pygame.draw.line(windowSurface, CRATER_GREY, (680, 430), (655, 480)) #leg2
pygame.draw.line(windowSurface, CRATER_GREY, (720, 430), (735, 480)) #leg3
pygame.draw.circle(windowSurface, CRATER_GREY, (700, 470), 5, 3)
pygame.draw.circle(windowSurface, CRATER_GREY, (655, 480), 5, 3)
pygame.draw.circle(windowSurface, CRATER_GREY, (735, 480), 5, 3)

#alien
pygame.draw.circle(windowSurface, GREEN, (700, 340), 20, 0) #head
pygame.draw.arc(windowSurface, GREEN, (700, 320, 30, 20), pi/3, pi, 1) #antenna stem
pygame.draw.circle(windowSurface, GREEN, (725, 325), 4, 0) #antenna
pygame.draw.circle(windowSurface, WHITE, (685, 332), 8, 0) #eye
pygame.draw.circle(windowSurface, BLACK, (681, 332), 4, 0) #pupil
pygame.draw.rect(windowSurface, GREEN, (690, 355, 20, 35)) #body

#UFO lasers
y1=398
y2=390
for i in range(620, 540, -10):
    pygame.draw.line(windowSurface, GREEN, (i, y1), (i, y2))
    y1+=4
    y2-=4


fname = "spacebattle.png"
pygame.image.save(windowSurface, fname)
print("file {} has been saved".format(fname))


#windowSurface.blit(text, textRect)
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



