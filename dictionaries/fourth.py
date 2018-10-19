"""
Syntax:
{___:___ for ___ in ___}
"""

numbers = dict(first=1, second=2, third=3)
squared_numbers = {keys: value ** 2 for key, value in numbers.items()}
print(squared_numbers) # {'first': 1, 'second': 4, 'third': 9}

squared_numbers = {num: num**2 for num in [1, 2, 3, 4, 5]}
print(squared_numbers) # {1: 1, 2: 4, etc}

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo) # {'A':'1', 'B':'2', 'C':'3'}

even_odd_dict = {num:("even" if num%2 == 0 else "odd") for num in [1, 2, 3, 4, 5]}
print(even_odd_dict) # {1: 'odd', 2: 'even', 3: 'odd'}