import matplotlib.pyplot as plt
import numpy as np
k = np.linspace(-30,30,60)
a_k1 = np.sin(2*k*np.pi*(1/4))/(np.pi*k)
##$a_k=\frac{\sin((2k*\pi)*T_1/T}{\pi*k}$
plt.scatter(k,a_k1,s=10)
plt.xticks((-30,-20,-10,0,10,20,30))
plt.title('$a_k=\\frac{\sin(2k*\pi*\\frac{T_1}{T})}{\pi*k},T=4T_1$'
,fontsize=19)
plt.show()