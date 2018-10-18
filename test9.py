##################non-recursion version
def factorial1(n):
	result = n
	for i in range(1,n):
		result *= i
	return result
##################recursion version
def factorial2(n):
	if n == 1:
		return 1
	else:
		return n * factorial2(n-1)

##################main

num = int(input("please input a num:"))
print('result1 =', factorial1(num))
print('result2 =', factorial2(num))