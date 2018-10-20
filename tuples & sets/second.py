"""
- Sets are like formal mathematical sets.
- Sets do not have duplicate values.
- Elements in sets aren't ordered.
- Sets can be useful if you need to keep track of a collection of elements,
	but don't care about ordering, keys or values and duplicates
"""

# Sets cannot have duplicates
s = set({1, 2, 3, 4, 5, 5, 5}) # {1, 2, 3, 4, 5}

# Creating a new set
s = set({1, 4, 5})

# Creates a set with the same values as above
s = {1, 4, 5}

4 in s
# True

8 in s
# False

# There's no way of accessing items in order

# Looping in set

numbers = {1, 2, 3, 4}

for number in numbers:
	print(number)

# 1
# 2
# 3
# 4

"""
Common Use case for Sets

- If you say have a list of cities generated from your website signups you can
use sets to get collection of unique cities.

- use this for number of unique cities
	print(len(set([1, 2, 3, 3, 3]))) #3
"""