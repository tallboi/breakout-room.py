import time
#This will be the simple player tracking system
#FUNCTIONS: It uses arrow keys: Up is +1, down is -1, right is + .1, and left is - .1
#This allows me to track the player through the room and detect when the player has reached a wall
#Room will be a 3x3 cube with the left wall being valued 1-3, bottom to top, with all proceeding values to the right adding .1
#Northern walls will be 4, southern walls will be 0 


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


#All of this was roughly put together, and I have yet to create a decent system

#I still need to figure out how to create a system that completes the desired funtions after pressing an arrow key (see functions above)
