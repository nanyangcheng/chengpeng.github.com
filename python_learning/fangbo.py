import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,20)
y=[]
for i in x:
    if np.sin(i)>0:
        y.append(-1)
    else:
        y.append(1)
y=np.array(y)
plt.plot(x,y)
plt.show()
