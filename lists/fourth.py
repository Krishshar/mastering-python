#Work with nested lists to build more complex data structures

"""
Why nested lists?
 Complex data structures - matricies, Game Boards / Mazes, Rows and Columns for visualizations,
 tabulation and grouping data

"""

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

nested_list[0][2] #3
nested_list[2][0] #7
nested_list[-1][-1] #9

# printing values in nested list

for list_item in nested_list:
	for val in list_item:
		print(val)

# Example 1:

coords [[10.423, 9.132], [37.212, -14.092], [21.367, 32.572]]

for loc in coords:
	for coord in loc:
		print(coord)

# Nested List Comprehension

[[print(val) for val in l] for l in nested_list]

# Example 2:

board = [[num for num in range(1,4)] for val in range(1,4)]
print(board) #[[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# Example 3:

[["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
# [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']] 