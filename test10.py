def fab(n):
	if n < 1:
		print('input error!')
		return -1
	if n == 1 or n == 2:
		return 1
	else:
		return fab(n-1) + fab(n-2)

num = int(input('input a nmu:'))
result = fab(num)
print('fab num:',result)