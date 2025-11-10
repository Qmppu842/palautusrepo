import requests
from player import Player


class PlayerReader:
    def __init__(self, url: str):
        self.url = url

    def get_players(self):
        response = requests.get(self.url, timeout=10000).json()

        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players


class PlayerStats:
    def __init__(self, player_reader: PlayerReader):
        self.pr = player_reader

    def gettetete(self, where: str = "nationality", where_value: str = "FIN"):
        collected = list(
            filter(
                lambda x: str(getattr(x, where)) == where_value, self.pr.get_players()
            )
        )
        return collected

    def top_scorers_by_nationality(self, nationality: str):
        collected = self.gettetete(where_value=nationality)
        collected = sorted(collected, key=lambda x: -(x.goals + x.assists))
        return collected


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
