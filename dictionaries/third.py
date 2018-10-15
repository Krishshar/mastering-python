#clear - clears all the keys and values in dictionary

d = dict(a=1, b=1, c=3)
d.clear()
print(d) # {}

#copy - makes a copy of a dictionary

d = dict(a=1, b=1, c=3)
c = d.copy() #different from c = d  c is d == False
print(c)

#fromkeys - creats key-value pairs from comma seperated values, generally used to generate default values
{}.fromkeys("a", "b") # {'a', 'b'}

new_user = {}.fromkeys(['name', 'score', 'email', 'bio'], 'unknown')
print(new_user) # {'name': 'unknown', 'score': 'unknown', 'email': 'unknown', 'bio': 'unknown'}

#get - retrieves a key in an object and return None, instead of KeyError if the key does not exist:
d = dict(a=1, b=1, c=3)
d['a'] # 1
d.get('a') # 1
#d['no_key'] # KeyError
d.get('no_key') # None

#pop - takes a single argument corresponding to a key and removes that key - value
#pair from the dictionary. Returns the value corresponding to the key that was removed

d = dict(a=1, b=1, c=3)
d.pop("b") # true
print(d)

#popitem - removes a random item from the dict
print(d.popitem())

#update - updates keys and values in a dictionary with another set of
# key value pairs

first = dict(a=1, b=2, c=3, d=4, e=5)
second = dict(f=6)
second.update(first)
#can only overwrite and add stuff


