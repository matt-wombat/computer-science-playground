#
# Needed Modules:
# pip install pandas numpy matplotlib cvxopt
#
# Portfolio 1 contains Delta, Jet Blue, Chevron, Exxon, Adobe and Honeywell
#

import pandas as pd
import matplotlib.pyplot as plt
from mpttools import return_portfolios, optimal_portfolio
import numpy as np

path='stock_prices_portfolio1.csv'
stock_data = pd.read_csv(path)
selected=list(stock_data.columns[1:])

returns_quarterly = stock_data[selected].pct_change()
expected_returns = returns_quarterly.mean()
cov_quarterly = returns_quarterly.cov()

df = return_portfolios(expected_returns, cov_quarterly) 

weights, returns, risks = optimal_portfolio(returns_quarterly[1:])


df.plot.scatter(x='Volatility', y='Returns', fontsize=12)
try:
	plt.plot(risks, returns, 'y-o')
except:
  pass
plt.ylabel('Expected Returns',fontsize=14)
plt.xlabel('Volatility (Std. Deviation)',fontsize=14)
plt.title('Efficient Frontier', fontsize=24)
plt.show()
