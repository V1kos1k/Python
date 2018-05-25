import pygame,sys
pygame.init()
# Переменные
speed = 3 # Скорость движения шара и самолета
angle = 0
# Окно
color = (255,255,255) # Цвет фона
size = width, height = 500, 500   # Размер окна
screen = pygame.display.set_mode(size)
scr = pygame.display.set_mode(size)
# Шарик
ball_image = pygame.image.load('ball.bmp') # Изображение шара
ball_rect = ball_image.get_rect()
image = pygame.transform.rotate(ball_image, angle)
# Треугольник
poligon_points = [(0,height),(0,height/2-15),(width/2+15,height)] # Вершины
poligon_color = (0, 0, 0)  # Начальный вет треугольника                                   # Сербобуромалиновый 115 81 132
poligon_width = 0
# Самолетик
plane_width =  0
plane_points = [(0,0),(20,0),(50,30),(160,30),(200,70),(0,70)]
plane_image = pygame.Surface((200, 80), flags=0)
plane_coord = [(0,0),(200,0),(200,200),(0,200)]
pygame.draw.polygon(plane_image,(255,255,255),plane_coord,plane_width)
pygame.draw.polygon(plane_image,(15,81,132),plane_points,plane_width)
plane_points = [(100,50),(80,80),(100,80),(130,50)]
pygame.draw.polygon(plane_image,(100,50,200),plane_points,plane_width)
#plane_image = pygame.image.load('plane.bmp') # Изображение самолета
plane_rect = ball_image.get_rect()
# Таймер
clok = pygame.time.Clock()

'''
-------------------------------Рисование-Шара-----------------------------------
'''
def rotate_ball():
    global ball_rect
    global image
    image = pygame.transform.rotate(ball_image, angle)
    ball_rect = image.get_rect(center=ball_rect.center)

def move_ball(x,y):
    global ball_rect
    global speed
    ball_rect = ball_rect.move(x,y)

def ball():
    global ball_rect
    global angle
    if ball_rect.bottom < height / 2:
        move_ball(0,2*speed)
        angle += speed
    elif ball_rect.bottom >= height / 2 and ball_rect.bottom < height:
        move_ball(speed,speed)
        rotate_ball()
    else:
        move_ball(speed,0)
        rotate_ball()
    angle -= speed
'''
--------------------------------Рисование-Самолета------------------------------
'''

def move_plane(x,y):
    global plane_rect
    global speed
    plane_rect = plane_rect.move(x,y)

def plane():
    move_plane(speed,0)

'''
----------------------------------Цикл-Программы--------------------------------
'''
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: exit(0)
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit(0)
        if e.type == pygame.KEYDOWN and e.key == pygame.K_PRINT:
            ball_image = pygame.image.load('extra.jpg')
            image = pygame.transform.rotate(ball_image, angle)
    screen.fill(color)
    ball()
    plane()
    if plane_rect.x > width:
        plane_rect.x = -200
    screen.blit(image, ball_rect)
    screen.blit(plane_image, plane_rect)
    pygame.draw.polygon(screen, poligon_color, poligon_points, poligon_width)
    if max(poligon_color) != 255:   # Осветление треугольника
        poligon_color = (poligon_color[0]+1,poligon_color[1]+1, poligon_color[2]+1)
    #else:
    #    pygame.quit()
    #    sys.exit(0)
    pygame.display.update()
    clok.tick(60)
