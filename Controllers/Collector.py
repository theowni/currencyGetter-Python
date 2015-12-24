import requests
import datetime
BASE_URL = u'http://api.fixer.io/{0}'
SUPP_CURRENCIES = ["AUD", "CAD", "CHF", "CYP", "CZK", "DKK", "EEK",
                   "GBP", "HKD", "HUF", "ISK", "JPY", "KRW", "LTL",
                   "LVL", "MTL", "NOK", "NZD", "PLN", "ROL", "SEK",
                   "SGD", "SIT", "SKK", "TRL", "USD", "ZAR"]


class Collector:
    def __init__(self, _currencies, _base, _data):
        self.currencies = _currencies
        self.base = _base
        self.data = _data  # Currencies(_base, _tick, _direction)
        self.tick = _data.tick

    def CollectData(self, _startDate, _endDate=datetime.date.today()):
        curDate = _startDate

        if self.data.direction == 1:
            params = {
                'base': self.base,
                'symbols': ','.join(self.currencies)
            }

            while curDate <= _endDate:
                url = BASE_URL.format(curDate)
                res = requests.get(url, params=params)
                resJson = res.json()

                realDate = datetime.datetime.strptime(resJson['date'],
                                                      "%Y-%m-%d")

                for k, v in resJson['rates'].items():
                    self.data.AddRate(k, v, realDate)

                curDate += self.tick

        elif self.data.direction == -1:
            while curDate <= _endDate:
                url = BASE_URL.format(curDate)

                for currency in self.currencies:
                    params = {
                        'base': currency,
                        'symbols': self.base
                    }

                    res = requests.get(url, params=params)
                    resJson = res.json()

                    realDate = datetime.datetime.strptime(resJson['date'],
                                                          "%Y-%m-%d")

                    v = resJson['rates'].items()[0][1]
                    self.data.AddRate(currency, v, realDate)

                curDate += self.tick

        return self.data
