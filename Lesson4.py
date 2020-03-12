###################################
# Author: Bekircan Keceoglu
# Lesson: Lists 2
###################################

players = ['lebron','davis','kobe','melo']

# loop through elements 
for player in players:
	# dont forget indentation
	print(player+ " is a player")

# generate number
for value in range(1,4):
	print(value)
	
# make list
numbers = list(range(1,5))
print(numbers)

# even numbers
even_num = list(range(2,11,2))
print(even_num)

# create squares
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

# min number
print(min(squares))

# max number
print(max(squares))

# slicing list
players = ['lebron','davis','kobe','melo']
print(players[0:2])
print(players[:3])
print(players[1:])

# copying list
players2 = players[:]
print(players2) 

# tuples
players_tuple = ('lebron','kobe')
print(players_tuple[0])
# error players_tuple[0] = 'dirk'