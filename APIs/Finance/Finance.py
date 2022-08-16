"""
Script to analyze finance trading
"""


# imports
import yfinance as yf
import datetime as dt
from pytrends.request import TrendReq
import matplotlib.pyplot as plt


# google trends
pytrends = TrendReq(hl='en-US', tz=360)

# start date to watch
start = dt.datetime(2021, 9, 1)

# end date
end = dt.datetime.now()

# stock price
bitcoin_price = yf.download('BTC-USD', start, end)


# google trend price
kw_list = ['Bitcoin']
bitcoin_search = pytrends.get_historical_interest(kw_list, year_start=2021, month_start=9, day_start=1, hour_start=0,
                                 year_end=2021, month_end=11, day_end=23, hour_end=0,
                                 cat=0, geo='', gprop='', sleep=0)

bitcoin_price.to_csv("bitcoin_fin_9-1_11-24.csv")
bitcoin_search.to_csv("bitcoin_search_9-1_11-24.csv")
print(bitcoin_search)
print(bitcoin_search.head())

# bit_date = bitcoin_price['Date']
bit_open = bitcoin_price['Open']
bit_close = bitcoin_price['Close']
bit_high = bitcoin_price['High']

fig, ax1 = plt.subplots()
ax1.plot(bitcoin_price.index, bit_high)
ax2 = ax1.twinx()
ax2.plot(bitcoin_search.index, bitcoin_search['Bitcoin'], 'r')
plt.show()



