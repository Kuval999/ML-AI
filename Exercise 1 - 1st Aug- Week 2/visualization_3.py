
import matplotlib.pyplot as plt
import numpy as np

temp = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1]
sales = [215, 325, 185, 332, 406, 522, 412, 614]

def best_fit(x, y):
    xbar = np.mean(x)
    ybar = np.mean(y)
    n = len(x)
    num = sum(xi * yi for xi, yi in zip(x, y)) - n * xbar * ybar
    den = sum(pow(xi,2) for xi in x) - n * pow(xbar, 2)
    b = num/den
    a = ybar - b * xbar
    return a, b

a, b = best_fit(temp, sales)
plt.scatter(temp, sales)
plt.xlabel("Temperature")
plt.ylabel("Sales of ice cream")
yfit = [a + b * xi for xi in temp]
plt.plot(temp, yfit)
plt.grid()
plt.show()