from gradient_descent import gradient_descent
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heights.csv")

X = df["height"]
y = df["weight"]

plt.plot(X, y, 'o')
#plot your line here:
b = 0
m = 0
b, m = gradient_descent(X, y, 0.0001, 1000)

y_predictions = [x_elem * m + b for x_elem in X]

plt.plot(X, y_predictions)
plt.title("Linear Regression for Player Weight vs. Height")
plt.xlabel("Height (in)")
plt.ylabel("Weight (lb)")
plt.legend(["Weight/Height", "Linear Regression"])


plt.show()