#iterate over lists using loops and list comprehensions
#What does list comprehension does?
# takes one list and outputs manipulated list
# great to convert one type/form of list to another

nums = [1, 2, 3]
print([x*10 for x in nums]) #[10, 20, 30]

# Method 1

numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
	doubled_number = num * 2
	doubled_numbers.append(doubled_number)

print(doubled_numbers) # [2, 4, 6, 8, 10]

# Method 2 using list comprehension

numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers) # [2, 4, 6, 8, 10]

# Example 2

name = 'jayesh'
[char.upper() for char in name] # ['C', 'O', 'L', 'T']

friends = ['ashish', 'akku', 'lokesh']
[friends[0].upper() for friend in friends] # ['Ashish', 'Akku', 'Lokesh']

# Example 3

[num*10 for num in range(1,6)] # [10, 20, 30, 40, 50]

# Example 4

[bool(val) for val in [0, [], '']] # [False, False, False]

# Example 5

numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers]
print(string_list) # ['1', '2', '3', '4', '5']

#      List Comprehension with Conditional Logic
#------------------------------------------------------

# Example 6 - if only

numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

# Example 7 - if else

[num*2 if num % 2 == 0 else num/2 for num in numbers] # [0.5, 4, 1.5, 8, 2.5, 12]

# Example 8 - conditional logic with 'in' keyword

with_vowels = "This is incredible! But hard to remember."
print(''.join(char for char in with_vowels if char not in "aeiou")) # Ths s ncrdbl! Bt hrd t rmmbr.




