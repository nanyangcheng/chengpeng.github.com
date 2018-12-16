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

n = list(np.arange(-5,7,1))

for i in n:
	if i>=0 :
		y = i
		plt.scatter(i,y,color='black')
	else:
		y = 0
		plt.scatter(i,y,color='black')
		
for i in n:
	if i >= 0 :
		plt.plot([i,i],[0,i],color='black',linewidth=1.5)

plt.xticks([])
plt.yticks([])

plt.text(0.2,-0.3,'O',fontdict={'size':16})
plt.text(1,-0.3,'1')
plt.text(2,-0.3,'2')
plt.text(3,-0.3,'3')
plt.text(0,7,'r[n]',fontdict={'size':16})
plt.text(7,-0.05,'n',fontdict={'size':16})
plt.text(7,3.5,'....',fontdict={'size':16})

plt.show()
