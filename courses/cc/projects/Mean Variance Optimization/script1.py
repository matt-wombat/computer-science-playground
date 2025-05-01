import pandas as pd
import matplotlib.pyplot as plt
from rf import return_portfolios, optimal_portfolio
import numpy as np

# 1. Load the stock data
stock_data = pd.read_csv('stock_data_weak.csv')
#print(stock_data)

# 2. Find the quarterly return for each period
returns_quarterly = stock_data[list(stock_data.columns[1:])].pct_change()
#print(returns_quarterly)

# 3. Find the expected returns 
expected_returns = returns_quarterly.mean()
#print(expected_returns)

# 4. Find the covariance 
cov_quarterly = returns_quarterly.cov()
#print(cov_quarterly)

# 5. Find a set of random portfolios
random_portfolios = return_portfolios(expected_returns, cov_quarterly)
#print(random_portfolios)

# 6. Plot the set of random portfolios
plt.plot(random_portfolios.Volatility, random_portfolios.Returns, "o")
plt.xlabel('Volatility (Std. Deviation)')
plt.ylabel('Expected Returns')
plt.title('Efficient Frontier')

# 7. Calculate the set of portfolios on the EF
weights, returns, risks = optimal_portfolio(returns_quarterly[1:])


# 8. Plot the set of portfolios on the EF
plt.plot(risks, returns, "y-o")


# Compare the set of portfolios on the EF to the 
try:
  single_asset_std=np.sqrt(np.diagonal(cov_quarterly))
  plt.scatter(single_asset_std,expected_returns,marker='X',color='red',s=200)
except:
  pass
plt.show()