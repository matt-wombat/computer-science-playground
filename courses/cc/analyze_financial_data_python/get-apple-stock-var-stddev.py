import pandas as pd

apple_stock = pd.read_csv('apple_stock_quotes.csv')

print("Apple Stock Variance: ", apple_stock['open'].var())
print("Apple Stock Standard Variation: ", apple_stock['open'].std())

