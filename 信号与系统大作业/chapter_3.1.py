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
spectrum.low_pass(cutoff=600,factor=0.01)
wave = spectrum.make_wave()
wave.write(filename='wave')
thinkdsp.play_wave(filename='wave',player='groove')
wave.play('wave')

