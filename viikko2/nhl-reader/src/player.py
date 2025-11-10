class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.nationality = dict["nationality"]
        self.team = dict["team"]
        self.goals = dict["goals"]
        self.assists = dict["assists"]

    def __str__(self):
        return f"{self.name}, {self.nationality}"

    def dyna_str(self, attribute):
        return f"{self.name:20}, {getattr(self, attribute)}"

    def stats_str(self):
        return f"{self.name:20} {self.team:15} {self.goals:2} + {self.assists:2} = {(self.goals + self.assists):2}"
