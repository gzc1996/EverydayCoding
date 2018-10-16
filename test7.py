###################closure application
def FuncX():
	x = 5
	def FuncY():
		nonlocal x #强制转换为非局部变量
		x *=x
		return x
	return FuncY()

print(FuncX())
###################lambda&filter application
odd = list(filter(lambda x : x % 2, range(10)))#filter 0 or false
print('all odd nums smaller than 10:',odd)
###################lambda&map application
even = list(map(lambda x : x *2, range(10)))#map(a,b) means the nums in b map function a
print('all even nums smaller than 20:',even)