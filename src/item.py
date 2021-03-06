# Write a calss to hold item information. This should have name and
# description attributes.


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        # return f"item: {self.name}"
        return f"item name: {self.name}, item description: {self.description}."

    def on_take(self):
        return f"you took the: {self.name}, it is: {self.description}"

    def on_drop(self):
        return f"you dropped the: {self.name}, you don't need it anyways."

# add subclasses of items
