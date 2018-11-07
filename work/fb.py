import matplotlib.pyplot as plt
import numpy as np
k = np.linspace(-30,30,100)
a_k1 = np.sin(2*k*np.pi*0.25)/(np.pi*k)
plt.plot(k,a_k1)
plt.xticks((-30,-20,-10,0,10,20,30))
plt.title('$T=4T_1$')
plt.show()