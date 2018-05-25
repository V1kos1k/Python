# защита Мхитарян

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
    [-3, 2],
    [-4, 2],
    [-4, 3],
    [-1, 4],
    [3, 2],
    [3, 4]
]

B = [
    [[-5, 1], [-5, 5], [-1, 1]],
    [[2, 3], [2, 6], [4, 4]],
    [[4, 1], [5, 1], [5, 2]]
]


root=Tk()
canv = Canvas(root,width=500,height=500,bg="snow",
              cursor="pencil")  # создание холста

lenA = len(A)
lenB = len(B)
maximum = 0


n = 0
for i in range(lenA):
    count = 0
    canv.create_text(250 + A[i][0]*20, 250 - A[i][1]*20, text="*",
        font="Verdana 12", anchor="w",justify=CENTER,fill="purple1") # Текст

    for k in range(lenB):
        
        p1 = (B[k][0][0] - A[i][0])*(B[k][1][1] -
                            B[k][0][1]) - (B[k][1][0] - B[k][0][0])*(B[k][0][1]
                                                            - A[i][1])
        p2 = (B[k][1][0] - A[i][0])*(B[k][2][1] -
                            B[k][1][1]) - (B[k][2][0] - B[k][1][0])*(B[k][1][1]
                                                            - A[i][1])
        p3 = (B[k][2][0] - A[i][0])*(B[k][0][1] -
                            B[k][2][1]) - (B[k][0][0] - B[k][2][0])*(B[k][2][1]
                                                            - A[i][1])
        #print(p1, p2, p3)
        if (p1 <= 0 and p2 <= 0 and p3 <= 0) or (p1 >= 0 and p2 >= 0 and
                                                 p3 >= 0):
            count += 1
            #print('count ', count)
        if count > maximum:
            maximum = count
            t = k
            n = 1
            #print('+', maximum)
if n == 0:
    print("Нет точек в треугольниках")
else:
    for k in range(lenB):
        if k != t:
            canv.create_line(250 + B[k][0][0] * 20, 250 - B[k][0][1] *
                            20, 250 + B[k][1][0]* 20, 250 - B[k][1][1] * 20,
                                     width=2, fill="red")  # линия
        canv.create_line(250 + B[k][1][0] * 20, 250 - B[k][1][1] *
                            20, 250 + B[k][2][0]* 20, 250 - B[k][2][1] * 20,
                                     width=2, fill="red")  # линия
        canv.create_line(250 + B[k][0][0] * 20, 250 - B[k][0][1] *
                            20, 250 + B[k][2][0]* 20, 250 - B[k][2][1] * 20,
                                     width=2, fill="red")  # линия
    else:
        canv.create_line(250 + B[t][0][0] * 20, 250 - B[t][0][1] *
                            20, 250 + B[t][1][0]* 20, 250 - B[t][1][1] * 20,
                                     width=2, fill="blue")  # линия
        canv.create_line(250 + B[t][1][0] * 20, 250 - B[t][1][1] *
                            20, 250 + B[t][2][0]* 20, 250 - B[t][2][1] * 20,
                                     width=2, fill="blue")  # линия
        canv.create_line(250 + B[t][0][0] * 20, 250 - B[t][0][1] *
                            20, 250 + B[t][2][0]* 20, 250 - B[t][2][1] * 20,
                                     width=2, fill="blue")  # линия

canv.create_line(0, 250, 500, 250, width = 1, fill = "black")  # ось X
canv.create_line(250, 0, 250, 500, width = 1, fill = "black")  # ось у
#print(t)
canv.pack()
root.mainloop()
