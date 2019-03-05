from room import Room
from item import Item
from player import Player

import random

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", ""),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south. But you see a light coming from 
behind the large bookshelf to the north""", ""),

    'tunnel': Room("Secret Tunnel", """The secret tunnel is damp, dark and long, some
    creepy stuff is hanging from the ceiling and the only bit of light are at the
    ends of the tunnel""", ""),

    'cemetary': Room("Small graveyard", """Up on a tiny hill lies a headstone, 
    you can't seem to make out the name, but under it there are foreign words
    that you think may be latin, to the west and north lie small structures""", ""),

    'church': Room("Chapel", """Inside the chapel there are amazing artworks
    on the wall and marble statues scattered throughout; you can also make out
    a dusty piano in the corner""", ""),

    'castle': Room("Castle", """The small castle has no doors, there is only a
    small opening on one of the towers where you can see a candle flickering in
    the wind, there is a sign to the west that reads do not approach""", ""),

    'unknown': Room("Unknown", """As you move west from the castle, you loose footing
    and fall into darkness""", "")

}

# Declare all items

item = {
    'sword': Item("sword", "a pretty cool sword"),

    "shield": Item("shield", "a pretty sturdy shield"),

    "boots": Item("boots", "a pair of pretty fashionable boots"),

    "armor": Item("armor", "a pretty weird looking suit"),

    "helmet": Item("helmet", "a pretty regal looking headpiece"),

    "bow": Item("bow", "a pretty flexible looking bow"),

    "red_potion": Item("hp_potion", "cool health potion"),

    "blue_potion": Item("mana_potion", "cool mana potion"),

    "yellow_potion": Item("energy_potion", "cool energy potion"),

    "key": Item("rusty_key", "old rusty key"),

    "pouch": Item("pouch", "cool pouch... filled with gems and jewels!")

}

# declare player

# Make a new player object that is currently in the 'outside' room.

player = Player(room["outside"], "", "", "", "")

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].n_to = room['tunnel']
room['tunnel'].s_to = room['treasure']
room['tunnel'].n_to = room['cemetary']
room['cemetary'].s_to = room['tunnel']
room['cemetary'].n_to = room['church']
room['church'].s_to = room['cemetary']
room['cemetary'].w_to = room['castle']
room['castle'].e_to = room['cemetary']
room['castle'].w_to = room['unknown']

# add items to rooms:

# room["narrow"].items.append(item["sword"])
# room["narrow"].items.append(item["shield"])
# room["foyer"].items.append(item["armor"])
# room["foyer"].items.append(item["helmet"])
# room["overlook"].items.append(item["boots"])

room_list = [room["outside"], room["foyer"],
             room["overlook"], room["narrow"], room["treasure"], room["tunnel"], room["cemetary"],
             room["church"], room["castle"], room["unknown"]]


item_list = [item["sword"], item["shield"],
             item["boots"], item["armor"], item["helmet"],
             item["bow"], item["red_potion"], item["blue_potion"],
             item["yellow_potion"], item["key"], item["pouch"]]


for item in item_list:
    random_num = random.randint(0, len(room_list)-1)
    room_list[random_num].items.append(item)

# print(len(room_list))
# print(random_num)
# random_room = room_list[random.randint(0, len(room_list))]
# print(random_room)
