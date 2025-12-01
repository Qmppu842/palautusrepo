class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        score_as_text = ""
        if self.player1_score == self.player2_score:
            score_as_text = self.tie_names(self.player1_score)
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score_as_text = self.advantage_names(
                self.player1_score - self.player2_score
            )
        else:
            score_as_text = self.other_score_names()
        return score_as_text

    def tie_names(self, score, score_as_text=""):
        if score == 0:
            score_as_text = "Love-All"
        elif score == 1:
            score_as_text = "Fifteen-All"
        elif score == 2:
            score_as_text = "Thirty-All"
        else:
            score_as_text = "Deuce"
        return score_as_text

    def advantage_names(self, score_difference, score_as_text=""):
        if score_difference > 0:
            score_as_text += self.player1_name
        elif score_difference < 0:
            score_as_text += self.player2_name

        score_diff_magnitude = abs(score_difference)
        if score_diff_magnitude == 1:
            score_as_text = "Advantage " + score_as_text
        elif score_diff_magnitude >= 2:
            score_as_text = "Win for " + score_as_text
        return score_as_text

    def other_score_names(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]

        player1_score_text = ""
        if self.player1_score < len(score_names):
            player1_score_text = score_names[self.player1_score]
        else:
            player1_score_text = self.player1_score

        player2_score_text = ""
        if self.player2_score < len(score_names):
            player2_score_text = score_names[self.player2_score]
        else:
            player2_score_text = self.player2_score

        return f"{player1_score_text}-{player2_score_text}"
