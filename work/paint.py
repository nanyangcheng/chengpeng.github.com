import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2*np.pi,2*np.pi,1000)
y = 5*(1-np.sin(x))
plt.figure(num='r=a(1-np.sin(&))',figsize=(10,6),dpi=120,facecolor='y',edgecolor='g')
l1=plt.plot(x,y,color='red')
plt.xlabel('a(1-sin(&))')
plt.ylabel('r')
plt.xticks((-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi),('$-2π$', '$-3π/2$', '$-π$', '$-π/2$', r'$0\ \alpha_i$', 'π/2', 'π', '3π/2', '2π'))
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom') 
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left') 
ax.spines['left'].set_position(('data', 0))
plt.show()