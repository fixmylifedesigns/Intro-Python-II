from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Irving', room['outside'])
print(player)
# userInput = ""
# Write a loop that:
#
while True:

# * Prints the current room name
    print(player.location.name)
# * Prints the current description (the textwrap module might be useful here).
    print(player.location.description)
# * Waits for user input and decides what to do.
    user_input = input(
        "where do you want go? (N)orth, (S)outh, (E)ast, or (W)est?")
# If the user enters a cardinal direction, attempt to move to the room there.
    if(user_input == 'n' or user_input == 'N'):
        target = player.location.n_to
    # print(current_room.n_to)
    elif(user_input == 's' or user_input == 'S'):
        target = player.location.s_to
    elif(user_input == 'e' or user_input == 'E'):
        target = player.location.e_to
    elif(user_input == 'w' or user_input == 'W'):
        target = player.location.w_to
    elif(user_input == 'q' or user_input == 'Q'):
        break
    else:
        print("invalid input")

    if(target != None):
        player.move(target)
    else: print("cant go there")
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
