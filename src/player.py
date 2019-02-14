# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room, health, mana, energy, inventory):
        self.room = room
        self.health = 100
        self.mana = 100
        self.energy = 100
        self.inventory = []

    def input_name(self, name):
        self.name = name
