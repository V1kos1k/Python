# Защита
# Отсортировать массив методом пузырька с флагом

from random import *

def Xrandom(n):
    X = []
    i = 0
    while i < n:
        k = randrange(0,n)
        X.append(k)
        i += 1
    return X

def sort(a):
    f = True
    while f:
        f = False
        for i in range(len(a)-1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                f = True
    return a


M = int(input('Введите размер массива < 10: '))
x1 = list(map(float, input('Введите элемены массива: ').split()))
'''
x1 = Xrandom(M)
'''
print('Изначальный массив: ')
print(x1)
print('Отсортированный массив: ')
print(sort(x1))