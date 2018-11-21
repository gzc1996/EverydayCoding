def showMaxFactor(num):
	count = num // 2
	while count > 1:
		if num % count == 0:
			print('%d\'s max factor is %d.\n' % (num , count))
			break
		count -= 1
	else:
		print('%d is prime num.\n' % num)

if __name__ == '__main__':
	num = int(input('please input a num:'))
	showMaxFactor(num)
