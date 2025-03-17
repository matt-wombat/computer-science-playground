from datetime import datetime

import pandas_datareader.data as web

start = datetime(2019, 1, 1)
end = datetime(2019, 2, 1)

# SP500 = S&P 500 index daily market cap
sap_data = web.DataReader('SP500', 'fred', start, end)
print(sap_data)