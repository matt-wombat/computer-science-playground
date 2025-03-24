import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

startdate = datetime(2010, 1, 1)
enddate = datetime(2025, 1, 1)

gas_prices = web.DataReader('APUS12A74714', 'fred', startdate, enddate) # us monthly gas prices 
oil_prices = web.DataReader('MCOILBRENTEU', 'fred', startdate, enddate) # europe monthly brent oil barrel prices 

print(gas_prices)
print(oil_prices)