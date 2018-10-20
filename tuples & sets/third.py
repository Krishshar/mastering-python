s = set([1, 2, 3, 4, 5])
# add

s.add(6)
s # {1, 2, 3, 4, 5, 6}
s.add(4) # throws no error if 4 already in set
s # {1, 2, 3, 4, 5, 6}

# remove

s.remove(6)
s # {1, 2, 3, 4, 5}
s.remove(6) #KeyError (Because 6 is not in the set)

# discard
s.discard(6) #no KeyError

# copy

s = set([1, 2, 3])
another_s = s.copy()
another_s # {1, 2, 3}
another_s is s # False (Because they are situated in different memory locations)

# clear

s.clear() 
s # Empty

# Set Math

s = set([1, 2, 3, 4])
p = set([3, 4, 5, 6])

	# Set Union excludes common elements
	s | p # {1, 2, 3, 4. 5, 6}

	# Set Intersection includes only common elements
	s & p # {3, 4}

"""
**************** Set Comprehension ****************
"""

s = {x**2 for x in range(6)}
# {0, 1, 25, 4, 36, 9, 16}

s = {c.upper() for c in 'hello'}
# {'H', 'E', 'L', 'O'}