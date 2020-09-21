from pylab import *
from scipy.stats import *
from numpy import random
import matplotlib.pyplot as plt


def cdf_laplace(x):
    y = laplace.cdf(x)
    plt.plot(x, y, 'b')

def emp_dist(num, x, start, end):
    x.sort()
    y = linspace(0, 1, num)
    y.sort()

    for j in range(num):
        if x[j] < start:
            x[j] = start
        elif x[j] > end:
            x[j] = end

    numDouble = num * 2
    xx = empty(numDouble)
    xx[0] = start
    for j in range(num - 1):
        xx[j * 2 + 1] = x[j]
        xx[j * 2 + 2] = x[j]
    xx[num * 2 - 1] = end

    yy = empty(numDouble)
    yy[0] = 0
    yy[1] = y[0]
    for j in range(num - 1):
        yy[j * 2 + 2] = y[j + 1]
        yy[j * 2 + 3] = y[j + 1]

    plt.plot(xx, yy, 'r')

def rvs_laplace(num):
    return laplace.rvs(scale=1 / sqrt(2), size=num)

def emp_research():
    num = 100
    start = -4
    end = 4
    x = linspace(start, end, 1000)
    cdf_laplace(x)
    xx = rvs_laplace(num)
    emp_dist(num, xx, start, end)
    plt.show()

emp_research()