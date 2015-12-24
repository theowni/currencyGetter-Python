import datetime
from Models.Currencies import Currencies
from Controllers.Collector import Collector
from Controllers.Graph import Graph

# Get exchange rates since August 2015
startDate = datetime.date(year=2015, month=8, day=1)
tick = datetime.timedelta(days=14)

currencies = [u'USD', u'EUR']
base = u'PLN'

data1 = Currencies(base, tick, -1)
collector1 = Collector(currencies, base, data1)
collector1.CollectData(startDate)

data2 = Currencies(base, tick, 1)
collector2 = Collector(currencies, base, data2)
collector2.CollectData(startDate)

graph1 = Graph(data1)
graph1.ShowGraph()

# When You close first graph second appears
graph2 = Graph(data2)
graph2.ShowGraph()
