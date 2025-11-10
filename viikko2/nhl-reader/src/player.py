class Player:
    def __init__(self, player_data_dict):
        self.name = player_data_dict["name"]
        self.nationality = player_data_dict["nationality"]
        self.team = player_data_dict["team"]
        self.goals = player_data_dict["goals"]
        self.assists = player_data_dict["assists"]

    def dyna_str(self, attribute):
        return f"{self.name:20}, {getattr(self, attribute)}"

    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals:2} + {self.assists:2} = {(self.goals + self.assists):2}"
