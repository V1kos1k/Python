# Мхитарян ИУ7-14 вариант 7
# Дана строка состоящая из слов.
# Между словами один или несколько пробелов. Сформировать новую строку из слов,
# отличных от первого либо от последнего слова,
# преобразовав каждое из них по следующему правилу:
# перенести все слова, входящие в текст по одному разу.

print('18 ноября 2016')
print()

s = input('Введите строку, состоящую из слов: ')
L = len(s)
X = []

print('Введенная строка: ', s)
print()
# создаем массив со словами из строки

k = 0 
while k < L:
    Sp = '' 
    R = s[k] 
    while 'a' <= R <= 'z' or 'а' <= R <= 'я': 
        Sp += R 
        k += 1 
        if k < L: 
            R = s[k] 
        else: 
            break 
    k += 1 
    if Sp != ' ' and Sp != '': 
        X.append(Sp)

# удаляем первое слово и совпадающие с ним слова из списка

perv = X[0]
k = 0
while k < len(X):
    if X[k] == perv:
        X.remove(X[k])
    k += 1

A = set(X)

stroka = ' '.join(A)
print('Формируем новую строку из слов, отличных от первого '
      'и переносим все слова в новую строку по одному разу')
print()
print('Полученная строка из заданных слов: ', stroka)
