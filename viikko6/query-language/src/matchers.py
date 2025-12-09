class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class All:
    def __init__(self, *matchers, players: list = None):
        self._matchers = matchers
        self.status = True
        self.players = players if players is not None else []

    def test(self, _):
        for matcher in self._matchers:
            for player in self.players:
                if not matcher.test(player):
                    self.status = False
                    return False

        return self.status


class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        counter = 0
        for matcher in self._matchers:
            if matcher.test(player):
                counter += 1

        return counter > 0
