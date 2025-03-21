import pandas_datareader.data as web
from datetime import datetime

start = datetime(2010, 1, 1)
end = datetime(2025, 1, 1)

gdp = web.DataReader('GDP', 'fred', start, end)
gdp['growth'] = gdp['GDP'] - gdp['GDP'].shift(1)
print(gdp)
print(type(gdp))

