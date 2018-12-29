import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

plt.figure(figsize=(14,14))

plt.subplot(3,2,1)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_color('none') 
plt.xticks([])
plt.yticks([])
plt.text(10,0,'n')

a = 2
n = np.arange(0,10,0.5)
y = pow(a,n)
plt.scatter(n,y,color='black')
for i in n:
		plt.plot([i,i],[0,pow(a,i)],color='black',linewidth=1.5)
plt.title('a>1')

plt.subplot(3,2,2)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_color('none') 
plt.xticks([])
plt.yticks([])
plt.text(10,0,'n')
a = 0.5
n = np.arange(0,10,0.5)
y = pow(a,n)
plt.scatter(n,y,color='black')
for i in n:
		plt.plot([i,i],[0,pow(a,i)],color='black',linewidth=1.5)
plt.title('0<a<1')		

plt.subplot(3,2,3)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_color('none') 
plt.xticks([])
plt.yticks([])
plt.text(10,0,'n')
a = -0.5
n = np.arange(0,10,0.5)
y = pow(a,n)
plt.scatter(n,y,color='black')
for i in n:
		plt.plot([i,i],[0,pow(a,i)],color='black',linewidth=1.5)
plt.title('-1<a<0')

plt.subplot(3,2,4)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_color('none') 
plt.xticks([])
plt.yticks([])
plt.text(10,0,'n')
a = -2
n = np.arange(0,10,0.5)
y = pow(a,n)
plt.scatter(n,y,color='black')
for i in n:
		plt.plot([i,i],[0,pow(a,i)],color='black',linewidth=1.5)
plt.title('a<-1')

plt.subplot(3,2,5)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_color('none') 
plt.xticks([])
plt.yticks([])
plt.text(10,0,'n')
a = -1
n = np.arange(0,10,0.5)
y = pow(a,n)
plt.scatter(n,y,color='black')
for i in n:
		plt.plot([i,i],[0,pow(a,i)],color='black',linewidth=1.5)
plt.title('a=-1')

plt.subplot(3,2,6)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_color('none') 
plt.xticks([])
plt.yticks([])
plt.text(10,0,'n')
a = 1
n = np.arange(0,10,0.5)
y = pow(a,n)
plt.scatter(n,y,color='black')
for i in n:
		plt.plot([i,i],[0,pow(a,i)],color='black',linewidth=1.5)
plt.title('a=1')
plt.show()

