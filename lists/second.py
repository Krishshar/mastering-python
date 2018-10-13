#Use built in methods to modify and copy lists
data = [1, 2, 3]

#Append an item to the end of list
data.append(4)
print(data)

#To append more than one item
data.extend([5, 6, 7, 8])
print(data)

#To insert at a given position
data.insert(2, "Hi!")
data.insert(len(data), "Last")
print(data)

#To remove a single item from last
last_data = data.pop()
print(last_data)

#To remove a item from some position
data_at_position = data.pop(1) #data.pop(index)
print(data_at_position)

#To remove a specific item from a list (use when you know what to remove)
data.remove(5) #Only removes the first occurence of 5
print(data)

#To remove everything from a list
data.clear()
print(data)

#To find the index of specific item in the list
numbers = list(range(5,11))
numbers.index(6) #1
numbers.index(9) #4


numbers = [5, 5, 6, 7, 5, 8, 8, 9, 10]
#You can specify start and end
#syntax -> list.index(item, start_point, end_point)
#returns -> index
#throws -> valueError saying requested something is not in the list
numbers.index(5, 2) #4
numbers.index(8, 6, 8) #6

#To count the number of times something occurs in a list
numbers.count(5) #3
numbers.count(8) #2
#count doesn't throws an error if something is not found

#sort and reverse are carried out in place i.e no new list needs to be created

#To reverse a list
numbers.reverse()

#To sort a list
numbers.sort()
print(numbers)

#To Join elements of list into a string
# Join technically a String method that take an iterable argument
# concatenates(combines) a copy of the base string between each item of the iterable
# returns a new string
# can be used to make sentences out of a list of words by joining on a space, for instance

words = ['Coding', 'Is', 'Fun!']
' '.join(words) # 'Coding is Fun!'

name = ['Mr', 'Steele']
'. '.join(name) # Mr. Steele

names = ['Ashish','Aakansha', 'Lokesh']
friends = ', '.join(names)
print(friends) # Ashish, Aakansha, Lokesh

#Slicing i.e getting list from start and end index and step
# Syntax -> some_list[start:end:step]

numbers = list(range(1,10,2))

numbers_sliced1 = numbers[1:]
#[2, 3, 4, 5 ....]

numbers_sliced2 = numbers[2:5]
#[3, 4, 5]

numbers_sliced3 =  numbers[:5]
#[1, 2, 3 ,4, 5]

numbers_sliced4 = numbers[:5:2]
#[1, 3, 5]

#Use negative numbers to reverse the order

#Modifying portions of lists
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = ['a', 'b', 'c']

print(numbers) #[1, 'a', 'b', 'c', 4, 5]

colors = ["Orange", "Akku"]
colors[0][::-1] #egnarO

#Swapping values in lists
colors[0], colors[1] = colors[1], colors[0]

print(colors)
