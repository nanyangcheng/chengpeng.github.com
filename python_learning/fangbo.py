import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,300)
y=[]
for i in x:
    if np.sin(i)>0:
        y.append(-1)
    else:
        y.append(1)

plt.plot(x,y)
plt.show()
