from pytrends.request import TrendReq


# https://github.com/GeneralMills/pytrends

pytrends = TrendReq(hl='en-US', tz=360)

# trending searches in us
class Gtrends:
    def __init__(self):
        self.x = None


# top_us = pytrends.trending_searches(pn='united_states') # trending searches in real time for United States


# trending searches in real time for United States
kw_list = ["Stocks", "Crypto"]
s_int = pytrends.get_historical_interest(kw_list, year_start=2020, month_start=1, day_start=1, hour_start=0,
                                 year_end=2020, month_end=2, day_end=1, hour_end=0,
                                 cat=0, geo='', gprop='', sleep=0)

print(s_int)

# investing 107
