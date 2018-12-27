import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

plt.figure(figsize=(20,6))

plt.subplot(1,3,1)

n = np.arange(0,40,0.5)
y = np.cos(2*np.pi*n/12)
plt.scatter(n,y,color='black')

for i in n:
		plt.plot([i,i],[0,np.cos(2*np.pi*i/12)],color='black',linewidth=1.5)

plt.title(r'$\cos(2 \pi n /12)$')


plt.subplot(1,3,2)

n = np.arange(0,40,0.5)
y = np.cos(8*np.pi*n/31)
plt.scatter(n,y,color='black')

for i in n:
		plt.plot([i,i],[0,np.cos(8*np.pi*i/31)],color='black',linewidth=1.5)

plt.title(r'$\cos(8 \pi n /31)$')


plt.subplot(1,3,3)

n = np.arange(0,40,0.5)
y = np.cos(n/6)
plt.scatter(n,y,color='black')

for i in n:
		plt.plot([i,i],[0,np.cos(i/6)],color='black',linewidth=1.5)

plt.title(r'$\cos(n / 6)$')

plt.show()

