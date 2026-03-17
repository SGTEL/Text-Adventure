from room import Room

class Player:
    def __init__(self, name: str, starting_room: Room):
        self.name: str = name
        self.room: Room = starting_room


    def look(self):
        """ Get a description of the current room """

        self.room.describe()

    
    def talk(self, msg: str):
        """ Talk to the NPC in the room """

        self.room.talk(msg)

    
    def go(self, next_room: Room):
        """ Go to the next room """
        pass


    def take(self, item):
        """ Pick up an item """
        pass
