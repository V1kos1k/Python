# Сортировка массива режимом вставки
# Сортировка массива режимом вставки с барьером

N = [100, 10000, 10000, 40000, 60000]

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
    return X

'''
# Режим вставки с барьером

def sort(X):
    start = time()
    print(X)
    back = X[0]
    lenn = len(X)
    for i in range(2, lenn):
        if X[i - 1] > X[i]:
            X[0] = X[i]
            j = i - 1
            while X[j] > X[0]:
                X[j + 1] = X[j]
                j -= 1
            X[j + 1] = X[0]
    X[0] = back

    i = 1
    while X[i] < back:
        X[i - 1] = X[i]
        i += 1

    X[i - 1] = back
    end = time()
    print(X)
    return end - start

T = []
def sort(array):
    t1 = time()
    back = array[0]
    len_n = len(array)
    for i in range(2, len_n):
        if array[i - 1] > array[i]:
            array[0] = array[i]
            j = i - 1
            while array[j] > array[0]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = array[0]
    array[0] = back

    i = 1
    while array[i] < back:
        array[i-1] = array[i]
        i += 1
        # тут костыль проверки на выход за границы массива, пока не придумал как без него
        if i == len(array):
            break

    array[i-1] = back
    t2 = time()
    T.append(t2 - t1)
    return t2 - t1

# Вставками
# 1)
def sort(array):
    for i in range(1, len(array)):
        while i > 0 and array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array

# 2)
def sort(X):
    start = time()
    lenn = len(X)
    for i in range(2, lenn):
        k = X[i]
        j = i - 1
        X[0] = k
        while k < X[j]:
            X[j + 1] = X[j]
            j -= 1
            X[j + 1] = k


    end = time()
    return X

# Бинарные вставки

def sort (x):
    t1 = time()
    for i in range(1, len(x)):
        key = x[i]
        left = 0
        right = i
        while right > left:
            mid = int(left+right) // 2
            if x[mid] < key:
                left = mid+1
            else:
                right = mid-1

        for j in range(i-1, left-1, -1):
            x[j+1] = x[j]
        x[left] = key
    dt = time() - t1
    return(x)

# Пузырек

def sort (x):
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] > x[j]:
                x[j], x[i] = x[i], x[j]
    return(x)

# Улучшенный пузырек

def sort(A):
    t1 = time()
    for i in range(len(A)):
        f = 0
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                f = 1
        if f == 0:
            break
    dt = time() - t1
    return A

# Пузырек с флагом

def sort(a):
    f = True
    while f:
        f = False
        for i in range(len(a)-1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                f = True
    return a
'''
# Пирамидальная

def sort(li):
    """Сортирует список в возрастающем порядке с помощью алгоритма пирамидальной сортировки"""
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
    return end - start
'''
# Простым выбором

def sort1(A):
    for i in range(N):
        min = 100
        for j in range(i,N):
            if A[j] < min:
                min = A[j]
                poz = j
        A[poz], A[i] = A[i], A[poz]
    return A

# Шелла

def sort(A = []):
    start = time()
    for i in range(len(A)):
        flag = 0
        for j in range(len(A)-1):
            if A[j] > A[j + 1]:
                A[j] , A[j + 1] = A[j + 1] , A[j]
                flag = 1
        if flag == 0:
            break
    end = time()
    return A

# Быстрая

def sort (x):
    if len(x) <= 1:
        return(x)
    else:
        q = x[len(x) // 2]
        l = []
        m = []
        r = []
        for i in range(len(x)):
            if x[i] < q:
                l.append(x[i])
            elif x[i] == q:
                m.append(x[i])
            else:
                r.append(x[i])

        return(sort(l) + m + sort(r))

# Шейкер

def sort (x):
    left = 0
    right = len(x)-1

    while left <= right:
        for i in range(left, right):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
        right = right - 1

        for i in range(right, left, -1):
            if x[i-1] > x[i]:
                x[i-1], x[i] = x[i], x[i-1]
        left = left + 1

    return(x)


# Выбором
def sort(mylist):
    for k in range(len(mylist) - 1):
        m = k
        i = k + 1
        while i < len(mylist):
            if mylist[i] < mylist[m]:
                m = i
            i += 1
        t = mylist[k]
        mylist[k] = mylist[m]
        mylist[m] = t
    return mylist






def graphic(sort_type, array_lengths):
    X = [str(i) for i in range(len(array_lengths))]
    X_ticks = [str(i) for i in array_lengths]
    Y = [set_time(sort_type, generate_array(i)) for i in array_lengths]
    plt.plot(X, Y)
    plt.xticks([i for i in range(len(X_ticks))], X_ticks)
    plt.title('Сортировка: quick-sort')
    plt.ylabel('Time')
    plt.xlabel('Array length')
    plt.show()


print('\nСортировка массивов методом прямых вставок с барьером.\n')
print('Количество элементов\t\t\tВремя выполнения')
for i in N:
    x1 = Xrandom(i)
    x2 = sort(x1)
    print(i, '\t\t\t\t\t\t    ', x2)

graphic(sort, N)

plt.plot(N, T)
plt.grid(True)
plt.xlabel('Count of elements')
plt.ylabel('Time')
plt.show()
'''

def generate_array(array_length=1000, ot=-1000, till=1000):
    return [randint(ot, till) for i in range(array_length)]

# Выбором
def choose_sort(array):
    for i in range(len(array)):
        min_ind = i
        for j in range(i, len(array)):
            if array[min_ind] > array[j]:
                min_ind = j
        array[i], array[min_ind] = array[min_ind], array[i]

    return array


# фунция проверки длинны массива
def array_length_check(array, required_length=1):
    if len(array) >= required_length:
        return True
    else:
        return False


for n in N:
    # 100500 тестов интересные 3-5 и 9, 10, иногда 7 и 8
    x1 = generate_array(n)
    test1 = [-1, -1, -1]
    test2 = [0, 0, 0]
    test3 = []
    test4 = [-1]
    test5 = [1]
    test6 = [-1, 1, -1, 1]
    test7 = [-1, 1, -1]
    test8 = [-1, -1, 1]
    test9 = [935, 929, -601, 436, 315, 911, 335, -910, -258, 506]
    test10 = [1, -1]

    # ввод типа соритровки
    sort_type = choose_sort

    print(x1)
    print(sort_type(x1))
    print('test1 ', sort_type(test1))
    print('test2 ', sort_type(test2))

    # 2-5 тесты по умолчанию работать не будут, чтобы их проверить надо поменять 2-й аргумент на 0
    if array_length_check(test3, 2):
        print('test3 ', sort_type(test3))
    if array_length_check(test4, 2):
        print('test4 ', sort_type(test4))
    if array_length_check(test5, 2):
        print('test5 ', sort_type(test5))
    print('test6 ', sort_type(test6))
    print('test7 ', sort_type(test7))
    print('test8 ', sort_type(test8))
    print('test9 ', sort_type(test9))
    print('test10 ', sort_type(test10))


# засекание времении
def set_time(sort_type, array):
    import time
    start = time.clock()
    sort_type(array)
    end = time.clock()
    return end - start


# график зависимости времени от кол-ва
def graphic(sort_type, array_lengths):
    X = [str(i) for i in range(len(array_lengths))]
    X_ticks = [str(i) for i in array_lengths]
    Y = [set_time(sort_type, generate_array(i)) for i in array_lengths]
    plt.plot(X, Y)
    plt.xticks([i for i in range(len(X_ticks))], X_ticks)
    plt.title('Сортировка: quick-sort')
    plt.ylabel('Time')
    plt.xlabel('Array length')
    plt.show()