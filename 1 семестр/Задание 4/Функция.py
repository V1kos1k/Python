#  Мхитарян ИУ7-14
#  Вычислить K, получить решение для двух значений аргументов

print('19 сентября 2016')

from math import *
try:
    N=int(input('Введите значение аргумента N = '))
except ValueError:
    print('Ошибка при записи')
else:
    if N<=0:
        K=pow(N,2)-8*N+5
        print('K = ', K)
    else:
        K=log(pow(N,4))-98.75*N/15
        print('K = ', K)
