import numpy as np

dividends_microsoft_eur = [0.6358, 0.6308, 0.6364, 0.6854, 0.6876, 0.7016, 0.7016, 0.7906]
variance_dividends_microsoft = np.var(dividends_microsoft_eur)
stddev_dividends_microsoft = np.std(dividends_microsoft_eur)

print('The variance of Microsoft stock dividends in 2023 and 2024 is {:.2f}%'.format(variance_dividends_microsoft * 100))

print('The standard deviation of Microsoft stock dividends in 2023 and 2024 is {:.2f}%'.format(stddev_dividends_microsoft * 100))