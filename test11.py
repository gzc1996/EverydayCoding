def hanoi(n,x,y,z):
	if n == 1:
		print(x, '-->',z)#如果只有1个碟则直接x移动到z
	else:
		hanoi(n-1, x, z, y)#前n-1个碟从x移动到y
		print(x, '-->',z)#把第n个碟从x移动到z
		hanoi(n-1, y, x, z)#把y上的n-1个碟移动到z

order = int(input('please input order num:'))
hanoi(order, 'X', 'Y', 'Z')