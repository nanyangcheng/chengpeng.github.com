import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,100)
y=2*x+1
y2=2**x
plt.figure()
l1,=plt.plot(x,y,label='you')
l2,=plt.plot(x,y2,color='yellow',label='me')
plt.legend(handles=[l1,l2],labels=['she','her'],loc='best')     ##给函数加上注释，名字
plt.xlabel("i am x")
plt.ylabel("i am y")
new_ticks=np.linspace(-10,10,20)
print(new_ticks)
plt.xticks(new_ticks)
new_ticks1=np.linspace(-20,30,50)
print(new_ticks1)
plt.yticks(new_ticks1)
plt.yticks([-1,5],["good","bad"])
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.show()

