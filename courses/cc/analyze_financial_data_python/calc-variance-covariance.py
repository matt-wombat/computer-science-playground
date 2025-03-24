import pandas as pd

incomes_funds_data = pd.read_csv("incomes_funds_data.csv", header = 0, index_col = 0)

print(incomes_funds_data)
print(incomes_funds_data.var()) # print variance of dataset
print(incomes_funds_data.cov()) # print covariance of dataset