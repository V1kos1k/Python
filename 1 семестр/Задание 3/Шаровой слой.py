#  Мхитарян ИУ7-14
#  Найти объём и площадь поверхности шарового слоя.

print('23 сентября 2016')

from math import *
try:
    h = float(input('Введите значение верхней высоты h = '))
    h1 = float(input('Введите значение нижней высоты h1 = '))
    R = float(input('Введите значение радиуса щара R = '))
except ValueError:
    print ('Введено неверное значение')
else:
    if (h<0) or (h1<0) or (R<0):
        print('Введено отрицательное значение')
    else:
        # Находим радиус верхнего среза.
        # Находим радиус нижнего среза.
        # Находим высоту шарового слоя.

        r = sqrt(2*R*h - h*h)
        r1 = sqrt(2*R*h1 - h1*h1)
        H = 2*R - h1 - h

        # Находим объем шарового слоя.
        # Находим площадь поверхности шарового слоя.

        V = 1/2*pi*H*(r*r + r1*r1 + 1/3*H*H)
        S = 2*pi*R*H
        print('Объем шарового слоя V = ''{:7.4f}'.format(V))
        print('Площадь шарового слоя S = ''{:7.4f}'.format(S))
