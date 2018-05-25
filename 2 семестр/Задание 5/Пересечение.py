# На пл-ти заданы мн-во точек (int)(n <= 7) А и мн-во треугольников (n <= 4).
# Найти две такие точки из А, что походящая через них прямая пересекается
# с максимальным кол-вом треугольников из В.

print('14 апреля 2017')
print()

from tkinter import *

'''
A = []
n = int(input('Задайте количество точек: '))
for point in range(n):
    print('Введите ', point + 1, 'точку (x y): ', end = '')
    x, y = map(int, input().split())
    A.append([x,y])


m = int(input('Задайте количество треугольников: '))
B = []

for i in range(m):
    B.append([])
for i in range(m):
    for j in range(3):
        print('Введите ',j+1,'вершину ',i+1,'треугольника: ',end='')
        x,y = map(int,input().split())
        B[i].append([x,y])
'''
A = [
        [2, 2],
        [5, 3],
        [11, 3],
        [8, 5],
        [4, 7],
        [12, 7],
        [13, 12]
           ]
B = [
        [[15, 12], [13, 15], [16, 15]],
        [[7, 2], [9, 4], [10, 2]],
        [[1, 0], [3, 2], [2, 3]],
        [[4, 2], [5, 4], [2,5]],
         ]
'''

A = [
    [-8, 4],
    [-3, 8],
    [-3, 9]
]

B = [
    [[-5, 3], [-1, 3], [-3, 2]],
    [[-5, 6], [-1, 6], [-3, 5]],
    [[2, 6], [6, 6], [4, 5]]
]
'''
root=Tk()
canv = Canvas(root,width=500,height=500,bg="snow", cursor="pencil")  # создание холста


lenA = len(A)
lenB = len(B)
maximum = 0

cross = 0  # кол-во переченных строн
count = 0  # кол-во пересеченных треугольников
for i in range(lenA):
    canv.create_text(250 + A[i][0]*20, 250 - A[i][1]*20, text="*", font="Verdana 12",
                     anchor="w",justify=CENTER,fill="purple1") # Текст
    for j in range(i + 1, lenA):

        for k in range(lenB):
            for z in range(0, 2):
                for q in range(1, 3):
                    canv.create_line(250 + B[k][z][0] * 20, 250 - B[k][z][1] *
                                     20, 250 + B[k][q][0]* 20, 250 - B[k][q][1] * 20,
                                     width=1, fill="red")  # линия
                    if z == 1 and q == 1:
                        continue
                    else:
                        ch = (A[j][0] - A[i][0])*(A[i][1] -
                                                  B[k][z][1]) - (A[j][1]
                                        - A[i][1])*(A[i][0] - B[k][z][0])
                        zn = (B[k][q][1] - B[k][z][1])*(A[j][0] -
                        A[i][0]) - (B[k][q][0] - B[k][z][0])*(A[j][1] -
                                                              A[i][1])

                        if zn == 0 or ch/zn == 0:  # параллельны или совпадают
                            break
                        elif 0 <= ch/zn <= 1:  # пересекает
                            cross += 1
                            #print(A[i][0], A[i][1])
            if cross >= 2:
                count += 1
            cross = 0
        if count > maximum:
            maximum = count
            #print(count)
            p1 = i
            p2 = j
        count = 0
print('Координаты точек, через которые проходит прямая,')
print('пересекающая максимальное количество треугольников: \n')

print('1 точка: (', A[p1][0],';', A[p1][1],")")
print('2 точка: (', A[p2][0],';', A[p2][1],')')

x1 = (500 - A[p1][1]*20)*(A[p2][0]*20 - A[p1][0]*20)/(A[p2][1]*20 -
                                                A[p1][1]*20) + A[p1][0]*20
x2 = (0 - A[p1][1]*20)*(A[p2][0]*20 - A[p1][0]*20)/(A[p2][1]*20
                                            - A[p1][1]*20) + A[p1][0]*20


canv.create_line(0, 250, 500, 250, width = 1, fill = "black")  # ось X
canv.create_line(250, 0, 250, 500, width = 1, fill = "black")  # ось у


#canv.create_line(x1, -225, x2, 275, width = 1, fill = "blue")
canv.create_line(253+x1, 0, 253+x2, 500, width = 1, fill = "blue")



canv.pack()
root.mainloop()
