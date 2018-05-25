# Задается большой отрезок. Найти большой отрезок с шагом h.
# Находим отрезки, где есть один корень и уточняем его с заданной точностью.
# Исходные данные: a, b, h, eps, abs(x2 - x1) < eps (значение ф-ии < eps2),
# максимальное число итераций.
# Вывод: полученный корень (6 - 9 знаков), значение ф-ии в т. корня,
# реальное число итераций,код ошибки (0-нет ошибки,1-нет кореня при max кол-ве итераций),
# название ф-ии, таблица.

print('9 марта 2017')

import numpy as np
from math import sin, cos, sqrt, fabs
import matplotlib.pyplot as plt
import time


def func(x):
    return np.sin(x)*x

def derivative(x):
    return np.cos(x)*x + np.sin(x)

def derivative2(x):
    return -1*np.sin(x)*x + 2*np.cos(x)



begin, end = map(float, input('Введите начало и конец отрезка ab: ').split())
h = float(input('Введите шаг разделения отрезка h: '))
eps = float(input('Введите точность эпсилон eps: '))
iteration = int(input('Введите максимальное число итераций: '))

# ПЕРВАЯ ЧАСТЬ

LeftLimit = []  # левые границы
RightLimit = []  #  правые границы
LeftLimitForEx = []
RightLimitForEx = []
LeftLimitForBend = []
RightLimitForBend = []
CharacterX = []  #
X = []  # значения х
Count = []  # значения количества итераций
Code = []
Extrem = []
Bend = []

present = begin
fi = (1 + sqrt(5))*0.5  # пропорция золотого сечения


kon = end

while ((fabs(begin) + fabs(end))/h - int((fabs(begin) + fabs(end))/h)) != 0:
    end += 1

for i in range(int((fabs(begin) + fabs(end))/h)):  # середина отрезка
    if (func(present)*func(present + h) <= 0):  # проверка на наличие корня
        a = present      # новая левая граница
        if present + h < end:
            b = present + h
        else:
            b = kon

        LeftLimit.append(a)
        RightLimit.append(b)

        count = 0  # подсчет итераций

        while fabs(b - a) > eps:
            x2 = b - (b - a)/fi
            x1 = a + (b - a)/fi
            if fabs(x1) > fabs(x2):
                x = x1
            else:
                x = x2
            if func(x)*func(a) <= 0:
                b = x
            else:
                a = x
            count += 1
        X.append(x)
        Count.append(count)
    present += h
    if present > kon:
        present -= h
        break

if X != []:
    plt.plot(X[0], func(X[0]), 'ro', color = 'black', label = 'Korni')
    for i in range(1, len(X)):
        plt.plot(X[i], func(X[i]), 'ro', color='black')




# проверка на ошибку

if X == []:
    Error = 'Корнии не найдены.'
    code = 1

else:
    for i in range(len(X)):
        if Count[i] > iteration:
            Error = 'Превышено количество итераций.'
            code = 2
        else:
            code = 0
        Code.append(code)


print()
if code == 1:
    print('Ошибка!')
    print(Error)
    print('Код ошибки: ', code)
    print()


# ВЫВОД ТАБЛИЦЫ
else:
    print('Уточнение корней методом золотого сечения: ')
    print()
    print('№ корня \t\t Xn \t\t Xn+1 \t\t\t    X \t\t\t f(X) \t\t Количество итераций \t Код ошибки')

for i in range(len(X)):
    if Code[i] == 2:
        print('{:7}'.format(i + 1), end='    ')
        print('{:9.2f}'.format(LeftLimit[i]), end='    ')
        print('{:9.2f}'.format(RightLimit[i]), end='\t\t\t\t')
        print('--', end='\t\t\t   ')
        print('--', end='\t\t\t\t\t ')
        print('{:7}'.format(Count[i]), end='\t\t')
        print('{:7}'.format(Code[i]))
    else:
        print('{:7}'.format(i + 1), end = '    ')
        print('{:9.2f}'.format(LeftLimit[i]), end = '    ')
        print('{:9.2f}'.format(RightLimit[i]), end = '\t\t')
        print('{:10.7f}'.format(X[i]), end = '\t\t')
        print('{:9.1e}'.format(func(X[i])), end = '\t\t\t\t\t ')
        print('{:7}'.format(Count[i]), end = '\t\t')
        print('{:7}'.format(Code[i]))

print()





# ВТОРАЯ ЧАСТЬ

# поиск экстремумов

h = 1
present = begin

if code != 1:

    for i in range(int((fabs(begin) + fabs(end))/h)):  # середина отрезка
        if (derivative(present)*derivative(present + h) <= 0):  # проверка на наличие корня
            a = present      # новая левая граница
            if present + h < end:
                b = present + h
            else:
                b = kon
            a1 = a
            b1 = b
            if derivative(a) <= derivative(b):  # поиск минимума
                while fabs(b1 - a1) >= eps:
                    x1 = b1 - (b1 - a1) / fi
                    x2 = a1 + (b1 - a1) / fi
                    if func(x1) >= func(x2):
                        a1 = x1
                    else:
                        b1 = x2

            elif derivative(a) > derivative(b):  # поиск максимума
                while fabs(b1 - a1) >= eps:
                    x1 = b1 - (b1 - a1) / fi
                    x2 = a1 + (b1 - a1) / fi
                    if func(x1) <= func(x2):
                        a1 = x1
                    else:
                        b1 = x2
            x = (a1 + b1) / 2
            Extrem.append(x)
        present += h
        if present > kon:
            break


    plt.plot(Extrem[0], func(Extrem[0]), 'ro', color = 'green', label = 'Extremum')
    for i in range(1, len(Extrem)):
        plt.plot(Extrem[i], func(Extrem[i]), 'ro', color='green')


    min = max = 0
    for i in range(len(Extrem)):
        if func(Extrem[i]) <= func(min):
            min = Extrem[i]
        if func(Extrem[i]) >= func(max):
            max = Extrem[i]

    Min = []
    for i in range(len(Extrem)):
        if func(Extrem[i]) == func(min):
            Min.append(Extrem[i])

    Max = []
    for i in range(len(Extrem)):
        if func(Extrem[i]) == func(max):
            Max.append(Extrem[i])


    if Min != []:
        plt.plot(Min[0], func(Min[0]), 'ro', color = 'blue', label = 'Minimum')
        for i in range(1, len(Min)):
            plt.plot(Min[i], func(Min[i]), 'ro', color='blue')

    if Max != []:
        plt.plot(Max[0], func(Max[0]), 'ro', color = 'yellow', label = "Maximum")
        for i in range(1, len(Max)):
            plt.plot(Max[i], func(Max[i]), 'ro', color = 'yellow')



    present = begin





# точки перегиба

    a = begin
    b = end
    b1 = a
    a1 = a
    for i in range(int((b-a)//h)):
        b1 += h
        a1 = b1 - h
        if derivative2(a1) * derivative2(b1) <= 0:
            px = a1
            per1 = 100
            for j in range(int((b1-a1)//eps)):
                if fabs(derivative2(px)) < per1:
                    per1 = fabs(derivative2(px))
                    pxx = px
                px = px+eps
            Bend.append(pxx)


    if Bend != []:
        plt.plot(Bend[0], func(Bend[0]), 'ro', color = 'cyan', label = 'Peregib')
        for i in range(1, len(Bend)):
            plt.plot(Bend[i], func(Bend[i]), 'ro', color='cyan')

    print('Время работы программы: ', time.clock(), ' секунд.')



    xAxis = np.linspace(begin, kon, 100)
    #for1stFunction = func(xAxis)
    plt.axis([begin - 2, end + 2, -5, 10])


    plt.plot(np.linspace(-100, 100), np.linspace(0, 0), 'k', linewidth = 1.5)
    plt.plot(np.linspace(0, 0), np.linspace(-100, 100), 'k', linewidth = 1.5)
    plt.plot(xAxis,  color = 'red')     # функция #1
    plt.title('y = sin(x) * x')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()