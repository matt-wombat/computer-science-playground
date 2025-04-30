#
# Needed Modules:
# pip install pandas numpy matplotlib cvxopt
#
# Portfolio 1 contains Delta, Jet Blue, Chevron, Exxon, Adobe, Honeywell
# and as additional asset Nvidia. How does it change when compared to 
# portfolio1 without Nvidia?
#

import pandas as pd
import matplotlib.pyplot as plt
from mpttools import *
import numpy as np

#path='stock_prices_portfolio1.csv'
path='stock_prices_portfolio1+nvidia.csv'

stock_data = pd.read_csv(path)
selected=list(stock_data.columns[1:])

returns_quarterly = stock_data[selected].pct_change()
expected_returns = returns_quarterly.mean()
cov_quarterly = returns_quarterly.cov()

single_asset_std=np.sqrt(np.diagonal(cov_quarterly))
df = return_portfolios(expected_returns, cov_quarterly) 
weights, returns, risks = optimal_portfolio(returns_quarterly[1:])

df.plot.scatter(x='Volatility', y='Returns', fontsize=12)
plt.plot(risks, returns, 'y-o')
plt.scatter(single_asset_std,expected_returns,marker='X',color='red',s=200)
for xc in single_asset_std:
    plt.axvline(x=xc, color='red')

if 'nvidia' in path:
  plt.axvline(single_asset_std[-1], color='green')
  plt.scatter(single_asset_std[-1],expected_returns[-1],marker='X',color='green',s=200)
  original_EF=np.genfromtxt("stock_risk_returns_nvidia.csv", delimiter=',')
  plt.plot(risks, returns, 'g-o')
  plt.plot(original_EF[:,0],original_EF[:,1], 'y-o')
plt.ylabel('Expected Returns',fontsize=14)
plt.xlabel('Volatility (Std. Deviation)',fontsize=14)
plt.title('Efficient Frontier', fontsize=24)
plt.show()