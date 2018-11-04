import matplotlib.pyplot as plt
import numpy as np
def fangbo(t):
    if np.sin(t) > 0:
        return 1
    else:
        return -1

x = np.arange(-10,10,20)
y = []

for i in x:
    y_1=fangbo(i)
    y.append(y_1)

plt.plot(x,y)
plt.show()