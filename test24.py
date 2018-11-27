import random as r

class Fish:
	def __init__(self):
		self.x = r.randint(0, 10)
		self.y = r.randint(0, 10)

	def move(self):
		self.x += 1
		print("current location:",self.x,self.y)

class Goldfish(Fish):
	pass

class Carp(Fish):
	pass

class Salmon(Fish):
	pass

class Shark(Fish):
	def __init__(self):
		super().__init__()
		self.hungry = True

	def eat(self):
		if self.hungry:
			print("wanna sth to eat!")
			self.hungry = False
		else:
			print("full!")


if __name__ =="__main__":
	fish = Fish()
	fish.move()
	fish.move()

	goldfish = Goldfish()
	goldfish.move()
	goldfish.move()

	shark = Shark()
	shark.move()
	shark.move()
	shark.eat()
	shark.eat()
