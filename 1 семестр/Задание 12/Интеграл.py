# Мхитарян ИУ7-14
# 1)Вычислить интеграл методом срединных прямоугольников и методом 3/8
# 2)Вычислить интеграл 1-м методом с заданной точностью эпсилон, нужно выбирать
# метод, который даёт меньшую точность
# 3) Вычислить абсолютную и относительную ошибки.

print('9 ноября 2016')
def func(x):
    return x*x

def srednie(n):
    h = (b - a)/n  # шаг
    integral = 0
    x = 0
    y = 0
    for i in range(n):
        x = a + h*i + h/2
        y += func(x)
    integral = y*h
    return(integral)


def tri(n):
    integral = 0
    if n % 3 == 0:
        integral = func(a) + func(b)
        h = (b - a)/n
        for i in range(3, n, 3):
            integral += 2*func(a + h*i)
        for i in range(1, n, 3):
            integral += 3*func(a + h*i)
        for i in range(2, n, 3):
            integral += 3*func(a + h*i)
        integral *= 3*h/8
    return integral


a, b = map(int, input('Введите начало и конец отрезка ab: ').split())
n1 = int(input('Введите первое колличество разбиений n1: '))
n2 = int(input('Введите второе колличество разбиений n2: '))
eps = float(input('Введите точность эпсилон: '))
print()
print()
print(' Метод \t\t\t\t n1 =', n1,' \t n2 = ', n2)
print(' Средние прямоугольники \t {:4.6f}'
      '\t {:4.6f}'.format(srednie(n1), srednie(n2)))
t1 = tri(n1)
t2 = tri(n2)
if t1 == 0 and t2 == 0:
    print(' 3/8   \t\t\t\t ---- \t\t  ----')
elif t1 != 0 and t2 == 0:
    print(' 3/8   \t\t\t\t {:4.6f} \t ----'.format(tri(n1)))
elif t1 == 0 and t2 != 0:
    print(' 3/8   \t\t\t\t ---- \t\t {:4.6f}'.format(tri(n2)))
elif t1 != 0 and t2 != 0:
    print(' 3/8   \t\t\t\t {:4.6f} \t {:4.6f}'.format(tri(n1), tri(n2)))
print()


#print('3/8:', tri8(n1), tri8(n2))



# II часть
n = 1
print('Так как метод срединных прямоугольников вычисляется с меньшей точностью'
      ', чем метод 3/8, то мы находим интеграл с заданной точностью с '
          'помощью метода срединных прямоугольников.')
print()
Itoch = b**3/3 - a**3/3
print('Точная: ', Itoch)
while abs(srednie(2*n) - srednie(n)) > eps:
    n *= 2
print('Вычисленный интеграл с точностью эпсилон: {:4.6f}'.format(srednie(2*n)))
# Абсолютная ошибка

absolut = abs(Itoch - srednie(2*n))

# Относительная ошибка
otnos = abs((Itoch - srednie(2*n))/Itoch)
print('Абсолютная ошибка : {:4.5f}'.format(absolut))
print('Относительная ошибка : {:4.5f}'.format(otnos))
print('Колличество разбиений отрезка : ', 2*n)
