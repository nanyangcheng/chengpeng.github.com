import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
font = {'family':'SimHei'}                
matplotlib.rc('font',**font)              
matplotlib.rcParams['axes.unicode_minus']=False

fig = plt.figure()

plt.subplot(1,2,1)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 0)) 

t = np.arange(-10,10,0.1)
y=0*(t<0)+1*(t>=0)

plt.text(0,-0.08,'O',fontdict={'size':16})
plt.text(10,-0.08,'t',fontdict={'size':16})
plt.text(0,1.5,'u(t)',fontdict={'size':16})
plt.xticks([])
plt.yticks([])
plt.ylim(0,1.5)
plt.plot(t,y)

plt.subplot(1,2,2)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', -0.5))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 0))
plt.xticks([])
plt.yticks([])
plt.text(0,-0.5,'O',fontdict={'size':16})
plt.text(0.75,-0.5,r'$\omega$',fontdict={'size':16})
plt.text(0,1,'u(t)',fontdict={'size':16})

t = np.arange(-1,1,0.1)
y=0*(t<0)+1*(t>=0)


plt.xlim(-0.75,0.75)
plt.ylim(-2,1)
plt.plot(t,np.fft.fft(y))

plt.show()
