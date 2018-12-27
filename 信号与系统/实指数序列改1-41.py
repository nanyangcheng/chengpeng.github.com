import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

plt.figure(figsize=(14,14))

plt.subplot(3,2,1)

a = 2
n = np.arange(0,10,0.5)
y = pow(a,n)
plt.scatter(n,y,color='black')
for i in n:
		plt.plot([i,i],[0,pow(a,i)],color='black',linewidth=1.5)
plt.title('a>1')

plt.subplot(3,2,2)
a = 0.5
n = np.arange(0,10,0.5)
y = pow(a,n)
plt.scatter(n,y,color='black')
for i in n:
		plt.plot([i,i],[0,pow(a,i)],color='black',linewidth=1.5)
plt.title('0<a<1')		

plt.subplot(3,2,3)
a = -0.5
n = np.arange(0,10,0.5)
y = pow(a,n)
plt.scatter(n,y,color='black')
for i in n:
		plt.plot([i,i],[0,pow(a,i)],color='black',linewidth=1.5)
plt.title('-1<a<0')

plt.subplot(3,2,4)
a = -2
n = np.arange(0,10,0.5)
y = pow(a,n)
plt.scatter(n,y,color='black')
for i in n:
		plt.plot([i,i],[0,pow(a,i)],color='black',linewidth=1.5)
plt.title('a<-1')

plt.subplot(3,2,5)
a = -1
n = np.arange(0,10,0.5)
y = pow(a,n)
plt.scatter(n,y,color='black')
for i in n:
		plt.plot([i,i],[0,pow(a,i)],color='black',linewidth=1.5)
plt.title('a=-1')

plt.subplot(3,2,6)
a = 1
n = np.arange(0,10,0.5)
y = pow(a,n)
plt.scatter(n,y,color='black')
for i in n:
		plt.plot([i,i],[0,pow(a,i)],color='black',linewidth=1.5)
plt.title('a=1')
plt.show()

