import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

fig = plt.figure(figsize=(8,8))


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

plt.ylim(-2,8 )
plt.text(0,-0.15,'O',fontdict={'size':14})
plt.text(11,-0.5,r'$\omega$',fontdict={'size':14})



plt.plot(t,np.fft.fft(y)) 
plt.show()
