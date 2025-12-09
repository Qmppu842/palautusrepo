from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, Not, PlaysIn, All, Or
from query_builder import QueryBuilder
from query_builder import *


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # matcher = And(HasAtLeast(5, "goals"), HasAtLeast(20, "assists"), PlaysIn("PHI"))

    # matcher = And(Not(HasAtLeast(2, "goals")), PlaysIn("NYR"))

    # matcher = Or(HasAtLeast(45, "goals"), HasAtLeast(70, "assists"))

    matcher = And(
        HasAtLeast(70, "points"), Or(PlaysIn("COL"), PlaysIn("FLA"), PlaysIn("BOS"))
    )

    for player in stats.matches(matcher):
        print(player)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))


def main2():
    url = "https://studies.cs.helsinki.fi//nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    matcher = query.plays_in("NYR").build()

    for player in stats.matches(matcher):
        print(player)


def main3():
    url = "https://studies.cs.helsinki.fi//nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    matcher = (
        query.plays_in("NYR")
        .has_at_least(10, "goals")
        .has_fewer_than(20, "goals")
        .build()
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main3()
