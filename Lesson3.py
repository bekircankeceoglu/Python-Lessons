###################################
# Author: Bekircan Keceoglu
# Lesson: Lists
###################################

#list example
players = ['lebron', 'kobe', 'mj', 'melo']
print(players)

# accesing list elements
print(players[0])
print(players[1])
print(players[-1])
print(players[0].title())

# combining with string
message = "Best player is "+players[0] 
print(message)

# modifying elements
players[2] = "dirk"
print(players)

# append element
players.append("tim")
print(players)

# insert any position
players.insert(1,"davis")
print(players)

# removing elements
del players[1]
print(players)

# remove with pop
player = players.pop()
print(player)
print(players)

# remove with pop
player = players.pop(1)
print(player)
print(players)

# remove by value
players.remove("melo")
print(players)

# sorting list
players = ['lebron','kobe','davis','avery']
players.sort()
print(players)

# sorting original
players = ['lebron','kobe','davis','avery']
print(sorted(players))
print(players)

#find length of list
print(len(players))