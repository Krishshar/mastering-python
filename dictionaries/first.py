"""
Limitations of Lists:
	-Not enough information
	-We want to describe this data in more detail

So we will use dictionaries:
	- A data structure that consists of key value pairs
	- We use keys to describe our data and the values to represent the data

"""

# Example 1 - Simple Dictionary

student = {
	"name": "Jayesh",
	"owns_laptop": True,
	"has_friends": False,
	"gre_score": 318
}

# Example 2 - Using dict(key = 'value') function

student2 = dict(name = "Jayesh", age = "21")

# Example 3 - Extracting Data

print(student["name"]) #Jayesh
# student["hula"] - KeyError