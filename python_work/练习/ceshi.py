import wave
import struct
import numpy as np
import pylab as pl
from scipy import *
from pylab import *
 

filename = 'boy.wav'
wavefile = wave.open(filename, 'r') 

nchannels = wavefile.getnchannels()
sample_width = wavefile.getsampwidth()
framerate = wavefile.getframerate() 
numframes = wavefile.getnframes()
 
print("channel",nchannels)
print("sample_width",sample_width)
print("framerate",framerate)
print("numframes",numframes)
 
y = zeros(numframes)
 
for i in range(numframes):
    val = wavefile.readframes(1)
    left = val[0:2]

    v = struct.unpack('h', left )[0]
    y[i] = v
 


Fs = framerate
specgram(y, NFFT=1024, Fs=Fs, noverlap=900)
show()
