import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
font = {'family':'SimHei'}                
matplotlib.rc('font',**font)              
matplotlib.rcParams['axes.unicode_minus']=False

fig = plt.figure()

plt.subplot(2,3,1)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 0)) 

t = np.arange(-10,10,0.1)
c = 5
y=0*(t<c)+1*(t>=c)


plt.text(0,-0.08,'O',fontdict={'size':16})
plt.text(10,-0.08,'t',fontdict={'size':16})
plt.text(0,1.5,'u(t)',fontdict={'size':16})
plt.xticks([c],[r'$t_0$'])
plt.yticks([])
plt.ylim(0,1.5)
plt.plot(t,y)

plt.subplot(234)
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

t = np.arange(-10,10,0.1)
c = 5
y=0*(t<c)+1*(t>=c)

plt.xlim(-0.75,0.75)
plt.ylim(-2,1)
plt.plot(t,np.fft.fft(y))

plt.subplot(2,3,2)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 0)) 

t = np.arange(-10,10,0.1)
c = 0
y=0*(t<c)*np.sin(t)+1*(t>=c)*np.sin(t)

plt.text(0,-0.08,'O',fontdict={'size':16})
plt.text(10,-0.08,'t',fontdict={'size':16})
plt.text(-9,1,'f(t)=sin(t)u(t)',fontdict={'size':16})
plt.xticks([c],[r'$t_0$'])
plt.yticks([])
plt.xlim(-10,10)
plt.plot(t,y)

plt.subplot(2,3,5)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 0)) 

t = np.arange(-10,10,0.1)
c = 0
y=0*(t<c)*np.sin(t)+1*(t>=c)*np.sin(t)

plt.text(0,-0.08,'O',fontdict={'size':16})
plt.text(10,-0.08,r'$\omega$',fontdict={'size':16})
plt.text(0,33,'f(t)',fontdict={'size':16})
plt.xticks([])
plt.yticks([])
plt.xlim(-10,10)
plt.plot(t,np.fft.fft(y))

plt.subplot(2,3,3)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 0)) 

t = np.arange(-10,10,0.1)
c = 5
b=0
y=0*(t<b)+1*(t>=b)-0*(t<c)-1*(t>=c)

plt.text(0,-0.08,'O',fontdict={'size':16})
plt.text(10,-0.08,'t',fontdict={'size':16})
plt.text(0,2,'G(t)',fontdict={'size':16})
plt.xticks([c],[r'$t_0$'])
plt.yticks([])
plt.xlim(-10,10)
plt.ylim(0,2)
plt.plot(t,y)

plt.subplot(2,3,6)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 0)) 

t = np.arange(-10,10,0.1)
c = 5
b=0
y=0*(t<b)+1*(t>=b)-0*(t<c)-1*(t>=c)

plt.text(0,-0.08,'O',fontdict={'size':16})
plt.text(2,-0.08,r'$\omega$',fontdict={'size':16})
plt.text(0,1.95,'G(t)',fontdict={'size':16})
plt.xticks([])
plt.yticks([])
plt.xlim(-2,2)
plt.ylim(0,2)
plt.plot(t,np.fft.fft(y))
plt.show()
