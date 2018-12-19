def check_permutation(str1, str2):
	return sorted(str1) == sorted(str2)

if __name__ == '__main__':
	str1, str2 = input().split()
	print(check_permutation(str1, str2))