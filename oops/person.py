# Defining the simplest possible class

class User:
	def __init__(self, first, last, age):
		#self keyword refers to current class instance
		self.first = first
		self.last = last
		self.age = age

user1 = User("Bee", "Baa", 25)
user2 = User("Buu", "Baa", 22)

print(user1.first)