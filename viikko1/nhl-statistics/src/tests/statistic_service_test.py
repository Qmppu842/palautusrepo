import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54),  # 45+54 = 99
            Player("Kurri", "EDM", 37, 53),  # 37+53 = 90
            Player("Yzerman", "DET", 42, 56),  # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89),  # 35+89 = 124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_non_existing(self):
        self.assertEqual(self.stats.search("kala"), None)

    def test_search_existing_existing(self):
        self.assertEqual((self.stats.search("Semenko")).assists, 12)

    def test_team_thing(self):
        players_of_team = self.stats.team("EDM")
        self.assertEqual(len(players_of_team), 3)

    def test_top_thing(self):
        result = self.stats.top(2)
        print("kala")
        for x in result:
            print(x.__str__())

        self.assertEqual(len(result), 3)
        
    def test_top_thing3(self):
        result = self.stats.top(-1)
        self.assertEqual(len(result), 0)

    def test_top_thing2(self):
        result: list[Player] = self.stats.top(2)

        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].team, "PIT")
        self.assertEqual(result[2].points, 98)
        
        
    def test_top_thing4(self):
        result = self.stats.top(100)
        self.assertEqual(len(result), 5)
