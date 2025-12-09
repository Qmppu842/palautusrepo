import matchers
from matchers import *


class QueryBuilder:
    def __init__(self, query=All()):
        self.query = query

    def plays_in(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def has_at_least(self, value, attribute):
        return QueryBuilder(And(self.query, HasAtLeast(value, attribute)))

    def not_(self):
        return QueryBuilder(Not(self.query))

    def has_fewer_than(self, value, attribute):
        return QueryBuilder(And(self.query, HasFewerThan(value, attribute)))

    def or_(self, *matchers):
        return QueryBuilder(Or(self.query, *matchers))

    def build(self):
        return self.query
