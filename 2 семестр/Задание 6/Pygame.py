# Шорикн ИУ7-21

import pygame
import sys
from pygame import *
from math import pi, cos, sin

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
DISPLAY = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption('Лабораторная работа по pygame')

done = False

clock = pygame.time.Clock()
speed_by_second = 250
x = 0
teta = 0
teta1 = 0
teta2 = 0
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    bg = Surface(DISPLAY)
    bg.fill(Color("lightblue"))
    pygame.draw.rect(bg, Color("#8a6642"),
                     Rect(0, SCREEN_HEIGHT*0.85,
                          SCREEN_WIDTH, SCREEN_HEIGHT*0.15), 0)
    
    screen.blit(bg, (0, 0))

  
    
    
    car = Surface((300,150))
    
    TRANSPARENT_COLOR = Color("#123456")
    car.set_colorkey(TRANSPARENT_COLOR)
    car.fill(TRANSPARENT_COLOR)
      
    pygame.draw.rect(car, Color("red"), Rect(150, 0, 100, 55), 0)
    pygame.draw.rect(car, Color("lightblue"), Rect(165, 15, 70, 35), 0)
    pygame.draw.rect(car, Color("red"), Rect(30, 55, 270, 60), 0)
    
    pygame.draw.circle(car, Color("lightblue"), (70, 120), 35, 0)
    pygame.draw.circle(car, Color("lightblue"), (260, 120), 35, 0)
    pygame.draw.circle(car, Color("black"), (70, 120), 30, 0)
    pygame.draw.circle(car, Color("black"), (260, 120), 30, 0)

    pygame.draw.line(car, Color("white"),
                     (30*cos(teta1+pi/2)+70, 120-30*sin(teta1+pi/2)),
                     (30*cos(teta2-pi/2)+70, 120-30*sin(teta2-pi/2)), 3)
    pygame.draw.line(car, Color("white"),
                     (30*cos(teta1+pi)+70, 120-30*sin(teta1+pi)),
                     (30*cos(teta2)+70, 120-30*sin(teta2)), 3)
    pygame.draw.line(car, Color("white"),
                     (30*cos(teta1+pi/2)+260, 120-30*sin(teta1+pi/2)),
                     (30*cos(teta1-pi/2)+260, 120-30*sin(teta1-pi/2)), 3)
    pygame.draw.line(car, Color("white"),
                     (30*cos(teta1+pi)+260, 120-30*sin(teta1+pi)),
                     (30*cos(teta2)+260, 120-30*sin(teta2)), 3)

   
    sun = Surface((200,200))
    sun.set_colorkey(TRANSPARENT_COLOR)
    sun.fill(TRANSPARENT_COLOR)

    pygame.draw.circle(sun, Color("yellow"),(100,100),50,0)
    pygame.draw.line(sun, Color("yellow"), (100,40),(100,0),3)
    pygame.draw.line(sun, Color("yellow"), (100,160),(100,200),3)
    pygame.draw.line(sun, Color("yellow"), (27,27), (57,57),3)
    pygame.draw.line(sun, Color("yellow"), (177,27), (147,57),3)
    pygame.draw.line(sun, Color("yellow"), (0,100), (40,100),3)
    pygame.draw.line(sun, Color("yellow"), (160,100), (200,100),3)
    pygame.draw.line(sun, Color("yellow"), (57,147), (27,177),3)
    pygame.draw.line(sun, Color("yellow"), (147,147), (177,177),3)

    pygame.draw.circle(sun, Color("white"), (75,85), 15, 0)
    pygame.draw.circle(sun, Color("white"), (125,85), 15, 0)
    pygame.draw.circle(sun, Color("black"), (75,85), 5, 0)
    pygame.draw.circle(sun, Color("black"), (125,85), 5, 0)
    pygame.draw.circle(sun, Color("orange"), (100,100), 10, 0)
    pygame.draw.arc(sun, Color("pink"), (65,65,70,70), 7*pi/6, 11*pi/6, 7)

    
    milli = clock.tick(40)
    sec = milli/1000.0
    dm = speed_by_second*sec
    teta -= sec*pi/12
    teta1 -= 3*sec*pi/4
    teta2 -= 3*sec*pi/4
    
    #x1 = 30*cos(teta1+pi/2)+70
    #y1 = 120-30*sin(teta1+pi/2)
    #x2 = 30*cos(teta2-pi/2)+70
    #y2 = 120-30*sin(teta2-pi/2)
    #x3 = 30*cos(teta1+pi)+70
    #y3 = 120-30*sin(teta1+pi)
    #x4 = 30*cos(teta2)+70
    #y4 = 120-30*sin(teta2)
    
    x += dm
    if x > 700:
        x = -300
    if cos(teta) > 0.7:
        teta = 5*pi/6
    x1 = 580*cos(teta)+280
    y1 = 600-580*sin(teta)
    

    screen.blit(sun,(x1,y1))      
    screen.blit(car, (x, 0.57*SCREEN_HEIGHT))
  
    pygame.display.update()

pygame.quit()
