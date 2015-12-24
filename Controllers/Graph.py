import matplotlib.pyplot as plt
import matplotlib.dates as dts
import numpy as np


class Graph:
    def __init__(self, _data):
        self.data = _data

    def ShowGraph(self,
                  _currencies=None,
                  _intval=3,
                  _degree=3,
                  _density=10,
                  _rotation=None):
        if _currencies is None:
            currencies = self.data.GetCurrencies()
        else:
            currencies = _currencies

        lines = list()

        for curr in currencies:
            x = self.data.GetRateDates(curr)
            y = self.data.GetRateValues(curr)

            xNum = dts.date2num(x)

            z = np.polyfit(xNum, y, _degree)
            fApprox = np.poly1d(z)

            date = x[-1]

            for i in xrange(0, _intval):
                date += self.data.tick
                xNum = np.append(xNum, dts.date2num(date))

            ptsLen = (len(x)+_intval)*self.data.tick.days/30*_density
            xApprox = np.linspace(xNum[0], xNum[-1], ptsLen)
            yApprox = fApprox(xApprox)

            lines.append(plt.plot(x, y, 'o', xApprox, yApprox)[0])

        plt.legend(lines, currencies, loc='upper right', shadow=True)

        if _rotation:
            plt.xticks(rotation=_rotation)

        plt.xlabel('Dates')
        plt.ylabel('Rates')
        plt.title('How much You can buy for 1 ' + self.data.base)
        plt.show()
