"""
Why use a Tuple?
- Tuples are faster than lists
- It makes your code safer
- Valid keys in a dictionary

.items() dictionary method returns tuples.
"""
months = ('Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

first_month[0] # 'Jan'

# Tuples as key for dictionary | You can not use lists as keys for dictionary

locations = {
	(43.1212, 64.1212): 'Tokyo Office',
	(75.3344, 54.1212):	'New York Office',
	(89.6533, 98.3233):	'San Franscisco Office'
}

type(locations.items()) # tuples 

# Looping in tuples:

for month in months:
	print(month)

i = 0

while(i < len(months)):
	print(months[i])
	i++

# Methods in tuples:

	#count - gives count of a value in tuple

x = (1, 2, 2, 3, 3)
x.count(1) # 1
x.count(3) # 2

	#index - returns first matching index of the value passed

t = (1, 2, 3, 3, 3)
t.index(1) # 0
t.index(5) # ValueError: tuple.index(x): x not in tuple
t.index(3) # 2

# Nested tuples - access same as list & can use slices too

nums = (1, 2, 3, (4, 5), 6)

"""
Best used when you want a list of things you won't change in your codebase
"""

