import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

fig = plt.figure(figsize=(6,6))


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
y=0*(t<0)+1*(t>=0)

plt.text(0,-0.08,'O',fontdict={'size':16})
plt.text(10,-0.08,'t',fontdict={'size':16})
plt.text(0,1.5,'u(t)',fontdict={'size':16})
plt.xticks([])
plt.yticks([])
plt.ylim(0,1.5)
plt.plot(t,y)
plt.show()
