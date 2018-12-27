import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

fig = plt.figure()


ax = axisartist.Subplot(fig, 111)  
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right")

t = np.arange(-10,10,0.1)
y = np.cos(t-1)

plt.title(r'$x(t)=A\cos(wt+\phi)$',fontsize=16)
plt.xticks([])
plt.yticks([])
plt.ylim(-2,2)
plt.text(-2.5,np.cos(-1),r'$A\cos\phi$',fontdict={'size':14})
plt.text(0,-0.15,'O',fontdict={'size':14})
plt.text(0.15,1.90,'x(t)',fontdict={'size':14})
plt.text(11,-0.15,'t',fontdict={'size':14})
plt.text(1.2,0.96,'<-------------->',fontdict={'size':14})
plt.text(np.pi,1.1,r'$T_0=\frac{2\pi}{\omega_0}$',fontdict={'size':14})
  
dy = 0.4
plt.errorbar(1,1,yerr=dy,fmt='o')
plt.errorbar(1+2*np.pi,1,yerr=dy,fmt='o')

plt.plot(t,y) 
plt.show()


