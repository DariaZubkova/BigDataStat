import numpy as np

def Zq(x):
    return (np.quantile(x, 1/4) + np.quantile(x, 3/4)) / 2

y = np.random.standard_cauchy(100)
print("Распределение Коши:\n", end="")
print("Порядковые статистики:\n", end="")
y.sort()
for i in range(100):
    if (i + 1) % 5 == 0:
        print('x(',i+1,') = ',y[i],'\n', end="")
    else:
        print('x(',i+1,') = ',y[i],' ', end="")
x = sum(y)/len(y)
print("Выборочное среднее: ", x,'\n', end="")
med = np.median(y)
print("Выборочная медиана: ", med,'\n', end="")
xx = (np.min(y) + np.max(y)) / 2
print("Полусумма экстремальных значений: ", xx,'\n', end="")
zq = Zq(y)
print("Полусумма квантилей: ", zq,'\n', end="")

