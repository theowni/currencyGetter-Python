import datetime
from Models.Currencies import Currencies
from Controllers.Collector import Collector
from Controllers.Graph import Graph


startDate = datetime.date(year=2015, month=1, day=1)
tick = datetime.timedelta(days=14)

currencies = u'USD,EUR'
base = u'PLN'
direction = 1

data = Currencies(base, tick, direction)
collector = Collector(currencies, base, data, direction)
collector.CollectData(startDate)

graph = Graph(data)
graph.ShowGraph()
