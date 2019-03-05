from room import Room
from item import Item
from player import Player
from data import room as room, item as item, player as player

from colorama import init
init()


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))  # warning


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))  # player inventory


def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))  # room


# input parser
actionList = ["get", "drop"]

#


def action_parser(action, item_name):
    if action in actionList:
        if action == "get":
            for item in player.room.items:
                if item.name == item_name:
                    item_found = item
                    prGreen(item.on_take())
                    player.inventory.append(item_found)
                    player.room.items.remove(item_found)
        elif action == "drop":
            for item in player.inventory:
                if item.name == item_name:
                    item_found = item
                    prGreen(item.on_drop())
                    player.room.items.append(item_found)
                    player.inventory.remove(item_found)
    else:
        print("invalid input")
# list items in room


def list_items(room):
    if len(room.items) == 0:
        return "No items in room"
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
                prCyan(player.room)
                prGreen(list_items(player.room))
            else:
                prRed("Dead end, can't go North")
        if move == 'e':
            if hasattr(player.room, "e_to"):
                player.room = player.room.e_to
                prCyan(player.room)
                prGreen(list_items(player.room))
            else:
                prRed("Dead end, can't go East")
        if move == 's':
            if hasattr(player.room, 's_to'):
                player.room = player.room.s_to
                prCyan(player.room)
                prGreen(list_items(player.room))
            else:
                prRed("Dead End, can't go South")
        if move == 'w':
            if hasattr(player.room, 'w_to'):
                player.room = player.room.w_to
                prCyan(player.room)
                prGreen(list_items(player.room))
            else:
                prRed("Dead End, can't go West")
    else:
        prRed("bad input for movement")

# inventory function


def search_inventory():
    inventory = []
    for item in player.inventory:
        inventory.append(item.name)
    return inventory
