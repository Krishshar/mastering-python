student = {
	"name": "Jayesh",
	"owns_laptop": True,
	"has_friends": False,
	"gre_score": 318
}

# Method 1
for val in student.values():
	print(val)

for key in student.keys():
	print(key)

# Method 2
for key,value in student.items():
	print(f"key is {key} and value is {value}") 

# Additional (Using in)
"name" in student # True 
#Above statements only checks in keys for values:

"Jayesh" in student.values() # True
