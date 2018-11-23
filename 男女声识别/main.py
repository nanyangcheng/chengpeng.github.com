import wave
import struct
import thinkdsp
import thinkplot
import numpy as np
import pylab as pl
import matplotlib
import matplotlib.pyplot as plt
from scipy import *
from pylab import *

wave = thinkdsp.read_wave('sheng.wav')
spectrum = wave.make_spectrum()
plt.figure(figsize=(15,6))
plt.axis([0,2000,0,2500])
spectrum.plot()
thinkplot.show()

