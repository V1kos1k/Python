# Мхитарян ИУ7-24
# Даётся текстовый файл, в каждой строке файла 2-3 поля.
# Нужно создать меню:
# 1)Создание файла (открывается пустой файл)
# 2)Добавить в существующий файл новую запись
# 3)Вывести содержимое файла
# 4)Поиск (результат поиска сохраняется в новый файл)
# 5)Выход

print('17 февраля 2017')

X = []
choice = None
while choice != 0:
    print(
        '''
            1 - Создать файл
            2 - Добавить в существующий файл новую запись
            3 - Вывести содержимое файла
            4 - Поиск по году выхода фильма

            0 - Выход
        '''
    )
    choice = input('Выбор:')
    if choice == '0':
        print('Выход.')
        break

    elif choice == '1':
        name = input('Введите название нового файла: ')
        f = open(name + '.txt', 'w')  # открываем пустой файл
        #f.write('Режиссёр \t Название \t Год')
        f.close()

    elif choice == '2':
        s = None
        print('Введите новые данные:')
        f = open(name + '.txt', 'a')
        print('Введите режиссёра, название, и год выпуска:')
        while s != '' and s != ' ':
            s = input()
            f.write(s + ' ' + '\n')
        f.close()

    elif choice == '3':
        name = input('Введите название файла, который вы хотите открыть: ')

        f = open(name + '.txt')
        fr = f.read()
        print(fr)
        f.close()

    elif choice == '4':
        word = input('Введите год выхода фильма: ')
        f = open(name + '.txt')
        s = open('search.txt', 'w')  # создаём файл для записи результата поиска
        sl = 0
        for line in f:
            if (word in line or word.capitalize() in line or
                        word.upper() in line or word.lower() in line or
                        word.title() in line):
                s.write(line)
                sl += 1
                #break
        f.close()
        s.close()
        if sl == 0:
            print('Поиск не дал результатов.')
        else:
            s = open('search.txt')
            sr = s.read()
            print(sr)
            s.close()