f1 = open('f1.txt','r')
f4 = open('f4.txt','w')
f4.close()
f4 = open('f4.txt','a')
k = 0
n = '\n'
last_line = None
for line in f1:
	k += 1
	last_line = line
if n not in last_line:
	last_line = last_line + n

for i,line in enumerate(open('f1.txt','r')):
	if ((i + 1) % 2 == 0) and ((i + 1) != k):
		f4.write(line)
	elif ((i + 1) % 2 == 0) and ((i + 1) == k):
		f4.write(last_line)
for i,line in enumerate(open('f1.txt','r')):
	if ((i + 1) % 2 != 0) and ((i + 1) != k):
		f4.write(line)
	elif ((i + 1) % 2 != 0) and ((i + 1) == k):
		f4.write(last_line)

			
			
