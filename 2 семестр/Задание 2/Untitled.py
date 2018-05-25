# Защита файлов

f1 = open('f1.txt', 'a')

f1.write('\n')

f1.close()

f1 = open('f1.txt')



f2 = open('f2.txt', 'w')
f2.close()

c = 0
for line in f1:
    f2 = open('f2.txt')
    c += 1
    if line not in f2:
        f2.close()
        f2 = open('f2.txt', 'a')
        f2.write(line)
        f2.close()



f1.close()

f2 = open('f2.txt')
fr = f2.read()
print(fr)
f2.close()
