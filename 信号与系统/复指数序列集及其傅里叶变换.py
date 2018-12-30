import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
font = {'family':'SimHei'}                
matplotlib.rc('font',**font)              
matplotlib.rcParams['axes.unicode_minus']=False

fig = plt.figure()

plt.subplot(2,1,1)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 8)) 
plt.xticks([2],[r'$T_1$'])
plt.yticks([])
plt.title(r'$x(t)=Ce^{\sigma t}cos(w_0t+\theta) \sigma>0$')
plt.text(10,0,'n',fontdict={'size':14})

plt.xlim(5,10)
x = np.arange(4,10,0.04)
c=1
n=1
y = c*np.exp(n*x)*np.cos(10*x)
for i in x:
     plt.plot([i,i],[0,c*np.exp(n*i)*np.cos(10*i)],color='black')
plt.scatter(x,y,color='black',s=5)

plt.subplot(2,1,2)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', -7)) 
plt.xticks([2],[r'$T_1$'])
plt.yticks([])
plt.title(r'$x(t)=Ce^{\sigma t}cos(w_0t+\theta) \sigma<0$')
plt.text(-5,0,'n',fontdict={'size':14})

plt.xlim(-10,-5)
x = np.arange(-10,-5,0.04)
c=1
n=-1
y = c*np.exp(n*x)*np.cos(10*x)
for i in x:
     plt.plot([i,i],[0,c*np.exp(n*i)*np.cos(10*i)],color='black')

plt.scatter(x,y,color='black',s=5)

fig = plt.figure()

plt.subplot(2,1,1)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 8)) 
plt.xticks([2],[r'$T_1$'])
plt.yticks([])
plt.title(r'$x(t)=Ce^{\sigma t}cos(w_0t+\theta) \sigma>0$')
plt.text(10,0,r'$\omega$',fontdict={'size':14})

x = np.arange(4,10,0.1)
c=1
n=1
y = c*np.exp(n*x)*np.cos(10*x)

plt.scatter(x,np.fft.fft(y),color='black',s=10)

plt.subplot(2,1,2)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', -7)) 
plt.xticks([2],[r'$T_1$'])
plt.yticks([])
plt.title(r'$x(t)=Ce^{\sigma t}cos(w_0t+\theta) \sigma<0$')
plt.text(-5,0,r'$\omega$',fontdict={'size':14})

plt.xlim(-10,-5)
x = np.arange(-10,-5,0.1)
c=1
n=-1
y = c*np.exp(n*x)*np.cos(10*x)

plt.scatter(x,np.fft.fft(y),color='black',s=10)

plt.show()
