#It's just a collection or grouping of items!
#This program describe, create and access list data structure

#Instead doing:-
task1 = "Install"
task2 = "Play"
task3 = "Uninstall"

#We can do:-
task_list = ["Install", "Play", "Uninstall"]

#We can show number of items using:-
print(len(task_list)) #Built in methods

#Making list of numbers using built-in functions range and list
r = range(1, 10, 2)
numbers_list = list(r)
print(numbers_list)

#Accessing values in list (list always start at zero)
print(task_list[0]) #Install
print(task_list[1]) #PLay
print(task_list[2]) #Unistall
print(task_list[-1]) #Uninstall
print(task_list[-2]) #Play

#Check if a value is in a lists(Case matters)
print("Install" in task_list)
if "Uninstall" in task_list:
    print("Fuck Off!")

#Accessing all values in a lists
for number in numbers_list:
    print(number * number)

print("Using While Loop:")

i = 0
while i < len(numbers_list):
    print(numbers_list[i])
    i += 1
