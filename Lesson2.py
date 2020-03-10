###################################
# Author: Bekircan Keceoglu
# Lesson: Variables and Data Types
###################################

print("Hello World")

message = "Hello W0rld"
print(message)

# name error
#print(mesage)

# Strings
name = "albert einstein"
print(name.title())
print(name.upper())
print(name.lower())

#combining strings
name = "albert"
surname = "einstein"
fullname = name + " " + surname
print(fullname)

# tabs
print(fullname)
print("\t"+fullname)

# new line
print(name+"\n"+surname)

# stripping whitespaces
name = " albert einstein "
print(name.rstrip())
print(name.lstrip())
print(name.strip())

# numbers int
print("3 + 2 = "+str(3+2))
print("3 / 2 = "+str(3/2))

# float
print("3.1 + 2.1 = "+str(3.1+2.1))

#comments