# Мхитарян ИУ7-14
# Вычислить таблицу значений функций a1, a2, a3.
# Построить график одной из функций.
# Определить колличество вычисленных значений функции a2, которые больше 0.

from math import cos, pi, sqrt, fabs
print('Введите начальное и конечное значения аргумента'
      'g при условии, что -100-20 < g < 1000')
gn = float(input('Начальное значение аргумента g :'))
gk = float(input('Конечное значение аргумента g: '))
h = float(input('Введите шаг вычисления функции h: '))
if -1000 < gn < 1000 and -1000 < gk < 1000:

    # Таблица значений

    fmin = 0
    fmax = 0
    print('\n \t\tТаблица значений\n')
    print('   g\t\t     a1\t\t     a2\t\t     a3')
    n = 0  # Кол-во a2 > 0
    b = round(abs(gk - gn)/h)  # Кол-во повторений
    g = gn
    for i in range (b + 1):
        a1 = g**3 + 6.1*g**2 - 35.4*g - 25.7
        if a1 > fmax or fmax == 0:
            fmax = round(a1)
        if a1 < fmin or fmin == 0:
            fmin = round(a1)
        a2 = g**2 - cos(pi)*g
        a3 = sqrt(a1**2 + a2**2)
        if a2 > 0:
            n += 1
        if (0.0001 < fabs(a1) < 10000 and 0.0001 < fabs(a2) < 10000
            and 0.0001 < fabs(a3) < 10000):
            print('{:7.3f} \t {:10.3f} \t {:10.3f}'
                  '\t {:10.3f}'.format(g,a1,a2, a3))
        elif ((fabs(a1) >= 10000 or fabs(a1) <= 0.0001)
              and 0.0001 < fabs(a2) < 10000 and 0.0001 < fabs(a3) < 10000):
            print('{:7.3f} \t {:10.3e} \t {:10.3f}'
                  '\t {:10.3f}'.format(g,a1,a2, a3))
        elif (0.0001 < fabs(a1) < 10000 and (fabs(a2) >= 10000 or fabs(a2) <= 0.0001)
              and 0.0001 < fabs(a3) < 10000):
              print('{:7.3f} \t {:10.3f} \t {:10.3f}'
                  '\t {:10.3f}'.format(g,a1,a2, a3))
        elif (0.001 < fabs(a1) < 10000 and 0.0001 < fabs(a2) < 10000
              and (fabs(a3) >= 10000 or fabs(a3) <= 0.0001)):
            print('{:7.3f} \t {:10.3f} \t {:10.3f}'
                  '\t {:10.3e}'.format(g,a1,a2, a3))
        elif ((fabs(a1) >= 10000 or fabs(a1) <= 0.0001) and
              (fabs(a2) >= 10000 or fabs(a2) <= 0.0001) and 0.0001 < fabs(a3) < 10000):
            print('{:7.3f} \t {:10.3e} \t {:10.3e}'
                  '\t {:10.3f}'.format(g,a1,a2, a3))
        elif (0.0001 < fabs(a1) < 10000 and (fabs(a2) >= 10000 or fabs(a2) <= 0.0001)
              and (fabs(a3) >= 10000 or fabs(a3) <=0.0001)):
            print('{:7.3f} \t {:10.3f} \t {:10.3e}'
                  '\t {:10.3e}'.format(g,a1,a2, a3))
        elif ((fabs(a1) >= 10000 or fabs(a1) <= 0.0001) and
              0.0001 < fabs(a2) < 10000 and (fabs(a3) >= 10000 or fabs(a3) <= 0.0001)):
            print('{:7.3f} \t {:10.3e} \t {:10.3f}'
                  '\t {:10.3e}'.format(g,a1,a2, a3))
        else:
            print('{:7.3f} \t {:10.3e} \t {:10.3e}'
                  '\t {:10.3e}'.format(g,a1,a2, a3))
        g += h
    print('\n Колличество значений функции a2, которые больше 0 = ', n)

    # График функции a1

    print('\n \t График функции a1 = g^3 + 6.1*g^2 - 35.4*g - 25.7')
    print()
    print()
    print('{:10.3e}'.format(fmin),' '*65,'{:10.3e}'.format(fmax))
    print(' '*10,'+','-'*59,'+',sep='')
    g = gn
    # g = правое значние(максимальное) - х // g = fmax - x
    for i in range (b + 1):
        a1 = g**3 + 6.1*g**2 - 35.4*g - 25.7
        m = int(round((a1 - fmin)/(fmax - fmin)*59 + 1))  # пробелы перед *
        if fmin <= 0 and fmax >= 0:
            x = int(round(abs((0 - fmin)/(fmax - fmin)*59 + 1)))
            #print(' '*x,'|')
            if x<m:
                print('{: 8.3f}'.format(g),' '*x,'|',' '*(m-x),'*',sep='')
            elif x>m:
                print('{: 8.3f}'.format(g),' '*m,'*',' '*(x-m-1),'|',sep='')
            elif x==m:
                print('{: 8.3f}'.format(g),' '*(m - 2),'*')
        else:
            print('{: 8.3f}'.format(g),' '*m,'*')
        g += h
else:
    print('g должен соответствовать условию -1000 < g < 1000')
