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

t = np.arange(-16,16,0.1)
y = np.sin(t)/t

plt.title(r'$Sa(t)=\frac{\sin(t)}{t}$',fontsize=14)
plt.text(0,-0.06,'O',fontdict={'size':16})
plt.text(16.5,-0.06,'t',fontdict={'size':14})
plt.xticks([])
plt.yticks([])
plt.plot(t,y)
plt.show()
