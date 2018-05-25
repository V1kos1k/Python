# Мхитарян защита

import pygame
from pygame import *
from math import pi, sin, cos

display = (1200, 600)
pygame.init()
screen = pygame.display.set_mode(display)  # 0, 32
pygame.display.set_caption('triangle')
window_color = (30,144,255)
clock = pygame.time.Clock()
window_colo = (0,0,0)


def triangle():
    #pygame.draw.polygon(b, (50, 205, 50),((0,300), (50,200), (100,300)), 0)
    #pygame.transform.rotate(b, pi/4)
    pygame.draw.polygon(b, Color("red"),((30,60), (50,20), (70,60)), 0)

#def bum():
#    pygame.draw.rect(bim, Color("red"), ((0,0), (100,100)), 0)

x = 0
y = 100
x1 = 1
x2 = 0
teta = 90
done = True
while done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = False
    screen.fill(window_color)  # заливаем окно голубым

    b = Surface([100, 100])
    b.fill(window_color)

    bim = Surface([100, 100])
    bim.fill(window_color)
    if x <= 100:
        x2 += 1
    elif x > 100 and x <= 200:
        x2 -= 1

    if x<=100:
        y+=3
        x+=1
    elif x>100 and x<= 150:
        y+=2
        x+=1
    elif x>150 and x<=200:
        y-=2
        x+=1
    elif x>200 and x<=300:
        y-=3
        x+=1
    elif x>300 and x<=350:
        y-=2
        x+=1
    elif x>350 and x<=400:
        y+=2
        x+=1
    elif x>400 and x<=500:
        y+=3
        x+=1
    elif x>500 and x<=550:
        y+=2
        x+=1
    elif x>550 and x<=600:
        y-=2
        x+=1
    elif x>600 and x<=700:
        y-=3
        x+=1
    elif x>700 and x<=750:
        y-=2
        x+=1
    elif x>750 and x<=800:
        y+=2
        x+=1
    elif x>800 and x<= 900:
        y+=3
        x+=1
    elif x>900 and x<=950:
        y+=2
        x+=1
    elif x>950 and x<=1000:
        y-=2
        x+=1
    elif x>1000 and x<=1100:
        y-=3
        x+=1
    elif x>1100 and x<=1150:
        y-=2
        x+=1
    elif x>1150 and x<= 1200:
        y+=2
        x+=1
    
    triangle()
    #bum()
    b = pygame.transform.rotate(b, teta)
    #bim = pygame.transform.scale(bim, (x2, x2))
    screen.blit(b, (x,y) )
    screen.blit(bim, (600,300))
    teta += 90
    
    #Rect.x = rect.x + 1
    #Rect.y = sin(Rect.x)
    #milli = clock.tick(40)
    #sec = milli/1000.0
    #x1 += 3*sec*pi/6

    #triangle(x, y)
    
    pygame.display.update()
    clock.tick(20)

pygame.quit()
