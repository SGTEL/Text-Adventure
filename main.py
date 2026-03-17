from room import bathroom
from player import Player

player: Player = Player("Bob", bathroom)

print("Welcome to Bob's text adventure! You are Bob.")

while True:
    player_input: str = input("\nBob: ").lower().strip()
    cmd: str = player_input.split()[0]
    content: str = " ".join(player_input.split()[1:])
    
    match cmd:
        case "look":
            player.look()

        case "talk":
            player.talk(content)

        case "go":
            player.go(player.room.next_room)
            print(f"\nYou enter the {player.room.name}")

        case "exit":
            quit()

        case _:
            print("\nUnknown instruction.")
