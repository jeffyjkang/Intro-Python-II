from room import Room
from item import Item
from player import Player
from data import room as room, item as item, player as player
from functions import actionList as actionList, action_parser as action_parser, list_items as list_items, movementList as movementList, movement as movement, search_inventory as search_inventory

#
# Main
#

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
userInput = ''
while userInput != 'q':
    if (len(userInput) == 0):
        print("Press q to quit")
        print("for movement, press n for north, e for east, s for south, w for west \n")
        print(player.room)
        print(list_items(player.room))
    userInput = input(">> ")
    # movement input
    if(len(userInput) > 0):
        if userInput in movementList:
            movement(userInput)
        if userInput == "i":
            player.inventory = search_inventory()
            print(
                f"you currently have these items in your inventory: {player.inventory}")
    # action input
    if(len(userInput) > 1):
        userInput = userInput.split(" ")
        action_parser(userInput[0], userInput[1])
