def is_one_away(str1, str2):
	table = [0 for _ in range(ord('z') - ord('a') + 1)]
	for c in str1:
		table[char_number(c)] += 1
	for c in str2:
		table[char_number(c)] -= 1
	neg = 0
	pos = 0
	for i in range(len(table)):
		if(table[i] < 0):
			neg += 1
		if(table[i] > 0):
			pos += 1
	return neg < 1 and pos < 1

def char_number(c):
	a = ord('a')
	z = ord('z')
	A = ord('A')
	Z = ord('Z')
	val = ord(c)

	if(a <= val <= z):
		return val - a
	elif(A <= val <= Z):
		return val - A
	return -1


if __name__ == '__main__':
	str1, str2 = input("Enter two space seperated strings: ").split()
	print(is_one_away(str1, str2))