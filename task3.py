import numpy as np
import matplotlib.pyplot as plt

sample = np.random.uniform(0, 1, 100)
n, bins, patches = plt.hist(sample, 20, density=True)
array = np.arange(-0.1, 1.1, 0.01)
answer = []
for item in array:
    if (item <= 1) and (item >= 0):
        answer.append(1)
    else:
        answer.append(0)
for item in patches:
    item.set_height((item.get_height() - min(n)) / (max(n) - min(n)))
plt.plot(array, answer)
plt.ylim(0, 2)
plt.show()
