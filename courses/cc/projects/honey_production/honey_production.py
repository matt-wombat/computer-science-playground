import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("honeyproduction.csv")

print(df.head())

prod_per_year = df.groupby('year').totalprod.mean().reset_index()

print(prod_per_year)

#x = df[["year"]]
# x = prod_per_year.keys()
x = prod_per_year["year"]
x = x.values.reshape(-1,1)
print(x)

y = prod_per_year["totalprod"]
print(y)

regr = linear_model.LinearRegression()
regr.fit(x, y)

print("Slope:", regr.coef_[0])
print("Intercept:", regr.intercept_)

y_predict = regr.predict(x)

x_future = np.array(range(2013, 2050))
x_future = x_future.reshape(-1, 1)
print(x_future)
future_predict = regr.predict(x_future)



plt.scatter(x, y)
plt.plot(x, y_predict)
plt.plot(x_future, future_predict)
plt.title("Honey Production Prediction until 2050")
plt.xlabel("Year")
plt.ylabel("Total Production (lb)")

plt.show()


