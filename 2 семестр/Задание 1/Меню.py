# Мхитарян ИУ7-24
# Меню для вычисления интеграла методом трапеции

print('10 февраля 2017')

def func(x):
    return x*x

'''def trap(a,b,n):
    h = (b - a)/n
    i = 0
    s = h/2*(func(a) + 2*(func(a + h) + func(a + 2*h)) + func(b))'''

def trap(n):
    s2 = 0
    h = (b-a)/n
    for i in range(n):
        s2 += ((func(a + i * h) + func(a + (i + 1) * h)) / 2) * h
    return s2

choice = None
while choice != 0:
    print(
    '''
            1 - Вычисление интеграла с заданной точностью
            2 - Вычисление интеграла для заданного количества разбиений

            0 - Выход
    '''
    )
    choice = input('Выбор:')
    if choice == '0':
        print('Выход')
        break
    elif choice == '1':
        a, b = map(int, input('Введите начало и конец отрезка ab: ').split())
        eps = float(input('Введите точность эпсилон: '))
        n = 1
        i = 0
        while True:
            i += 1
            k = abs(trap(2*n) - trap(n))
            if k < eps:
                break
            else:
                n = 2*n
        print()
        print('Ответ: {:6.4f}'.format(trap(n)))
        print()
    elif choice == '2':
        a,b = map(int,input('Введите начало и конец отрезка ab: ').split())
        n = int(input('Введите количество разбиений: '))
        print()
        print('Ответ: {:6.4f}'.format(trap(n)))
        print()
