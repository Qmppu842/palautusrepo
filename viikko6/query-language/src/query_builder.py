import matchers
from matchers import *


class QueryBuilder:
    def __init__(self, query=All()):
        print(f"Nyt tulee querry: {query}")
        self.query = query

    def plays_in(self, team):
        print(f"lisätty plays_in: {team}")
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def has_at_least(self, value, attribute):
        print(f"lisätty has_at_least: {value} {attribute}")
        return QueryBuilder(And(self.query, HasAtLeast(value, attribute)))

    def not_(self):
        print(f"Lisätty not")
        return QueryBuilder(Not(self.query))

    def has_fewer_than(self, value, attribute):
        print(f"lisätty fewer than: {value}, {attribute}")
        return QueryBuilder(And(self.query, HasFewerThan(value, attribute)))

    def or_(self, *matchers):
        print(f"lisätty or {matchers}")
        print(f"aaaaa")
        print(f"typeof {type(matchers)}")
        matchers2 = [match.build() for match in matchers]
        print(f"mathcers2: {matchers2}")
        return QueryBuilder(And(self.query, Or(tuple(matchers2))))

    def one_of(self, *matchers):
        print(f"lisätty one of: {matchers}")
        return QueryBuilder(And(self.query, Or(*matchers)))

    def build(self):
        print(f"Buildattu")
        return self.query
