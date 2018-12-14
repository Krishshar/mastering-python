# all function returns true if all values in a collection is truthy

print(all([char for char in 'eio' if char in 'aeiou']))
print(all([num for num in range(10) if num % 2 == 0]))

# any function returns true if any value in a collection is truthy

print(any([num for num in range(10) if num % 2 == 0]))