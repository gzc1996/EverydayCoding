def calqual(str):
	atom = {'H':1,'C':12,'O':16}
	sum = 0
	for i in range(len(str)):
		sum += atom[str[i]]
	return sum

if __name__ == '__main__':
	count = int(input())
	qual = []
	for i in range(count):
		qual.append(input())
	for x in range(len(qual)):
		print(calqual(qual[x]))
