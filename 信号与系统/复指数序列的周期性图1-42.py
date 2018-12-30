import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

plt.figure()

plt.subplot(3,1,1)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_color('none') 
plt.xticks([])
plt.yticks([])
plt.text(40,0.05,'.......',fontdict={'size':16})
plt.text(41,-0.3,'n',fontdict={'size':14})

n = np.arange(0,40,0.5)
y = np.cos(2*np.pi*n/12)
plt.scatter(n,y,color='black')

for i in n:
		plt.plot([i,i],[0,np.cos(2*np.pi*i/12)],color='black',linewidth=1.5)

plt.title(r'$x[n]=\cos(2 \pi n /12)$')


plt.subplot(3,1,2)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_color('none') 
plt.xticks([])
plt.yticks([])
plt.text(40,0.05,'.......',fontdict={'size':16})
plt.text(41,-0.3,'n',fontdict={'size':14})

n = np.arange(0,40,0.5)
y = np.cos(8*np.pi*n/31)
plt.scatter(n,y,color='black')

for i in n:
		plt.plot([i,i],[0,np.cos(8*np.pi*i/31)],color='black',linewidth=1.5)

plt.title(r'x[n]=$\cos(8 \pi n /31)$')


plt.subplot(3,1,3)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_color('none') 
plt.xticks([])
plt.yticks([])
plt.text(40,0.05,'.......',fontdict={'size':16})
plt.text(41,-0.3,'n',fontdict={'size':14})

n = np.arange(0,40,1)
y = np.cos(n/6)
plt.scatter(n,y,color='black')

for i in n:
		plt.plot([i,i],[0,np.cos(i/6)],color='black',linewidth=1.5)

plt.title(r'$x[n]=\cos(n / 6)$')

plt.show()

