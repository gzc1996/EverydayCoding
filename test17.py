def height(m,n):
	for i in range(0,n):
		m /=2
	return m

def totaldis(m,n):
	count = 0
	for i in range(0,n+1):
		count += m
		m = m/2
	return count

if __name__ =='__main__':
	m,n = map(int,input().split())
	h = height(m, n)
	d = totaldis(m, n)
	print('{:.2f} {:.2f}'.format(h,d))


