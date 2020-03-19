###################################
# Author: Bekircan Keceoglu
# Lesson: Dictionaries
###################################

# simple dictionary
player_0 = {'name':'Lebron', 'age':35}
print(player_0['name'])
print(player_0['age'])
print(player_0['name'] + " is " + str(player_0['age']))

# adding new key
player_0['power'] = 99
print(player_0)

# modifying values
player_0['power'] = 98
print(player_0)

# removing key-value
del player_0['power']
print(player_0)

# looping in dictionary
for key, value in player_0.items():
	print("\n Key: "+key)
	print(" Value: "+str(value))

# looping all values
for values in player_0.values():
	print("\n Values: "+str(values))

# looping all keys
for key in player_0.keys():
	print("\n Key: "+key)

# list of dictionaries
player_0 = {'name':'Lebron', 'age':35}
player_1 = {'name':'Kobe', 'age':40}
players = [player_0, player_1]

for player in players:
	print(player)

# list in dictionary
player_0 = {'name':'Lebron', 'age':35, 'skills':['shoot', 'drible', 'dunk']}

for skill in player_0['skills']:
	print(skill)

# dictionary in dictionary
player_0 = {'name':'Lebron', 'age':35, 'skills':{'shooting':95, 'dunk':99, 'speed':94}}
print(player_0['skills']['dunk'])