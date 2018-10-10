import random
secret = random.randint(1, 10)
temp = input("input a num:")
guess = int(temp)
while guess != secret:
	if guess > secret:
		print("big")
	else:
		print("small") 
	temp = input("re-input a num:")
	guess = int(temp)
print("correct")
print("over") 