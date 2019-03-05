from room import Room
from item import Item
from player import Player
from data import room as room, item as item, player as player


# input parser
actionList = ["get", "drop"]

#


def action_parser(action, item_name):
    if action in actionList:
        if action == "get":
            for item in player.room.items:
                if item.name == item_name:
                    item_found = item
                    player.inventory.append(item_found)
                    player.room.items.remove(item_found)
            print("got item")
        elif action == "drop":
            for item in player.inventory:
                if item.name == item_name:
                    item_found = item
                    player.room.items.append(item_found)
                    player.inventory.remove(item_found)
            print("dropped item")
    else:
        print("invalid input")
# list items in room


def list_items(room):
    if len(room.items) == 0:
        return ""
    items = [
        f'item name: {i.name}, item description: {i.description}' for i in room.items]
    return items


# movement
movementList = ["n", "e", "s", "w"]


def movement(move):
    if move in movementList:
        if move == 'n':
            if hasattr(player.room, 'n_to'):
                player.room = player.room.n_to
                print(player.room)
                print(list_items(player.room))
            else:
                print("Dead end, can't go North")
        if move == 'e':
            if hasattr(player.room, "e_to"):
                player.room = player.room.e_to
                print(player.room)
                print(list_items(player.room))
            else:
                print("Dead end, can't go East")
        if move == 's':
            if hasattr(player.room, 's_to'):
                player.room = player.room.s_to
                print(player.room)
                print(list_items(player.room))
            else:
                print("Dead End, can't go South")
        if move == 'w':
            if hasattr(player.room, 'w_to'):
                player.room = player.room.w_to
                print(player.room)
                print(list_items(player.room))
            else:
                print("Dead End, can't go West")
    else:
        print("bad input for movement")
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
    # action input
    if(len(userInput) > 1):
        userInput = userInput.split(" ")
        action_parser(userInput[0], userInput[1])
