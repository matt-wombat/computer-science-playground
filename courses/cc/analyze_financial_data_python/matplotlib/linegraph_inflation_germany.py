from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Inflation Germany 2023
y1 = [8.7, 8.7, 7.4, 7.2, 6.1, 6.4, 6.2, 6.1, 4.5, 3.8, 3.2, 3.7]
# Inflation Germany 2024
y2 = [2.9, 2.5, 2.2, 2.2, 2.4, 2.2, 2.3, 1.9, 1.6, 2.0, 2.2, 2.6]

plt.plot(x, y1, color='pink', marker='o')
plt.plot(x, y2, color='gray', marker='o')
plt.title('Inflation in Germany')
plt.xlabel("Month")
plt.ylabel("Inflation in %")

ax = plt.subplot()
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend(['2023', '2024'], loc=0)


plt.show()