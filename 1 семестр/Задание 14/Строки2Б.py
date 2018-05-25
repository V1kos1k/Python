# Мхитарян ИУ7-14 вариант 2
# Программа без использования функций Python
# Задан текст массивом строк. Найти:
#  +    - самое длинное слово в каждом предложении
#  +    - кол-во слов между самым длинным и самым коротким словами в тексте   (ИСПРАВИТЬ!!!!!!)
#  +    - слово, которое наиболее редко встречается.
# Замена арифметического выражения (+/) на результат.
# Выравнивание строк по ширине (число пробелов между словами в строке не должно
# отличаться больше чем на 1) и по правому краю максимальной строки.
# Замена одного слова другим в указанном предложении (по номеру).
# Удалить из каждой нечётной строки заданное слово.


print('5 декабря 2016')

N = int(input('Введите количество элементов массива: '))
print('Введите массив, состоящий из строк: ')
X = [0]*N
k = 0
while k < N:
    s = input()
    X[k] = s
    k += 1
print()

print('Исходный текст:')
print()
k = 0
while k < N:
    print(X[k])
    k += 1
print()

# создаём единый список для всех массивов

poln = ''
k = 0
while k < N:
    poln += X[k]
    k += 1

dlin = len(poln)  # длина строки poln

nslov = 0  # кол-во слов со знаками

i = 0


kol = 0  # кол-во слов
znak = 0  # кол-во знаков

# Задание 1

i = 0
l = 0  # длина текущего слова
lmax = 0  # длина самого длинныго слова
x = ''  # текущее слово
xmax = ''  # самое длинное слово
number = 1
while i < dlin:
    if ('a' <= poln[i] <= 'z' or 'а' <= poln[i] <= 'я' or
                    'A' <= poln[i] <= 'Z' or 'А' <= poln[i] <= 'Я'):
        l += 1
        x += poln[i]
    elif poln[i] == ' ':
        if l > lmax:
            lmax = l
            xmax = x
        kol += 1
        l = 0
        x = ''
    elif poln[i] == '.' or poln[i] == '?' or poln[i] == '!':
        if l > lmax:
            lmax = l
            xmax = x
        print('Самое длинное слово в ', number, ' предложении: ', xmax)
        number += 1
        lmax = 0
        xmax = ''
        l = 0
        x = ''
    i += 1
print()

# Задание 2

i = 0
qs = ''
kzn = 0  # кол-во знаков
while i < dlin:
    if ('a' <= poln[i] <= 'z' or 'а' <= poln[i] <= 'я' or 'A' <= poln[i] <= 'Z' or
                    'А' <= poln[i] <= 'Я' or poln[i] == ' '):
        qs += poln[i]
        kzn += 1
    i += 1

i = 0
l = 0
x = ''
lmax = 0
lmin = 0
xmax = ''
xmin = ''
while i < kzn:
    if ('a' <= qs[i] <= 'z' or 'а' <= qs[i] <= 'я' or 'A' <= qs[i] <= 'Z' or
            'А' <= qs[i] <= 'Я'):
        l += 1
        x += qs[i]
    else:
        if qs[i] == ' ' and x != '':
            if l > lmax:
                lmax = l
                xmax = x
                imax = i
            if l < lmin or lmin == 0:
                lmin = l
                xmin = x
                imin = i
            l = 0
            x = ''
    i += 1


count = -1
if imin < imax:
    while imin < imax:
        if qs[imin] == ' ' and qs[imin - 1] != ' ':
            count += 1
        imin += 1
elif imin > imax:
    while imax < imin:
        if qs[imax] == ' ' and qs[i - 1] != ' ':
            count += 1
        imax += 1
print('Количество слов между самым длинным (', xmax,') и самым коротким (',
        xmin,') словами в тексте: ', count)
print()



# Задание 3

Q = []
k = 0
i = 0
while k < dlin:
    Sp = ''
    R = poln[k]
    while ('a' <= R <= 'z' or 'а' <= R <= 'я' or 'A' <= R <= 'Z'
           or 'А' <= R <= 'Я'):
        Sp += R
        k += 1
        if k < dlin:
            R = poln[k]
        else:
            break
    k += 1
    if Sp != ' ' and Sp != '':
        Q += [Sp]
        i += 1

Lenq = len(Q)
WQ = [0]*Lenq
i = 0
z = 0
while i < Lenq:
    if Q[i] not in WQ:
            WQ[z] = Q[i]
            z += 1
    i += 1

LenQ = len(Q)  # длина массива из всех слов
LenWQ = len(WQ)  # длина множества из Q
minpovtor = 0
c = 0
for i in range(LenWQ):
    povtor = 0
    for j in range(LenQ):
        if WQ[i] == Q[j]:
            povtor += 1
            slv = WQ[i]
            c += 1
    if povtor < minpovtor or minpovtor == 0:
        minpovtor = povtor
        xminpovt = slv
#if c == LenQ:
#    print('В данном тексте нет повторяющихся слов.')
#else:
print('Слово, которе наиболее редко встречается в тексте: ', xminpovt)
print()


# Задание 4



w = len(X)
MAS = []  # массив из всех знаков
i = 0
while i < w:
    k = 0
    LenXi = len(X[i])
    mas = []
    c = 0
    while k < LenXi:
        Sp = ''
        R = X[i][k]
        while 'a' <= R <= 'z' or 'а' <= R <= 'я' or '0' <= R <= '9' or \
                        R == '/' or R == '+' or R == '*' or \
                        R == '(' or R == ')' or R == '=' or \
                        R == '-' or 'A' <= R <= 'z' or \
                        'А' <= R <= 'Я' or R == ',' or R == ':' or R == '—':
            Sp += R
            k += 1
            if k < LenXi:
                R = X[i][k]
            else:
                break
        if Sp != ' ' and Sp != '':
            mas += [Sp]
            c += 1
        if R == '!' or R == '.' or R == '?':
            mas += [R]
            c += 1
        k += 1
    MAS += [mas]
    i += 1


NOV = []
LenM = len(MAS)
for i in range(LenM):
    lmi = len(MAS[i])
    nov = []
    j = 0
    z = 0
    while j < lmi - 1:
        if MAS[i][j + 1] != '+' and MAS[i][j + 1] != '/':
            nov += [MAS[i][j]]
            j += 1
            z += 1
        elif MAS[i][j + 1] == '+':
            pred = int(MAS[i][j])
            posl = int(MAS[i][j + 2])
            calc = str(pred + posl)
            nov += [calc]
            z += 1
            j += 3
        elif MAS[i][j + 1] == '/':
            pred = int(MAS[i][j])
            posl = int(MAS[i][j + 2])
            calc = str(pred / posl)
            nov += [calc]
            z += 1
            j += 3
    if MAS[i][j - 3] != '+' and MAS[i][j - 3] != '/':
        nov.append(MAS[i][lmi - 1])
    if MAS[i][j - 4] != '+' and MAS[i][j - 4] != '/' and (MAS[i][j] == '.' or
                                        MAS[i][j] == ',' or MAS[i][j] == '?' or MAS[i][j] == '!'):
        nov += [MAS[i][j]]
        z += 1
    NOV += [nov]


#i = len(NOV) - 1
#j = len(NOV[i]) - 1
#del (NOV[i][j])
'''print('Текст с заменой арифметических выражений + / :')
print()
i = 0
while i < len(NOV):
    j = 0
    while j < len(NOV[i]):
        print(NOV[i][j], end=' ')
        j += 1
    print()
    i += 1
print()'''


# Задание 6

M = int(input('Введите номер предложения, в котором нужно заменить слово: '))
slovo = input('Введите слово, которое нужно заменить: ')
zamena = input('Введите слово на которое нужно заменить: ')
print()

q = []
num = 1  # подсчет предложений
i = 0
while i < LenM:
    w = []
    lenn = len(NOV[i])
    j = 0
    while j < lenn:
        if NOV[i][j] == '.' or NOV[i][j] == '!' or NOV[i][j] == '?':
#            if NOV[i][j] == '.':
#                NOV[i][j - 1] == NOV[i][j - 1] + '.'
#                NOV[i][j] == []
            num += 1
        if NOV[i][j] == slovo or NOV[i][j] == slovo.capitalize() or\
                    NOV[i][j] == slovo + ',' or NOV[i][j] == slovo + ':' or\
                NOV[i][j] == '(' + slovo or NOV[i][j] == slovo + ')' or\
                NOV[i][j] == '(' + slovo + ')' or NOV[i][j] == slovo.upper() or\
                NOV[i][j] == slovo.lower():
            if num == M:
                if NOV[i][j] == slovo + ',':
                    w += [zamena + ',']
                elif NOV[i][j] == slovo + ':':
                    w += [zamena + ':']
                elif NOV[i][j] == '(' + slovo:
                    w += ['(' + zamena]
                elif NOV[i][j] == slovo + ')':
                    w += [zamena + ')']
                elif NOV[i][j] == '(' + slovo + ')':
                    w + ['(' + zamena + ')']
                else:
                    w += [zamena]
            else:
                w += [NOV[i][j]]
        else:
            w += [NOV[i][j]]
        j += 1
    q += [w]
    i += 1

'''print('Текст с заменой слова "', slovo,'" на слово "', zamena,'":')
print()

i = 0
while i < len(q):
    j = 0
    while j < len(q[i]):
        print(q[i][j], end=' ')
        j += 1
    print()
    i += 1
print()'''

# Задание 7

ydal = (input('Введите слово, которое нужно удалить из каждой нечётной строки: '))
print()
nav = []
i = 0
while i < LenM:
    nov = []
    lenm = len(q[i])
    j = 0
    while j < lenm:
        if i + 1 % 2 != 0:
            if q[i][j] == ydal or q[i][j] == ydal.capitalize() or\
                    q[i][j] == ydal + ',' or q[i][j] == ydal + ':' or\
                            q[i][j] == '(' + ydal or q[i][j] == ydal + ')' or \
                            NOV[i][j] == slovo.upper() or\
                            NOV[i][j] == slovo.lower():
                j += 1
                continue
            else:
                nov += [q[i][j]]
        else:
            nov += [q[i][j]]
        j += 1
    nav += [nov]
    i += 1

i = 0
nav2 = []
while i < LenM:
    lenm = len(nav[i])
    nav1 = []
    j = 0
    while j < lenm - 1:
        if nav[i][j + 1] == '.':
            nav1 += [nav[i][j] + '.']
            j += 1
        elif nav[i][j + 1] == '!':
            nav1 += [nav[i][j] + '!']
            j += 1
        elif nav[i][j + 1] == '?':
            nav1 += [nav[i][j] + '?']
            j += 1
        if nav[i][j] == '.' or nav[i][j] == '!' or nav[i][j] == '?':
            j += 1
            continue
        else:
            nav1 += [nav[i][j]]
        j += 1
    nav1 += [nav[i][lenm - 1]]
    nav2 += [nav1]
    i += 1

i = len(nav2) - 1
j = len(nav2[i]) - 1
del (nav2[i][j])

i = 0
while i < len(nav2) -1:
    j = len(nav2[i]) - 1
    if nav2[i][j] == '!' or nav2[i][j] == '?' or nav2[i][j] == '.':
        del nav2[i][j]
    i += 1
'''print('Текст в котором из каждой нечётной строки удалено слово "', ydal,'":')
print()
i = 0
while i < len(nav):
    j = 0
    while j < len(nav[i]):
        print(nav[i][j], end=' ')
        j += 1
    print()
    i += 1
print()'''

# Задание 5

lmax = 0
i = 0
while i < LenM:
    no = ' '.join(nav2[i])
    lenn = len(no)
    if lenn > lmax:
        lmax = lenn
        ind = i
    i += 1

# по правому краю

NO = []
print('Текст, выравненный по правому краю максимальной строки:')
print()
i = 0
while i < LenM:
    no = ' '.join(nav2[i])
    dl = lmax - len(no)
    NO += [no]
    print(' '*dl, no)
    i += 1
print()

# по ширине

print('Текст, выравненный по ширине: ')
print()

maxi = 0
maxis = ''
j = 0
SP = []
n_strk = ''
for i in range(len(NO)):
    if len(NO[i]) > maxi:
        maxi = len(NO[i])
        maxis = NO[i]
rasn = 0
space = []
s_count = 0
n_strk = ''
y = 0
s = 0
maxis = len(maxis)
for k in NO:
    K = list(k.split())
    for l in range(len(K)):
        s += 1
    s_count = s - 1
    space = [' ']*s_count
    rasn = maxis - len(k)
    for i in range(rasn):
        space[i % s_count] += ' '
    for e in k:
        if e != ' ':
            n_strk += e
        elif e == ' ' and y != len(space):
            n_strk += space[y]
            y += 1
    print('',n_strk)
    rasn = 0
    space = []
    s_count = 0
    n_strk = ''
    y = 0
    s = 0
print()