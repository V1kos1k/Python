
f2 = open('f2.txt', 'w')
f2.close()

f1 = open('f1.txt', 'r')


count1 = 0
for line in f1:
    count1 += 1
f1.close()

k = 0

f1 = open('f1.txt', 'r')

for line in f1:
	k += 1
	if k == count1:
		s = line.isspace()
		print(s)

f1.close()

k=0
if s == False:
	f1 = open('f1.txt', 'r+')
	for line in f1:
		k+=1
		if k == count1:
			f1.write('\n')
			print('+')
	f1.close()
mc = count1

f1 = open('f1.txt', 'r')

count2 = 0

for line in f1:
    count2 += 1
    if count2%2 == 0:
        if line == '\n' and count2 == mc:
            break
        f2 = open('f2.txt', 'a')
        f2.write(line)
        f2.close()
f1.close()

f1 = open('f1.txt', 'r')
count = 0
for line in f1:
    count += 1
    if count%2 != 0:
        if line == '\n' and count == mc:
            break
        f2 = open('f2.txt', 'a')
        f2.write(line)
        f2.close()
f1.close()