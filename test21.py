f = open('test.txt')

A = []
B = []

for each_line in f:
	#print(each_line[:3])
	if each_line[:2] != '==':
		role,line = each_line.split(':',1)
		if role == 'A':
			A.append(line)
		if role == 'B':
			B.append(line)
		#print(A)
		#print('========')
		#print(B)
		#print('========')
	else:
		continue

filename_A = 'dialog_A.txt'
filename_B = 'dialog_B.txt'

file_A = open(filename_A,'w')
file_B = open(filename_B,'w')

file_A.writelines(A)
file_B.writelines(B)

file_A.close()
file_B.close()

#print('^^^^^^')

f.close()





