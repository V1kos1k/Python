 # Мхитарян ИУ7-14 вариант 2
# Программа с использованием функций Python
# Задан текст массивом строк. Найти:
#  +    - самое длинное слово в каждом предложении
#  +    - кол-во слов между самым длинным и самым коротким словами в тексте
#  +    - слово, которое наиболее редко встречается.               (############ДОДЕЛАТЬ№№№№№№№№№№!!!!!!!!)
#  +    Замена арифметического выражения (+/) на результат.
#  +    Выравнивание строк по ширине (число пробелов между словами в строке не должно
#       отличаться больше чем на 1) и по правому краю максимальной строки.
#  +    Замена одного слова другим в указанном предложении (по номеру).
#  +    Удалить из каждой нечётной строки заданное слово.


'''Все проходит: любовь, искусство, планета Земля, вы, я. Смерть настолько
неизбежна, что всех застает врасплох. Как узнать про этот день — не последний
ли он? Вы думаете, что у вас уйма
времени впереди 900 + 100 и 2000 / 2 часов. А потом вдруг — здрасьте пожалуйста! — вы тонете, вы утонули, ваше время
истекло. Смерть — единствення встреча, не записанная в вашем органайзере.'''


print('22 ноября 2016')

N = int(input('Введите количество элементов массива: '))
print('Введите массив, состоящий из строк: ')
X = []
for i in range(N):
    s = input()
    X.append(s)
print()
print()

print('Исходный текст:')
print()
for i in X:
    print(i)
print()

# создаем единый список для всех массивов

poln = ' '.join(X)

poln = poln.lower()

dlin = len(poln)

# массив из слов

Q = []
k = 0
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
            print('+')
            break
    k += 1
    if Sp != ' ' and Sp != '':
        Q.append(Sp)


mnog = set(Q)  # множество из полной строки

W = ' '.join(set(Q))

# массив из mnog
LenW = len(W)

WQ = []
k = 0
while k < LenW:
    Sp = ''
    R = W[k]
    while ('a' <= R <= 'z' or 'а' <= R <= 'я' or 'A' <= R <= 'Z'
           or 'А' <= R <= 'Я' or '0' <= R <= '1' or R == '+' or
                   R == '/'):
        Sp += R
        k += 1
        if k < LenW:
            R = W[k]
        else:
            break
    k += 1
    if Sp != ' ' and Sp != '':
        WQ.append(Sp)


# Задание 1
#  самое длинное слово в каждом предложении

l = 0  # длина текущего слова
lmax = 0  # длина самого длинныго слова
x = ''  # текущее слово
xmax = ''  # самое длинное слово
number = 1
for i in range(dlin):
    if ('a' <= poln[i] <= 'z' or 'а' <= poln[i] <= 'я' or 'A' <= poln[i] <= 'Z'
           or 'А' <= poln[i] <= 'Я'):
        l += 1
        x += poln[i]
    elif poln[i] == ' ':
        if l > lmax:
            lmax = l
            xmax = x
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
print()

# Задание 2
# кол-во слов между самым длинным и самым коротким словами в тексте

# нахождение самого длинного и короткого слова в тексте

qs = ' '.join(Q)
l = 0
x = ''
lmax = 0
lmin = 0
xmax = ''
xmin = ''
for i in range(len(qs)):
    if ('a' <= qs[i] <= 'z' or 'а' <= qs[i] <= 'я' or 'A' <= qs[i] <= 'Z' or
            'А' <= qs[i] <= 'Я'):
        l += 1
        x += qs[i]
    else:
        if qs[i] == ' ':
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

# кол-во слов между самым длинным и самым коротким
count = -1
if imin < imax:
    for i in range(imin, imax):
        if qs[i] == ' ':
            count += 1
elif imin > imax:
    for i in range(imax, imin):
        if qs[i] == ' ':
            count += 1
if count == -1:
    print('Количество слов между самым длинным (', xmax, ') и самым коротким (',
          xmin, ') словами в тексте: 0')
else:
    print('Количество слов между самым длинным (', xmax,') и самым коротким (',
        xmin,') словами в тексте: ', count)
print()

# Задание 3
# слово, которое наиболее редко встречается


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
# Замена арифметического выражения (+/) на результат.


w = len(X)
MAS = []  # массив из всех знаков
for i in range(w):
    k = 0
    mas = []
    LenXi = len(X[i])
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
            mas.append(Sp)
        if  R == '!' or R == '.' or R == '?':
            mas.append(R)
        k += 1
    MAS.append(mas)

NOV = []
LenM = len(MAS)
for i in range(LenM):
    nov = []
    lmi = len(MAS[i])
    j = 0
    while j < lmi - 1:
        if MAS[i][j + 1] != '+' and MAS[i][j + 1] != '/':
            nov.append(MAS[i][j])
            j += 1
        elif MAS[i][j + 1] == '+':
            pred = int(MAS[i][j])
            posl = int(MAS[i][j + 2])
            calc = str(pred + posl)
            nov.append(calc)
            j += 3
        elif MAS[i][j + 1] == '/':
            pred = int(MAS[i][j])
            posl = int(MAS[i][j + 2])
            calc = str(pred / posl)
            nov.append(calc)
            j += 3
    if MAS[i][j - 3] != '+' and MAS[i][j - 3] != '/':
        nov.append(MAS[i][lmi - 1])
    if MAS[i][j - 4] != '+' and MAS[i][j - 4] != '/' and (MAS[i][j] == '.' or
                                        MAS[i][j] == ',' or MAS[i][j] == '?' or MAS[i][j] == '!'):
        nov.append(MAS[i][j])
    NOV.append(nov)

#i = len(NOV) - 1
#j = len(NOV[i]) - 1
#del (NOV[i][j])


#print('Текст с заменой арифметических выражений + / :')
#print()
#for i in range(LenM):
#    p = ' '.join(NOV[i])
#    print(p)
#print()


# Задание 6
# Замена одного слова другим в указанном предложении (по номеру).

M = int(input('Введите номер предложения, в котором нужно заменить слово: '))
slovo = input('Введите слово, которое нужно заменить: ')
zamena = input('Введите слово на которое нужно заменить: ')
print()

q = []
num = 1  # подсчет предложений
for i in range(LenM):
    w = []
    lenn = len(NOV[i])
    for j in range(lenn):
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
                    w.append(zamena + ',')
                elif NOV[i][j] == slovo + ':':
                    w.append(zamena + ':')
                elif NOV[i][j] == '(' + slovo:
                    w.append('(' + zamena)
                elif NOV[i][j] == slovo + ')':
                    w.append(zamena + ')')
                elif NOV[i][j] == '(' + slovo + ')':
                    w.append('(' + zamena + ')')
                else:
                    w.append(zamena)
            else:
                w.append(NOV[i][j])
        else:
            w.append(NOV[i][j])
    q.append(w)

'''print('Текст с заменой слова "', slovo,'" на слово "', zamena,'":')
print()
for i in range(LenM):
    p = ' '.join(q[i])
    print(p)
print()'''
# Задание 7
# Удалить из каждой нечётной строки заданное слово.

ydal = (input('Введите слово, которое нужно удалить из каждой нечётной строки: '))

nav = []
for i in range(LenM):
    nov = []
    lenm = len(q[i])
    for j in range(lenm):
        if i + 1 % 2 != 0:
            if q[i][j] == ydal or q[i][j] == ydal.capitalize() or\
                    q[i][j] == ydal + ',' or q[i][j] == ydal + ':' or\
                            q[i][j] == '(' + ydal or q[i][j] == ydal + ')' or\
                            NOV[i][j] == slovo.upper() or \
                            NOV[i][j] == slovo.lower():
                continue
            else:
                nov.append(q[i][j])
        else:
            nov.append(q[i][j])
    #nav1.append(nov)
    nav.append(nov)


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
for i in range(LenM):
    p = ' '.join(nav[i])
    print(p)'''

print()
# Самое длинное предложение
lmax = 0
for i in range(LenM):
    no = ' '.join(nav2[i])
    lenn = len(no)
    if lenn > lmax:
        lmax = lenn
        ind = i

# по правому краю

NO = []
print('Текст, выравненный по правому краю максимальной строки:')
print()
for i in range(LenM):
    no = ' '.join(nav2[i])
    NO.append(no)
    print(no.rjust(lmax))
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
