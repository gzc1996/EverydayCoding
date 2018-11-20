try:
	file = open('file1.txt')
	print(file.read())
	file.close()
except OSError:
	print('read file error')