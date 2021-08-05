import time
#This will be the simple player tracking system
#It uses arrow keys: Up is +1, down is -1, right is + .1, and left is - .1
#This allows me to track the player through the room and detect when the player has reached a wall

y = 1
z = .1

def up(x, y):
    return x + y

def down(x, y):
    return x - y

def right(x, z):
    return x + z

def left(x, z):
    return x - z

location = 1.1
print(location)
