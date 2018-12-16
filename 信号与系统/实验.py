import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=np.array([1,2,3.2,2.3,4.6,7.5,2.3,6.5,7.8,9])
data_1=np.unique(data)

fig,axes=plt.subplots(figsize=(16,13))

axes.plot(data_1,'mo-.',label='line_point')

axes.plot(data_1,'r--',drawstyle='steps-post',label='line')

axes.legend(loc='gest')

plt.show()
