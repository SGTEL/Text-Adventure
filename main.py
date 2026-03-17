from room import bathroom
from player import Player

player: Player = Player("Bob", bathroom)

while True:
    player_input: str = input("\nPlayer: ").lower().strip()
    cmd: str = player_input.split()[0]
    content: str = " ".join(player_input.split()[1:])
    
    match cmd:
        case "look":
            player.look()

        case "talk":
            player.talk(content)

        case "exit":
            quit()

        case _:
            print("\nUnknown instruction.")
