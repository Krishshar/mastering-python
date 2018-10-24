"""
What is a function?
	- a process for executing a task
	- it can accept input and return an output
	- useful for executing similar procedures over and over

Why use functions?
	- Stay DRY - Don't Repeat Yourself
	- Clean up code and prevent code duplications
	- Abstract away code for other users
		- Imagine you have to rewrite thes print()

Function Structure?
def name_of_function() #snake_case
"""

def sing_happy_birthday(name):
	print("Happy Birthday to you!")
	print("Happy Birthday to you!")
	print("Happy Birthday to you Dear "+name+"!")
	print("Happy Birthday to you!")

sing_happy_birthday("Jayesh")