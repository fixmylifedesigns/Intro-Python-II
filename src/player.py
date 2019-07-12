# Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items= []

    def move(self, location):
        self.location = location


    def __str__(self):
        return f"{self.name} is in {self.location}"

    def get_item(self, item):
        self.items.append(item)
        self.location.items.remove(item)

    def drop_item(self, item):
        self.items.remove(item)
        self.location.items.append(item)