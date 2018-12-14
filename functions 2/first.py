#Using *args

def sum_all_nums(*args):
	sum = 0
	for val in args:
		sum += val
	return val

print(sum_all_nums(1, 2, 3))
print(sum_all_nums(1, 2, 3, 99, 102, 103))
print(sum_all_nums(1))


#Using **kwargs some pronounce it as "QWARGS"

def fav_colors(**kwargs):
	for person, color in kwargs.items():
		print(f"{person}'s favorite color is {color}")

fav_colors(colt="purple", ruby="red", ethel="teal")