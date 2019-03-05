from colorama import Fore, Back, Style
from room import Room
from item import Item
from player import Player
from data import room as room, item as item, player as player
from functions import actionList as actionList, action_parser as action_parser, list_items as list_items, movementList as movementList, movement as movement, search_inventory as search_inventory
from colorama import init
init()


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))  # warning


# player inventory / items
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def prYellow(skk): print(
    "\033[93m {}\033[00m" .format(skk))  # movement options


def prLightPurple(skk): print(
    "\033[94m {}\033[00m" .format(skk))  # in-depth options


def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))  # options


def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))  # room


def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))


def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

#systemList and inventory


systemList = ["q", "1", "2", "3", "4", "5", "i"]

#
# Main
#

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#

# game start


prLightGray("\nWelcome to the game Dungeon Something.")

userInput = ''
while userInput != 'q':
    if (len(userInput) == 0):
        prPurple(
            "\nFor system options: input [1] / For player options: input [2] / for help: press [return]")
        prCyan(player.room)  # room
        prGreen(list_items(player.room))  # item in room
    userInput = input(">> ")
    if(len(userInput) < 2):  # input single variable, single char
        if userInput in systemList or userInput in movementList:
            if userInput == "1":
                prLightPurple("To exit: input [q]")  # exit
            if userInput == "2":
                prLightPurple(
                    "For movement options: input [3] / For action options: input [4] For inventory: input [i]")  # player options
            if userInput == "3":
                prYellow(
                    "To move North: input [n] / To move East: input [e] / To move South: input [s] / To move West: input [w]")  # movement options
            if userInput == "4":
                prYellow(
                    "To get item: input <'get'> <'itemname'> / To drop item: input <'drop'> <'itemname'>")  # action options
        # movement input
            if userInput in movementList:
                movement(userInput)
            if userInput == "i":
                player.inventory = search_inventory()
                prGreen(
                    f"you currently have these items in your inventory: {player.inventory}")  # inventory list
        else:
            prRed("Input invalid")
    # action input
    if(len(userInput) > 1):
        userInput = userInput.split(" ")
        if userInput[0] in actionList:
            action_parser(userInput[0], userInput[1])
        else:
            prRed("Input invalid")  # invalid input not in actionList
