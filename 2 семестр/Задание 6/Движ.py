# Мхитарян ИУ7-24
# танк, пуля, солнце

import pygame
from pygame.locals import *
from math import pi, sin, cos

display = (1200, 600)
pygame.init()
screen = pygame.display.set_mode(display)  # 0, 32
pygame.display.set_caption('Tank')
window_color = (30,144,255)
clock = pygame.time.Clock()

def earth():
    pygame.draw.rect(screen, (50, 205, 50), ((0, 500), (1200, 100)), 0)

def tank(x):

    
    
    
    pygame.draw.rect(screen, (23,40,11), ((250 + x, 375), (250, 15)), 0)
    pygame.draw.ellipse(screen, (23,40,11), ((350 + x, 400), (500, 300)), 0)
    pygame.draw.polygon(screen, (46,82,21), ((450 + x, 425), (475 + x, 350),
                                        (700 + x, 350), (750 + x, 425)), 0)
    pygame.draw.polygon(screen, (37, 64, 18), ((350 + x, 525), (400 + x, 425),
                                       (800 + x, 425), (850 + x, 525)), 0)

    
    pygame.draw.circle(screen, (47, 44, 39), (400 + x, 565), 39, 0)
    pygame.draw.circle(screen, (47, 44, 39), (500 + x, 565), 39, 0)
    pygame.draw.circle(screen, (47, 44, 39), (600 + x, 565), 39, 0)
    pygame.draw.circle(screen, (47, 44, 39), (700 + x, 565), 39, 0)
    pygame.draw.circle(screen, (47, 44, 39), (800 + x, 565), 39, 0)

    pygame.draw.line(screen, (0,0,0),
                     (30*cos(teta1+pi/2)+x+400, 565-30*sin(teta1+pi/2)),
                     (30*cos(teta2-pi/2)+x+400, 565-30*sin(teta2-pi/2)), 3)
    pygame.draw.line(screen, (0,0,0),
                     (30*cos(teta1+pi)+x+400, 565-30*sin(teta1+pi)),
                     (30*cos(teta2)+x+400, 565-30*sin(teta2)), 3)

    pygame.draw.line(screen, (0,0,0),
                     (30*cos(teta1+pi/2)+x+500, 565-30*sin(teta1+pi/2)),
                     (30*cos(teta2-pi/2)+x+500, 565-30*sin(teta2-pi/2)), 3)
    pygame.draw.line(screen, (0,0,0),
                     (30*cos(teta1+pi)+x+500, 565-30*sin(teta1+pi)),
                     (30*cos(teta2)+x+500, 565-30*sin(teta2)), 3)

    pygame.draw.line(screen, (0,0,0),
                     (30*cos(teta1+pi/2)+x+600, 565-30*sin(teta1+pi/2)),
                     (30*cos(teta2-pi/2)+x+600, 565-30*sin(teta2-pi/2)), 3)
    pygame.draw.line(screen, (0,0,0),
                     (30*cos(teta1+pi)+x+600, 565-30*sin(teta1+pi)),
                     (30*cos(teta2)+x+600, 565-30*sin(teta2)), 3)

    pygame.draw.line(screen, (0,0,0),
                     (30*cos(teta1+pi/2)+x+700, 565-30*sin(teta1+pi/2)),
                     (30*cos(teta2-pi/2)+x+700, 565-30*sin(teta2-pi/2)), 3)
    pygame.draw.line(screen, (0,0,0),
                     (30*cos(teta1+pi)+x+700, 565-30*sin(teta1+pi)),
                     (30*cos(teta2)+x+700, 565-30*sin(teta2)), 3)

    pygame.draw.line(screen, (0,0,0),
                     (30*cos(teta1+pi/2)+x+800, 565-30*sin(teta1+pi/2)),
                     (30*cos(teta2-pi/2)+x+800, 565-30*sin(teta2-pi/2)), 3)
    pygame.draw.line(screen, (0,0,0),
                     (30*cos(teta1+pi)+x+800, 565-30*sin(teta1+pi)),
                     (30*cos(teta2)+x+800, 565-30*sin(teta2)), 3)
    

        # вращение
        
def pula(x):
    pygame.draw.rect(screen, (107, 67, 28), ((275 + x, 375), (25, 15)), 0)
    pygame.draw.polygon(screen, (107, 67, 28), ((265 + x, 382), (275 + x, 375),
                                                (275 + x, 390)), 0)

def wall(x):
    pygame.draw.polygon(screen, (102, 0, 0), ((50 + x, 600), (50 + x, 300),
                                              (200 + x, 250),(200 + x, 550)), 0)
    pygame.draw.rect(screen, (93, 0, 0), ((15 + x, 600), (35, -300)), 0)
    pygame.draw.polygon(screen, (93, 0, 0), ((15 + x, 300), (165 + x, 250),
                                             (200 + x, 250), (200 + x, 550)), 0)
def sun(x, y):
    pygame.draw.line(screen, (255, 255, 0), (-150 + x, 350 + y),
                     (-50 + x, 250 + y), 4)
    pygame.draw.line(screen, (255, 255, 0), (-150 + x, 250 + y),
                     (-50 + x, 350 + y), 4)
    pygame.draw.line(screen, (255, 255, 0), (-175 + x, 300 + y),
                     (-25 + x, 300 + y), 4)
    pygame.draw.line(screen, (255, 255, 0), (-100 + x, 225 + y),
                     (-100 + x, 375 + y), 4)
    pygame.draw.circle(screen, (255, 255, 0), (-100 + x, 300 + y), 40, 0)


x = 975 
x1 = 800
x2 = -200
x3 = 0
y3 = 100
teta = 0
teta1 = 0
teta2 = 0

done = True
while done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = False
    screen.fill(window_color)  # заливаем окно голубым

    earth() # земля
    x -= 3

    if x3 < 500:
        x3 += 4
        y3 -= 2
    elif x3 >= 500 and x3 <= 600:
        x3 += 4
        y3 -=1
        
    elif x3 > 600 and x3 <= 800:
        x3 += 4
    elif x3 > 800 and x3 <= 900:
        x3 += 4
        y3 += 1
    else:
        x3 += 4
        y3 += 2
    sun(x3, y3)

    
    if x1 >= -160:
        wall(x2)
        x2 += 1
    if x < 600 and x1 > -160:
        pula(x1)
        x1 -= 8
    if x1 == -160:
        x1 -= 8
    
        
    
    tank(x)

    milli = clock.tick(50)
    sec = milli/500.0


    teta += sec*pi/12
    teta1 += 3*sec*pi/4
    teta2 += 3*sec*pi/4
    if x < -950:
        x = 975
        x1 = 800
        x2 = -200
        x3 = 0
        y3 = 100
    
    pygame.display.update()
    clock.tick(50)

pygame.quit()
