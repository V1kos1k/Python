N = [100, 1000, 10000, 25000, 50000, 100000, 400000, 900000]

from random import *
from time import *
import matplotlib.pyplot as plt

def Xrandom(n):
    X = []
    i = 0
    while i < n - 1:
        k = randrange(0,n)
        X.append(k)
        i += 1
    X.append(0)
    return X

def sort(li):
    start = time()
    def downHeap(li, k, n):
        new_elem = li[k]
        while 2 * k + 1 < n:
            child = 2 * k + 1
            if child + 1 < n and li[child] < li[child + 1]:
                child += 1
            if new_elem >= li[child]:
                break
            li[k] = li[child]
            k = child
        li[k] = new_elem

    size = len(li)
    for i in range(size // 2 - 1, -1, -1):
        downHeap(li, i, size)
    for i in range(size - 1, 0, -1):
        temp = li[i]
        li[i] = li[0]
        li[0] = temp
        downHeap(li, 0, i)
    end = time()
    return li, end - start

print('\nСортировка массивов методом .\n')
print('Количество элементов\t\t\tВремя выполнения')
Period = []
for i in N:
    x1 = Xrandom(i)
    x2, period = sort(x1)
    Period.append(period)
    print(i, '\t\t\t\t\t\t    {:6.4f}'.format(period))




plt.plot(N, Period)
plt.grid(True)
plt.xlabel('Count of elements')
plt.ylabel('Time')
plt.title('Зависимость времени сортировки от размера массива')
plt.show()
