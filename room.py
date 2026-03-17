from npc import NPC, fred, mary

class Room:
    def __init__(self, npc: NPC, items: dict, desc: str, name: str):
        self.npc: NPC = npc
        self.items: dict = items
        self.desc: str = desc
        self.name: str = name


    def next_room(self, room):
        """ Sets up the room relationships"""

        self.next_room = room


    def describe(self):
        """ Tells the player information about a room """

        print(f"\n({self.name}): {self.desc}")

    
    def talk(self, player_msg: str):
        """ Talk to the NPC in the room """

        self.npc.talk(player_msg)


bathroom: Room = Room(fred, {}, "A dingey toilet, a small window lets in some light.", "Bathroom")
reception: Room = Room(mary, {}, "A sparkling reception, a small priest sits in the corner.", "Reception")

bathroom.next_room(reception)
reception.next_room(bathroom)