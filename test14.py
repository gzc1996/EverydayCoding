def isPalindromewithstr(x):
	'''
	:type x: int 
	:rtype: bool
	'''
	if x < 0:
		return False
	return (str(x) == str(x)[::-1])

def isPalindromewithoutstr(x):
	if x < 0:
		return False
	tmp = x
	num = 0
	while tmp > 0:
		tmp,mod = tmp//10,tmp%10
		num = num*10 + mod
	return (x == num)

num = int(input('please input a num:'))
print(isPalindromewithstr(num))
print(isPalindromewithoutstr(num))