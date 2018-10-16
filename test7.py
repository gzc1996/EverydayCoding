def FuncX(a):
	def FuncY(b):
		return a*b
	return FuncY

i = FuncX(8)
print(i(5))