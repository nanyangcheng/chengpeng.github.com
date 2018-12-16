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

n = list(np.arange(-3,4,1))
y = list(np.ones(7,dtype=int))
plt.scatter(n,y,color='black')

for i in n:
		plt.plot([i,i],[0,1],color='black',linewidth=1.5)
		
plt.text(0.1,-0.1,'O',fontdict={'size':16})
plt.xticks([-3,-2,-1,1,2,3],[r'$-3N$',r'$-2N$',r'$-N$',r'$N$',r'$2N$',r'$3N$'])
plt.text(3.1,0.5,'...',fontdict={'size':16})
plt.text(-3.3,0.5,'...',fontdict={'size':16})
plt.text(0.1,1.6,r'$\delta_N[n]$',fontdict={'size':16})
plt.ylim(-0.4,1.5)
plt.yticks([])
 
plt.show()

