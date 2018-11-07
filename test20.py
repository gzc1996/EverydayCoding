def strlength(str):
	return len(str)

if __name__ == '__main__':
	count = int(input())
	num = []
	for i in range(count):
		num.append(input())
	for x in range(len(num)):
		print(strlength(num[x]))