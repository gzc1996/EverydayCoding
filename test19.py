if __name__ == '__main__':
	num = 0
	letter = 0
	other = 0
	strlist = input()
	for i in strlist:
		if ord(i) >= 48 and ord(i) <= 57:
			num +=1
		elif ord(i) >= 65 and ord(i) <= 90 or ord(i) >=97 and ord(i) <= 122:
			letter +=1
		else:
			other +=1
	print('{} {} {}'.format(letter,num,other))
