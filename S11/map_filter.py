import pprint
import time
import urllib.request


def beautify(list_of_btc):
    beauty_list = []
    for price in list_of_btc:
        beauty_list.append(Price(*price))
    return beauty_list


class CoinPrice:
    link = "https://api.pro.coinbase.com/products/BTC-USD/candles/"
    valid_intervals = ['1m', '5m', '15m', '1h', '1d']

    def __init__(self, intervals='5m'):
        if not intervals in self.valid_intervals:
            raise ValueError(f'invalid interval {intervals}')

        self.intervals = intervals
        self.__data = None

    @property
    def url(self):
        return self.link + self.intervals

    @property
    def data(self):
        if self.__data is None:
            req = urllib.request.Request(self.url, headers={'User-Agent': 'Mozilla/66.0.2'})
            req = urllib.request.urlopen(req)
            html = req.read()
            text = html.decode('utf-8')

            self.__data = beautify(eval(text))

        return self.__data


    def __repr__(self):
        return '\n'.join([repr(d) for d in self.data])


class Price:
    def __init__(self, _time, opening, highest, lowest, closed, volume):
        self.time = time.ctime(_time)
        self.opening = opening
        self.highest = highest
        self.lowest = lowest
        self.closed = closed
        self.volume = volume

    @property
    def is_asc(self):
        return self.opening < self.closed

    @property
    def diff(self):
        return self.highest - self.lowest

    def __repr__(self):
        if self.is_asc:
            color_code = "\033[31;1m"
        else:
            color_code = "\033[32;1m"
        reset_code = "\033[0m"
        return f"{color_code}|{self.time}|{self.volume:10.1f}|{self.diff:10.1f}|{reset_code}"


if __name__ == '__main__':
    btc = CoinPrice('1m')
    out = sorted(btc.data, key=lambda x: x.diff)
    print(repr(btc))
