import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        # print(f"player_dict: {player_dict}")
        player = Player(player_dict)
        players.append(player)

    # print("Oliot:")

    for player in players:
        # print(player)
        pass

    # where = "nationality"
    # where_value = "FIN"
    where = "goals"
    where_value = "9"

    collected = []
    collected = list(filter(lambda x: str(getattr(x, where)) == where_value, players))

    print("pelaajat:")

    for player in collected:
        print(player.dyna_str(where))
        pass


if __name__ == "__main__":
    main()
