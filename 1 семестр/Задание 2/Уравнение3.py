#  Мхитарян ИУ7-17
#  Решить уравнение

print('16.09.2016')

try:
    print('Введите число x=')
    x=int(input())
except ValueError:
    print('Ошибка при записи')
else:
    a=(x+2)
    b=pow((x+2),2)
    c=pow((x+2),4)
    Z=a*(b+3)/(c+b+3)
    print('{:7.5f}'.format(Z))
