#
#
# _direction=1 means 1*_baseCurrency = 0.47*_someCurrency
# _direction=-1" means 2.12765*_baseCurrency = 1*_someCurrency
#
#
from collections import defaultdict


class Currencies:
    def __init__(self, _base, _tick, _direction):
        self.data = defaultdict(lambda: defaultdict(list))
        self.base = _base
        self.tick = _tick
        self.direction = _direction

    def AddRate(self, _curr, _val, _date):
        self.data[_curr]['rate'].append(_val)
        self.data[_curr]['date'].append(_date)

    def GetCurrencies(self):
        return self.data.keys()

    def GetRateValues(self, _curr):
        return self.data[_curr]['rate']

    def GetRateDates(self, _curr):
        return self.data[_curr]['date']
