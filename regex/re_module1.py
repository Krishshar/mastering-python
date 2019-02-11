import re

pattern = re.compile(r'\d{3} \d{3}-\d{4}')
res = pattern.search("call me at 310 445-9876")
print(res.group())

res = pattern.findall("call me at 310 445-9876 310 443-4535")
print(res)