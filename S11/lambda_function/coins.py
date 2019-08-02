import time
import urllib.request

link = "https://api.pro.coinbase.com/products/BTC-USD/candles/1h"

req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/66.0.2'})

req = urllib.request.urlopen(req)
html = req.read()
text = html.decode('utf-8')
data = eval(text)


