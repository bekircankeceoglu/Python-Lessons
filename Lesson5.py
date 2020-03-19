###################################
# Author: Bekircan Keceoglu
# Lesson: IF Statements
###################################

players = ['James', 'Kobe', 'Oneal', 'Kareem', 'Michael']

for player in players:
	if player == 'James':
		print(player.upper())
	else:
		print(player)

# key sensitivity
player = 'James'

if player == 'JAMES':
	print('JAMES')
else:
	print(player)

# inequality
if player != 'Kobe':
	print(player)

# numerical comparison
value = 18
if value == 12:
	print('Same')
else:
	print('Different')

# multiple value checking
age = 39
if age > 18 and age < 35:
	print("You are young")
elif age < 18:
	print("You are kid")
else:
	print("You are old")

#check value in list
players = ['James', 'Kobe', 'Oneal', 'Kareem', 'Michael']
player = "Bush"

if player not in players:
	print("Not in the list")

# boolean expression
flag = True
if flag == True:
	print("Do something")

if flag:
	print("Do something")

# simple if statement
age = 22
if age > 18:
	print("You can vote")

# if else statement
age = 12
if age > 18:
	print("You can vote")
else:
	print("You cant vote")

# if-elif-else statement
age = 37
if age < 18:
	print("Admission cost is 10$")
elif age >= 18 and age <=35:
	print("Admission cost is 20$")
else:
	print("Admission cost is 30$")