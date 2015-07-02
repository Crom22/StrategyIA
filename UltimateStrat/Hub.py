from UltimateStrat.Data.BlackBoard import BlackBoard
import sys

__author__ = 'jbecirovski'


class Hub(object):
    """
    InfoManager is a simple question answerer and setter.
    """
    def initialize(self, field, team, op_team):
        self.black_board = BlackBoard(field, team, op_team)

    def update(self):
        self.black_board.update()

    registered_function = {}

    def __getattr__(self, key):
        return self.registered_function[key]

    def register_function(self, function):
        self.registered_function[function.__name__] = function
        return function

sys.modules[__name__] = Hub()
sys.modules["Hub"] = sys.modules[__name__]

from UltimateStrat.hub_plugins import *
