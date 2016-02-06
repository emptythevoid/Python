# looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


#copying a list
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
