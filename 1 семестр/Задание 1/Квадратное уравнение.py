#  Мхитарян Виктория ИУ7-14
#  13 сентября 2016

from math import sqrt
print ('Введите число a=')
a=int(input())
print ('Введите число b=')
b=int(input())
print ('Введите число c=')
c=int(input())
x1=0
x2=0
d=b*b-4*a*c
if a==0:
    if b==0:
        if c==0:
            print('Пустое множество')
        else:
            print('x- любое число')
    else:
        if c==0:
            print('x=0')
        else:
            x=-c/b
            print('x=', x)
else:
    if b==0:
        if c==0:
            print('x=0')
        else:
            x1=sqrt(-c/a)
            x2=-sqrt(-c/a)
            print('x1=',x1,'x2=',x2)
    else:
        if c==0:
            x1=0
            x2=-b/a
            print('x1',x1,'x2=',x2)
        else:
            if a>0:
                x1=(-b+sqrt(d))/2*a
                x2=(-b-sqrt(d))/2*a
            elif d==0:
                x=-b/2*a
                print('x=',x)
            else:
                print('Нет корней')
