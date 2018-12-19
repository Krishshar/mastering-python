from LinkedList import LinkedList

def sum_list(l1, l2):
	num1 = int(''.join(str(l1).split(' -> '))[::-1])
	num2 = int(''.join(str(l2).split(' -> '))[::-1])

	return num1 + num2

def sum_list_forward(l1, l2):
	num1 = int(''.join(str(l1).split(' -> ')))
	num2 = int(''.join(str(l2).split(' -> ')))

	return num1 + num2

if __name__ == '__main__':
	l1 = LinkedList()
	l1.generate(3, 0, 9)
	l2 = LinkedList()
	l2.generate(3, 0, 9)
	print(f"Backward order sum of ({l1}) & ({l2}) :")
	print(sum_list(l1, l2))
	print(f"Forward order sum of ({l1}) & ({l2}) :")
	print(sum_list_forward(l1, l2))