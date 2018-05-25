#  Мхитарян ИУ7-14
#  Определить:длину сторон треугольника по заданным координатам точек
#  Определить высоту проведённую из наименьшего угла.
#  Определить является ли треугольник прямоугольным.
#  Принадлежит ли указанная точка треугольнику.
#  Если принадлежит, найти расстояние от указанной точки до ближайшей стороны.

print('30 сентября 2016')
from math import sqrt
try:
    x1, y1 = map(int,input('Введите координаты вершины A = ').split(';'))
    x2, y2 = map(int,input('Введите координаты вершины B = ').split(';'))
    x3, y3 = map(int,input('Введите координаты вершины C = ').split(';'))
except ValueError:
    print('Введено неверное значение.')
    input('Нажмите Enter, чтобы выйти.')
    exit()
    
# Находим длину стороны a (AB).
# Находим длину стороны b (BC).
# Находим длину стороны c (AC).

a = (sqrt((x2 - x1)**2 + (y2 - y1)**2))
b = (sqrt((x3 - x2)**2 + (y3 - y2)**2))
c = (sqrt((x3 - x1)**2 + (y3 - y1)**2))
if a + b > c and b + c > a and c + a > b:
    print('Длина стороны a = ''{:7.3f}'.format(a))
    print('Длина стороны b = ''{:7.3f}'.format(b))
    print('Длина стороны c = ''{:7.3f}'.format(c))

    # Находим угол L.
    # Находим угол B.
    # Находим угол G.
    # Находим высоту, проведенную из наименьшего угла.

    c1 = (((x2 - x1)**2 + (y2 - y1)**2) + ((x3 - x1)**2 + (y3 - y1)**2)
          - ((x3 - x2)**2 + (y3 - y2)**2))/(2*a*c)
    c2 = (((x2 - x1)**2 + (y2 - y1)**2) + ((x3 - x2)**2 + (y3 - y2)**2)
          - ((x3 - x1)**2 + (y3 - y1)**2))/(2*a*b)
    c3 = (((x3 - x2)**2 + (y3 - y2)**2) + ((x3 - x1)**2 + (y3 - y1)**2)
          - ((x2 - x1)**2 + (y2 - y1)**2))/(2*c*b)
    if c1 < c2 and c3 < c2:
        h = sqrt(1 - (c3)**2)*b
        print('Высота проведенная из наименьшего угла h = ''{:7.3f}'.format(h))
    if c1 < c3 and c2 < c3:
        h = sqrt(1 - (c1)**2)*c
        print('Высота проведенная из наименьшего угла h = ''{:7.3f}'.format(h))
    if c2 < c1 and c3 < c1:
        h = sqrt(1 - (c2)**2)*a
        print('Высота проведенная из наименьшего угла h = ''{:7.3f}'.format(h))

    # Является ли треугольньк прямоугольным.
    
    if c1 == 0 or c2 == 0 or c3 == 0:
        print('Треугольник является прямоугольным')
    else:
        print('Треугольник не является прямоугольным')
    try:
        x0, y0 = map(float, input('Введиет координаты точки D = ').split(';'))
    except ValueError:
        print('Введено неверное значение.')
        input('Нажмите Enter, чтобы выйти.')
        exit()

    # Проверяем принадлежность точки треугольнику.

    p1 = (x1 - x0)*(y2 - y1) - (x2 - x1)*(y1 - y0)  # 12
    p2 = (x2 - x0)*(y3 - y2) - (x3 - x2)*(y2 - y0)  # 23
    p3 = (x3 - x0)*(y1 - y3) - (x1 - x3)*(y3 - y0)  # 31
    
    if (p1 <= 0 and p2 <= 0 and p3 <= 0) or (p1 >= 0 and p2 >= 0 and p3 >= 0):
        print('Точка принадлежит треугольнику.')

        # Находим расстояние от точки до ближайшей стороны.

        r1 = abs(p1/a)
        r2 = abs(p2/b)
        r3 = abs(p3/c)
        if r2 >= r1 and r3 >= r1:
            print('Расстояние от точки до ближайшей стороны = ','{:7.3f}'.format(r1))
        if r1 > r2 and r3 >= r2:
            print('Расстояние от точки до ближайшей стороны = ','{:7.3f}'.format(r2))
        if r1 > r3 and r2 > r3:
            print('Расстояние от точки до ближайшей стороны = ','{:7.3f}'.format(r3))

    else:
        print('Точка не принадлежит треугольнику.')
        input('Нажмите Enter, чтобы выйти.')
        exit()
else:
    print('Заданные точки не являются вершинами треугольника.')
    input('Нажмите Enter, чтобы выйти.')
    exit()
