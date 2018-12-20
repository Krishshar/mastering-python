f = open('test.txt')  #Open the file
# print(f.read())				#Read the file
# Python reads file by using a cursor
# this is like the cursor you see when you're typing
# After a file is read, the cursor is at the end
# Now how to move the cursor:

# f.seek(5) # takes to 5th character
# print(f.read())

f.seek(0)
print(f.readline())
f.seek(0)
print(f.readlines())
f.close()							#Close the file

#File cannot be read after closing