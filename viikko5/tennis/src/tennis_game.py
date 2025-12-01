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
            score_as_text = self.advantage()
        else:
            score_as_text = self.something_insane(score_as_text)
        return score_as_text

    def tie_names(self, score):
        if score == 0:
            score_as_text = "Love-All"
        elif score == 1:
            score_as_text = "Fifteen-All"
        elif score == 2:
            score_as_text = "Thirty-All"
        else:
            score_as_text = "Deuce"
        return score_as_text

    def advantage(self):
        minus_result = self.player1_score - self.player2_score

        if minus_result == 1:
            score_as_text = "Advantage player1"
        elif minus_result == -1:
            score_as_text = "Advantage player2"
        elif minus_result >= 2:
            score_as_text = "Win for player1"
        else:
            score_as_text = "Win for player2"
        return score_as_text

    def something_insane(self, score_as_text):
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_score
            else:
                score_as_text = score_as_text + "-"
                temp_score = self.player2_score

            if temp_score == 0:
                score_as_text = score_as_text + "Love"
            elif temp_score == 1:
                score_as_text = score_as_text + "Fifteen"
            elif temp_score == 2:
                score_as_text = score_as_text + "Thirty"
            elif temp_score == 3:
                score_as_text = score_as_text + "Forty"
        return score_as_text
