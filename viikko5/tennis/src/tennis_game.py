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
            score_as_text = self.advantage(self.player1_score - self.player2_score)
        else:
            score_as_text = self.something_insane(score_as_text)
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

    def advantage(self, score_difference, score_as_text=""):
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

    def something_insane(self, score_as_text="xx"):
        print(f"Starting new")
        print(f"player1_score:{self.player1_score}")
        print(f"player2_score:{self.player2_score}")
        temp_score = 0
        for i in range(1, 3):
            print(f"round: {i}")
            print(f"score_as_text1: {score_as_text}")
            if i == 1:
                print(f"score_as_text2: {score_as_text}")
                temp_score = self.player1_score
                print(f"score_as_text3: {score_as_text}")
            else:
                print(f"score_as_text4: {score_as_text}")
                score_as_text = score_as_text + "-"
                temp_score = self.player2_score
                print(f"score_as_text5: {score_as_text}")

            print(f"score_as_text6: {score_as_text}")
            if temp_score == 0:
                score_as_text = score_as_text + "Love"
                print(f"score_as_text7: {score_as_text}")
            elif temp_score == 1:
                score_as_text = score_as_text + "Fifteen"
                print(f"score_as_text8: {score_as_text}")
            elif temp_score == 2:
                score_as_text = score_as_text + "Thirty"
                print(f"score_as_text9: {score_as_text}")
            elif temp_score == 3:
                score_as_text = score_as_text + "Forty"
                print(f"score_as_text10: {score_as_text}")
            print(f"score_as_text11: {score_as_text}")
        return score_as_text
