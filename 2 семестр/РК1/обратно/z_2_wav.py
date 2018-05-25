
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

while count1 != 0:
    f1 = open('f1.txt', 'r')
    count2 = 0
    for line in f1:
        count2 += 1
        if count1 == count2:

            if line == '\n' and count2 == mc:
                break

            f2 = open('f2.txt', 'a')
            f2.write(line)
            f2.close()
    count1 -= 1
    f1.close()