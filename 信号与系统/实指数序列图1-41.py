import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

fig = plt.figure(figsize=(6,6))

ax = axisartist.Subplot(fig, 111)  
fig.add_axes(ax)
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_visible(False)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->", size = 1.0)
ax.axis["x"].set_axis_direction("top")

a = 2
n = np.arange(0,10,0.5)
y = pow(a,n)
plt.scatter(n,y,color='black')
for i in n:
		plt.plot([i,i],[0,pow(a,i)],color='black',linewidth=1.5)
plt.xticks([])
plt.yticks([])
plt.text(2,200,'a>1',fontdict={'size':16})
plt.text(10,-2,'n',fontdict={'size':16})

plt.show()


