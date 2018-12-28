import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib 
font = {'family':'SimHei'}                
matplotlib.rc('font',**font)              
matplotlib.rcParams['axes.unicode_minus']=False

fig = plt.figure()


plt.subplot(3,2,1)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 0.6)) 
plt.xticks([2],[r'$T_1$'])
plt.yticks([])
plt.title(r'$x_1(t)=\cos(w_1t)$')

x = np.arange(-3,5,0.1)
y = np.cos(5*x)
plt.plot(x,y,color='black')


plt.subplot(3,2,2)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 0.6)) 
plt.xticks([2],[r'$T_1$'])
plt.yticks([])
plt.title('$x_1(t)=\cos(w_1t)$''的傅里叶变换')

x = np.arange(-3,5,0.1)
y = np.cos(5*x)
plt.plot(x,np.fft.fft(y),color='black') 

plt.subplot(3,2,3)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 0.6)) 
plt.xticks([2],[r'$T_2$'])
plt.yticks([])
plt.title(r'$x_2(t)=\cos(w_2t)$')

x = np.arange(-3,5,0.1)
y = np.cos(3*x)
plt.plot(x,y,color='black')

plt.subplot(3,2,4)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 0.6)) 
plt.xticks([2],[r'$T_2$'])
plt.yticks([])
plt.title('$x_2(t)=\cos(w_2t)$''的傅里叶变换')

x = np.arange(-3,5,0.1)
y = np.cos(3*x)
plt.plot(x,np.fft.fft(y),color='black') 

plt.subplot(3,2,5)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 0.6)) 
plt.xticks([2],[r'$T_3$'])
plt.yticks([])
plt.title(r'$x_3(t)=\cos(w_3t)$')

x = np.arange(-3,5,0.1)
y = np.cos(x)
plt.plot(x,y,color='black')

plt.subplot(3,2,6)
ax = plt.gca()  
ax.spines['right'].set_color('none')  
ax.spines['top'].set_color('none')  
ax.xaxis.set_ticks_position('bottom')  
ax.spines['bottom'].set_position(('data', 0))  
ax.yaxis.set_ticks_position('left')  
ax.spines['left'].set_position(('data', 0.6)) 
plt.xticks([2],[r'$T_3$'])
plt.yticks([])
plt.title('$x_3(t)=\cos(w_3t)$''的傅里叶变换')

x = np.arange(-3,5,0.1)
y = np.cos(x)
plt.plot(x,np.fft.fft(y),color='black') 


plt.show()
