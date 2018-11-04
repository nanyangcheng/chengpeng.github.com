import matplotlib.pyplot as plt
import numpy as np
def fangbo(t):
    if t > 0:
        return 1
    else:
        return -1

x=np.linspace(-10,10,300)
y=fangbo(x)
plt.plot(x,y)
plt.show()
