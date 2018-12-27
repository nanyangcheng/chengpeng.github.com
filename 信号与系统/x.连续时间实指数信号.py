import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

fig = plt.figure()
ax = axisartist.Subplot(fig, 111)  
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,-0.8)
ax.axis["x"].set_axisline_style("->", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right") 

t = np.arange(-5,5,0.1)
s = 0.5
y = np.e**(s*t)
s = -0.5
y_1 = np.e**(s*t)
s = 0
y_2 = np.e**(s*t)

plt.title(r'$x(t)=Ce^{st},s=\sigma+jw_0$')
plt.xticks([])
plt.yticks([])
plt.ylim(-0.8,10)
plt.text(0,-1.2,'0',fontdict={'size':16})
plt.text(5.5,-1.2,'t',fontdict={'size':16})
plt.text(4,7,r'$\sigma>0$',fontdict={'size':16})
plt.text(-5.5,7,r'$\sigma<0$',fontdict={'size':16})
plt.text(0,1.5,'C',fontdict={'size':16})

plt.plot(t,y)
plt.plot(t,y_1)
plt.plot(t,y_2)
plt.show()
